**A.1 | Start**
=====================================================================

.. _rivt-start:

**[1]** Getting Started 
------------------------------------------------------------------------------- 

This section covers installation of *rivt* and *rivt doc* examples. As open 
source software you are free to download and modify the program as needed (see 
:ref:`FAQ <Licenses>`). The open source software installation process is built 
around the collection and management of the multiple open source components. This 
section covers three ways to install *rivt*.

#. For users unfamiliar with Python and open source software the simplest way to
   get started is to download the Windows portable zip file (~800 MB). It includes
   everything necessary to run and explore *rivt*. For further details see 
   :ref:`here <rivt-code>`.

#. For users with a `GitHub <https://github.com>`__ account *rivt* can be forked
   and run in a browser using `Codespaces <https://github.com/features/codespaces>`__.
   Further details are :ref:`here <rivt-codespace>`.

#. For users familiar with Python, *rivt* may be installed at the OS level or in
   an isolated environment using *uv*. Further details are :ref:`here <rivt-sys>`.

**[2]** rivt IDE
------------------------------------------------------------------------------- 

*rivt* may be edited in a simple text processor and run from the command line 
but efficient editing and compiling is typically done in an :term:`IDE`. Any IDE 
may be used but *VSCode* support is documented. A typical **VSCode IDE** layout 
editing a *rivt file* is shown below.

.. figure::  _static/img/vscode3.png
    :class: dark-light
    :width: 95%
    :align: center
    :alt: ide layout

    *rivt* files and docs in **VSCode** (click on image to enlarge)


A *rivt file* is a Python file (.py) that imports the 
`rivtlib <https://pypi.org/project/rivtlib/>`__ Python package and includes 
:doc:`rivt markup <rvD01-markup>`. The *rivt file* is in the center editing 
panel[2], the *doc* outputs are in the right panel[3] and the file explorer 
is the far left panel [1]. Text, PDF and HTML output files are accessed in 
the file explorer and displayed within panels. Individual *rivt* sections 
(cells) can be run and output to an interactive terminal during *doc* development. 
Panel locations may be customized by the user. Additional example *rivt files* 
and *docs* are :ref:`here <rivt-tutor>`.

-------------------------------

.. _rivt-code:

**[3]** rivt-code
-------------------------------------------------------------------------------- 

A *rivt-code* installation is recommended for Windows users unfamiliar with
Python. *rivt-code* is a zip file that includes the 
:ref:`rivt-code framework <rivt framework>`. 

 The zip file naming convention is:

.. code-block:: text

    win64-rivt-code-n.n.n[an].zip

where n is a number representing the major, minor and patch release number. An
*an* appended to the version is an *alpha* release where users should expect
missing and incomplete features. The zip file contents must be unzipped into a
directory with read-write access - typically the users home folder or a flash
drive. After unzipping, VSCode and examples are started by clicking on the
*start-rivt.cmd* file.

The primary features of *rivt-portable* are: 

#. simplified, isolated installation
#. package and framework integration
#. installation needs to be updated as a whole, not as individual components. 
#. integration with other programs may be more difficult. 

Releases are updated monthly and may be downloaded from the 
`GitHub repository <https://github.com/rivtlib-dev/rivt-portable/releases/>`__. 

-------------------------------

.. _rivt-codespace:

**[4]** rivt-codespace
-------------------------------------------------------------------------------- 

`VSCode <https://code.visualstudio.com/>`_ is a customizable code editor that
can be run locally or in the cloud. The cloud version of *VSCode* is referred
to as a `Codespace <https://github.com/features/codespaces>`__ . A 
:term:`rivt Codespace` is a *VSCode* cloud environment with *rivt* extensions 
for editing and running *rivt files*. It can be forked (copied) into a personal 
GitHub account. A rivt Codepsace can be forked from 

by following the steps below.  Example rivt files are included.

**Fork a rivt Codespace**

#. Set up a `GitHub account <https://github.com>`__ if needed.    
#. Go to the `rivt Codespace repository <https://github.com/rivt-info/rivt-codespace-examples>`__ 
#. Click the **Fork** button in the upper right corner. This creates a copy 
   of the repository in your GitHub account.
#. Switch to your GitHub account and naviate to the forked repository.
#. Click the green **Code** button.
#. Select the **Codespaces** tab.
#. Click the rivt-codespace-examples option.
#. This creates a Codespace environment in your GitHub account 
    and opens the repository in the online VSCode IDE. The environment 
    includes the rivt packages, extensions and examples. 


.. figure::  _static/img/codespace2.png
    :class: dark-light
    :width: 90%
    :align: center
    :alt: rivt Codespace repo


-------------------------------


.. _rivt-sys:

**[4]** rivt-system
--------------------------------------------------------------------------------

*rivt* may be installed into a system level Python. 

.. topic:: Step 1. Install Python

    Install Python using `Python installers <https://www.python.org/downloads/>`__
    if not already installed. The minimum required version is Python 3.14.

.. topic:: Step 2. install rivtlib and dependencies

    Install *rivtlib* and dependencies using pip

    .. code-block:: bash

        pip install rivtlib
    
A list of the installed dependencies is :ref:`here <rivt-depend>`.

*rivt* may also be installed and isolated environment using the `uv package
manager <https://docs.astral.sh/uv/>`__. The primary advantage of *uv* is the
simplicity of insalling and updating packages while keeping them isolated from
the system Python. 

*rivt-uv* installation is recommended for users with some familiarity with
Python and programming.

.. topic:: Step 1. Install uv

    Different methods for installing *uv* are described
    `here <https://docs.astral.sh/uv/getting-started/installation/#pypi>`__. 

    The recommended method for installing *uv* is from the command line:

    Windows:

    .. code-block:: bash
        
        winget install --id=astral-sh.uv  -e

        or

        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex 

    macOS and Linux:

    .. code-block:: bash
        
        curl -LsSf https://astral.sh/uv/install.sh | sh

.. topic:: Step 2. Create the rivt environment

    After installing *uv*, download and run the following rivt install script.
    It installs an isolated *rivt environment* and example files in a
    folder named *rivt-examples* in the users *Home* directory.

    Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 

    OSX and Linux: :download:`rivtuv.sh </_downloads/rivtuv.sh>`
    
.. topic:: Step 3. Run the example program from Pyzo.

    The *rivt environment* is activated by:
    
    Windows:

    .. code-block:: bash
        
        ./venv/Scripts/activate

    macOS and Linux:

    .. code-block:: bash
        
        source venv/bin/activate

    *rivt* includes the `Pyzo <https://pyzo.org/>`__ IDE for editing and
    running examples. Typing the command *pyzo-example* from the environment
    root will load the example file *rv00-simple-doc.py* where it can be edited
    and run.
    
    The example file can also be run from the command line with the command:

    .. code-block:: bash

        python -m rivt rv001-single-doc.py

    The uv environment can be completely removed with the following commands.

    .. code-block:: bash

        uv deactivate
        rmdir /s /q rivt-examples
        uv cache clean
        
---------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-tutor.rst
    rvA03-file.rst
    rvA04-txt.rst
    rvA05-html.rst
    rvA06-pdf.rst
    rvA07-faq.rst