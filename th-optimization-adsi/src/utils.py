"""Functions for tutorial notebooks."""
from time import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.optimize import bisect


# Part 1 - Iterative Methods


def gradient_descent(func, grad, x0, step, tol=1e-6, max_iter=1000):
    """Minimize function with gradient descent.

    Stopping condition based on size of the gradient.

    Parameters
    ----------
    func : function
        Objective function to minimize.
    grad : function
        Gradient of objective function.
    x0 : array
        Starting point for solver.
    step : float
        Step size for gradient step.
    tol : float, optional
        Gradient tolerance for terminating solver.
    max_iter : int, optional
        Maximum number of iterations for solver.

    Returns
    -------
    x : float
        Function minimizer.
    x_vals : array
        Iterates.
    func_vals : array
        Function values at iterates.
    grad_vals : array
        Norm of gradient at iterates.

    """
    # Initialize return values
    if type(x0) in (int, float):
        x_vals = np.zeros((1, max_iter + 1))
    else:
        x_vals = np.zeros((len(x0), max_iter + 1))
    x_vals[:, 0] = x0
    func_vals = np.zeros(max_iter + 1)
    func_vals[0] = func(x0)
    grad_vals = np.zeros(max_iter + 1)
    grad_vals[0] = np.linalg.norm(grad(x0))

    # Minimize function
    start = time()
    for ii in range(1, max_iter + 1):
        x_vals[:, ii] = x_vals[:, ii - 1] - step*grad(x_vals[:, ii - 1])
        func_vals[ii] = func(x_vals[:, ii])
        grad_vals[ii] = np.linalg.norm(grad(x_vals[:, ii]))

        # Check convergence
        if grad_vals[ii] < tol:
            print(f'Converged after {ii} iteration(s).')
            print(f'Minimum function value: {min(func_vals[:(ii + 1)]):.2f}')
            print(f'Total time: {time() - start:.2f} secs')
            return x_vals[:, ii], x_vals[:, :(ii + 1)].squeeze(), \
                func_vals[:(ii + 1)], grad_vals[:(ii + 1)]

    print(f'Maximum number of iterations reached: {ii}.')
    print(f'Minimum function value: {min(func_vals[:(ii + 1)]):.2f}')
    print(f'Total time: {time() - start:.2f} secs')
    return x_vals[:, -1], x_vals.squeeze(), func_vals, grad_vals


def plot_1d(func, results):
    """Plot 1D results from gradient_descent().

    Parameters
    ----------
    func : function
        Function to be minimized.
    results : list
        Results from gradient_descent().

    Returns
    -------
    None.

    """
    # Plot set up
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))
    cmap = 'viridis_r'
    norm = plt.Normalize(0, len(results[1]) - 1)
    pad = (max(results[1]) - min(results[1]))/10
    x_vals = np.linspace(min(results[1]) - pad, max(results[1]) + pad)

    # Plot iterates
    ax[0].plot(x_vals, func(x_vals))
    ax[0].scatter(results[1], results[2], c=np.arange(0, len(results[1])),
                  zorder=3, cmap=cmap, norm=norm)
    ax[0].set_xlabel('$x$')
    ax[0].set_ylabel('$f(x)$')
    fig.colorbar(cm.ScalarMappable(cmap=cmap, norm=norm), label='Iteration',
                 ax=ax[0])

    # Plot function values
    ax[1].plot(results[2])
    ax[1].scatter(np.arange(len(results[2])), results[2], zorder=3, cmap=cmap,
                  c=np.arange(0, len(results[1])), norm=norm)
    ax[1].set_xlabel('Iteration ($k$)')
    ax[1].set_ylabel('$f(x^k)$')

    # Plot norm of gradient values
    ax[2].plot(results[3])
    ax[2].scatter(np.arange(len(results[3])), results[3], zorder=3, cmap=cmap,
                  c=np.arange(0, len(results[1])), norm=norm)
    ax[2].set_xlabel('Iteration ($k$)')
    ax[2].set_ylabel(r'$||\nabla f(x^k)||$')
    plt.show()


def plot_2d(func, results):
    """Plot 2D results from gradient_descent().

    Parameters
    ----------
    func : function
        Function to be minimized.
    results : list
        Results from gradient_descent().

    Returns
    -------
    None.

    """
    # Plot set up
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))
    x_vals = np.linspace(*get_bounds(results))
    X = np.meshgrid(x_vals, x_vals)
    norm = plt.Normalize(np.min(func(X)), np.max(func(X)))

    # Plot iterates
    ax[0].contour(x_vals, x_vals, func(X))
    ax[0].plot(results[1][0, :], results[1][1, :], '.')
    ax[0].set_xlabel('$x$')
    ax[0].set_ylabel('$y$')
    fig.colorbar(cm.ScalarMappable(norm=norm), label='$f(x, y)$', ax=ax[0])

    # Plot function values
    ax[1].plot(results[2])
    ax[1].set_xlabel('Iteration ($k$)')
    ax[1].set_ylabel('$f(x^k, y^k)$')

    # Plot norm of gradient values
    ax[2].plot(results[3])
    ax[2].set_xlabel('Iteration ($k$)')
    ax[2].set_ylabel(r'$||\nabla f(x^k, y^k)||$')


def get_bounds(results):
    """Get upper and lower bounds for 2D plot."""
    max_val = max(max(results[1][0]), max(results[1][1]))
    min_val = min(min(results[1][0]), min(results[1][1]))
    bound = max(abs(max_val), abs(min_val))
    pad = bound/5
    return [-bound - pad, bound + pad]


def stochastic_descent(A, y, learning_rate, decay=None, batch_size=1,
                       tol=1e-6, max_iter=1000, random_seed=1):
    """Solve linear least-squares with stochastic gradient descent.

    Iterates are initialized as a random vector.
    Stopping condition based on difference between iterates.

    Parameters
    ----------
    A : array
        Training data coefficient matrix.
    y : array
        Training data solution vector.
    learning_rate : float
        Initial learning rate for stochastic gradient descent.
    decay : float, optional
        Learning rate schedule decay parameter.
    batch_size : int, optional
        Number of training examples used to approximate gradient.
    tol : float, optional
        Difference between iterates tolerance for terminating solver.
    max_iter : int, optional
        Maximum number of iterations for solver.
    random_seed : int, optional
        Random number generator seed for reproducibility.

    Returns
    -------
    x : float
        Function minimizer.
    x_vals : array
        Iterates.
    func_vals : array
        Function values at iterates.
    func_diff : array
        Difference between subsequent iterates.

    """
    m, n = A.shape
    if batch_size < 1:
        print(f'Invalid batch_size {batch_size}, using 1.')
        batch_size = 1
    if batch_size > m:
        print(f'Invalid batch_size {batch_size}, using {m}.')
        batch_size = m

    # Initialize return values
    np.random.seed(random_seed)
    x_vals = np.zeros((n, max_iter + 1))
    x_vals[:, 0] = np.random.randn(n)
    func_vals = np.zeros(max_iter + 1)
    func_vals[0] = np.linalg.norm(A.dot(x_vals[:, 0]) - y)**2/(2*m)
    func_diff = np.zeros(max_iter)

    # Minimize function
    start = time()
    for ii in range(1, max_iter + 1):
        idx = np.random.randint(0, m, batch_size)
        res = A[idx, :].dot(x_vals[:, ii - 1]) - y[idx]
        grad = 1/batch_size*np.transpose(A[idx, :]).dot(res)
        x_vals[:, ii] = x_vals[:, ii - 1] - learning_rate*grad
        func_vals[ii] = np.linalg.norm(A.dot(x_vals[:, ii]) - y)**2/(2*m)
        func_diff[ii - 1] = np.abs(func_vals[ii] - func_vals[ii - 1])

        # Check convergence
        if func_diff[ii - 1] < tol:
            print(f'Converged after {ii} iteration(s).')
            print(f'Minimum function value: {min(func_vals[:(ii + 1)]):.2f}')
            print(f'Total time: {time() - start:.2f} secs')
            return x_vals[:, ii], x_vals[:, :(ii + 1)].squeeze(), \
                func_vals[:(ii + 1)], func_diff[:ii]

        # Update learning rate
        if decay is not None:
            learning_rate = learning_rate/(1 + decay*ii)

    print(f'Maximum number of iterations reached: {ii}.')
    print(f'Minimum function value: {min(func_vals):.2f}')
    print(f'Total time: {time() - start:.2f} secs')
    return x_vals[:, -1], x_vals.squeeze(), func_vals, func_diff


def plot_sgd(results):
    """Plot results from stochastic_descent().

    Parameters
    ----------
    results : list
        Results from stochastic_descent().

    Returns
    -------
    None.

    """
    # Plot function values
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(results[2])
    ax[0].set_xlabel('Iteration ($k$)')
    ax[0].set_ylabel('$f(x^k)$')

    # Plot difference between function values
    ax[1].plot(np.arange(1, len(results[3]) + 1), results[3])
    ax[1].set_xlabel('Iteration ($k$)')
    ax[1].set_ylabel('$|f(x^k) - f(x^{k-1})|$')


# Part 2 - Linear Regression


def prox_descent(A, y, lam, step=None, tol=1e-6, max_iter=10000,
                 print_results=True):
    """Solve Lasso problem with proximal gradient descent.

    Iterates are initialized as a vector of zeros.
    Stopping condition based on difference between iterates.

    Parameters
    ---------
    A : array
        Training data coefficient matrix.
    y : darray
        Training data solution vector.
    lam : float
        Regularization parameter.
    step : float, optional
        Initial learning rate for stochastic gradient descent.
    tol : float, optional
        Difference between iterates tolerance for terminating solver.
    max_iter : int, optional
        Maximum number of iterations for solver.
    print_results : bool, optional
        If True, print convergence results.

    Returns
    -------
    x : float
        Function minimizer.
    x_vals : array
        Iterates.
    func_vals : array
        Function values at iterates.
    func_diff : array
        Difference between subsequent iterates.

    """
    # Initialize return values
    m, n = A.shape
    x_vals = np.zeros((n, max_iter + 1))
    func_vals = np.zeros(max_iter + 1)
    func_vals[0] = np.linalg.norm(A.dot(x_vals[:, 0]) - y)**2/2 + \
        lam*np.linalg.norm(x_vals[:, 0], 1)
    func_diff = np.zeros(max_iter)

    # Set step size
    if step is None:
        step = 1/(np.linalg.norm(np.transpose(A).dot(A)) + 2*lam*np.sqrt(m))

    # Minimize function
    start = time()
    for ii in range(1, max_iter + 1):
        grad = np.transpose(A).dot(A.dot(x_vals[:, ii - 1]) - y)
        x_vals[:, ii] = prox(x_vals[:, ii - 1] - step*grad, lam*step)
        func_vals[ii] = np.linalg.norm(A.dot(x_vals[:, ii]) - y)**2/2 + \
            lam*np.linalg.norm(x_vals[:, ii], 1)
        func_diff[ii - 1] = np.abs(func_vals[ii] - func_vals[ii - 1])

        # Check convergence
        if func_diff[ii - 1] < tol:
            if print_results:
                print(f'Converged after {ii} iteration(s).')
                print(f'Minimum function value: {min(func_vals[:(ii + 1)]):.2f}')
                print(f'Total time: {time() - start:.2f} secs')
            return x_vals[:, ii], x_vals[:, :(ii + 1)].squeeze(), \
                func_vals[:(ii + 1)], func_diff[:ii]

    if print_results:
        print(f'Maximum number of iterations reached: {ii}.')
        print(f'Minimum function value: {min(func_vals):.2f}')
        print(f'Total time: {time() - start:.2f} secs')
    return x_vals[:, -1], x_vals.squeeze(), func_vals, func_diff


def prox(x, lam):
    """Evaluate soft thresholding operator."""
    return np.maximum(x - lam, 0) - np.maximum(-x - lam, 0)


def plot_pgd1(A, x_true, y_true, results):
    """Plot results from prox_descent() example 1.

    Parameters
    ----------
    x_true : array
        True model parameter values.
    results : list
        Results from prox_descent().

    Returns
    -------
    None.

    """
    # Plot parameter values
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(x_true, 'o')
    ax[0].plot(results[0], '.')
    ax[0].set_xlabel('Index ($i$)')
    ax[0].set_ylabel('Model Parameter ($x_i$)')
    ax[0].legend(['True', 'Estimated'])

    # Plot estimates
    ax[1].plot(y_true, A.dot(results[0]), '.')
    ax[1].set_xlabel('True Output ($y_i$)')
    ax[1].set_ylabel('Estimated Output ($a_i^Tx$)')


def plot_lam1(A, y, x_true, lam_vals):
    """Plot Lasso results for different values of lambda (example 1).

    Parameters
    ---------
    A : array
        Training data coefficient matrix.
    y : array
        Training data solution vector.
    x_true : array
        True solution.
    lam_vals : array
        Regularization parameters.

    Returns
    -------
    None.

    """
    # Solve Lasso problems
    f_vals = np.zeros(len(lam_vals))
    nonzeros = np.zeros(len(lam_vals))
    x_vals = np.zeros((A.shape[1], len(lam_vals)))
    for ii in range(len(lam_vals)):
        results = prox_descent(A, y, lam_vals[ii], print_results=False)
        f_vals[ii] = results[2][-1]
        nonzeros[ii] = np.count_nonzero(results[0])
        x_vals[:, ii] = results[0]

    # Plot function values vs. number of nonzero elements
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    cmap = cm.get_cmap('viridis_r', len(lam_vals[1:-1]))
    norm = plt.Normalize(min(np.log10(lam_vals[1:-1])),
                         max(np.log10(lam_vals[1:-1])))
    ax[0].plot(nonzeros, f_vals)
    ax[0].scatter(nonzeros[1:-1], f_vals[1:-1], c=np.log10(lam_vals[1:-1]),
                  zorder=3, cmap=cmap, norm=norm)
    ax[0].set_xlabel('Number of Nonzeros in $x$')
    ax[0].set_ylabel('$f(x)$')
    fig.colorbar(cm.ScalarMappable(cmap=cmap, norm=norm),
                 label='$\lambda = 10^p$', ax=ax[0])

    # Plot values of nonzero elements in solution
    count = 0
    colors = cm.get_cmap('tab20')
    for ii in np.nonzero(x_true)[0]:
        if count == 0:
            h1, = ax[1].semilogx(lam_vals, x_true[ii]*np.ones_like(lam_vals),
                                 '--', c=colors(count))
            h2, = ax[1].semilogx(lam_vals, x_vals[ii, :], c=colors(count))
        else:
            ax[1].semilogx(lam_vals, x_true[ii]*np.ones_like(lam_vals), '--',
                           c=colors(count))
            ax[1].semilogx(lam_vals, x_vals[ii, :], c=colors(count))
        count += 1
    ax[1].set_xlabel('$\lambda$')
    ax[1].set_ylabel('Model Parameter ($x_i$)')
    ax[1].legend(handles=[h1, h2], labels=['True', 'Estimated'])


def g(x, a, b=None):
    """Mystery function for Part 2 Example 2."""
    if b is None:
        b = np.arange(len(a))
    y = np.zeros(len(x))
    for ii in range(len(a)):
        y += a[ii]*np.cos(b[ii]*x)
    return y


def plot_pgd2(a, b, x_train, y_train, x_test, y_test, results):
    """Plot results from prox_descent() example 2.

    Parameters
    ----------
    a : array
        Coefficient vector.
    b : array
        Frequency vector.
    x_train : array
        Training input.
    y_train : array
        Training output.
    x_test : array
        Test input.
    y_test : array
        Test output.
    results : list
        Results from prox_descent().

    Returns
    -------
    None.

    """
    # Plot parameter values
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(b, a, 'o')
    ax[0].plot(results[0], '.')
    ax[0].set_xlabel('Frequency ($b_i$)')
    ax[0].set_ylabel('Coefficient ($a_i$)')
    ax[0].legend(['True', 'Estimated'])

    # Plot estimates
    x_vals = np.linspace(0, 4, 1000)
    ax[1].plot(x_vals, g(x_vals, a, b))
    ax[1].plot(x_train, y_train, '.', markersize=10, zorder=3)
    ax[1].plot(x_test, y_test, '.', markersize=10, zorder=3)
    ax[1].plot(x_vals, g(x_vals, results[0]))
    ax[1].set_xlabel('$x_i$')
    ax[1].set_ylabel('$y_i$')
    ax[1].legend(['$g(x)$', 'Train', 'Test', 'Model'])


def plot_lam2(D, a, b, x_train, y_train, x_test, y_test, lam_vals):
    """Plot Lasso results for different values of lambda (example 2).

    Parameters
    ---------
    D : array
        Training data coefficient matrix.
    y : array
        Training data solution vector.
    a : array
        True coefficient vector.
    b : array
        True frequency vector.
    x_train : array
        Training input.
    y_train : array
        Training output.
    x_test : array
        Test input.
    y_test : array
        Test output.
    lam_vals : array
        Regularization parameters.

    Returns
    -------
    None.

    """
    # Solve Lasso problems
    f_train = np.zeros(len(lam_vals))
    f_test = np.zeros(len(lam_vals))
    nonzeros = np.zeros(len(lam_vals))
    a_vals = np.zeros((D.shape[1], len(lam_vals)))
    for ii in range(len(lam_vals)):
        results = prox_descent(D, y_train, lam_vals[ii], print_results=False)
        f_train[ii] = results[2][-1]
        f_test[ii] = np.linalg.norm(g(x_test, results[0]) - y_test)**2/2 \
            + lam_vals[ii]*np.linalg.norm(results[0], 1)
        nonzeros[ii] = np.count_nonzero(results[0])
        a_vals[:, ii] = results[0]

    # Plot function values vs. number of nonzero elements
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    cmap = cm.get_cmap('viridis_r', len(lam_vals[1:-1]))
    norm = plt.Normalize(min(np.log10(lam_vals[1:-1])),
                         max(np.log10(lam_vals[1:-1])))
    ax[0].plot(nonzeros, f_train)
    ax[0].plot(nonzeros, f_test)
    ax[0].scatter(nonzeros[1:-1], f_train[1:-1], c=np.log10(lam_vals[1:-1]),
                  zorder=3, cmap=cmap, norm=norm)
    ax[0].scatter(nonzeros[1:-1], f_test[1:-1], c=np.log10(lam_vals[1:-1]),
                  zorder=3, cmap=cmap, norm=norm)
    ax[0].set_xlabel('Number of Nonzeros in $x$')
    ax[0].set_ylabel('$f(x)$')
    ax[0].legend(['Train', 'Test'])
    fig.colorbar(cm.ScalarMappable(cmap=cmap, norm=norm),
                 label='$\lambda = 10^p$', ax=ax[0],
                 ticks=np.log10(lam_vals[1:-1]))

    # Plot values of nonzero elements in solution
    count = 0
    colors = cm.get_cmap('tab10')
    for ii in range(len(a)):
        if count == 0:
            h1, = ax[1].semilogx(lam_vals, a[ii]*np.ones_like(lam_vals),
                                 '--', c=colors(count))
            h2, = ax[1].semilogx(lam_vals, a_vals[b[ii], :], c=colors(count))
        else:
            ax[1].semilogx(lam_vals, a[ii]*np.ones_like(lam_vals), '--',
                           c=colors(count))
            ax[1].semilogx(lam_vals, a_vals[b[ii], :], c=colors(count))
        count += 1
    ax[1].set_xlabel('$\lambda$')
    ax[1].set_ylabel('Model Parameter ($a_i$)')
    ax[1].legend(handles=[h1, h2], labels=['True', 'Estimated'])


# Part 4 - Logistic Regression


class BinaryLogisticRegression:
    """Logistic regression with trimming"""
    def __init__(self,
                 idata,
                 lam=0.1,
                 inlier_pct=1.0):
        # pass in the data
        self.idata = idata
        self.lam = lam
        self.inlier_pct = inlier_pct

        # create optimization variables
        self.m = self.idata.num_images
        self.k = np.prod(self.idata.image_shape)
        self.A = self.idata.images
        self.y = self.idata.labels
        self.y[self.idata.class_slices[0]] = -1.0
        self.y[self.idata.class_slices[1]] = 1.0

        self.h = np.floor(self.inlier_pct*self.m)
        self.inlier_pct = self.h/self.m
        self.w = np.repeat(self.inlier_pct, self.m)

        self.use_trimming = self.inlier_pct != 1.0

    def objective(self, x):
        """objective function"""
        r = -self.y*self.A.dot(x)
        val = self.w.dot(np.log(1.0 + np.exp(r)))/self.h
        val += 0.5*self.lam*np.sum(x**2)
        return val

    def gradient(self, x):
        """gradient function"""
        r = -self.y*self.A.dot(x)
        grad = -self.A.T.dot(self.w*self.y*np.exp(r)/(1.0 + np.exp(r)))/self.h
        grad += self.lam*x
        return grad

    def hessian(self, x):
        """hessian function"""
        r = self.y*self.A.dot(x)
        hess = (self.A.T*(self.w*np.exp(r) /
                          (1.0 + np.exp(r))**2)).dot(self.A)/self.h
        hess += self.lam*np.eye(self.k)
        return hess

    def gradient_trimming_weights(self, x, normalize_grad=True):
        """gradient w.r.t. the trimming weights"""
        r = -self.y*self.A.dot(x)
        grad = np.log(1.0 + np.exp(r))/self.h
        if normalize_grad:
            grad /= np.max(np.abs(grad))
        return grad

    def update_trimming_weights(self, x, step_size, normalize_grad=True):
        """update trimming weight with given step size"""
        w_new = project_onto_capped_simplex(
                self.w - step_size*self.gradient_trimming_weights(
                        x, normalize_grad=normalize_grad),
                self.h)
        return w_new

    def fit_model(self,
                  x0=None,
                  max_iter=100,
                  tol=1e-6,
                  verbose=False,
                  trimming_step_size=500.0,
                  trimming_normalize_grad=True):
        if x0 is None:
            x0 = np.zeros(self.k)

        x = x0.copy()
        obj = self.objective(x)
        err = tol + 1.0
        iter_count = 0

        if verbose:
            print("initial obj: %7.2e" % obj)

        while err >= tol:
            # newton's step on x
            x_new = x - np.linalg.solve(self.hessian(x), self.gradient(x))
            # trimming step
            if self.use_trimming:
                w_new = self.update_trimming_weights(
                        x_new,
                        trimming_step_size,
                        normalize_grad=trimming_normalize_grad)

            # update information
            obj = self.objective(x_new)
            err = np.linalg.norm(self.gradient(x_new))
            if self.use_trimming:
                err += np.linalg.norm(w_new - self.w)
            np.copyto(x, x_new)
            if self.use_trimming:
                np.copyto(self.w, w_new)

            iter_count += 1
            if verbose:
                print("iter %i, obj %7.2e, err %7.2e" %
                      (iter_count, obj, err))

            # check stop criterion
            if iter_count >= max_iter:
                if verbose:
                    print("reach maximum number of iterations.")
                break

        classifier = BinaryImageClassifier(x, self.idata.image_shape)
        if self.use_trimming:
            outlier_id = self.w < 0.5
            outliers = ImageData(
                    self.idata.images[outlier_id],
                    self.idata.image_shape,
                    labels=self.idata.labels[outlier_id])
        else:
            outliers = None

        return classifier, outliers


class ImageData:
    """Image data used for classification"""
    def __init__(self,
                 images,
                 image_shape,
                 labels=None):
        # pass in the data
        self.images = images
        self.labels = labels
        self.image_shape = image_shape
        self.num_images = self.images.shape[0]

        # organize labels
        if self.labels is None:
            self.unique_labels = None
            self.num_classes = None
            self.class_sizes = None
            self.class_slices = None
        else:
            (self.unique_labels,
             self.class_sizes) = np.unique(self.labels, return_counts=True)
            self.num_classes = self.unique_labels.size
            self.class_slices = sizes_to_slices(self.class_sizes)

            sort_id = np.argsort(self.labels)
            self.images = self.images[sort_id]
            self.labels = self.labels[sort_id]

    def plot_image(self, image_id):
        """plot image data for given image_id"""
        image = self.images[image_id]
        image = image.reshape(self.image_shape)
        plt.imshow(image)


class BinaryImageClassifier:
    """Result from logistic regression"""
    def __init__(self,
                 classifier,
                 image_shape,
                 class_labels=np.array([-1, 1])):
        # pass in the data
        self.classifier = classifier
        self.image_shape = image_shape
        self.class_labels = class_labels

    def modify_class_labels(self, class_labels):
        """change to other labels"""
        self.class_labels = class_labels

    def classify_images(self, images):
        """predict the given image(s)"""
        if images.ndim == 1:
            images = images.reshape(1, images.size)
        num_images = images.shape[0]

        pred = images.dot(self.classifier)
        class0_id = pred < 0.0
        class1_id = pred >= 0.0

        labels = np.empty(num_images, dtype=self.class_labels.dtype)
        labels[class0_id] = self.class_labels[0]
        labels[class1_id] = self.class_labels[1]

        return labels

    def plot_classifier(self):
        """plot the classifier for fun"""
        classifier = self.classifier.reshape(self.image_shape)
        plt.imshow(classifier)
        plt.axis('off')


def sizes_to_slices(sizes):
    """convert sizes to slices"""
    slices = []
    break_points = np.cumsum(np.insert(sizes, 0, 0))
    for i in range(len(sizes)):
        slices.append(slice(break_points[i], break_points[i + 1]))
    return slices


def project_onto_capped_simplex(w, w_sum):
    """project onto the capped simplex"""
    a = np.min(w) - 1.0
    b = np.max(w) - 0.0

    def f(x):
        return np.sum(np.maximum(np.minimum(w - x, 1.0), 0.0)) - w_sum

    x = bisect(f, a, b)

    return np.maximum(np.minimum(w - x, 1.0), 0.0)


def print_blr(A, y, x, str):
    """Print number of observations classified correctly.

    Parameters
    ----------
    A : array
        Data features.
    y : array
        Data labels.
    x : array
        Classifier.
    str : {'training', 'test'}
        Training or test data sets.

    Returns
    -------
    None.

    """
    z = A.dot(x)
    p = [0 if zi < 0 else 1 for zi in z]
    n_correct = sum(p == y)
    print(f'Correctly classified in {str} set: {n_correct}/{len(y)}')


def plot_blr(a, y, x, outliers=None):
    """Plot results for simple binary logistic regression.

    Parameters
    ----------
    a : array
        Data features.
    y : array
        Data labels.
    x : array
        Classifier.
    outliers : ImageData
        Outliers observations.

    Returns
    -------
    None.

    """
    # Separate data into classes and outliers
    a0 = a[y == 0]
    a1 = a[y == 1]
    if outliers is not None:
        a2 = np.array([a[1] for a in outliers.images])
        y2 = np.array([0 if y == -1 else 1 for y in outliers.labels])

    # Plot log-odds
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(a0, x[0] + x[1]*a0, '.')
    ax[0].plot(a1, x[0] + x[1]*a1, '.')
    if outliers is not None:
        ax[0].plot(a2, x[0] + x[1]*a2, 'o', markerfacecolor='w', zorder=1)
    ax[0].plot([0, 10], [0, 0], 'k--')
    ax[0].set_xlabel('Data Features ($a_i$)')
    ax[0].set_ylabel('Log-Odds for $y_i=1$')
    ax[0].legend(['$y_i = 0$', '$y_i = 1$'])

    # Plot probability
    p = lambda a: 1/(1 + np.exp(-(x[0] + x[1]*a)))
    ax[1].plot(a, y, '.')
    ax[1].plot(a, p(a))
    if outliers is not None:
        ax[1].plot(a2, y2, 'o', markerfacecolor='w', zorder=1)
    ax[1].set_xlabel('Data Features ($a_i$)')
    ax[1].set_ylabel('$P(y_i=1)$')
    ax[1].legend(['Class Label ($y_i$)'])
    plt.show()


def plot_mnist(results):
    """Plot MNIST results from gradient_descent().

    Parameters
    ----------
    results : list
        Results from gradient_descent().

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))

    # Plot solution
    ax[0].imshow(results[0].reshape(28, 28))
    ax[0].set_ylabel('Solution ($x^*$)')
    ax[0].set_xticklabels([])
    ax[0].set_yticklabels([])

    # Plot function value
    ax[1].plot(results[2])
    ax[1].set_xlabel('Iteration ($k$)')
    ax[1].set_ylabel('$f(x^k)$')

    # Plot norm of gradient
    ax[2].plot(results[3])
    ax[2].set_xlabel('Iteration ($k$)')
    ax[2].set_ylabel(r'$||\nabla f(x^k)||$')
