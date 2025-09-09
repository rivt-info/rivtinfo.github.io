2. Installation
==================   


**[01]** Installation types
----------------------------------

.. raw:: html

    <hr>


.. topic:: *rivt*

    *rivt* is a Python project. In addition to the `rivtlib <https://www.rivt.info>`_, 
    it includes :doc:`these packages </dv02-install/python>`.  *rivt docs and reports*
    may be written and published using a text editor.

.. raw:: html

    <br>


.. topic:: *VSCode framework*

    The *VSCode framework* includes productiviy tools for writing and
    collaborating on *rivt files*. It includes `VSCode <https://code.visualstudio.com/>`_
    and `extensions <https://marketplace.visualstudio.com/vscode>`_.


.. raw:: html

    <br>

.. topic:: *complete framework*

    The *complete framework* adds the following additional open source
    programs and services:

    #. `Git <https://git-scm.com>`_ and `GitHub <hhttps://github.com>`_ for version control and collaboration
    #. `LaTeX <https://www.tug.org/texlive/>`_ for precise typesetting
    #. `QCAD <https://qcad.io/en/>`_ for diagramming


**[02]** Install *rivt*
----------------------------------

.. raw:: html

    <hr>

**Method 1 - uv**

This is the recommended method for most users.

1. Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 
   The recommended method for Windows is: 

.. code-block::
      
    winget install --id=astral-sh.uv  -e 

1. Run the following commands or download and run this
   :download:`command file </_downloads/rivt-install.cmd>`. This creates a
   subfolder named rivt (it can be renamed in the init command) and installs 
   rivt from GitHub in the subfolder.

.. code-block::

    init uv rivt
    cd rivt
    uv add "git+https://github.com/rivtlib-dev/rivtlib.git#subdirectory=src"


.. raw:: html

    <br>


**Method 2 - System**

Use Python installers and *pip* to install the packages here. 


**[03]** Install *VSCode framework*
------------------------------------------

.. raw:: html

    <hr>


**Method 1 - VSCode**

#. Install *rivt*

#. Install `VSCode <https://code.visualstudio.com/>`_ and 
   `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_.  
   Extensions can be installed with this script.


**Method 2 - rivt.zip**

A single folder portable version of a **rivt framework** including Python,
VSCode and all of the required libraries and extensions. *VSCode* and its
*rivt-markup* extensions are installed separately to complete a **rivt
framework**.


**[04]** Install *complete  framework*
--------------------------------------------------

.. raw:: html

    <hr>


`Git <https://git-scm.com>`_ and a `GitHub <hhttps://github.com>`_ 

`LaTeX <https://www.tug.org/texlive/>`_ 

`QCAD <https://qcad.io/en/>`_ 



.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
    
  