.. _installation:

Installation
************

Following Sections provide overview on how to install the package.

.. contents:: Contents
   :backlinks: top
   :local:


Using This Project Template
===========================

Use the following guide to fully take advantage of this project template:

1. Install Pyenv_ (only if not already present):

   A. Download and install using bash:

      .. code-block:: console

         $ curl https://pyenv.run | bash

   B. Add the following lines to your :file:`~/.bashrc` to make pyenv known to
      your system:

      .. code-block:: console

	 $ export PATH="~/.pyenv/bin:$PATH"
	 $ eval "$(pyenv init -)"
	 $ eval "$(pyenv virtualenv-init -)"

   C. Open a new shell, or :code:`source ~/.bashrc` in your current shell

   D. Install the Python build dependencies for your platform, using one of the
      commands listed in the `official instructions`_. For example, on a recent
      Ubuntu this would be:

      .. code-block:: console

	 $ sudo apt update && sudo apt install -y make build-essential libssl-dev zlib1g-dev \
	 $ libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
         $ libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

2. Create a new folder representing your repo/published package using `kebab case`_:

   .. code-block:: console

      $ mkdir my-project

3. Install the desired `python versions`_ using pyenv:

   .. code-block:: console

      $ pyenv install 3.10.4
      $ pyenv install 3.9.13
      $ pyenv install 3.8.13


4. Change into the new project folder and ctivate the desired `python versions`_

   .. code-block:: console

      $ cd my-project
      $ pyenv local 3.10.4 3.9.13 3.8.13


5. Clone the `hpmpy-template` into your new local repo folder:

   .. code-block:: console

      $ git clone https://github.com/tZ3ma/hpmpy-project my-project


6. Install poetry (only if not already present)

   1. Download the poetry install script and run it

      .. code-block:: console

         $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

   2. Open a new shell or :code:`source ~/.poetry/env` in your current shell


7. Install nox:

   .. code-block:: console

      $ pip install --user --upgrade nox

8. Rename all hpmpy instances after your project using git grep by replacing
   :code:`MY-PROJECT` below:

   .. code-block:: console

      $ git grep -lz hpmpy-project | xargs -0 sed -i -e "s/hpmpy-project/MY-PROJECT/g"
      $ git grep -lz hpmpy_project | xargs -0 sed -i -e "s/hpmpy-project/MY_PROJECT/g"

9. Rename the :file:`src/hpmpy_project` package folder by replacing
   :code:`MY_PROJECT` below:

      .. code-block:: console

         $ mv src/hpmpy_project src/MY_PROJECT

10. Install your package using poetry:

    .. code-block:: console

       $ poetry install

11. Run your first nox sessions:

    .. code-block:: console

       $ nox

12. Bump your package version to 0.1.0:

    .. code-block:: console

       $ poetry version minor

13. Create a remote repo on Github_

14. Integrate your PyPI_  and TestPyPI_ API-Token_ as explained in the
    :ref:`release workflow <workflows_releases>` sections.

15. Add, commit and push all changes to your new remote repo:

    .. code-block:: console

       $ git add -A
       $ git commit -m "Project Initialization"
       $ git remote add origin https://github.com/GIT-USER/MY-PROJECT.git
       $ git branch -M main
       $ git push -u origin main

16. All set up! You can now branch of your default branch

17. Make sure to checkout the :ref:`Workflows Developer Guide <workflows>` to
    acquaint yourself with the usage of Poetry_, Nox_ and Github_.




Development Install of Your Package Created with this Template
==============================================================

1. Install Pyenv_ (only if not already present)
2. Install Poetry_ and Nox_ (only if not already present)
3. Clone the repo to a local directory (uses package name if square bracket
   part is omitted):

   .. code-block:: console

      $ git clone https://github.com/tZ3ma/hpmpy-project [hpmpy-project-develop]

4. Install the package with development requirements:

   .. code:: console

      $ poetry install

5. Auto generate and activate a virtual environment where the installed package
   is installed:

   .. code:: console

      $ poetry shell

6. (Optional) Alternatively, you can now run an interactive Python session, or
   the command-line interface if your package supports it:

   .. code:: console

      $ poetry run python
      $ poetry run MY-PROJECT


User Install of  Your Package Created with this Template
========================================================

Use the following advice to install the standard / user version of this
package, once you have **at least one push** on yout **main** and **develop**
branch (so the respective :ref:`release workflows <workflows_releases>` are
triggered).

Linux
-----

Install using a console with your virtual environment activated:

Latest Stable Version
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

   $ pip install MY-PROJECT

Latest Development Version (potentially unstable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ MY-PROJECT

This installs the TestPyPI_ version of :code:`MY-PROJECT` while resolving the dependencies on PyPI_.

.. _PyPI: https://pypi.org/
.. _TestPyPI: https://test.pypi.org/
.. _Poetry: https://python-poetry.org/
.. _Nox: https://nox.thea.codes/
.. _Pyenv: https://github.com/pyenv/pyenv
.. _official instructions: https://github.com/pyenv/pyenv/wiki/Common-build-problems
.. _kebab case: https://en.wiktionary.org/wiki/kebab_case
.. _python versions: https://www.python.org/downloads/
.. _Github: https://github.com/
.. _API-Token: https://pypi.org/help/#apitoken
