2. Installation
==================   


A *rivt* installation includes:

- *Python* and all of the required libraries.

A *rivt framework* installation includes:

- *rivt*
- *VSCode* with extensions for document editing and collaboration

A *rivt extended framework* installation includes:

- *rivt framework*
- *Git* and **GitHub** for version control and collaboration
- *LaTeX* for precise typesetting
- *QCAD* for diagramming

Installations may be done in several different ways depending on individual needs for
control and integration. These include:

#. :doc:`rivt-sys </dv02-install/rivtsys>` :
    a user controlled installation of the *rivt and extended framework* 

#. :doc:`rivt-zip </dv02-install/rivtzip>` :
    a single folder portable version of the *rivt framework* including 
    Python, VSCode and all of the required libraries and extensions


#. :doc:`rivt-uv </dv02-install/rivtuv>` :
    a single command installation of *rivt* in an isolated environment that 
    can also be fully deleted with a single command. *rivt-uv* requires the 
    installation of *uv*, a Python package manager. This is the recommended 
    installation method for most users.


.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
    rivtzip.rst
    rivtsys.rst
    rivtuv.rst
    
  