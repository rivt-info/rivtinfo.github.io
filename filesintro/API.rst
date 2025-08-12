**API**
========


A **rivt** file is a Python text file (.py) importing the **rivtlib** API:: 

    import rivtlib.rvapi as rv

that provides 7 API functions::

    rv.R(rS) - (Run Script) Run shell scripts 
    rv.I(rS) - (Insert) Insert static text, images, tables and equations 
    rv.V(rS) - (Values) Evaluate tables and equations 
    rv.T(rS) - (Tools) Execute Python functions and scripts
    rv.D(rS) - (Doc Write) Write formatted rivt docs
    rv.S(rS) - (Skip String) Skip evaluation of rivt-string
    rv.Q(rS) - (Quit) Stop processing 

Each RIVT API function evaluates its triple-quoted string argument
(rivt-string) to a formatted utf-8 text string and outputs it to the terminal.
They format to a doc section unless the sectioning is explicitly suppressed.
RIVT API functions may be run as cells in interactive notebook evaluations.

The other three API functions are used to control document evaluation and doc
output format. When the **Doc Write** function is called the entire rivt
file is evaluated and a doc is output in the specified format.


