2. Installation
==================   

The following terms apply to **rivt** and its framework installations: 

**[01]** Installation Terms
----------------------------------

.. raw:: html

    <hr>


.. topic:: rivt:

    *rivt* is a Python project. In addition to the `rivtlib package <https://www.rivt.info>`_, 
    it includes :doc:`these packages </dv02-install/python>`. 
    After *rivt* is installed any text editor may be used to write, edit and publish 
    *rivt docs and reports*.

.. raw:: html

    <br>


.. topic:: rivt framework:

    For productive writing and collaboration the *rivt framework* includes *rivt*, 
    `VSCode <https://code.visualstudio.com/>`_ and 
    `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_.


.. raw:: html

    <br>

 

.. topic:: extended rivt framework: 

    The *extended rivt framework* includes the following additional open source
    programs and services:

    #. `Git <https://git-scm.com>`_ and a `GitHub <hhttps://github.com>`_ account for version control and collaboration
    #. `LaTeX <https://www.tug.org/texlive/>`_ for precise typesetting
    #. `QCAD <https://qcad.io/en/>`_ for diagramming


**[02]** Install *rivt*
----------------------------------

.. raw:: html

    <hr>

**Method 1 - uv**

This is the recommended method for most users.

#. Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 
   The recommended method for Windows is: 

        winget install --id=astral-sh.uv  -e 

#. Install *rivt* in a subfolder by running the following shell command. This
   installs *rivt* in an isolated environment that can be deleted by deleting the
   rivt folder. You can download the command file 
   :download:`here </_downloads/rivt.cmd>`.

        init uv rivt
        cd rivt
        uv add "git+https://github.com/rivtlib-dev/rivtlib.git#subdirectory=src"


.. raw:: html

    <br>


**Method 2 - System**

Use Python installers and *pip* to install the packages here. 


**[03]** Install *rivt framework*
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


**[04]** Install the *extended rivt framework*
--------------------------------------------------

.. raw:: html

    <hr>



.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
    
  