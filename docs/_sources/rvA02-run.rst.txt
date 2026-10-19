**A.2 |** Run rivt
=========================

.. _run-rivt:

**[1]** Summary
--------------------------------------------------------------------------------

This section covers installation of *rivt* and running examples. *rivt* files may be
edited in a simple text processor and run from the command line but efficient
editing and compiling is typically done in an :term:`IDE`. Any Python IDE may
be used, but *VSCodium* with extensions is the IDE component used in
*rivtStudio*.

There are three ways to run *rivtlib*.

#. For most users the best way to get started is to download
   *rivtStudio*  (~1 GB zipped, ~2 GB expanded). 
   For further details see :ref:`here <rivt-studio>`.

#. For users familiar with Github or containers in general, a version of 
*rivtStudio* named *rivtRemote* may be run in the browser. 
Further details are :ref:`here <rivt-remote>`.

#. For users familiar with Python, the *rivtlib* packagemay be installed at the 
   system level using *pip* or  *uv*. Further details are :ref:`here <rivt-sys>`.

-------------------------------

.. _rivt-studio:

**[2]** rivtStudio
-------------------------------------------------------------------------------- 

A typical **rivtStudio** layout for editing a *rivt file* is shown
below.

.. figure::  _static/img/vscode3a.png
    :class: dark-light
    :width: 95%
    :align: center
    :alt: ide layout

    rivt files and docs in **VSCode** (click on image to enlarge)


- The :ref:`rivt file <example-file>` is in the center editing panel[blue] 

- The :ref:`text doc <text-doc>` output is in the right panel[brown]. 

- The *file explorer* is the far left panel [green]. 
  *rivt* and *doc* files are accessed in the file explorer. 

- Extension buttons are located on the top and bottom status bars [red]. 

Links to individual *rivt file* sections are provided in both the navigation
panel and in the text doc output. An example 
*rivt file*, *docs* and tutorial are :ref:`here <rivt-tutor>` and may be 
downloaded for local use

**Install rivtStudio**

*rivtStudio*  may be downloaded from
`Github <https://github.com/rivtlib-dev/rivtstudio/releases/>`_.  
The *rivtStudio* zip file naming convention uses semantic versioning. When an "a"
is appended it indicates an alpha release.

.. code-block:: text

    rivtStudio-major#.minor#.patch#

The zip file contents must be unzipped into a directory with read-write access
which is typically the users home folder or a flash drive. After unzipping,
click the *rivtStudio* shortcut to open the interface.

- Open the rivt project folder.
- Accept the trust prompts as needed.
- Navigate to the example report folder
- Open the example rivt file (.py)

Click on the triangle in the upper right of the editor to run the
file and output text, pdf or html docs, depending on the | PUBLISH | setting.
See the :ref:`publish settings <rivt-publish>` for details.

*rivtStudio* includes preinstalled extensions designed to simplify editing 
navigation and running *rivt files*. They are listed in 
:ref:`rivtStudio settings <rivtStudio-settings>` and may be explored and 
modified in the interface. 

-------------------------------


.. _rivt-remote:

**[3]** rivtRemote
-------------------------------------------------------------------------------- 

For users with a `GitHub <https://github.com>`_ account or limitations
on running local software, the best way to get started is to fork and run
:ref:`rivtRemote <rivt-remote>` in a browser. 

`VSCode <https://code.visualstudio.com/>`_ is a customizable code editor that
can be run locally or in the cloud. The cloud version of *VSCode* is referred
to as a `Codespace <https://github.com/features/codespaces>`_ . A 
:term:`rivt Codespace` is a *VSCode* cloud environment with *rivt* extensions 
for editing and running *rivt files*. 

Codespaces are run in a personal GitHub account. When rivtstudiospace is forked
into a personal account and run, an example rivt file is loaded. The example
file may be run and edited in the Codespace and the rivt interface extensions
may be explored.

The first time a rivtstudiospace is run, it may take a few minutes to load and
initialize the environment. After it is set up, it will load in a few seconds.
The same delays apply to running a rivt file. The first time will be a minute
or two to compile the Python files. Subsequent runs will be a few seconds. The
rivtstudiospace environment is persistent and will save any changes made to the
example files.

Steps for running rivtstudiospace are provided in the README `here
<https://github.com/rivtlib-dev/rivtlib>`_.


.. figure::  _static/img/codespace2.png
    :class: dark-light
    :width: 90%
    :align: center
    :alt: rivt Codespace repo


-------------------------------


.. _rivt-sys:

**[4]** rivt System
--------------------------------------------------------------------------------

*rivt* may be installed into a system level Python. 

.. topic:: Step 1. Install Python

    Install Python using `Python installers <https://www.python.org/downloads/>`_
    if not already installed. The minimum required version is Python 3.14.

.. topic:: Step 2. install rivtlib and dependencies

    Install *rivtlib* and dependencies using pip

    .. code-block:: bash

        pip install rivtlib
    
A list of the installed dependencies is :ref:`here <rivt-depend>`.

*rivt* may also be installed and isolated environment using the `uv package
manager <https://docs.astral.sh/uv/>`_. The primary advantage of *uv* is the
simplicity of insalling and updating packages while keeping them isolated from
the system Python. 

*rivt-uv* installation is recommended for users with some familiarity with
Python and programming.

.. topic:: Step 1. Install uv

    Different methods for installing *uv* are described
    `here <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 

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

    After installing *uv*, the following rivt install scripts
    will install an isolated *rivt environment*  folder named *rivt-start* 
    in the users *Home* directory.

    Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 

    OSX and Linux: :download:`rivtuv.sh </_downloads/rivtuv.sh>`

    The uv environment can be completely removed with the following commands.

    .. code-block:: bash

        uv deactivate
        rmdir /s /q rivt-examples
        uv cache clean
    
.. topic:: Step 3. Download example rivt report folders

    Example folders can be downloaded and unzipped through
    `openmodels.info <https://www.openmodels.info>`_ or directly from  
    `Google Cloud <https://drive.google.com/drive/u/1/folders/1NP04tdp3FRAir0ErvL2hlm3YBaFlLk5V>`_ .

    *rivt* also includes the `Pyzo <https://pyzo.org/>`_ IDE for editing and
    running examples. Pyzo may be configured in the uv environment and
    provides an effective environment for running rivt examples. 


