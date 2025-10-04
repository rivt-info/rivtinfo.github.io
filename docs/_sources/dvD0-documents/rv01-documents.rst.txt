
.. raw:: html

    <hr>


**D.1** - Documents 
========================

.. raw:: html

    <hr>






**[1]** Docs
--------------------------------------------------------------------- 

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

*rivt files* are typically stored in *division* folders unless they are *single
docs*. *Reports* are assembled from and written to files in the *report* folder
which has the top level structure of:

.. code-block:: bash
 
    [rivt]-Report-Label/              Report Folder 
        ├── [dv01-]divlabel/          division folder 
        ├── [dv02-]divlabel/          division folder
        
        ...

        ├── [public]/                 public rivt files
        ├── [report]/                reports and docs
        ├── [source]/                 source files      
        └── README.txt                text report 


*rivt files* are processed sequentially. Calculated values and programatically
generated objects can be passed between files. Sources used in a *doc* are read
from the *source* folder. Further explanation of the *report folder* is 
:doc:`here </dvD0-documents/rv02-folders>`

PDF files are produced in two ways, referred to as *rpdf* and *tpdf*. An *rpdf*
doc is formatted using the *rst2pdf* library, a susbset of the larger
*ReportLab* library. It is the default *rivt PDF doc*. Its advantage is a much
smaller required library compared to other PDF libraries. A *rivt LaTeX doc*
(*tpdf*) requires separate installation of the large texlive LaTeX library
(approx. 2GB). Its advantage is additional control over *doc* formatting and
appearance.


**[2]** Single Docs
----------------------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

For a simple document that will not be part of a report, a *single doc* may
also be published using only the local folder, without reference to the project
folder. In this case all of the files are read from and written to the same
folder as the *rivt file*. 

A *single doc* is published by including the following:

#. The *command* path is specified with the alias *rvlocal*.
#. For the *Value* API function (*rv.V*) add *rvlocal* to header parameters. 
   Separate parameters with a comma.
#. Ensure that *doc* source files are in the local folder.

Any *rivt file* can be converted to a *single doc* using the above steps. The
text, PDF and HTML *docs* will be written to the local file using standard
format settings built into *rivtlib*. 

*Single docs* provide less formatting control but require less setup and are
useful for quick *doc* production.

.. toctree::
    :maxdepth: 1
    :hidden:

    rv02-folders.rst
    rv03-reports.rst
    rv04-settings.rst
