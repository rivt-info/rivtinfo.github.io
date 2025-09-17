3.10 **Process** Commands
===========================

*Process commands* control the process of generating and assembling *docs*. They
do not directly generate *doc* content.

Most commands have a *relative path* parameter with three modes:

    *rvsource* : when this value is provided *rivt* looks for the file in the
    division source directory. For example if the rivt file is in division 1
    and the API function is *Insert* the subfolder *i01* in the *source* folder
    is searched.

    *rvlocal* : when this value is provided *rivt* looks for the source file in
    the rivt file directory.

    specified source : a specific folder in the *source* subfolder may be
    provided. For example if *v02* is specified the *v02* folder in the
    *source* folder is searched.


Project folder organization is described 
:doc:`here. </dv04-reports/rv0401-folders>`


**KEY**  
-------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

    - input or output file types
    - applicable doc types


.. raw:: html

    <hr>


**[01]** | APPEND  | - append PDF file
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | APPEND | path | filename | before; after

   appends PDF file to *doc*
   PDF, HTML

**[02]** | DOC |  - write doc file
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | DOC | path |  txt; html; rpdf; tpdf

    - writes text, PDF or HTML files
    - PDF, HTML, text
  
    Exits after writing doc file

