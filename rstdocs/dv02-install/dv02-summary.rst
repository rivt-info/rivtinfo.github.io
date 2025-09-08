2. Installation
==================   

The following terms apply to **rivt** and framework installations: 

**[01]** Installation terms
----------------------------------

.. topic:: rivt project:

    In addition to the `rivtlib library <https://www.rivt.info>`_, *rivt*
    includes :doc:`these </dv02-install/python>` additional packages and
    libraries. Any text editor may be used to write and publish *rivt files,
    docs and reports*.


.. topic:: rivt framework:

    The *rivt framework* includes *rivt*, `VSCode
    <https://code.visualstudio.com/>`_ and 
    `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_ 
    for productive writing and editing.


.. topic:: extended rivt framework 

    The *extended rivt framework* includes the following additional open source
    programs and services.

    #. `Git <https://git-scm.com>`_ and a `GitHub <hhttps://github.com>`_ account for version control and collaboration
    #. `LaTeX <https://www.tug.org/texlive/>`_ for precise typesetting
    #. `QCAD <https://qcad.io/en/>`_ for diagramming


**[02]** *rivt* installation
----------------------------------


Several methods are available for these installations, depending on individual
needs for control and integration. These include:

- :doc:`rivt-sys </dv02-install/rivtsys>` : a user controlled installation of 
    the various **rivt framework components**. 

- :doc:`rivt-zip </dv02-install/rivtzip>` :
    a single folder portable version of a **rivt framework** including 
    Python, VSCode and all of the required libraries and extensions.

- :doc:`rivt-uv </dv02-install/rivtuv>` :
    a **rivt** system install in an isolated environment that 
    can be installed and deleted with a single command. **rivt-uv** requires the 
    installation of **uv**, a Python package manager. This is the recommended 
    installation method for most users. **VSCode** and its *rivt-markup* 
    extensions are installed separately to complete a **rivt framework**.


.. toctree::
    :maxdepth: 1
    :hidden:

    rivtsys.rst
    rivtzip.rst
    rivtuv.rst
    python.rst
    vscode.rst
    
  