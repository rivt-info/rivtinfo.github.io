2. Installation
==================   


**[01]** Installation types
----------------------------------

.. raw:: html

    <hr>

.. topic:: *rivt*

    *rivt* is a Python project that includes `rivtlib <https://www.rivt.info>`_
    and other :doc:`Python packages </dv02-install/python>`.  After *rivt* 
    is installed *rivt docs and reports* may be edited and published 
    using a text editor.

.. raw:: html

    <br>

.. topic:: *rivt framework*

    The *rivt framework* includes *rivt* and additional programs installed
    separately. It includes important productiviy tools for editing, document
    control and diagramming.
    
    #. *VSCode and extensions* for editing and collaboration.
    #. *Git and GitHub* for version control and document sharing.
    #. *LaTeX* for precise typesetting.
    #. *QCAD* for diagramming.

.. raw:: html

    <br>

.. topic:: *rivt.zip*

    A single folder, portable version of *rivt* integrated with *VSCode*.
    

**[02]** Install *rivt*
----------------------------------

.. raw:: html

    <hr>

**Method 1 - uv**

This is the recommended method for most users.

1. Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 
   The recommended method for installing *uv* on Windows is: 

.. code-block::
      
    winget install --id=astral-sh.uv  -e 

After installing uv run the following commands 

.. code-block::

    init uv rivt
    cd rivt
    uv add "git+https://github.com/rivtlib-dev/rivtlib.git#subdirectory=src"

or download and run this :download:`command file </_downloads/rivt-install.cmd>`. 
This series of commands 

#. creates a subfolder named rivt and initializes it. Any folder name can be used.
#. changes the working directory to the subfolder just created.
#. installs *rivt* in the subfolder.

The installation can be deleted by simply deleting the folder.
   

.. raw:: html

    <br>

**Method 2 - System**

Use `Python installers <https://www.python.org/downloads/>`_ and 
`pip <https://pypi.org/project/pip/>`_ to install packages from 
`PyPI <https://pypi.org/>`_.  The requirements.txt file is here. 



**[03]** Install *rivt framework*
------------------------------------------

.. raw:: html

    <hr>

The *rivt framework* includes installation of the following programs:

#. `VSCode <https://code.visualstudio.com/>`_ and 
   `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_.  

#. `Git <https://git-scm.com>`_ and set up a `GitHub <hhttps://github.com>`_ 

#. `LaTeX <https://www.tug.org/texlive/>`_ 

#. `QCAD <https://qcad.io/en/>`_ 


**[04]** Download *rivt.zip*
--------------------------------------------------

*rivt.zip* is a portable, single folder version of *rivt* and *VSCode*
including libraries and extensions. It can be downloaded here.

The advantages of this setup include:

#. No installation steps - just unzip.
#. Can be moved anywhere.
#. Ensured compatiblity and integration between libraries. 

Disadvantages include:

#. Cannot be updated. However new releases are planned monthly.
#. Not as easily integrated with other programs. 


.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
    
  