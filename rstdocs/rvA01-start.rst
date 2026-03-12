**A.1 Start**
=====================================================================

**[1t]** Run examples
--------------------------------------------------------------------- 

.. raw:: html

   <hr> 

*rivt file* examples can be run in the cloud or on a local computer. In both 
cases editing and publishing is typically carried out in an IDE. *rivt* 
documentation is focused on *VSCode*, but any IDE may be used. A typical IDE 
layout can be viewed at `Codesandbox
<https://codesandbox.io/p/devbox/rivt1-dkmqfm?file=%2Frv001-single-doc.txt>`__.
The sandbox allows scrolling through an example rivt file (left panel) and
text doc (right panel). Files may be downloaded from the file explorer 
(far left panel) including the text, pdf and html reports. Because the 
is unregistered editor files cannot be edited or processed.

.. figure::  _static/img/ide2.png
    :class: dark-light
    :width: 90%
    :align: center
    :alt: ide layout

*VSCode*  is a customizable `Microsoft IDE <https://code.visualstudio.com/>`__
that can be run locally or in the cloud. The cloud version is 
referred to as a `Codespace <https://github.com/features/codespaces>`__ .
It can be forked (copied) and run in a personal GithUb account
that may be set up `here <https://github.com>`__.  

A :term:`rivt Codespace` is an environment with *rivt* extensions for 
editing and running *rivt files*.  A rivt Codepsace with examples can be forked 
from `this repository <https://github.com/rivt-info/rivt-codespace-examples>`__ 
by following the steps below.

.. topic::  Fork a *rivt Codespace* in the cloud 

    .. code-block:: text

        1. Click the Fork button in the upper right corner. 
           This creates a copy of the repository in your GitHub account.
        2. Switch to your GitHub account and open the forked repository
        3. Click the green Code button
        4. Select the Codespaces tab
        5. Click the rivt-codespace-examples option.
        6. This creates a Codespace environment in your GitHub account 
           and opens the repository in the online VSCode IDE. The environment 
           includes the rivt packages and extensions needed to run and 
           publish rivt docs and files.

.. figure::  _static/img/codespace2.png
    :class: dark-light
    :width: 90%
    :align: center
    :alt: rivt Codespace repo

.. topic::  Local installation methods

    1. Windows portable zip folder (:ref:`rivt-portable`) 
    2. uv package manager (:ref:`rivt-uv`) 
    3. system Python package (:ref:`rivt-sys`)

    *rivt-portable* is recommended for Windows users unfamiliar with Python

.. _rivt-portable:

**[2t]** rivt-portable
--------------------------------------------------------------------- 

.. raw:: html

   <hr> 

A *rivt-portable* installation is recommended for Windows users
unfamiliar with Python. The portable zip filename is :
 
.. code-block:: text

    win64-rivt-portable-n.n.n[an].zip

where n-n-n is the major, minor and patch release number. An *an* appended to
the version is an *alpha* release, which indicates that features are missing
and *rivt markup* syntax may change in the future. Zip file contents must be
unzipped into a directory with read-write access - typically the users home
folder or a flash drive. The zipped and unzipped file sizes are approximately
1GB and 2GB respectively, and the contents include:

.. code-block:: text

    release: rivt-portable-1.0.0a4.zip

    1. Python 3.14 with rivt packages 
    2. VSCode 1.109 with rivt extensions
    3. rivt-1.1.0a4
    4. Example rivt files

Releases may be download from  `GitHub <https://github.com/rivtlib-dev/rivt-portable/releases/>`__. 

The primary advantages of *rivt-portable* are simplified installation, package
integration, and isolation from system files. VSCode and examples are started
with a single shortcut.

The primary disadvantages of *rivt-portable* are that *rivt* packages
components, extensions must be updated as a single zip file, and that it is
more difficult to integrate with other Python programs. Each zip file is about
300 MB and releases are planned monthly.

.. _rivt-uv:

**[3t]** rivt-uv
--------------------------------------------------------------------- 

.. raw:: html

    <hr> 

**rivt-uv** uses the `uv <https://astral.sh/uv/>`__ package manager to create an
isolated rivt environment and install rivt packages and dependencies not
already installed in the system Python. The primary advantage of *rivt-uv* is
that it allows for updating rivt without affecting the system Python.


The *rivt-uv* installation method is recommended for most users.

.. topic:: Step 1. Install uv

    Install *uv* from 
    `here <https://docs.astral.sh/uv/getting-started/installation/#pypi>`__. 

    The recommended method for installing *uv* is from the command line:

    Windows:

    .. code-block:: bash
        
        winget install --id=astral-sh.uv  -e 

    macOS and Linux:

    .. code-block:: bash
        
        curl -LsSf https://astral.sh/uv/install.sh | sh

.. topic:: Step 2. Create the rivt environment

    After installing *uv*, download and run the following command or shell
    script. It installs an isolated *rivt* environment and example files in a
    folder named *rivt-examples* in the users *Home* directory.

    Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 

    OSX and Linux: :download:`rivtuv.sh </_downloads/rivtuv.sh>`
    
.. topic:: Step 3. Run the example program from Pyzo.

    The *rivt* installation includes the `Pyzo <https://pyzo.org/>`__ IDE for
    editing and running examples. Typing the command *pyzo-example* from the uv
    environment root will load the example file *rv00-simple-doc.py* where it
    can be edited and run.
    
    The example file can also be run from the command line with the command:

    .. code-block:: bash

        python -m rivt rv001-single-doc.py

    The uv environment can be completely removed with the following commands.

    .. code-block:: bash

        uv deactivate
        rmdir /s /q rivt-examples
        uv cache clean

.. _rivt-sys:

**[4t]** rivt-sys
--------------------------------

.. raw:: html

    <hr>

*rivt* may be installed at the system level. 

#.  Install Python using `Python installers <https://www.python.org/downloads/>`__
    if not already installed. The minimum version required by *rivt* is 
    Python 3.13.

#.  Install *rivtlib* and dependencies 

.. code-block:: bash

    pip install rivtlib
    
A list of the dependencies is :ref:`here <Project requirements>`.


.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-motivation.rst
    rvA03-faq.rst

