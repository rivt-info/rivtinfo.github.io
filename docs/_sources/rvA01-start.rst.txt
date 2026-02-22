**A.1 Start**
=====================================================================

**[1t]** Run examples
--------------------------------------------------------------------- 

.. raw:: html

   <hr> 

*rivt file* examples may be run in the cloud or on a local computer. A 
typical IDE layout for running a rivt file is shown below and can be 
explored online `here <https://codesandbox.io/p/devbox/rivt1-dkmqfm?file=%2Frv001-single-doc.py%3A62%2C15>`__. 

.. figure::  _static/img/ide2.png
    :class: dark-light
    :scale: 40%
    :align: center
    :alt: ide layout

The above online example is inactive. A live, cloud based example in Codespace
can be forked (copied), edited and run in a personal GitHub account. GitHub
Codespaces is a cloud-hosted, secure development environment that provides a
ready-to-use workspace in a web browser or local Visual Studio Code IDE. It
requires a free GitHub account.

A rivt Codespace with examples can be forked (copied) into a personal GitHub
from the repo `here <https://github.com/rivt-info/rivt-codespace>`__.

.. figure::  _static/img/codespace2.png
    :class: dark-light
    :scale: 40%
    :align: center
    :alt: ide layout

Local installation methods include the following options: 

#. portable zip folder (:ref:`rivt-portable`) 
#. uv package manager (:ref:`rivt-uv`) 
#. system Python package (:ref:`rivt-sys`). 

*rivt-zip* is recommended for users unfamiliar with Python. An interface for
finding *rivt files* on *GitHub* is :doc:`here <rvE03-ghsearch>`.

.. _rivt-portable:

**[2t]** rivt-portable
--------------------------------------------------------------------- 

.. raw:: html

   <hr> 

rivt-portable is a zipped folder that includes:

#. Python 3.13 with rivt packages 
#. VSCode 1.109 with rivt extensions
#. rivt file examples

The folder may be downloaded `here <https://github.com/rivtlib-dev/rivt-zip>`.
The zip file name is:
 
.. code-block:: text

    rivt-portable-n.n.n.zip

where n-n-n is the major, minor and patch release number. The folder contents
are unzipped into a directory with read-write access - typically the users home
folder. 

The primary advantage of *rivt-zip* is installation simplicity and isolation
from the operating system. Packages and extensions are pre-installed. VSCode
with rivt extensions and examples can be started with a single click. Updated
releases of *rivt-zip* are planned monthly. The primary disadvantage of
*rivt-zip* is that individual files (package components and extensions) are not
easily updated or integrated with other programs.

.. _rivt-uv:

**[3t]** rivt-uv
--------------------------------------------------------------------- 

.. raw:: html

    <hr> 

**rivt-uv** uses the `uv <https://astral.sh/uv/>` package manager to create an
isolated rivt environment and install rivt packages and dependencies not
already installed in the system Python. The primary advantage of *rivt-uv* is
that it allows for updating rivt without affecting the system Python.


The *rivt-uv* installation method is recommended for most users.

.. topic:: Step 1. Install uv

    Install *uv* from 
    `here <https://docs.astral.sh/uv/getting-started/installation/#pypi>`. 

    The recommended method for installing *uv* is from the command line:

    Windows:

    .. code-block:: bash
        
        winget install --id=astral-sh.uv  -e 

    macOS and Linux:

    .. code-block:: bash
        
        curl -LsSf https://astral.sh/uv/install.sh | sh

.. topic:: Step 2. Create the rivt environment

    After installing *uv*, download and run the following command or shell script.     It installs an isolated *rivt* environment and example files in the 
    It will install *rivt* in a folder named *rivtuv* in the users *Home* directory. 

    Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 

    OSX and Linux: :download:`rivtuv.sh </_downloads/rivtuv.sh>`
    

.. topic:: Step 3. Run the example program from Pyzo.

    A *rivt* installation includes the `Pyzo <https://pyzo.org/>`. IDE for
    editing and running examples. The *rivt-uv* installation includes commands
    named *rivt-example.cmd* (Windows) or *rivt-example.sh* (Macos or Linux)
    that start *Pyzo* with the example file *rv001-single-doc.py*.
    
    The example file can also be run from the command line with the command:

    .. code-block:: bash

        python -m rivt rv001-single-doc.py


.. _rivt-sys:

**[4t]** rivt-sys
--------------------------------

.. raw:: html

    <hr>

*rivt* may be installed at the system level. 

#. Install Python using `Python installers <https://www.python.org/downloads/>`. 
   The minimum Python version required is Python 3.13.

#. Install *rivtlib* and dependencies 

.. code-block:: bash

    pip install rivtlib
    
A list of the dependencies is :ref:`here <package requirements>`.

.. _CodeSpace:

**[5t]** CodeSpace
--------------------------------

.. raw:: html

    <hr>




.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-motivation.rst
    rvA03-faq.rst

