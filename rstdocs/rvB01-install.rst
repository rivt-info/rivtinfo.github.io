**B.1 rivt Installation**
=================================  

**[1t]** rivt Project
----------------------------------

.. raw:: html

    <hr>

*rivt* is an open source Python project that includes :term:`rivtlib` and
approximately two dozen additional :doc:`Python packages<rvB02-python>`. When
*rivt* is installed, *rivt files* may be edited using the light weight IDE
`Pyzo <https://pyzo.org/>`_ . *rivt* is also designed to work with other open
source programs and tools in an integrated framework that adds extends editing
and analysis capabilities.

There are four installation methods for *rivt* and its framework, each with
varying degrees of system and program integration.

.. topic:: 1. *rivtuv* 

    *uv* is a `Python package manager <https://docs.astral.sh/uv/>`_ and
    installer that simplifies installing isolated Python environments. See
    :ref:`rivtuv <rivt-uv>` for procedure.

.. raw:: html

    <hr>

.. topic:: 2. *rivt system* 

    *rivt* may be installed at the system level using standalone installers.
    See :ref:`rivt system <rivt-system>` for procedure.

.. raw:: html

    <hr>

.. topic:: 3. *rivt framework* 

    The *rivt framework* includes *rivt* and additional integrated programs and
    tools with their own installers. It includes important productivity tools
    for editing, document control and diagramming.
    
    #. *VSCode and extensions* for editing and collaboration.
    #. *Git and GitHub* for version control and document sharing.
    #. *LaTeX* for precise typesetting.
    #. *QCAD* for diagramming.

    See :ref:`rivt framework <rivt-framework>` for procedure.

.. raw:: html

    <hr>

.. topic:: 4. *rivtzip* 

    *rivtzip* is a single folder, portable and isolated version of *rivt* that
    is integrated with *VSCode*.


    See :ref:`rivtzip <rivt-zip>` for procedure.


.. _rivt-uv:

**[2t]** Install *rivtuv*
----------------------------------

.. raw:: html

    <hr>

Until *rivt* is uploaded to PyPI, the *rivtuv* installation method is
recommended for most users.

**Step 1. Install uv**

Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 

The recommended method for installing *uv* is:

Windows:

.. code-block:: bash
      
    winget install --id=astral-sh.uv  -e 

macOS and Linux:

.. code-block:: bash
      
    curl -LsSf https://astral.sh/uv/install.sh | sh

**Step 2. Create a rivt environment and install rivtlib** 

After installing *uv*, download and run the following command or shell file.
This installs an isolated *rivt* environment and example files in the users
*Home* directory

Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 
OSX: :download:`rivtuv.sh </_downloads/rivtuv.sh>` 

Additional explanation for the install scripts can be found 
`here <https://github.com/rivt-info/rivtuv-install/edit/main/>`_.


.. _rivt-system:

**[3t]** Install *rivt system*
----------------------------------

.. raw:: html

    <hr>

*rivt* may be installed at the system level. 

#. Install Python using `Python installers <https://www.python.org/downloads/>`_ 

#. Install *rivtlib* and dependencies using `pip <https://pypi.org/project/pip/>`_ 

A list of the dependencies and *requirements.txt* file is 
:doc:`here <rvB01-install>`.


.. _rivt-framework:

**[4t]** Install *rivt framework*
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

#. No installaion steps - just unzip and use.
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
