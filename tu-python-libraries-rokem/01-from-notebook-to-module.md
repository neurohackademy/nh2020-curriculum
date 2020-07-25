# Creating Python shareable Python libraries

The goal of this tutorial is to show you the way to make your code
more modular, more shareable and more robust.

## Not all code needs to be shareable

Not every analysis that you do on your data needs to be easy for others to use.
Ideally, if you want your work to be reproducible, it will be possible for
others to run your code and get the same results. But this is not what we are
talking about here. In the course of your work, you will sometimes find that you
are creating pieces of code that are useful for you in more than one place, and
may also be useful to others. For example, collaborators in your lab, or other
researchers in your field. These pieces of code deserve to be written and
shared in a manner that others can easily adopt them into their code. To do
so, the code needs to be packaged into a library. Here, we will look at the
nuts and bolts of doing that.


## From notebook to module

In the course of my work on analysis of diffusion MRI data, I have written the
following code in a script or a Jupyter notebook:

```
# analysis.ipynb or analysis.py
import numpy as np
import pandas as pd

blob_data = pd.read_csv('./input_data/blob.csv')

blob_radius = blob_data['radius']

blob_area = np.pi * blob_radius ** 2
blob_circ = 2 * np.pi * blob_radius

pd.DataFrame(dict(area=blob_area, circ=blob_circ)).to_csv('./output_data/blob_properties.csv')
```

Unfortunately, this code is not very reusable, even while the results may be
perfectly reproducible (provided the input data is accessible).

This is because it mixes file input and output with computations and different
computations with each other (e.g., computation of area and circumference).

The first step is to identify what are reusable components of this script and
to move these components into a module. For example, here the calculation of
area and circumference seem like they could each be (separately) useful in many
different contexts.

Let's isolate them and rewrite them as functions:

```
# analysis.ipynb or analysis.py
import numpy as np
import pandas as pd


def calculate_area(r):
    area = np.pi * r **2
    return area


def calculate_circ(r):
    circ = 2 * np.pi * r
    return circ

blob_data = pd.read_csv('./input_data/blob.csv')
blob_radius = blob_data['radius']
blob_area = calculate_area(blob_radius)
blob_circ = calculate_circ(blob_radius)
pd.DataFrame(dict(area=blob_area, circ=blob_circ)).to_csv('./output_data/blob_properties.csv')
```

In the next step, we might move these functions out into a separate file,
and document what they do:

```
# geometry.py
import numpy as np

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

Note that nothing is accidental about these docstrings. They carefully comply
with the [numpy docstring
guide](https://numpydoc.readthedocs.io/en/latest/format.html). This guide
provides details about how to write documentation so that: 1) People who are
used to reading documentation formatted in this way know how to read your
documentation; and 2) Programs that automatically process documentation do what
they are supposed to do with your docstrings. For example in converting the
docstrings into webpages for online documentation (more about that later).

## Importing and using functions

Before we continue, we need to know a bit about what happens when you
call `import` statements in Python. When you type call `import geometry`,
Python starts by looking for a file called `geometry.py` in your present working
directory.

That means that if you saved `geomtry.py` alongside your analysis script, you
can now rewrite that as:

```
# analysis.ipynb or analysis.py
import geometry as geo
import pandas as pd

blob_data = pd.read_csv('./input_data/blob.csv')
blob_radius = blob_data['radius']
blob_area = geo.calculate_area(blob_radius)
blob_circ = geo.calculate_circ(blob_radius)
pd.DataFrame(dict(area=blob_area, circ=blob_circ)).to_csv('./output_data/blob_properties.csv')
```

This is already good, because now you can import and reuse these functions
across many different analysis scripts without having to copy this code
everywhere. In summary: you have transitioned this part of your code from a
one-off notebook or script to a module. Next, let's see how you transition from
a module to a library.