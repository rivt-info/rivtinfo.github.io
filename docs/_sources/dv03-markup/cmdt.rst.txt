3.9 Commands in [T]ools
========================

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

**PYTHON** - Python functions and scripts
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | PYTHON | path | filename

   reads .py files


**HTML** - HTML markup
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | path | filename  

   reads .html files


**LATEX** - LaTeX code
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | path | filename 

   reads .tex file


**QCAD** - QCAD script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | QCAD | path | filename 

   reads .js file