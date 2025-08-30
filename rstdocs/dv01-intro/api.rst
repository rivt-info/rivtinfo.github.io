
 **1.2** API
================


[01] - Import
---------------

A **rivt** file is a Python text file (.py) importing the **rivtlib** API:: 

    import rivtlib.rvapi as rv

API functions may be run interactively as cells in a notebook IDE (e.g.
VSCode), using the standard cell decorator *# %%*. They are evaluated top to
bottom, similar to a Python script, and may be combined in any order as long as
variables and expressions are previously defined.

[02] - API functions
----------------------

The rvapi.py module provides 7 API functions:

=========== =============== ===================================
API         Name             Purpose
=========== =============== ===================================
**rv.R**    Run               Run shell commands
**rv.I**    Insert            Insert static resources 
**rv.V**    Values            Calculate values
**rv.T**    Tools             Run Python functions
rv.D        Docs              Write docs 
rv.S        Skip              Skip section
rv.Q        Quit              Exit rivt 
=========== =============== ===================================


[03] - Content Functions
-----------------------------------

The first four functions (**R I V T**) generate content.
They evaluate the triple-quoted string argument
(**rivt-string**) and output utf-8 text to the terminal.


[04] - Process Functions
-----------------------------------

The last three functions (**D S Q**) process sections or files. The *Doc* 
function processes the file and writes it to a text, PDF or HTML file. The  
*Skip* and *Quit* functions are typically used in interactive 
editing and processing.




