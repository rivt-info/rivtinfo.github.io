3.1 Syntax
================

[01] Overview
--------------

The basic syntax of a *rivt string* is a string of utf-8 characters preceded by
a header. The *rivt string* is enclosed within one of 7 API functions that
start in column one. Each function may also define a *doc* section. 

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
This allows for embedding *restructuredText* commands for formatting PDF and
HTML docs.

[02] Header 
--------------

The first line of a *rivt-string* is a header containing a *section label* and
two control *parameters*. The *section label* is the title for a new section. When
preceeded by two dashes (--) the section is merged with the prior section.
  
.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content
        ...
        
        """)

The *parameters* specifiy whether the *section content* is output to *docs*,
and whether the section is written to a *public rivt file*. The paramters only
need to be specified where different from the defaults.

============= ============================
API function    default header parameters       
============= ============================
rv.R             noprint, private
rv.I             print, private
rv.V             print, private
rv.T             noprint, private
rv.D             noprint, private
rv.S             noprint, private
rv.Q             noprint, private
============= ============================


[03] Section Content
----------------------

Section content is indented four spaces (for legibility and code folding) and
includes *commands* for file operations and *tags* for text formatting. Any
text not defined by commands or tags is passed through as formatted text or 
`restructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_.

*rivt markup* wraps and extends *restructuredText* and adds two additional
markup elements - *tags* and *commands* - that simplify improve legiblity and use.
They generate different doc types (text, PDF and HTML) using the same rivt file.

**Tags**

*Line tags* format a line of text and are denoted with _[**TAG**], typically
added at the end of the line and

*Block tags* evaluate a multi-line text block that starts with _[[**TAG**]]
and ends with _[[**Q**]]. 

**Commands**

*Commands* read and write files and assign values to variables. They start in the
first column with double vertical bars, followed by the command name, the
relative file path and parameters. The exceptions are the assign (=) and define
(:=) commands, related to equations.

*RestructuredText*

Text in a *rivt string* not defined by *commands* or *tags* is passed through
to a *restructuredText (reST)* file used to write PDF and HTML *docs*. In
addition, *commands* and *tags* are often converted to *reST* when processing a
*rivt file*. Most *restructuredText* syntax is stripped out
when writting a *text doc*.


Common *restructuredText* useful in a *rivt string* include surrounding test
with * for italics and ** for bold.




