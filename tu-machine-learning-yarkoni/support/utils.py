# +
import gzip
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from sklearn.model_selection import learning_curve
import nibabel as nib
from nilearn.plotting import plot_roi, plot_stat_map
from nilearn.image import new_img_like


# -

def plot_learning_curves(estimators, X_sets, y, train_sizes, labels=None,
                         errors=True, **kwargs):
    ''' Generate multi-panel plot displaying learning curves for multiple
    predictor sets and/or estimators.
    
    Args:
        estimators (Estimator, list): A scikit-learn Estimator or list of
            estimators. If a list is provided, it must have the same number of
            elements as X_sets.
        X_sets (NDArray-like, list): An NDArray or similar object, or list. If
            a list is passed, it must have the same number of elements as
            estimators.
        y (NDArray): a 1-D numpy array (or pandas Series) representing the
            outcome variable to predict.
        train_sizes (list): List of ints providing the sample sizes at which to
            evaluate the estimator.
        labels (list): Optional list of labels for the panels. Must have the
            same number of elements as X_sets.
        errors (bool): If True, plots error bars representing 1 StDev.
        kwargs (dict): Optional keyword arguments passed on to sklearn's
            `learning_curve` utility.
    '''
    # Set up figure
    n_col = len(X_sets)
    fig, axes = plt.subplots(1, n_col, figsize=(4.5 * n_col, 4), sharex=True,
                             sharey=True)
    
    # If there's only one subplot, matplotlib will hand us back a single Axes,
    # so wrap it in a list to facilitate indexing inside the loop
    if n_col == 1:
        axes = [axes]

    # If estimators is a single object, repeat it n_cols times in a list
    if not isinstance(estimators, (list, tuple)):
        estimators = [estimators] * n_col
    
    cv = kwargs.pop('cv', 10)

    # Plot learning curve for each predictor set
    for i in range(n_col):
        ax = axes[i]
        results = learning_curve(estimators[i], X_sets[i], y,
                                 train_sizes=train_sizes, shuffle=True,
                                 cv=cv, **kwargs)
        train_sizes_abs, train_scores, test_scores = results
        train_mean = train_scores.mean(1)
        test_mean = test_scores.mean(1)
        ax.plot(train_sizes_abs, train_mean, 'o-', label='Train',
                lw=3)
        ax.plot(train_sizes_abs, test_mean, 'o-', label='Test',
                lw=3)
        axes[i].set_xscale('log')
        axes[i].xaxis.set_major_formatter(ScalarFormatter())
        axes[i].grid(False, axis='x')
        axes[i].grid(True, axis='y')
        if labels is not None:
            ax.set_title(labels[i], fontsize=16)
        ax.set_xlabel('Num. obs.', fontsize=14)
        
        if errors:
            train_sd = train_scores.std(1)
            test_sd = test_scores.std(1)
            ax.fill_between(train_sizes, train_mean - train_sd,
                            train_mean + train_sd, alpha=0.2)
            ax.fill_between(train_sizes, test_mean - test_sd,
                            test_mean + test_sd, alpha=0.2)
    
    # Additional display options
    plt.legend(fontsize=14)
    plt.ylim(0, 1)
    axes[0].set_ylabel('$R^2$', fontsize=14)
    axes[-1].set_ylabel('$R^2$', fontsize=14)
    axes[-1].yaxis.set_label_position("right")


def plot_hcp_mmp1(values=None, **kwargs):
    data_dir = Path(__file__).parent / '..' / 'data'
    img = nib.load(data_dir / 'HCP-MMP1_on_MNI152_ICBM2009a_nlin.nii.gz')

    if values is None:
        plot_roi(img, **kwargs)

    else:
        img_data = np.round(img.get_fdata())
        for i in range(360):
            img_data[img_data==(i + 1)] = values[i]
        img = new_img_like(img, img_data, img.affine)
        plot_stat_map(img, **kwargs)
