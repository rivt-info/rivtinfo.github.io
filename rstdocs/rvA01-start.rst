**A.1 Start**
=====================================================================

**[1t]** Run examples
--------------------------------------------------------------------- 

.. raw:: html

   <hr> 

*rivt file* examples can be run in the cloud or on a local computer. In both 
cases editing and publishing is typically carried out in IDE. Any IDE
maay be used but VSCode is supported as part of the :term:`rivt framework`.
A typical *rivt* editor layout can be viewed at `Codesandbox
<https://codesandbox.io/p/devbox/rivt1-dkmqfm?file=%2Frv001-single-doc.txt>`__.
The sandbox allows scrolling through an example rivt file (left panel) and
text doc (right panel). Files may be downloaded from the file explorer (far left
panel) including the text, pdf and html reports. As an unregistered editor it 
does not allow editing or processing files.

.. figure::  _static/img/ide2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: ide layout

`VSCode <https://code.visualstudio.com/>`__ is an extensible IDE by 
*Microsoft* that can be run locally or in the cloud. The cloud version is 
referred to as a `Codespace <https://github.com/features/codespaces>`__ .
A :term:`rivt Codespace` is a *Codespace* environment with extensions 
for editing and running *rivt files*. 

A *rivt Codespace* with *rivt file* examples can be cloned into a personal account 
`from here <https://github.com/rivt-info/rivt-codespace-examples>`__.  
To edit and run the examples, a required GitHub account can be set up 
`from here <https://github.com>`__. The *rivt Codespace* can be deployed in a 
*GitHub Codespace* 

.. code:: bash

    1. click the "Fork" button in the upper right corner of the page 
        to create a copy of the repository in your GitHub account
    2. change to your GitHub account and open the forked repository
    3. click the green "Code" button on the GitHub page 
    4. select the "Codespaces" tab
    5. click the"rivt-codespace-examples" option 
        to create and open a *rivt Codespace* with the examples


.. figure::  _static/img/codespace2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: rivt example repo

Local installation methods include the following options: 

#. portable zip folder (:ref:`rivt-portable`) 
#. uv package manager (:ref:`rivt-uv`) 
#. system Python package (:ref:`rivt-sys`)

*rivt-portable* is recommended for users unfamiliar with Python. 

.. _rivt-portable:

**[2t]** rivt-portable
--------------------------------------------------------------------- 

.. raw:: html

   <hr> 

rivt-portable is a zipped folder that includes:

#. Python 3.13 with rivt packages 
#. VSCode 1.109 with rivt extensions
#. rivt file examples

The folder may be downloaded `here <https://github.com/rivtlib-dev/rivt-zip>`.
The zip file name is:
 
.. code-block:: text

    rivt-portable-n.n.n.zip

where n-n-n is the major, minor and patch release number. The folder contents
are unzipped into a directory with read-write access - typically the users home
folder. 

The primary advantage of *rivt-zip* is installation simplicity and isolation
from the operating system. Packages and extensions are pre-installed. VSCode
with rivt extensions and examples can be started with a single click. Updated
releases of *rivt-zip* are planned monthly. The primary disadvantage of
*rivt-zip* is that individual files (package components and extensions) are not
easily updated or integrated with other programs.

.. _rivt-uv:

**[3t]** rivt-uv
--------------------------------------------------------------------- 

.. raw:: html

    <hr> 

**rivt-uv** uses the `uv <https://astral.sh/uv/>` package manager to create an
isolated rivt environment and install rivt packages and dependencies not
already installed in the system Python. The primary advantage of *rivt-uv* is
that it allows for updating rivt without affecting the system Python.


The *rivt-uv* installation method is recommended for most users.

.. topic:: Step 1. Install uv

    Install *uv* from 
    `here <https://docs.astral.sh/uv/getting-started/installation/#pypi>`. 

    The recommended method for installing *uv* is from the command line:

    Windows:

    .. code-block:: bash
        
        winget install --id=astral-sh.uv  -e 

    macOS and Linux:

    .. code-block:: bash
        
        curl -LsSf https://astral.sh/uv/install.sh | sh

.. topic:: Step 2. Create the rivt environment

    After installing *uv*, download and run the following command or shell
    script. It installs an isolated *rivt* environment and example files in a
    folder named *rivt-examples* in the users *Home* directory.

    Windows:  :download:`rivtuv.cmd </_downloads/rivtuv.cmd>` 

    OSX and Linux: :download:`rivtuv.sh </_downloads/rivtuv.sh>`
    
.. topic:: Step 3. Run the example program from Pyzo.

    The *rivt* installation includes the `Pyzo <https://pyzo.org/>`. IDE for
    editing and running examples. Typing the command *pyzo-example* from the uv
    environment root will load the example file *rv00-simple-doc.py* where it
    can be edited and run.
    
    The example file can also be run from the command line with the command:

    .. code-block:: bash

        python -m rivt rv001-single-doc.py

    The uv environment can be completely removed with the following commands.

    .. code-block:: bash

        uv deactivate
        rmdir /s /q rivt-examples
        uv cache clean

.. _rivt-sys:

**[4t]** rivt-sys
--------------------------------

.. raw:: html

    <hr>

*rivt* may be installed at the system level. 

#.  Install Python using `Python installers <https://www.python.org/downloads/>`
    if not already installed. The minimum version required by *rivt* is 
    Python 3.13.

#.  Install *rivtlib* and dependencies 

.. code-block:: bash

    pip install rivtlib
    
A list of the dependencies is :ref:`here <Project requirements>`.


.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-motivation.rst
    rvA03-faq.rst

