4. Reports
=============== 

The assembly and organization of a *rivt report* is inferred from:

#. The *rivt file* and *doc* name
#. The *project folder* names

.. topic:: Note: 
    
   In the examples below, brackets identify the fixed part of the file or
   folder name and are not included in the actual name.

**Files and Docs**

A *rivt file* name has a *doc number* prefix:

.. code-block:: bash
    
    [rvss-]file-name.py
    
where ss is a two digit subdivision number. e.g., rv03-loads.py is subdivision
3 within a division folder. Each *rivt file* outputs a *doc file* with the same
*doc number* prefix. The *doc number* and *project folder structure* are used
to assemble and organize reports.

**Project Folders**

*rivt project folders* organize files used to generate *docs* and *reports*.
The files include *rivt files*, external source documents, settings,
and public/private files. The top level structure is shown below. The full
structure is shown :doc:`here</dv04-reports/rv02-folders>`

.. code-block:: bash

    [rivt]-Project-Label/             Project Folder 
        ├── [dv01-]divlabel/          division folder
        ├── [dv02-]divlabel/          division folder

        ...

        ├── [public]/                 public rivt files
        ├── [reports]/                reports and docs
        ├── [source]/                 source files      
        └── README.txt                text report 


A *rivt file* may also generate a *single doc* that reads from and writes to the
local *rivt file* folder, independent of the *project folders*.

.. toctree::
    :maxdepth: 1
    :hidden:

    rv01-documents.rst
    rv02-folders.rst
    rv03-settings.rst

