**B.1 Installation**
=================================  

**[1t]** rivt Project
----------------------------------

.. raw:: html

    <hr>

*rivt* is an open source Python project that includes :term:`rivtlib` and
approximately two dozen additional :doc:`Python packages<rvB02-python>`. The 
IDE `Pyzo <https://pyzo.org/>`_ is installed with *rivt* as an effective 
lightweight program for editing and publishing *rivt docs*. 

*rivt* is designed to wrork in an integrated framework with other open source
programs. In the installation methods described below some install *rivt* 
and some install a *rivt framework*. 

.. topic:: rivtuv

    *uv* is a `Python package manager <https://docs.astral.sh/uv/>`_ and
    installer that simplifies installing isolated Python environments. See
    :ref:`rivtuv <rivt-uv>` for procedure.

.. raw:: html

    <hr>

.. topic:: rivt system

    *rivt* may be installed at the system level using standalone installers.
    See :ref:`rivt system install` for procedure.

.. raw:: html

    <hr>

.. topic:: rivtzip

    *rivtzip* installs *rivtframework1*. It is is a single folder, portable 
    and isolated version of *rivt* integrated with *VSCode*.

    See :ref:`rivtzip <rivt-zip>` for procedure.

.. raw:: html

    <hr>

.. topic:: rivt framework2

    *rivt framework1* includes *rivt* and additional integrated programs and
    tools with their own installers. It includes important productivity tools
    for editing, document control and diagramming.
    
    #. *VSCode and extensions* for editing and collaboration.
    #. *Git and GitHub* for version control and document sharing.
    #. *LaTeX* for precise typesetting.
    #. *QCAD* for diagramming.

    See :ref:`rivt framework <rivt-framework>` for procedure.

.. _rivt-uv:

**[2t]** Install **rivtuv**
----------------------------------

.. raw:: html

    <hr>

The *rivtlib* package is not uploaded to PyPI yet. The *rivtuv* installation 
method is recommended for most users.

.. topic:: Step 1. Install uv

    Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 

    The recommended method for installing *uv* is:

    Windows from the command line:

    .. code-block:: bash
        
        winget install --id=astral-sh.uv  -e 

    macOS and Linux from the command line:

    .. code-block:: bash
        
        curl -LsSf https://astral.sh/uv/install.sh | sh

.. topic:: Step 2. Create an isolated rivt environment

    After installing *uv*, download and run the following command or shell file.
    
    Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 

    OSX and Linux: :download:`rivtuv.sh </_downloads/rivtuv.sh>`
    
    This installs an isolated *rivt* environment and example files in the 
    xxxx folder in the users *Home* directory. Additional install script detaild 
    can be found `here <https://github.com/rivt-info/rivtuv-install/edit/main/>`_.

.. topic:: Step 3. Run example program from Pyzo or command line.

    Some text.


.. _rivt system install:

**[3t]** rivt system install 
--------------------------------

.. raw:: html

    <hr>

*rivt* may be installed at the system level. 

#. Install Python using `Python installers <https://www.python.org/downloads/>`_ 

#. Install *rivtlib* and dependencies using `pip <https://pypi.org/project/pip/>`_ 

A list of the dependencies and *requirements.txt* file is 
:doc:`here <rvB01-install>`.


.. _rivt-framework:

**[4t]** Install rivt framework
------------------------------------------

.. raw:: html

    <hr>

*rivt framework* includes installation of the following programs:

#. `VSCode <https://code.visualstudio.com/>`_ and 
   `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_. 
   *rivt* extensions and snippets are :doc:`here <rvB03-vscode>`.

#. `Git <https://git-scm.com>`_ and set up a `GitHub <hhttps://github.com>`_ 

#. `LaTeX <https://www.tug.org/texlive/>`_ 

#. `QCAD <https://qcad.io/en/>`_ 


.. _rivt-zip:

**[5t]** Install *rivtzip*
--------------------------------------------------

.. raw:: html

    <hr>

*rivtzip* is a portable, single folder version of *rivt* and *VSCode*
including libraries and extensions. It can be downloaded here.

The advantages of this installation method include:

#. No installation steps - just unzip and use.
#. Can be moved anywhere as a unified folder.
#. Ensures compatiblity and integration between libraries. 

Disadvantages include:

#. The software components cannot be individually updated. (New releases monthly)
#. Integration with other programs and tools may be more difficult.


.. toctree::
    :maxdepth: 1
    :hidden:

    rvB02-python.rst
    rvB03-vscode.rst
