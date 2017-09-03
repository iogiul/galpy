# Guide for new contributors

[This guide is also part of the [wiki](https://github.com/jobovy/galpy/wiki/Guide-for-new-contributors), which may or may not be more up to date]

If you want to start contributing to galpy, whether to simply open an issue or to add something to the code through a pull request, here are a few guidelines to help you get started. Because galpy has a [very high test coverage](https://coveralls.io/r/jobovy/galpy?branch=master) and [highly complete documentation](http://galpy.readthedocs.org/en/latest/) (and we would like to keep this high), contributing code to the core package can be a little challenging (because all new code requires tests and documentation). This guide provides a few ways to start contributing in a relatively simple manner.

## Contributing without touching the code!

One of the most important ways in which you can contribute to the development of galpy is to use the code, read the documentation, and make sure that everything works as you expect! If you find a bug in the code or an error in the documentation, open an [issue](https://github.com/jobovy/galpy/issues) here on GitHub and the galpy developers will try to help you out. The best way to report an issue is to provide a very simple example that illustrates the issue (a few lines of code, with an explanation of what you expect to get) that can be run by pasting into ipython (that is, include all of the necessary imports). If you get error messages, please post the entire error message, not an abbreviated version of it (if the error message is too long, use something like [pastebin](http://pastebin.com/) to post your error and link to it in the body of the issue). In general, but especially for installation errors, it is useful to know your system's properties (operating system, compilers, python version, version of required packages like the GSL). Please make sure to give your issue a short, informative title!

Another simple way to contribute is to publish your code in which you use galpy and link back to the galpy repository, for example, by posting an example ipython notebook as a [gist](https://gist.github.com/) or have the code of your project in a public GitHub repository. If you use galpy in a paper, feel free to add your paper to the [list of papers using galpy](http://galpy.readthedocs.io/en/latest/#papers-using-galpy) in the documentation (which lives under doc/source/index.rst in the repository) and you can also add a link to your code in this list. This will help other people use galpy in the way that you did!

## First steps

You can contribute to galpy's code itself by making changes to your own fork of galpy and opening a [pull request](https://github.com/jobovy/galpy/pulls) (PR). For any pull request, you should start from a clean fork of the [master branch](https://github.com/jobovy/galpy/tree/master). If there are updates to galpy's master (called the *upstream* master branch) while you are working on your fork, it is best practice to [sync your fork](https://help.github.com/articles/syncing-a-fork/) by pulling in the upstream changes (and also doing this before starting a pull request). Your first, simple PR will be small and fast enough that this shouldn't be an issue.

Because any changes to the core code need to be accompanied by code testing the additions, the simplest place to make a first contribution is the [documentation](galpy.readthedocs.org/en/latest/). galpy's documentation is extended and complex and sure to be out of date at any given time. As you are working with the code and using the documentation, note any places where the documentation is out of date and fix these in a fork. The main pages of the documentation live under ``doc/source`` in the repository (The quick-start guide and the tutorials); the function definitions are grabbed from the functions in the code itself (under ``galpy/``). If you find a mistake in Quick-start guide or in the tutorials, find these pages under ``doc/source`` and make the necessary edits there; if you find an error in the API, you need to find the function in the code and fix its documentation there. If all you are changing is the documentation (no code), please add ``[ci skip]`` to *all* commit messages (this will cause the test suite to not be run, as it is unnecessary).

Another way to contribute is to add a new tutorial in the ``Tutorials`` section of the documentation. While the single tutorial that currently exists in this section is quite elaborate, in general these tutorials could be simple applications from your own work along the lines of the ``Examples`` in the Quick-start guide. Tutorials are added as separate pages under ``doc/source`` and linked into the ``doc/source/index.rst`` file. An example new tutorial could be how you implemented a new potential using the galpy tools (without necessarily adding this potential to galpy).

If you have sphinx installed, you can generate the documentation locally using the ``Makefile`` in ``doc/`` by doing ``make html``. The default setup is to build the documentation in a directory ``BASE/galpy-docs/`` if your galpy repository is ``BASE/galpy``. Especially if you are adding a tutorial or a larger part of documentation, it is good to check that everything looks okay before submitting the pull request.

## Adding to the core package

Now you are ready to start contributing to the core package! galpy has both Python and C code and the simplest additions only concern the Python code. A common addition is to add a new, generally-useful gravitational potential to the ``galpy.potential`` subpackage; this is not too difficult providing the potential is simple and you only add it in Python. [This page](http://galpy.readthedocs.io/en/latest/potential.html#adding-potentials-to-the-galpy-framework) in the documentation lists all of the steps necessary to add a potential to the code. In addition to this, you should add tests to ``nose/test_potential.py`` that test the new potential (note that the consistency between the potential, force, and any implemented second derivatives are tested automatically for the default setting of the new potential). You might have to fiddle with the tolerances of some of the tests in ``nose/test_potential.py`` and ``nose/test_orbit.py``. You should also add a page to the API documentation in ``doc/source/reference/`` with the class definition of the new potential (these are simple two-line pages, follow the lead of one of the existing potentials like [that of the Plummer potential](https://raw.githubusercontent.com/jobovy/galpy/master/doc/source/reference/potentialplummer.rst)).

Other simple changes would be additional ``galpy.orbit.Orbit`` methods (if your favorite orbital property is not included already) or other ways to plot an Orbit. Tests for these would be pretty simple and would be added to ``nose/test_orbit.py``.

This process can be challenging, but the galpy developers are here to help you! If you get stuck, don't hesitate to contact the developers for help or start the pull request and we can help you out that way.

## More ambitious additions

If you are still reading and are still willing to contribute to galpy's code, take a look at the [possible galpy extensions](https://github.com/jobovy/galpy/wiki/Possible-galpy-extensions) listed on the wiki. These are somewhat more complicated (although some are relatively easy), but if they are useful to your work, consider implementing them for general use. Again, the galpy developers are more than happy to help out with getting these into the code!