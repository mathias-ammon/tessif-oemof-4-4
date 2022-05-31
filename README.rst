hpmpy-project
====================================================================================================

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/hpmpy_project.svg
   :target: https://pypi.org/project/hpmpy_project/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/hpmpy_project.svg
   :target: https://pypi.org/project/hpmpy_project/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/hpmpy_project
   :target: https://pypi.org/project/hpmpy_project
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/hpmpy_project
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/hpmpy_project/latest.svg?label=Read%20the%20Docs
   :target: https://hpmpy_project.readthedocs.io/
   :alt: Read the documentation at https://hpmpy_project.readthedocs.io/
.. |Tests| image:: https://github.com/tZ3ma/hpmpy_project/workflows/Tests/badge.svg
   :target: https://github.com/tZ3ma/hpmpy_project/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/tZ3ma/hpmpy_project/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/tZ3ma/hpmpy_project
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

Newb tweaked non-typing version of the excellent Hypermodern-Python_ project
foundation proposed by `Claudio Jolowicz <cj>`_

Installation
------------

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

15. Add coverage reports using Codecov_:

    1. Go to the Codecov_ website and login using your Github_ account.

    2. Click on ``not yet setup`` and copy the API-Token in point 2.

    3. Make it a Secret_ in your remote repo called ``CODECOV_TOKEN``

    4. Your next push to the remote repo  will trigger the test workflow in
       :file:`.github/workflows/tests.yml` which will then automatically upload
       the coverage report to Codecov_

15. Install and add git pre-commit hooks:

    .. code-block:: console

       pip install --user --upgrade pre-commit
       pre-commit install

16. Add, commit and push all changes to your new remote repo:

    .. code-block:: console

       $ git add -A
       $ git commit -m "Project Initialization"
       $ git remote add origin https://github.com/GIT-USER/MY-PROJECT.git
       $ git branch -M main
       $ git push -u origin main

17. All set up! You can now branch of your default branch

18. Make sure to checkout the :ref:`Workflows Developer Guide <workflows>` to
    acquaint yourself with the usage of Poetry_, Nox_ and Github_.


License
-------
Distributed under the terms of the `MIT license`_,
*hpmpy-project* is free and open source software.

.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _TestPyPI: https://test.pypi.org/
.. _pip: https://pip.pypa.io/
.. _Hypermodern-Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
.. _cj: https://github.com/cjolowicz
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://hpmpy_project.readthedocs.io/en/latest/usage.html
