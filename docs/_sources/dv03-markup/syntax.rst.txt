3.1 Syntax
================

[01] Overview
--------------

The basic syntax of a *rivt string* is a string of utf-8 characters preceded by
a header. The *rivt string* is enclosed within one of 7 API functions that
start in column one. Each function also, optionally, defines a *doc* section. 


that are not *tags* or *commands* are passed to an
intermediate .rst file. This allows for embedding *restructuredText* commands
that format PDF and HTML docs. Most *restructuredText* syntax is stripped out
when writting a *text doc*.


[02] Header 
--------------

The first line of a *rivt-string* is a header that specifies a section label
and two formatting parameters. When the section label is preceeded by two
dashes (--) the section content is merged with the prior section without
creating a new section.

The parameters specifiy whether the section contents are formatted and output
to docs and whether the section is written to a public rivt file.
  
.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content
        ...
        
        """)


[03] Section Content
----------------------

Section content is indented four spaces (for legibility and code folding) and
includes *commands* for file operations and *tags* for text formatting. Any
text not defined by commands or tags is passed through as `restructuredText
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_.

**rivt markup** wraps and extends *restructuredText* and adds two additional
markup elements - *tags* and *commands* - that simplify improve legiblity and use.
They generate different doc types (text, PDF and HTML) using the same rivt file.

*Tags*

**Line** tags format a line of text and are denoted with _[**TAG**], typically
added at the end of the line and

**Block** tags evaluate a multi-line text block that starts with _[[**TAG**]]
and ends with _[[**Q**]]. 

*Commands*

Commands read and write files and assign values to variables. They start in the
first column with double vertical bars, followed by the command name, the
relative file path and parameters. The exceptions are the assign (=) and define
(:=) commands, related to equations.

*RestructuredText*

Text in a *rivt string* not defined by *commands* or *tags* is passed through
to a *restructuredText (reST)* file used to write PDF and HTML *docs*. In
addition, *cxommands* and *tags* are often converted to *reST* when processing a
*rivt file*.

Common *restructuredText* useful in a *rivt string* include surrounding test
with * for italics and ** for bold.




