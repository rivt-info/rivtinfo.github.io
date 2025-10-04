
**B.1 Install**
=================================  

**[1]** rivt Project
----------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

*rivt* is a Python project. It includes :doc:`rivtlib </dvA0-intro/rv01-intro>`
and another two dozen  :doc:`Python packages </dvB0-install/rv02-python>`. When
*rivt* is installed, *rivt docs and reports* may be edited and published using a
text editor. 

*rivt* is also designed to work with auxiliary open source programs and tools
that add editing and analysis capabilities. There are four installation methods
for *rivt* and its auxiliary programs.

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

**[2]** Install *rivt-uv*
----------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>


This *rivt* installation method is recommended for most users. The procedure
for Windows is shown below. Other OS installs are similar.

**Step 1. Install uv**

Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 
The recommended method for installing *uv* on Windows is: 

.. code-block:: bash
      
    winget install --id=astral-sh.uv  -e 


**Step 2. Create rivt environment and install rivtlib** 

After installing *uv*, run the following commands to set up and activate an
isolated *rivt* environment in the users *Home* directory (omit the explanatory
REM lines). The commands may be downloaded and run from the command file
:download:`rivt-uv.cmd </_downloads/rivt-uv.cmd>`. 

They execute the following steps:

#. name the *uv* environment in the first SET command
#. switch to the %HOMEPATH% (User) folder
#. remove any prior existing environment, cache and folders.
#. download the rivt install file.
#. create a new environment and activates it.
#. install *rivt* in the *uv* environment.
#. create an *example1* folder
#. download an example  *rivt file* and *sources* into the *example1* folder



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
    REM run example (no quotes) "python rv00-simple-single-doc.py"
    cmd /k

Within the *example1* folder run the rivt file:

.. code-block:: bash
      
    python rv00-simple-single-doc.py


.. _rivt-system:

**[3]** Install *rivt-system*
----------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

*rivt* may be installed at the system level. 

#. Install Python using `Python installers <https://www.python.org/downloads/>`_ 

#. Install *rivtlib* and dependencies using `pip <https://pypi.org/project/pip/>`_ 

A list of the dependencies and *requirements.txt* file is 
:doc:`here </dvB0-install/rv01-install>`.


**[4]** Install *rivt-framework*
------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>


The *rivt-framework* includes installation of the following programs:

#. `VSCode <https://code.visualstudio.com/>`_ and 
   `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_. 
   *rivt* extensions and snippets are :doc:`here </dvB0-install/rv03-vscode>`.

#. `Git <https://git-scm.com>`_ and set up a `GitHub <hhttps://github.com>`_ 

#. `LaTeX <https://www.tug.org/texlive/>`_ 

#. `QCAD <https://qcad.io/en/>`_ 


**[5]** Install *rivt.zip*
--------------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

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

    rv02-python.rst
    rv03-vscode.rst
