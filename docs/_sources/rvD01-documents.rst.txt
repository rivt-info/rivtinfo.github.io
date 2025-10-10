**D.1 Documents**
========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** rivt Files and Docs
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt files* are typically part of a *report* and reference files in the *rivt
report folder*, unless they are published as stand-alone *docs*. Each *rivt
file* writes a *doc*. *Reports* are generated from *docs* in the *publish
folder*.

**Folder Key**

- Required folder and file prefixes names are shown in brackets [ ]. 
- Single vertical bar ( | ) identifies files provided by the report author. 
- Double vertical bar ( || ) identifies files written by rivtlib 
- Four vertical bars ( |||| ) mix of author and rivtlib written files


.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file

        ...
        ...

        ├── [log]/                      || log files folder
        ├── [public]/                   || public rivt files folder
        ├── [publish]/                  || doc and reports folder
        ├── [src]/                      |||| source files folder
        └── README.txt                  | GitHub searchable text report 

The :term:`doc` file name is taken from the *rivt file name* and written to the *publish*
folder.  Further explanation of the *rivt report folder* is :doc:`here<rvD02-folders>`

PDF *doc* files are produced by two different libraries, referred to as *pdf*
and *pdftex*. A *pdf* doc is formatted using the *rst2pdf* library, a susbset
of the larger *ReportLab* library. Its advantage is a much smaller 
library compared to LaTeX libraries. It is the default PDF *doc*.

A LaTeX *pdftex doc* requires separate installation of the large *texlive*
LaTeX library (approx. 3GB). Its advantage is additional control over *doc*
formatting and appearance.

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[2]** Stand-alone Docs
----------------------------------------------------------

.. raw:: html

    <hr>

A single document that will not be part of a report, may be published using the
local folder rivt folder for reading and writing files, without referencing the
*rivt report folder* structure.

A stand-alone *doc* is published using the following settings:

#. The path in *commands* is specified with the standard "./" current folder syntax. 
#. The *rv_local* variable in the *Meta API* is set to "True".
  
Any *rivt file* can be converted to a stand-alone *doc* using the above steps.
The text, PDF and HTML *docs* will be written to the local file using simple
style settings built into *rivtlib*. Stand-alone *docs* require less setup but
also offer less formatting control.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvD02-folders.rst
    rvD03-reports.rst
    rvD04-settings.rst
