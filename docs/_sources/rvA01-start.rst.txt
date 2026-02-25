**A.1 Start**
=====================================================================

**[1t]** Run examples
--------------------------------------------------------------------- 

.. raw:: html

   <hr> 

*rivt file* examples may be run in the cloud or on a local computer. A typical
*rivt* editor layout can be explored online in a `Codesandbox
<https://codesandbox.io/p/devbox/rivt1-dkmqfm?file=%2Frv001-single-doc.txt>`__.
The sandbox permits scrolling through the example rivt file (left panel) and
text doc (right panel) and downloading the text, pdf and html reports. It does
not allow for editing or running the file.

.. figure::  _static/img/ide2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: ide layout

`Codespaces <https://github.com/features/codespaces>`__ is a Microsoft 
secure cloud development environment with a ready-to-use VSCode IDE 
in the web browser. The online example can be scrolled and files may be downloaded, but they cannot 
be edited or run.

An online *rivt* environment with examples that can be edited and run in an
active Codespace is `here <https://github.com/rivt-info/rivt-codespace-examples>`__.  
To edit and run the examples, a GitHub account is required. A free GitHub
account can be set up `here <https://github.com>`__.
The active *Codespace* can be accessed by clicking the green "Code" button on
the GitHub page, selecting the "Codespaces" tab, and then clicking
"rivt-codespace-examples".

.. figure::  _static/img/codespace2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: rivt example repo

Local installation methods include the following options: 

#. portable zip folder (:ref:`rivt-portable`) 
#. uv package manager (:ref:`rivt-uv`) 
#. system Python package (:ref:`rivt-sys`)

*rivt-portable* is recommended for users unfamiliar with Python. 

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

    After installing *uv*, download and run the following command or shell
    script. It installs an isolated *rivt* environment and example files in a
    folder named *rivt-examples* in the users *Home* directory.

    Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 

    OSX and Linux: :download:`rivtuv.sh </_downloads/rivtuv.sh>`
    
.. topic:: Step 3. Run the example program from Pyzo.

    The *rivt* installation includes the `Pyzo <https://pyzo.org/>`. IDE for
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

#. Install Python using `Python installers <https://www.python.org/downloads/>`. 
   The minimum Python version required is Python 3.13.

#. Install *rivtlib* and dependencies 

.. code-block:: bash

    pip install rivtlib
    
A list of the dependencies is :ref:`here <Project requirements>`.


.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-motivation.rst
    rvA03-faq.rst

