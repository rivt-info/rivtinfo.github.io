3.4 Commands
===================

*rivt commands* read and write external files and assign values to
variables. They typically start in the first column with double vertical bars
followed by the command name, the relative file path and parameters.There are
two exceptions to this pattern - the assignment (=) and definition (:=)
commands are used to evaluate equations.

In the syntax description below parameter options are separated with
semi-colons and elements by commas. File locations are specified using paths
relative to the rivt file location. Using the standard folder structure is
strongly recommended. Folder organization is described `here <5-folders.html>`_.

In the syntax description below, parameters are separated by commas and
parameter options are separated by semi-colons. Commands have a function and
output scope.

**KEY**  
--------------------------------------------

|| COMMAND | : description

.. raw:: html

    <hr>

.. topic::  command syntax

    - input or output file types
    - function scope
    - applicable doc types


|| APPEND | :  append a PDF file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || APPEND | relative path | num; nonum 

    - reads PDF files
    - rv.D
    - PDF, HTML

|| DOC | :  write a doc file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || DOC | relative path | rpdf; txt; html; tpdf

    - writes PDF or HTML files
    - rv.D
    - PDF, HTML, text

|| IMG | :  read and insert image file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG | relative path | caption _[F], scale

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

|| IMG2 | :  read and insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG2 | relative path | cap1 _[F], cap2 _[F], sca1, sca2 

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

|| VALUES | :  read and insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG2 | relative path | title _[V], [rows]

    - reads values.txt file
    - rv.I, rv.V
    - PDF, HTML

|| TABLE | :  read and insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG2 | relative path | title _[T], col w, l;c;r, [r]

    - reads CSV, TEXT and EXCEL files (.csv, .txt, xlsx)
    - rv.I, rv.V
    - PDF, HTML

|| TEXT | :  read and insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG2 | relative path | _[[block tag]]

    - reads TEXT and TEX files (.txt, .tex)
    - rv.I, rv.V
    - PDF, HTML

=  :  assign value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: a = 10*IN | unit1, unit2 | description

    - assigns value to a variable
    - rv.V
    - PDF, HTML

:=  :  define equation
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: a := b * 10 | unit1, unit2 | var-deci, eq-deci  

    - defines variable in terms of expression
    - rv.V
    - PDF, HTML




  
