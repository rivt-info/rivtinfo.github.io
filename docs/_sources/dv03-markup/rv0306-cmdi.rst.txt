3.7 Commands in [I]nsert
==========================

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name and parameters. The exceptions to this pattern are the
assignment ( = ) and definition ( := ) commands which are used to assign values
and evaluate equations.

In the syntax description below parameter options are separated with
semi-colons and parameter elements by commas. Path names can be directly
specified (relative to the project *source folder*) or specified with an alias:

    *rvdefault* : this alias directs *rivtlib* to look for the file in the
    source folder. For example if the *rivt file* is in division 1
    and the API function is *Insert* the folder *i01* in *source* is searched.

    *rvlocal* : this alias directs *rivtlib* to look for the file in the *rivt
    file* directory. It is used when a *single doc*, ratherh than a *report
    doc* is processed.

The *rivt project* folder structure is described :doc:`here </dv04-reports/folders>`


**KEY**  
-------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

    - input or output file types
    - applicable doc types



**IMAGE** - insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | path | filename | caption _[F], scale

    - reads PNG and JPEG files (.png, jpg)
    - PDF, HTML

**IMAGE2** - insert adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | path | fname1, fname2 | cap1 _[F], cap2 _[F], sc1, sc2 

    - reads PNG and JPEG files (.png, jpg)
    - PDF, HTML

**TABLE** - insert table 
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title _[T]

    - reads text, csv and EXCEL files (.txt, .csv, .xls)
    - PDF, HTML, text


**TEXT** - insert text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | path | filename | title _[T]

    - reads text, text and reST files (.txt, .tex, .rst)
    - PDF, HTML, text

