# Creating shareable Python software

Data science and scientific computing are often taught in interactive
environments like the Jupyter notebook that facilitate exploration and
communication. But these environments do not encourage modularity and
reusability. This leaves many to wonder what the next step is. Once you have
written software that does what you want it to do, how do you reuse this
software? And how do you share the software with others? How do you harden and
future-proof it? What are some best practices for documenting your software for
others to use, and for making it easier for others to install, use and
ultimately contribute back to the software that you have written?

This tutorial focuses on these steps. Through the different steps of the
tutorial we will go from code that we write in an analysis script or notebook,
to a well-documented, properly-tested, installable Python package. We will also
see how we set up continuous integration, as well as a few socio-technical
constructs that make software broadly usable (if not useful...), and enable
collaboration.

# Table of contents

1. [01-from-notebook-to-module.md](From notebook to module)
1. [02-from-module-to-package.md](From module to package)
1. [03-setup-file.md](The `setup.py` file)
1. [04-testing.md](Software testing)
1. [05-continuous-integration.md](Continuous integration)
1. [06-what-next.md](A few next steps)

# LICENSE

Copyright (c) 2020 Ariel Rokem. This tutorial is released under the [CC-BY
4.0](https://creativecommons.org/licenses/by/4.0/) license.