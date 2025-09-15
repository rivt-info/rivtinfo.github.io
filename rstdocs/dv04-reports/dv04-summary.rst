4. Reports
=============== 


*rivt files* output PDF, HTML or text *docs* that are typically organized into
*rivt reports*. The *reports* are assembled from a *rivt folder structure**. A
*rivt file* may also be treated as a *single doc*

**[01]** rivt folders
----------------------

The folder structure includes rivt files, external source documents, settings
and separation of files into public and private categories to facilitate open
source sharing.


    [rivt]-Report-Label/          Project Folder 
    ├── [dv01-]divlabel/          division folder
    ├── [dv02-]divlabel/          division folder                   
    ├── [public]/                 public rivt files
    ├── [reports]/                reports and docs
    ├── [source]                  source files      
    └── README.txt                text report



 by 



Resource files used in *rivt files* are organized in the *source* folder.

**[02]** rivt files
----------------------

A *doc* may be a text, PDF or HTML file. Each *rivt file* is identified with a
*doc* number of the form:

    rvddss-file-name.py 
    
where dd is a two digit division number and ss is a two digit subdivision
number e.g., rv0203-loads.py. The *doc numbers* are used to insert sources and
assemble reports. Editing the doc number changes the report organization.

An example *rivt folder structure* for reports is shown below. *rivt files* are
organized into numbered division folders of the form:

    dvdd-division-name

where dd is the two digit division number.

*Docs* are written to the *reports* folder. A *report* is an organized assembly
of *docs*.

Report and document titles are taken from folder and file names unless
over-rides are specified in the rivt-config.ini file.


.. toctree::
    :maxdepth: 1
    :hidden:

    folders.rst
    documents.rst
    settings.rst


        [rivt]-Report-Label/          Project Folder 
        ├── [dv01-]divlabel/          division folder
        ├── [dv02-]divlabel/          division folder                   
        ├── [public]/                 public rivt files
        ├── [reports]/                reports and docs
        ├── [source]                  source files      
        └── README.txt                text report 