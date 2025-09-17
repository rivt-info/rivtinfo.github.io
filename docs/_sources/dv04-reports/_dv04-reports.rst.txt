4. Reports
=============== 

*rivt reports* are organized from a collection of *docs* generated from *rivt
files*. The structure of a *report* is inferred from

#. The *rivt* file name
#. The *rivt folder structure*

.. topic:: Note: 
    
   Brackets identify the fixed part of the file or folder labels -
   they are not included in an actual label.

A *rivt file* name has a *doc number* prefix of the form:

        [rvddss]-file-name.py
    
where dd is a two digit division number and ss is a two digit subdivision
number e.g., rv0203-loads.py. Each *rivt file* genearates a *doc* as a
subdivision in a *report*. Editing the *doc number* changes the report
organization and default locations of sources used in a doc. 

A *rivt file* may also generate a *single doc* that uses only local files and
is indenpendent of the folder structure.

The *rivt folder structure organizes* rivt files, external source documents,
settings and public/private files. The first level structure is shown below.

::

    [rivt]-Report-Label/          Project Folder 
    ├── [dv01-]divlabel/          division folder
    ├── [dv02-]divlabel/          division folder                   
    ├── [public]/                 public rivt files
    ├── [reports]/                reports and docs
    ├── [source]/                 source files      
    └── README.txt                text report 


.. toctree::
    :maxdepth: 1
    :hidden:

    rv0401-folders.rst
    rv0402-documents.rst
    rv0403-settings.rst

