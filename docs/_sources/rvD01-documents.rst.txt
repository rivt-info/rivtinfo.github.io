**D.1 Documents**
========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** rivt Files and Docs
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt files* are typically part of a *report* and are stored in *division*
folders unless they are :term:`single docs`. Each *rivt file* writes
a *doc*. *Reports* are assembled from and written to files in the *report*
folder which has the top level structure of:

.. code-block:: bash
 
    [rivt]-Report-Label/              Report Folder 
        ├── [dv01-]divlabel/          division folder 
        ├── [dv02-]divlabel/          division folder
        
        ...

        ├── [public]/                 public rivt files
        ├── [report]/                 reports and docs
        ├── [source]/                 source files      
        └── README.txt                text report 

The :term:`doc` title is taken from the *rivt file name* and written to the *report*
folder.  Further explanation of the *report folder* is 
:doc:`here<rvD02-folders>`

PDF *doc* files are produced by two different libraries, referred to as *rpdf*
and *tpdf*. An *rpdf* doc is formatted using the *rst2pdf* library, a susbset
of the larger *ReportLab* library. Its advantage is a much smaller required
library compared to other PDF libraries and it is the default *rivt PDF doc*.

A *rivt LaTeX doc* (*tpdf*) requires separate installation of the
large texlive LaTeX library (approx. 3GB). Its advantage is additional control
over *doc* formatting and appearance.

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[2]** Single Docs
----------------------------------------------------------

.. raw:: html

    <hr>

For a single rivt file document that will not be part of a report, 
a :term:`single doc` may be published using the local folder, without 
referencing  the *report folders*. In this case all of the files are 
read from and written to the same folder as the *rivt file*. 

A *single doc* is published by including the following:

#. The *command* path is specified with the alias *rvlocal*.
#. *doc* source files are stored in the local folder.
#. *Value* API functions (*rv.V*) have an extra *rvlocal* added to the 
    header parameters. 
   
Any *rivt file* can be converted to a *single doc* using the above steps. The
text, PDF and HTML *docs* will be written to the local file using style
settings built into *rivtlib*. *Single docs* provide less formatting control
but also require less setup.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvD02-folders.rst
    rvD03-reports.rst
    rvD04-settings.rst
