3.4 Commands
===================

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by 
the command name and parameters.

There are two exceptions to this pattern - the assignment ( = ) and definition
( := ) commands which are used to assign values and evaluate equations.

In the syntax description below parameter options are separated with
semi-colons and elements by commas. File locations are specified using paths
relative to the rivt file location. Using the standard folder structure is
strongly recommended. Folder organization is described `here <5-folders.html>`_.

In the syntax description below, parameters are separated by commas and
parameter options are separated by semi-colons. Commands have a function and
output scope.

**KEY**  
-------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

    - input or output file types
    - function scope
    - applicable doc types


 | APPEND |   append a PDF file
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | APPEND | relative path | filename | num; nonum 

    - reads PDF files
    - rv.D
    - PDF, HTML

 | DOC | :  write doc file
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | DOC | relative path | filename | rpdf; txt; html; tpdf

    - writes PDF or HTML files
    - rv.D
    - PDF, HTML, text

 | IMG | :  insert image file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | relative path | filename | caption _[F], scale

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

 | IMG2 | :  insert images side by side
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | rel path | fname1, fname2 | cap1 _[F], cap2 _[F], sc1, sc2 

    - reads PNG and JPEG files (.png, jpg)
    - rv.I, rv.V
    - PDF, HTML

 | TEXT | :  insert text file
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | relative path | filename | _[[block tag]]

    - reads TEXT and TEX files (.txt, .tex)
    - rv.I, rv.V
    - PDF, HTML

 | VALUES | :  insert and evaluate values
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | VALUES | relative path | filename | title _[V], [rows]

    - reads values.txt file
    - rv.I, rv.V
    - PDF, HTML

=  :  assign value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: a = 10*IN | unit1, unit2 | filename | description

    - assigns value to a variable
    - rv.V
    - PDF, HTML

:=  :  define equation
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b := a * 10 | unit1, unit2, var-deci, eq-deci 

    - defines a variable in terms of expression
    - rv.V
    - PDF, HTML
