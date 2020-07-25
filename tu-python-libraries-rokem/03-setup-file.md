# The setup file

The file called `setup.py` is saved in the top level directory of our package
and it is a file that we use to tell Python how to set our software up and how
to install it. We rely on the Python standard library
[setuptools](https://setuptools.readthedocs.io/en/latest/) module to do a lot of
the figuring out for us. The main thing that we will need to do is to provide
setuptools with some meta-data about our software and some information about the
available packages within our software.

For example, here is a minimal setup file (based loosely on an example in the
official python
[packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/)).

```
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="geometry",
    version="0.0.1",
    author="Ariel Rokem",
    author_email="author@example.com",
    description="Calculating geometric things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.6',
    install_requires=["numpy"]
)

```

Let's look at this. The core of this file is a call to a function called
`setup`. This function has [many different options](https://setuptools.readthedocs.io/en/latest/setuptools.html#command-reference). One of these options is `install`, which would take all the steps needed
to properly install the software in the right way into your Python path:

    python setup.py install

While developing the software you will often want to install the software in "editable" mode:

    python setup.py develop

In this case, the software is not directly installed into your Python path.
Instead a symbolic link is made from your Python path to your present working
directory. That means that when you make changes to the code in your present
working directory, you don't need to reinstall the software to propagate the
changes to programs that are using this software.

## Contents of a setup.py file

The first thing that happens in the `setup.py` is that a long_description is
read from a README file. So, we'll need to add that to our project before we
keep going.

Let's write something informative:

```
# README.md

# geometry

This is a library of functions for geometric calculations.

# Contributing

We welcome contributions from the community. Please create a fork of the
project on GitHub and use a pull request to propose your changes. We strongly encourage creating
an issue before starting to work on major changes, to discuss these changes first.

# Getting help

Please post issues on the project GitHub page.

```

The second thing that happens is a call to the setup function. The function takes
several key-word arguments:

- These are general metadata items:  nemae of the software

    name="geometry",
    author="Ariel Rokem",
    author_email="author@example.com",
    description="Calculating geometric things",
    long_description=long_description,

This one makes sure that the long description gets properly rendered in web
pages describing the software (for example in the Python package index, PyPi)

    long_description_content_type="text/markdown",

The classifiers used here are used to classify the software within PyPI, so that
interested users can more easily find it.

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],

Note in particular the license classifier. If you intend to share the software
with others, please put a license on your software. Please use a standard
OSI-approved license, and not one of your own design. If you are interested in
providing the software in a manner that would allow anyone to do what they want
with the software, including commercial applications, while maximally limiting
your liability and the use of your name (or your institution's), the MIT license
is not a bad way to go. Jake Vanderplas wrote a very useful blog post on the
topic of scientific software licensing [here](https://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/).

The next item is the version of the software. It is a good idea to use
the [semantic versioning conventions](https://semver.org/), which communicates
to potential users how stable the software is, and whether changes have happened
that dramatically change the way in which the software operates:

    version="0.0.1",

The next item points to the GitHub repository for the software. We haven't
created that, but we'll do that soon:

    url="https://github.com/arokem/geometry",

The next item is a call to a setuptools function that automatically traverses
the filesystem in this directory and finds the packages and sub-packages that
we have created:

    packages=find_packages(),

The last two items define the dependencies of the software. The first is the
version of Python that is required for the software to run properly. The other
is a list of other libraries that are imported within our software and that need
to be installed before we can install and use our software. In this case, it's
just the `numpy` library:

    python_requires='>=3.6',
    install_requires=["numpy"]


## Before we move on

At this point, our project is starting to take shape. This is a good time
to stop and create a GitHub repository for the project, linking it up with
a local git repo.

On GitHub, we create a new emptry repository, which we call `geometry`, we
clone this empty repository into our machine and start adding things into it.

When we are done, our file system should look like this:

| geometry/
| ├── LICENSE
| ├── README.md
| ├── geometry
| │   ├── __init__.py
| │   ├── __pycache__
| │   │   ├── __init__.cpython-37.pyc
| │   │   └── circle.cpython-37.pyc
| │   └── circle.py
| └── setup.py

The only file we haven't seen before  is the LICENSE file. We can copy over the
MIT license text from the [OSI website](https://opensource.org/licenses/MIT),
adjusting year and copyright.

We can add all these files (maybe we also need a .gitignore?) and then push
this into our repository on GitHub. Hooray!! 🎉 We are ready to share with others!

But before we throw a party, let's do a bit more software engineering, to make
sure that our software really does what we intend for it to do.
