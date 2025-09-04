**3.4** Commands
===================

*rivt commands* are used to read and write external files and assign values to
variables. They typically start in the first column with double vertical bars
followed by the command name, the relative file path and parameters.There are
two exceptions to this pattern - the assignment (=) and definition (:=)
commands are used to evaluate equations.

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

.. topic:: || IMG | relative path | caption, scale,;_[F]

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

|| IMG2 | :  read and insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG2 | relative path | cap1, cap2, sca1, sca2,;_[F] 

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

|| VALUES | :  read and insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG2 | relative path | title, [rows], -;_[V] 

    - reads values.txt file
    - rv.I, rv.V
    - PDF, HTML

|| TABLE | :  read and insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: || IMG2 | relative path | title, col w, l;c;r, [r], -;_[T]

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




  
