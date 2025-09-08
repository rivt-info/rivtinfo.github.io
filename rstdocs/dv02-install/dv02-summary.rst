2. Installation
==================   

The following terms apply to **rivt** and framework installations: 

**[01]** Installation terms
----------------------------------

.. topic:: rivt:

    In addition to the `rivtlib library <https://www.rivt.info>`_, *rivt*
    includes :doc:`these additional packages </dv02-install/python>`. 
    When rivt is installed any text editor may be used to write and publish 
    *rivt docs and reports*.



.. raw:: html

    <hr>

 

.. topic:: rivt framework:

    The *rivt framework* includes *rivt*, `VSCode
    <https://code.visualstudio.com/>`_ and 
    `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_ 
    for productive writing and editing.


.. raw:: html

    <hr>

 

.. topic:: extended rivt framework 

    The *extended rivt framework* includes the following additional open source
    programs and services:

    #. `Git <https://git-scm.com>`_ and a `GitHub <hhttps://github.com>`_ account for version control and collaboration
    #. `LaTeX <https://www.tug.org/texlive/>`_ for precise typesetting
    #. `QCAD <https://qcad.io/en/>`_ for diagramming


.. raw:: html

    <hr>

 

**[02]** Install *rivt*
----------------------------------

**Method 1 - uv**

    This is the recommended method for most users.

#. Install `uv <https://docs.astral.sh/uv/getting-started/installation/#pypi>`_. 
   The recommended method for Windows is: 

.. code-block:: 

   winget install --id=astral-sh.uv  -e 

#. Install by in a subfolder by running the following shell command. This
   installs *rivt* in an isolated environment that can be deleted by deleting the
   rivt folder.

.. code-block::

    init uv rivt
    cd rivt
    uv add "git+https://github.com/rivtlib-dev/rivtlib.git#subdirectory=src"


You can download the command file :download:`here </_downloads/rivt.cmd>`.

.. raw:: html

    <hr>

**Method 2 - System**

Use Python installers and *pip* to install the necessary packages listed here: 


**[03]** Install the *rivt framework*
------------------------------------------

- :doc:`rivt-zip </dv02-install/rivtzip>` :
    a single folder portable version of a **rivt framework** including 
    Python, VSCode and all of the required libraries and extensions.
**VSCode** and its *rivt-markup* 
    extensions are installed separately to complete a **rivt framework**.


**[03]** Install the *extended rivt framework*
--------------------------------------------------




.. toctree::
    :maxdepth: 1
    :hidden:

    python.rst
    vscode.rst
    
  