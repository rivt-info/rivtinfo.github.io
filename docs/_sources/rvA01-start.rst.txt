**A.1 Start**
=====================================================================

**[1]** Run examples 
------------------------------------------------------------------------------- 

This section outlines steps for installing *rivt* and running examples. *rivt*
is an open source project and, like all open source projects, is built from a
variety of components written by many contributors. Most of the
components are Python libraries but effective use of *rivt* also requires 
separate programs like the IDE `VSCode <https://code.visualstudio.com/>`__. 
For a general overview of *rivt* start :doc:`here <rvB01-overview>`. 

**There are three methods for installing and running *rivt* examples.**

--------------------------------

#.  If you are not familiar with Python or programming, *Portable-rivt* is the 
    recommended method to start with. *Portable-rivt* is a single zip folder 
    that contains a full *rivt* and *VSCode* installation with examples. 
    It is a single download for Windows that requires no installation. 
    Further details are given :ref:`here <rivt-portable>`

#.  If you are familiar with `GitHub <https://github.com>`__ and have an account
    you can run a cloud version of *rivt* in your browser using 
    `Codespace-rivt <https://github.com/features/codespaces>`__.  Further
    details are described :ref:`here <Code-rivt>`.


#.  Finally, if you are familiar with Python and want the most flexible and 
    extensible environment, the recommended method is to install *rivt* at the 
    system level in an isolated environment. *System-rivt* is described 
    :ref:`here <rivt-sys>`.

------------------------------


**[2]** Typical IDE layout 
------------------------------------------------------------------------------- 

.. figure::  _static/img/ide2.png
    :class: dark-light
    :width: 70%
    :align: center
    :alt: ide layout

*rivt* can be run from the command line but efficient editing and running of
*rivt files* is typically done in an :term:`IDE`. A typical **IDE** layout can
be viewed at

`Codesandbox <https://codesandbox.io/p/devbox/rivt1-dkmqfm?file=%2Frv001-single-doc.txt>`__.


This explorable browser example shows the *rivt file* in the left panel, the
text *doc* output in the right panel or second tab, and the file explorer in
the far left panel. Docs (txt, PDF and HTML output files) can be downloaded
from the file explorer including the text, pdf and html reports. The IDE cannot
be used to run files. Setting up a GitHub account and forking Codespace-rivt is
:ref:`needed <Code-rivt>`.

-------------------------------


.. _rivt-portable:

**[3]** Portable-rivt
-------------------------------------------------------------------------------- 

A *rivt-portable* installation is recommended for Windows users
unfamiliar with Python. *rivt-portable* is a zip file :
 
.. code-block:: text

    win64-rivt-portable-n.n.n[an].zip

where n is a number representing the major, minor and patch release number. An
*an* appended to the version is an *alpha* release where users should expect
that features are missing and *rivt markup* syntax may change in the future.
Zip file contents must be unzipped into a directory with read-write access -
typically the users home folder or a flash drive.

The zipped and unzipped file sizes include the following contents and are 
approximately 1GB and 2GB respectively:

.. code-block:: text

    release: rivt-portable-1.0.0a4.zip

    1. Python 3.14 with rivt packages 
    2. VSCode 1.109 with rivt extensions
    3. rivt-1.1.0a4
    4. Example rivt files

Releases may be download from the 
`GitHub repository <https://github.com/rivtlib-dev/rivt-portable/releases/>`__. 

The primary advantages of *rivt-portable* are 

#. simplified installation
#. package integration
#. isolation from system files. 
   
After unzipping, VSCode and examples are started with a single shortcut.

The primary disadvantages of *rivt-portable* are that *rivt* packages
and extensions must be updated by updating the zip file as a whole, and it is
more difficult to integrate with other Python programs. 


--------------------------------


.. _Code-rivt:

**[4]** Codespace-rivt
-------------------------------------------------------------------------------- 

*VSCode* can be run locally or in the cloud. For local installation 
see :ref:`rivt framework`. 

The cloud version is a `Codespace <https://github.com/features/codespaces>`__ . 
A :term:`rivt Codespace` is a *VSCode* cloud environment with *rivt* extensions 
for editing and running *rivt files*.  It can be forked (copied) into 
a personal GithUb account. Github setup is described `here <https://github.com>`__.  

A rivt Codepsace can be forked from 
`this repository <https://github.com/rivt-info/rivt-codespace-examples>`__ 
by following the steps below.  Example rivt files are included.

**Fork a rivt Codespace**

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

    1. Windows portable zip folder (:ref:`rivt-portable`) *rivt-portable* is
    recommended for Windows users unfamiliar with Python.
    
    2. System Python  (:ref:`rivt-sys`) with or without uv manager (:ref:`rivt-uv`) 


-------------------------------


.. _rivt-sys:

**[4]** System-rivt
--------------------------------------------------------------------------------

 

*rivt* may be installed at the system level. 

#.  Install Python using `Python installers <https://www.python.org/downloads/>`__
    The minimum version required by *rivt* is 
    Python 3.14.

#.  Install *rivtlib* and dependencies using pip

.. code-block:: bash

    pip install rivtlib
    
A list of the dependencies is :ref:`here <Project requirements>`.


.. _rivt-uv:

rivt-uv
~~~~~~~~

Rather than installing *rivtlib* at the system level, it can be installed in an
isolated environment using the `uv package manager <https://docs.astral.sh/uv/>`__. 
The primary advantage of *rivt-uv* is the simplicity of updating packages 
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
    rvA03-faq.rst

