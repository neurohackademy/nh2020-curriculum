# Continuous integration

Having tests is nice. But tests are not useful unless you run them. And you'd
ideally like to run them often. Continuous integration (CI) means that you have
systems in place that automatically run the tests for you every time that
changes are made to the software.

Here, we will use GitHub's built-in system for CI called GitHub Actions. The
system is actually very flexible and can allow you to configure GitHub to
run a variety of different operations triggered on a large range of events
in your repository (including regularly scheduled "cron" jobs).

GitHub Actions works by reading configuration files that are stored in a special
directory in your repository in `.github/workflows`. These files are written
in the YAML markup language.

Here, we'll use a pre-configured workflow for Python packages and change it
slightly for our purposes. GitHub allows you to edit files through the browser
and we will use this capability to edit the pre-configured configuration to
do what want it to do. To do so, we click through the Actions menu and choose
the "Python Package" action. This will open the editor and allow us to tweak.

We'll tweak the following items:

- The versions of Python tested: we'll use only 3.6 and 3.7. Remember that we
  set the software up to require version after 3.6
- Install the software with `python setup.py install`. There are other ways to
  install software, but will not consider them here. For more on that, you can
  look [here](https://pip.pypa.io/en/stable/)
- Run `pytest --doctest-modules geometry` to emulate what we did locally.


In the end the configuration will look like this:

    name: Python package

    on:
    push:
        branches: [ master ]
    pull_request:
        branches: [ master ]

    jobs:
    build:

        runs-on: ubuntu-latest
        strategy:
        matrix:
            python-version: [3.6, 3.7]

        steps:
        - uses: actions/checkout@v2
        - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
            python-version: ${{ matrix.python-version }}
        - name: Install
        run: |
            python -m pip install --upgrade pip
            pip install pytest flake8
            python setup.py install
        - name: Lint with flake8
        run: |
            # stop the build if there are Python syntax errors or undefined names
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        - name: Test with pytest
        run: |
            pytest --doctest-modules geometry


Once the workflow is commited to the repository, this workflow is triggered and
the steps in the configuration file are executed. Note that in addition to
running our tests, this configuration runs flake8, which checks the code for its
compliance with standards for formatting, and other best practices in how the
code is constructed. Given feedback from the CI system, we might need to address
some of these issues, before we can move on. But once the CI is all green, we
can see how this works in practice. Consider what happens when a new piece of
code is added.

Here, we will make a new branch, called `new_test` and add a test for the other
function:

```
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

    Examples
    --------
    >>> calculate_circ(1)
    3.141592653589793
    """
    circ = 2 * np.pi * r
    return circ
```

Let's commit this code and see what kind of feedback we get. We go through the
process: commit the code, push it to GitHub and make a pull request. After a
short while, we get our feedback back. We will also get an email telling us
that the test failed. Fixing the code:

```
# snip

    Examples
    --------
    >>> calculate_circ(1)
    6.283185307179586

# snip
```

And committing then pushing the code to GitHub now fixes the CI. Once the CI is
green, we can safely merge the PR. This pattern can save you a lot of pain. It
is much better to prevent errors from being introduced in the first place, than
to try fixing errors after they have already broken your software.

This is a good pattern to use yourself, but it becomes crucial when you are
collaborating with others. This is because it lets you vet new additions by
others in an automated manner. If you keep all of your code tested in this way,
it will also tell you when a new contribution is breaking existing functionality
of the software.
