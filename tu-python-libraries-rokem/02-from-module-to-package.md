# From module to package

In the previous part, we saw how to create modular code that can be reused. The
next level of reusability is to create a library that can be installed and
imported across multiple projects.

Again, let's consider what happens when `import geometry` is called. If there is
no file called `geometry.py` in the present working directory, the next thing
that Python will look for is a Python package called `geometry`. What is a
Python package? It's a folder that has a file called `__init__.py`. This can be
imported just like a module, so if the folder is in your present working
directory, importing it will execute the code in `__init__.py`. For example, if
you were to put the functions you previously had in `geometry.py` in
`geometry/__init__.py` you could import them from there.

More typically, a package might contain different modules that each has its own
code. For example, we might organize our package like this:

| .
| └── geometry
|     ├── __init__.py
|     └── circle.py

With the code that we previously had in `geometry.py` now in our `circle.py`
module of the geometry package. To make the names in `circle.py` available to us
we can import it explicitely like this:

    >>> from geometry import circle
    >>> circle.calculate_area

Or we can have the `__init__.py` file import it for us:

```
# __init__.py

from .circle import calculate_area, calculate_circ
```

This way, we can import our functions like this:

    >>> from geometry import calculate_area


This also means that if we decide to add more modules into the package, the
`__init__.py` file can manage all the imports from these modules. It can also
perform other setup steps that you might want to do whenever you import the
package.

Note: as your package becomes complex, you can create sub-packages by adding
more directories with more `__init__.py` files into your package.

Now that you have your code in a package, you'll want to install the code in
your machine, so that you can import the code from anywhere on your machine (not
only from this particular directory) and eventually also so that others can
easily install it and run it on their machines.

To do so, we need to understand one more thing about the `import` statement. If
`import` cannot find a module or package locally in the present working
directory, it will proceed to look for this name somewhere in the Python path.
The Python path is a list of file-system locations that Python uses to search
for packages and modules to import. You can see it (and manipulate it!) here:

    >>> import sys
    >>> sys.path

So, we need to copy the code into one of the file-system locations that are
stored in this variable. But no so fast! To not make a mess, let's instead let
Python do this for us. The
[`setuptools`](https://setuptools.readthedocs.io/en/latest/) library, part of
the Python standard library that ships with the Python interpreter, is intended
specifically for packaging and setup of this kind of thing. The main instrument
for `setuptools` operations is the `setup.py` file, which we will look at next.
