2. Installation
==================   

The following terms apply to installing *rivt* and its additional framework
components.

.. topic:: rivt includes:

    #. Installation of **Python** and all required libraries.

.. topic:: A rivt framework includes:

    #. A rivt installation
    #. Installation of **VSCode** and e*rivt markup* extensions for editing and execution

.. topic:: A rivt extended framework includes:

    #. A rivt framework installation
    #. Installation of **Git** and a **GitHub** account for version control and collaboration
    #. Installation of **LaTeX** for precise typesetting
    #. Installation of **QCAD** for diagramming

Several installation methods are available, depending on individual needs for
control and integration. These include:

#. :doc:`rivt-sys </dv02-install/rivtsys>` : 
    user controlled installation of  *rivt* and its *frameworks*.

#. :doc:`rivt-zip </dv02-install/rivtzip>` :
    a single folder portable version of the *rivt framework* including 
    Python, VSCode and all of the required libraries and extensions.


#. :doc:`rivt-uv </dv02-install/rivtuv>` :
    a single command system install of *rivt* in an isolated environment that 
    can also be deleted with a single command. *rivt-uv* requires the 
    installation of *uv*, a Python package manager. This is the recommended 
    installation method for most users. VSCode and extensions are installed 
    separately for a complete *rivt framework*.


.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
    rivtzip.rst
    rivtsys.rst
    rivtuv.rst
    
  