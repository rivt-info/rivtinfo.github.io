**1.1 - API**
==============


A **rivt** file is a Python text file (.py) importing the **rivtlib** API:: 

    import rivtlib.rvapi as rv

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

test  
-----

The first four functions (**R I V T**) are content functions - they generate
doc content. Content functions evaluate the triple-quoted string argument
(**rivt-string**) to a formatted utf-8 text string and outputs it to the terminal.
The output is a doc section, unless the section heading is explicitly
suppressed. 

The last three functions (**D S Q**) are process functions - they process
sections without generating content. When the **Doc** function is called the
entire rivt file is evaluated and a doc is output in the specified format -
text, PDF or HTML.

API functions may be run interactively as cells in a notebook IDE (e.g.
VSCode), using the standard cell decorator *# %%*. They are evaluated top to
bottom, similar to a Python script, and may be combined in any order as long as
variables and expressions are previously defined.

The syntax for each rivt-string is 

