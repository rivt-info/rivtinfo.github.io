**D.1 Docs**
========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** rivt Docs
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

Each :term:`rivt file` outputs a corresponding formatted :term:`doc` written to
the *publish* folder unless it is published as a :term:`stand-alone doc`. 

*Docs* may be text, HTML or PDF. PDF *doc* files are produced by two different
libraries, referred to as *pdf* and *pdftex*. A *pdf* doc is formatted using
the *rst2pdf* library, a subset of the larger *ReportLab* library. It is the
default PDF *doc*. Its advantage is a small library that has been incorporated
into *rivt*.

A *pdftex doc* requires separate installation of the much larger *texlive*
LaTeX library (approx. 3GB). Its advantage is additional control over *doc*
formatting and appearance.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Report Docs
----------------------------------------------------------

.. raw:: html

    <hr>

A *report* is assembled from multiple *docs* using the *doc numbers* to
organize the *docs* into divsions and subdivisions. The top level folder
structure for a *report* is shown below. Further *report folder* details are
:doc:`here. <rvD03-folders>`

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

        ├── [logs]/                      || Log files folder
        ├── [public]/                   || Public rivt files folder
        ├── [publish]/                  || Docs and reports folder
        ├── [src]/                      |||| Source files folder
        └── README.txt                  || Searchable text report 


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** Stand-alone Docs
----------------------------------------------------------

.. raw:: html

    <hr>

A document that will not be part of a report may be formatted using the
rivt file folder for reading and writing files, without referencing the
*rivt report folders*. A stand-alone *doc* is published using the
following settings:

#. The *rv_local* variable is set to "True" in the *Meta API*.
#. The *COMMAND* path is just the file name. 
  
A *rivt file* can be converted to a stand-alone *doc* using the above steps.
The text, PDF and HTML *docs* will be written to the local file folder using
simple style settings built into *rivtlib*. Stand-alone *docs* require less
setup but also offer less formatting control.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvD02-files.rst
    rvD03-folders.rst
    rvD04-setting.rst
    rvD05-reportex.rst
