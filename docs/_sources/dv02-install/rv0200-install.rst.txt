2. Installation
==================   

*rivt* is a Python project that includes `rivtlib <https://www.rivt.info>`_
with other :doc:`Python packages </dv02-install/rv0201-python>`. After
*rivt* is installed *docs and reports* may be edited and published using a
text editor. *rivt* is designed to work with other open source programs and
tools that add features and capability.

There are four methods for installing *rivt* and auxiliary programs.

.. topic:: 1. *rivt-uv* 

    *uv* is a `Python package manager <https://docs.astral.sh/uv/>`_ and
    installer that simplifies installing isolated Python environments. See
    :ref:`Install rivt-uv <rivt-uv>` for installation procedures.

.. raw:: html

    <hr>

.. topic:: 2. *rivt-system* 

    *rivt* may be installed at the system level using standalone installers.
    See :ref:`rivt-system <rivt-system>` for system installation procedures.

.. raw:: html

    <hr>

.. topic:: 3. *rivt-framework* 

    The *rivt-framework* includes *rivt* and additional integrated programs and
    tools with their own installers. It includes important productivity tools
    for editing, document control and diagramming.
    
    #. *VSCode and extensions* for editing and collaboration.
    #. *Git and GitHub* for version control and document sharing.
    #. *LaTeX* for precise typesetting.
    #. *QCAD* for diagramming.

.. raw:: html

    <hr>

.. topic:: 4. *rivt.zip* 

    *rivt.zip* is a portable, single folder, version of *rivt* integrated with
    *VSCode*.



.. _rivt-uv:

**[01]** Install *rivt-uv*
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


**Step 2. Create rivt environment and install rivtlib** 

After installing *uv*, run the following commands to set up and activate an
isolated *rivt* environment in the users *Home* directory (omit the explanatory
REM lines). The commands execute the following steps:

#. names the *uv* environment in the first SET command
#. changes to the %HOMEPATH% (User) folder
#. removes any prior existing environment, cache and folders.
#. downloads the rivt install file.
#. creates a new environment and activates it.
#. installs *rivt* in the *uv* environment.
#. creates an *example1* folder
#. downloads a  *rivt file* and *sources* into the *example1* folder

The commands may be downloaded and run from the command file
:download:`rivt-uv.cmd </_downloads/rivt-uv.cmd>`. 

.. code-block:: bash
    
    @echo on
    REM (1) clear any existing project, (2) create new venv
    REM (3) install rivt, (4) download example
    REM set rivt folder
    SET rvfolder=rivt-doc1
    REM go to home directory
    cd %HOMEPATH%
    REM double check deactivation
    uv deactivate
    REM double check that old project is deleted
    rmdir /s /q %rvfolder%
    REM (1) clean cache 
    uv cache clean
    REM set up venv
    mkdir %rvfolder%
    REM change directory
    cd %rvfolder%
    REM (2) make venv
    uv venv
    REM activate venv
    call .venv/scripts/activate
    REM (3) install rivt from GitHub
    uv pip install git+https://github.com/rivtlib-dev/rivtlib.git@main
    REM (4) download example project into new folder
    mkdir example1
    cd example1
    curl https://raw.githubusercontent.com/rivt-info/rivt-simple-single-doc/refs/heads/main/rv0000-simple-single-doc.py -O
    curl https://github.com/rivt-info/rivt-simple-single-doc/blob/main/beam.png?raw=true -O -L
    REM run example with (no quotes) "python rv0000-simple-single-doc.py"
    cmd /k

Within the *example1* folder run the rivt file:

.. code-block:: bash
      
    python rv0000-simple-single-doc.py


.. _rivt-system:

**[02]** Install *rivt-system*
----------------------------------

*rivt* may be installed at the system level. 

#. Install Python using `Python installers <https://www.python.org/downloads/>`_ 

#. Install *rivtlib* and dependencies using `pip <https://pypi.org/project/pip/>`_ 

A list of the dependencies and *requirements.txt* file is 
:doc:`here </dv02-install/rv0201-python>`.


**[03]** Install *rivt-framework*
------------------------------------------


The *rivt-framework* includes installation of the following programs:

#. `VSCode <https://code.visualstudio.com/>`_ and 
   `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_. 
   *rivt* extensions and snippets are :doc:`here </dv02-install/rv0202-vscode>`.

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

    rv0201-python.rst
    rv0202-vscode.rst
      
