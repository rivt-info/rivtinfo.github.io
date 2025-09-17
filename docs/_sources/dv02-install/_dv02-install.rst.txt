2. Installation
==================   


**[01]** Installation types
----------------------------------

.. raw:: html

    <hr>

.. topic:: *rivt* (see :ref:`rivt-spot`)

    *rivt* is a Python project that includes `rivtlib <https://www.rivt.info>`_
    and other :doc:`Python packages </dv02-install/python>`.  When *rivt* 
    is installed *rivt docs and reports* may be edited and published 
    using a text editor.

.. raw:: html

    <br>

.. topic:: *rivt framework* (see :ref:`rivtframe-spot`)

    The *rivt framework* includes *rivt* and additional programs installed
    separately. It includes important productiviy tools for editing, document
    control and diagramming.
    
    #. *VSCode and extensions* for editing and collaboration.
    #. *Git and GitHub* for version control and document sharing.
    #. *LaTeX* for precise typesetting.
    #. *QCAD* for diagramming.

.. raw:: html

    <br>

.. topic:: *rivt.zip* (see :ref:`rivtzip-spot`)

    A single folder, portable version of *rivt* integrated with *VSCode*.
    
.. _rivt-spot:

**[02]** Install uv *rivt*
----------------------------------

.. raw:: html

    <hr>

This method for installing *rivt* is recommended for most users. The procedure
for Windows is shown below. Other OS installs are similar.


**Step 1. Install uv**

Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 
The recommended method for installing *uv* on Windows is: 

.. code-block:: console
      
    winget install --id=astral-sh.uv  -e 


**Step 2. Create rivt environment** 

After installing *uv*, run the following commands to set up and activate and
isolated *rivt* environment called *rivt-test1* (omit the explanatory lines 
that begin with REM). The commands may also be downloaded and run from a
:download:`command file </_downloads/rivt-venv.cmd>`. This set of commands 
can also be run to remove an existing environment and install a clean one. They

#. remove any prior existing environment and directory
#. create a new environment and activates it

.. code-block:: console

    @echo on
    REM go to home directory
    cd %HOMEPATH%\
    REM double check deactivation for dev purposes
    uv deactivate
    REM ensure check that the old install is deleted
    rmdir /s /q rivt-test1 
    REM clean cache for dev purposes
    uv cache clean
    REM set up venv
    mkdir rivt-test1
    REM change directory
    cd rivt-test1
    REM make venv
    uv venv
    REM activate venv
    .venv/scripts/activate



**Step 3. Install rivt** 

Within the *rivt-test1* environment type the following set of commands
(omit the explanatory lines that begin with REM). The commands may also be
downloaded and run from a 
:download:`command file </_downloads/rivt-install.cmd>`. They

#. install *rivt* in the *rivt-test1* environment.
#. run a small test program built into *rivtlib*.  
   The last line can be omitted to skip this step. 

.. code-block:: console

    @echo on
    REM install rivt from GitHub
    uv pip install git+https://github.com/rivtlib-dev/rivtlib#subdirectory=src
    REM copy test file to base directory
    copy.venv\Lib\site-packages\rivtlib\scripts\rv0000-simple-doc.py
    REM run test case
    python rv0000-simple-doc.py


**[03]** Install System *rivt*
----------------------------------

.. raw:: html

    <hr>   

.. raw:: html

    <br>

**Method 2 - System**

Use `Python installers <https://www.python.org/downloads/>`_ and 
`pip <https://pypi.org/project/pip/>`_ to install packages from 
`PyPI <https://pypi.org/>`_.  The requirements.txt file is here. 


.. _rivtframe-spot:

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

.. _rivtzip-spot:

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
      
