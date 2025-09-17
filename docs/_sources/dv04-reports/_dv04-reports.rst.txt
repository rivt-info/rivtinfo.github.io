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

        [rvddss-]file-name.py
    
where dd and ss are a two digit division and subdivision numbers respectively.
e.g., rv0203-loads.py is rivt file 3 in division folder 2. Each *rivt file*
outputs a *doc file* with the same *doc number* prefix. The *doc number* and
*project folder structure* are used to assemble and organize reports.

**Project Folders**

*rivt project folders* organize files used to generate *docs* and *reports*.
The files include *rivt files*, external source documents, settings,
and public/private files. The top level structure is shown below. The full
structure is shown :doc:`here</dv04-reports/rv0402-folders>`

.. code-block:: console

    [rivt]-Project-Label/      Project Folder 
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

    rv0401-documents.rst
    rv0402-folders.rst
    rv0403-settings.rst

