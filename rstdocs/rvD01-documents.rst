**D.1 Documents**
========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** rivt Files and Docs
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

Each *rivt file* outputs a corresponding formatted *doc* written to the
*publish folder* unless they are published as a stand-alone *doc* as specified
in the *rv.M API* function. *rivt files* are typically assembled into a
*report*. Further *report folder* details are :doc:`here<rvD03-folders>`

**Folder Key**

- Required folder and file prefix names are shown in brackets [ ]. 
- Single vertical bar ( | ) identifies files provided by the report author. 
- Double vertical bar ( || ) identifies files written by rivtlib 
- Four vertical bars ( |||| ) are a mix of author and rivtlib written files



.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file

        ...
        ...

        ├── [log]/                      || Log files folder
        ├── [public]/                   || Public rivt files folder
        ├── [publish]/                  || Docs and reports folder
        ├── [src]/                      |||| Source files folder
        └── README.txt                  || Searchable text report 

PDF *doc* files are produced by two different libraries, referred to as *pdf*
and *pdftex*. A *pdf* doc is formatted using the *rst2pdf* library, a susbset
of the larger *ReportLab* library. It is the default PDF *doc*. Its advantage
is a small library that is part of *rivt*.

A LaTeX *pdftex doc* requires separate installation of the much larger
*texlive* LaTeX library (approx. 3GB). Its advantage is additional control over
*doc* formatting and appearance.

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[2]** Stand-alone Docs
----------------------------------------------------------

.. raw:: html

    <hr>

A single document that will not be part of a report, may be published using the
local folder rivt folder for reading and writing files, without referencing the
*rivt report folder* structure. A stand-alone *doc* is published using the
following settings:

#. The *rv_local* variable in the *Meta API* is set to "True".
#. The *COMMAND* path is specified with the standard "./" current folder syntax. 
  
A *rivt file* can be converted to a stand-alone *doc* using the above steps.
The text, PDF and HTML *docs* will be written to the local file folder using
simple style settings built into *rivtlib*. Stand-alone *docs* require less
setup but also offer less formatting control.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvD02-reports.rst
    rvD03-folders.rst
    rvD04-setting.rst
    rvD05-reportex.rst
