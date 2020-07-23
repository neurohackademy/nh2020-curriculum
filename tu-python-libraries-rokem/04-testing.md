#  Software testing

Before we move on to release our software, let's take a little detour into
better software engineering. We have written code that does some geometric
calculations. How do we know that it does what we expect it to do?

One way to do so is to write some examples of the code and make sure that the
examples do what they are supposed to do.

We'll use IPython


```
def calculate_area(r):
    """
    Calculates the area of a circle.

    Parameters
    ----------
    r : float or array
        The radius of a single circle or multiple circles

    Returns
    -------
    area : float or array
        The calculated area/s

    Examples
    --------
    >>> calculate_area(1)
    3.141592653589793

    """
    area = np.pi * r **2
    return area


def calculate_circ(r):
    """
    Calculates the circumference of a circle.

    Parameters
    ----------
    r : float or array
        The radius of a single circle or multiple circles

    Returns
    -------
    circ : float or array
        The calculated circumference/s
    """
    circ = 2 * np.pi * r
    return circ

```


To run the tests, we will rely on the
[pytest](https://docs.pytest.org/en/stable/) framework. This allows us to
execute:

    pytest --doctest-modules geometry

And produces the output:

```
jovyan:~/geometry$ pytest --doctest-modules geometry
=========================================================== test session starts ===========================================================
platform linux -- Python 3.7.8, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /home/jovyan/geometry
collected 1 item

geometry/circle.py .                                                                                                                [100%]

============================================================ 1 passed in 0.28s ============================================================

```

Which tells us that one test was run and it passed.