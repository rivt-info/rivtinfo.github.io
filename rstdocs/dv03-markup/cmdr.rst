3.6 **R** un Commands
=======================

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

   input file types



**WIN** - command script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | WIN | relative path | filename

   reads .txt, .cmd, .bat  files

**MACOS** - shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | relative path | filename  

   reads .sh files

**LINUX** - shell script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LINUX | relative path | filename 

   reads .sh files

