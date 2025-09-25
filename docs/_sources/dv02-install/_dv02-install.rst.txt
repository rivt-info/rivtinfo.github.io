2. Installation
==================   


**[01]** Installation types
----------------------------------

.. raw:: html

    <hr>

.. topic:: *rivt* 

    *rivt* is a Python project that includes `rivtlib <https://www.rivt.info>`_
    and other :doc:`Python packages </dv02-install/python>`.  When *rivt* 
    is installed, *rivt docs and reports* may be edited and published 
    using a text editor.

    See :ref:`rivt-uv <rivt-uv>` for uv install
    
    See :ref:`rivt-system <rivt-system>` for system install  

.. raw:: html

    <hr>


.. topic:: *rivt framework* 

    The *rivt framework* includes *rivt* and additional programs installed
    separately. It includes important productiviy tools for editing, document
    control and diagramming.
    
    #. *VSCode and extensions* for editing and collaboration.
    #. *Git and GitHub* for version control and document sharing.
    #. *LaTeX* for precise typesetting.
    #. *QCAD* for diagramming.

.. raw:: html

    <hr>

.. topic:: *rivt.zip* 

    A single folder, portable version of *rivt* integrated with *VSCode*.

.. raw:: html

    <hr>


.. _rivt-uv:

**[02]** Install *rivt-uv*
----------------------------------

.. raw:: html

    <hr>

This method for installing *rivt* is recommended for most users. The procedure
for Windows is shown below. Other OS installs are similar.

**Step 1. Install uv**

Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 
The recommended method for installing *uv* on Windows is: 

.. code-block:: bash
      
    winget install --id=astral-sh.uv  -e 


**Step 2. Create rivt environment** After installing *uv*, run the
following commands to set up and activate an isolated *rivt* environment
(omit the explanatory REM lines). The commands execute the following steps:

#. names the *uv* environment in the first SET command
#. changes to the %HOMEPATH% (User) folder
#. removes any prior existing environment, cache and folders.
#. downloads the rivt install file.
#. creates a new environment and activates it.

The commands may be downloaded and run from the command file
:download:`rivt-uv.cmd </_downloads/rivt-uv.cmd>`. 

.. code-block:: bash
    
    @echo on
    REM clear existing project, download rivt-install, create new venv
    REM set rivt folder
    SET rvfolder=rivt-doc1
    REM go to home directory
    cd %HOMEPATH%
    REM double check deactivation for dev purposes
    uv deactivate
    REM double check that old project is deleted
    rmdir /s /q %rvfolder%
    REM clean cache for dev purposes
    uv cache clean
    REM set up venv
    mkdir %rvfolder%
    REM change directory
    cd %rvfolder%
    REM download rivt install file
    curl  https://raw.githubusercontent.com/rivt-info/rivt-win-install/refs/heads/main/rivt-install.cmd -O   
    REM make venv
    uv venv
    cmd /k

**Step 3. Install rivt** 

Within the activated *uv* environment run the following set of commands
to install *rivt* and an example *rivt file*. The commands execute the following
steps:

#. install *rivt* in the *uv* environment.
#. creates an *example1* folder
#. downloads a  *rivt file* into the *example1* folder

.. code-block:: bash

    @echo on
    REM run this file - rivt-install
    REM activates venv, installs rivt, downloads example
    REM activate venv
    .venv/scripts/activate
    REM install rivt from GitHub
    uv pip install git+https://github.com/rivtlib-dev/rivtlib
    REM download example project into new folder
    mkdir example1
    cd example1
    curl https://raw.githubusercontent.com/rivt-info/rivt-simple-single-doc/refs/heads/main/rv0000-simple-single-doc.py -O
    curl https://github.com/rivt-info/rivt-simple-single-doc/blob/main/beam.png?raw=true -O -L
    REM run example with (no quotes )"python rv0000-simple-single-doc.py"

The commands may be executed by running the command file downloaded in Step 2:

.. code-block:: bash
      
    rivt-install.cmd

The commands may also be downloaded here -
:download:`rivt-install.cmd </_downloads/rivt-install.cmd>`.

Within the *example1* folder run the rivt file as:

.. code-block:: bash
      
    python rv0000-simple-single-doc.py


.. _rivt-system:

**[03]** Install *rivt-system*
----------------------------------

.. raw:: html

    <hr>   

.. raw:: html

    <br>


Use `Python installers <https://www.python.org/downloads/>`_ and 
`pip <https://pypi.org/project/pip/>`_ to install packages from 
`PyPI <https://pypi.org/>`_.  The requirements.txt file is here. 



**[04]** Install *rivt framework*
------------------------------------------

.. raw:: html

    <hr>

The *rivt framework* includes installation of the following programs:

#. `VSCode <https://code.visualstudio.com/>`_ and 
   `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_.  

#. `Git <https://git-scm.com>`_ and set up a `GitHub <hhttps://github.com>`_ 

#. `LaTeX <https://www.tug.org/texlive/>`_ 

#. `QCAD <https://qcad.io/en/>`_ 


**[04]** Install *rivt.zip*
--------------------------------------------------

*rivt.zip* is a portable, single folder version of *rivt* and *VSCode*
including libraries and extensions. It can be downloaded here.

The advantages of this installation method include:

#. No steps - just unzip and use.
#. Can be moved anywhere as a unified folder.
#. Ensures compatiblity and integration between libraries. 

Disadvantages include:

#. The installation itself cannot be updated. New releases are planned monthly.
#. Integration with other programs can be more difficult.


.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
      
