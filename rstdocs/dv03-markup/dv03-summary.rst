The basic syntax of a *rivt string* is a string of utf-8 characters preceded by
a header. The *rivt string* is enclosed within one of 7 API functions that
start in column one. Each function may also define a *doc section*. 

=============== =============== ===================================
API              Name             Purpose
=============== =============== ===================================
**rv.R(rs)**       Run               Run shell commands
**rv.I(rs)**       Insert            Insert static resources 
**rv.V(rs)**       Values            Calculate values
**rv.T(rs)**       Tools             Run Python functions
rv.D(rs)           Docs              Write docs 
rv.S(rs)           Skip              Skip section
rv.Q(rs)           Quit              Exit rivt 
=============== =============== ===================================

Text that is not a *tag* or *command* is passed to an intermediate .rst file.
This facilitates extending *rivt markup* by embedding 
`restructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_.
formatting commands in a *rivt string*.