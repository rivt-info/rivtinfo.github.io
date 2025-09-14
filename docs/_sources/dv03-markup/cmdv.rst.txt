3.8 Value Commands
===================

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name and parameters. The exceptions to this pattern are the
assignment ( = ) and definition ( := ) commands which are used to assign values
and evaluate equations.

In the syntax description below parameter options are separated with
semi-colons and parameter elements by commas. 

Most commands have a *relative path* parameter with three modes:

    *rvdefault* : when this value is provided *rivt* looks for the file in the
    division source directory. For example if the rivt file is in division 1
    and the API function is *Insert* the folder *i01* in *source* is searched.

    *rvlocal* : when this value is provided *rivt* looks for the file in the
    rivt file directory.

    specified source : a specific folder may also be provided. For example if
    *v02* is specified the *v02* folder in the *source* folder is searched.


Project folder organization is described :doc:`here </dv04-reports/folders>`


**KEY**  
-------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

    - input or output file types
    - function scope
    - applicable doc types


**APPEND** - append a PDF file
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | APPEND | relative path | filename | num; nonum 

    - reads PDF files
    - rv.D
    - PDF, HTML

**DOC** - writes doc file
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | DOC | relative path |  txt; html; rpdf; tpdf

    - writes text, PDF or HTML files
    - rv.D
    - PDF, HTML, text
  
    Exits after writing doc file


**IMG** - insert image file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | relative path | filename | caption _[F], scale

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

**IMG2** - insert images side by side
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | rel path | fname1, fname2 | cap1 _[F], cap2 _[F], sc1, sc2 

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

**TEXT** - insert text file
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | relative path | filename | _[[block tag]]

    - reads TEXT and TEX files (.txt, .tex)
    - rv.I, rv.V
    - PDF, HTML

**VALUES** - insert values
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | VALUES | relative path | filename | title _[V], [rows]

    - reads values.txt file
    - rv.I, rv.V
    - PDF, HTML

**=** - assign value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: a = 10*IN | unit1, unit2 | description

    - assigns value to a variable
    - rv.V
    - PDF, HTML

**:=** - define equation
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b := a * 10 | unit1, unit2 | reference

    - defines a variable in terms of expression
    - rv.V
    - PDF, HTML
