## What next?

You have created a software project that can easily be installed on your
machine, and on other computers. You have future-proofed your software with
tests and made it available through GitHub. What next?

There are a few further steps you can take, though we will not go over them in
detail.

### Making your software widely available

You have uploaded your code to GitHub, which means that people can access the
software and install it. To make it even more accessible and installable through
the `pip` Python package manager, you can go one further step and upload it to
the Python Package Index (PyPI). To do so, it is recommended to use
[twine](https://twine.readthedocs.io/en/latest/), which is a software tool that
builds the needed components and uploads them to PyPI. You can even add a GitHub
action to your repo that [automatically pushes updates to
PyPI](https://github.com/pypa/gh-action-pypi-publish).


### Documenting your software

You've already made the first step towards documentation, by including
docstrings in your function definitions. A further step is to write more
detailed documentation and make the documentation available together with your
software. A system that is routinely used across the Python universe is
[Sphinx](https://www.sphinx-doc.org/en/master/). It is a rather complex system
for generating documentation in many different formats, including a PDF manual,
but also a neat-looking website that includes your docstrings and other pages
you can write. Sphinx could be a topic for a [whole
tutorial](https://matplotlib.org/sampledoc/) by itself. Again, you guessed it,
there is a [GitHub Action](https://github.com/marketplace/actions/sphinx-build)
that will automatically builds your Sphinx documentation and can upload it to a
website.

### Make your software citeable

If you think that others will use the software that you produced in their
research, it can be beneficial to you to get credit for your work through
citations. Unfortunately, this is not as straightforward as getting your journal
articles cited and having this citation tracked and quantified appropriately
(for for further discussion, see
[this](https://www.force11.org/software-citation-principles) article)

To overcome some of these issues, you can create a persistent Digital Object
Identifier (DOI) for your software. For a long screed on this topic, you can
read [what Tal has to say about
that](https://www.talyarkoni.org/blog/2015/03/05/now-i-am-become-doi-destroyer-of-gates/),
but the short of it is that it can make your software properly citeable and the
citations quantifiable. You can easily get a DOI for research objects through
the [Zenodo](https://zenodo.org) website

Some of the objections ("what about peer review?") are further mitigated by
writing an article about your software and getting it published. Once you have
done the hard work of writing the software, and properly testing and documenting
it, that really shouldn't be much more work. This is the principle behind [the
Journal of Open Source Software](https://joss.theoj.org/) (or JOSS; AR is an
editor at this journal), which conducts all of its reviews based on a check-list
of features publishable software should have (does it have a research purpose?
Is it properly tested and documented? And so forth), publically, on GitHub (!).
Once the software (together with a short write up) is reviewed in this way, it
is published as a paper and can be cited in a quantifiable way.


### Being part of the community

#### Specializing late and pushing "up the stack"

Another thing to think about is whether your software should really remain
self-enclosed. If you think that what you have created complements an existing
project, you might consider contributing it to an already-existing project. For
example, if you wrote a particular kind of diffusion MRI model, you might
consider contributing it into [DIPY](https://dipy.org). If you wrote something
that is of broad utility beyond neuroscience, maybe it belongs in a more general
scientific computing library, such as [Scipy](https://scipy.org)? The benefits
of "pushing up the stack" is that more people might use your software this way.
You also gain the benefits of having a community of maintainers help keep your
software up to date and working, as other components of the ecosystem evolve.
Finally, it gives you a community of peers to belong to and collaborat with,
which is fun.

#### Am I obliged to help random strangers use my software?

Now that your software is easy to install, other people might start using it.
Inevitably, they might run into bugs and issues with the software. Some of
them might show up and ask for help. You are not obliged to help random
strangers with anything. If other scientists want you to do work for them,
this could lead to fruitful collaborations, and potentially to co-authorship
on papers resulting from that, but be sure to clarify that before you start
doing a lot of work for them.

On the other hand, it might not be such a bad idea to support use of your
software. For one, one of our goals as scientists is to have impact on the
understanding of the universe, and the improvement of the human condition.
Software the is supported is more likely to have such impact. Furthermore, with
time, users can become developers of the software. Initially, by helping you
expose errors that may exist in the code, and ultimately by contributing new
features. Some people have made careers out of building and supporting a
community of users and developers around software that they write and maintain.

Either way, it's not a bad idea to include a note in your README that sets the
expectations about the level of support and your interest in supporting use of
the software. That way, people know what they can expect when using their
software.