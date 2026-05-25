**A.1 Start**
=====================================================================

**[1]** Getting Started 
------------------------------------------------------------------------------- 

This section covers installation of *rivt* and *rivt doc* examples.
Open source software, including *rivt*, is built with multiple other open
source components. Open source software installation methods are based on this.

For users unfamiliar with Python and open source software the simplest way to
get started is to download Windows portable zip file (800 MB). It includes all
the neccessary components and examples to run and explore *rivt*. For further
details see :ref:`here <rivt-portable>`.

For users with a `GitHub <https://github.com>`__ account *rivt* can be forked
and run in a browser using 
`Codespaces <https://github.com/features/codespaces>`__.
Further details are :ref:`here <Code-rivt>`.

For users familiar with Python, *rivt* may be installed at the OS level or in
an isolated environment using *uv*. Further details :ref:`here <rivt-sys>`.

**[2]** Typical IDE layout 
------------------------------------------------------------------------------- 

*rivt* can be run from the command line but efficient editing and running of
*rivt files* is typically done in an :term:`IDE`. A typical **VSCode IDE**
layout is shown below.



.. figure::  _static/img/ide2.png
    :class: dark-light
    :width: 70%
    :align: center
    :alt: ide layout

    rivt IDE layout in VSCode (click on image to enlarge)

The *rivt file* is the left editing panel, the *text doc* output is in the right
terminal panel and the file explorer is the far left panel. Text, PDF and HTML
output files are accessed in file explorer and displayed within the IDE. When
developing docs, individual sections can be run and output to the terminal
during doc development.  

Additional example *rivt files* and *docs* are here. 

-------------------------------

.. _rivt-portable:

**[3]** Portable rivt
-------------------------------------------------------------------------------- 

A *rivt-portable* installation is recommended for Windows users unfamiliar with
Python. The zip file includes the :ref:`basic rivt framework<rivt framework>`. 
Releases are updated monthly and may be downloaded from the 
`GitHub repository <https://github.com/rivtlib-dev/rivt-portable/releases/>`__. 

 The zip file naming convention is:

.. code-block:: text

    win64-rivt-portable-n.n.n[an].zip

where n is a number representing the major, minor and patch release number. An
*an* appended to the version is an *alpha* release where users should expect
missing and incomplete features. The zip file contents must be unzipped into a
directory with read-write access - typically the users home folder or a flash
drive. After unzipping, VSCode and examples are started with a single shortcut.

The primary advantages of *rivt-portable* are: 

#. simplified installation
#. package integration
#. isolation from system files. 
   
The primary disadvantages are:

#. the installation needs to be updated as a whole, not as individual components. 
3. integration with other programs may be more difficult. 


-------------------------------

.. _Code-rivt:

**[4]** Codespace rivt
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

**[4]** System-rivt
--------------------------------------------------------------------------------

*rivt* may be installed at the Operating System level. 

#.  First install Python using `Python installers <https://www.python.org/downloads/>`__
    The minimum version required by *rivt* is 
    Python 3.14.

#.  Install *rivtlib* and dependencies using pip

.. code-block:: bash

    pip install rivtlib
    
A list of the dependencies is :ref:`here <Project requirements>`.


.. _rivt-uv:

rivt-uv
~~~~~~~~

Finally, rather than installing *rivtlib* at the system level, it can be installed in an
isolated environment using the `uv package manager <https://docs.astral.sh/uv/>`__. 
The primary advantage of *uv* is the simplicity of insalling and updating packages 
while keeping them isolated from the system Python.

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

    rvA02-motivation.rst
    rvA03-docex1.rst
    rvA04-faq.rst

