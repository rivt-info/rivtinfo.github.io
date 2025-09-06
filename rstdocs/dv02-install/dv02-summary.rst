2. Installation
==================   

The following terms apply to installing *rivt* and its additional framework
components.

.. topic:: A *rivt* installation includes:

    #. **Python** with the *rivt package* and additional libraries

.. topic:: A *rivt framework* installation includes:

    #. *rivt*
    #. **VSCode** and *rivt markup extensions* for editing and Python integration

.. topic:: A *rivt extended framework* installation includes:

    #. A *rivt framework*
    #. **Git** and a **GitHub** account for version control and collaboration
    #. **LaTeX** for precise typesetting
    #. **QCAD** for diagramming

Several installation methods are available, depending on individual needs for
control and integration. These include:

- :doc:`rivt-sys </dv02-install/rivtsys>` : 
    a user controlled installation of  *rivt* and its *frameworks*.

- :doc:`rivt-zip </dv02-install/rivtzip>` :
    a single folder portable version of a *rivt framework* including 
    Python, VSCode and all of the required libraries and extensions.

- :doc:`rivt-uv </dv02-install/rivtuv>` :
    a system install of *rivt* in an isolated environment that 
    can be installed and deleted with a single command. *rivt-uv* requires the 
    installation of *uv*, a Python package manager. This is the recommended 
    installation method for most users. **VSCode** and its *rivt-markup* 
    extensions are installed separately to complete a *rivt framework*.


.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
    rivtzip.rst
    rivtsys.rst
    rivtuv.rst
    
  