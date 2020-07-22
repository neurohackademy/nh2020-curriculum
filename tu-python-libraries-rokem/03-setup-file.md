# The setup file

The file called `setup.py` is saved in the top level directory and it is a
file that we use to tell Python how to set our software up and how to install
it. We rely on the Python standard library
[setuptools](https://setuptools.readthedocs.io/en/latest/) module to do a
lot of the figuring out for us. The main thing that we will need to do is
to provide setuptools with some meta-data about our software and some information
about the available packages within our software.

For example, here is a minimal setup file (based loosely on an example in the
official python
[packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/)).

```
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

```

Let's look at this. first of all