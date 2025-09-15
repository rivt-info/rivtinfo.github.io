3.1 Syntax
================

The general syntax of a rivt string is text enclosed in triple quotes, where
the first line is a section header and subsequent lines are section content
indented 4 spaces.

**[01]** Header 
------------------

The first line of a *rivt-string* is a header with a *section label* and two
*parameters* separated by a vertical bar. The *section label* is the title for
the new section and the *parameters* specify write settings for the section. A
section is a numbered, bookmarked and linked section in a *doc*.
  
.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section content
        ...
        
        """)


When the *section label* is preceeded by two dashes (--) the section output is
merged with the prior section output and does not start a new *doc section*.

The two write parameters specify

- whether the section output is written to the *docs*
- whether the section is written to a *public file* 
  
They only need to be specified when different from defaults.

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


**[02]** Section Content
-----------------------------

Section content is indented four spaces (for legibility and code folding) and
includes *tags* for text formatting and *commands* for file operations. Any
text not defined by *commands* or *tags* is passed through unchanged to
intermediate files for further PDF and HTML processing, or formatted to a utf-8
*doc*.


.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content
        ...
        
        """)

*rivt markup* includes *tag* and *command* elements and wraps and extends
*restructuredText*. It provides a unified markup that can generate text, PDF or
HTML docs from the same file.

:doc:`Tags </dv03-markup/quick>`

*Line tags* format a line of text and are denoted
with _[**TAG**], typically added at the end of the line.

*Block tags* evaluate a multi-line text block that starts
with _[[**TAG**]] and ends with _[[**Q**]].

:doc:`Commands </dv03-markup/quick>`

*Commands* read and write files and assign values to variables. They start in
the first column with a vertical bar, followed by the command name, the
relative file path, file path and parameters. The exceptions are the assign (=)
and define (:=) commands, related to equations.

`RestructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

Text in a *rivt string* not defined by *commands* or *tags* is passed through
to the intermediate *restructuredText (reST)* file that is used to write PDF
and HTML *docs*. In general *commands* and *tags* are often converted to
*reST* when processing a *rivt file* and stripped when writting a *text doc*.


Common *restructuredText* that is useful in a *rivt string* include: 

- surrounding test with * for italics and ** for bold.




