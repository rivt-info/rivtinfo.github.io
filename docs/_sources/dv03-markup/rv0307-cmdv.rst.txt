3.8 Commands in [V]alues
=========================

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name and parameters. The exceptions to this pattern are the
assignment ( = ) and definition ( := ) commands which are used to assign values
and evaluate equations.

In the syntax description below parameter options are separated with
semi-colons and parameter elements by commas. Path names can be directly
specified (relative to the project *source folder*) or specified with an alias:

    *rvsource* : this alias directs *rivtlib* to look for the file in the
    source folder. For example if the *rivt file* is in division 1
    and the API function is *Insert* the folder *i01* in *source* is searched.

    *rvlocal* : this alias directs *rivtlib* to look for the file in the *rivt
    file* directory. It is used when a *single doc*, ratherh than a *report
    doc* is processed.

The *rivt project* folder structure is described 
:doc:`here. </dv04-reports/rv0402-folders>`


**KEY**  
-------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

   input or output file types
   applicable doc types


.. raw:: html

    <hr>


**[01]** | IMAGE | 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | path | filename | caption _[F], scale

    - reads PNG and JPEG files (.png, jpg)
    - PDF, HTML

**[02]** | IMAGE2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | path | fname1, fname2 | cap1 _[F], cap2 _[F], sc1, sc2 

    - reads PNG and JPEG files (.png, jpg)
    - PDF, HTML

**[03]** | TABLE | 
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title _[T]

    - reads text, csv and EXCEL files (.txt, .csv, .xls)
    - PDF, HTML, text


**[04]** | VALUES | 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | VALUES | relative path | filename | title _[V], [rows]

    - reads values.txt file
    - PDF, HTML

**[05]** **=** - assign value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: a = 10*IN | unit1, unit2, decimals | description

    - assigns value to a variable
    - PDF, HTML

**[06]** **:=** - define equation
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b := a * 10 | unit1, unit2, decimals | reference

    - defines a variable in terms of expression
    - PDF, HTML
