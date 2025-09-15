3. Markup
==================

The general syntax of a *rivt string* is text enclosed in triple quotes. A
*rivt string* is the argument to each of the 7 API functions. Each function
starts in column one and defines a *doc section*.

=============== =============== ===================================
API Funct          Name             Purpose
=============== =============== ===================================
*rv.R(rs)*        Run               Run shell commands
*rv.I(rs)*        Insert            Insert static resources 
*rv.V(rs)*        Values            Calculate values
*rv.T(rs)*        Tools             Functions and scripts
*rv.D(rs)*        Docs              Write docs 
*rv.S(rs)*        Skip              Skip section
*rv.Q(rs)*        Quit              Exit rivt 
=============== =============== ===================================

**[01]** rivt string
----------------------

The first line in the string is a *section header*. Subsequent lines are
section content and are indented 4 spaces.

.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content (utf-8 text)
        ...
        
        """)

**[01]** Header 
------------------

The header starts with a *section label* followed by a vertical separator bar
and two write *parameters*, The *section label* is typically the section
title and the write *parameters* specify, for the case of API R,I,T or D:

- whether the section output is written to the *doc*
- whether the section is written to a *public rivt file* 

and for the case of V:

- whether the *value file* is written to the *local* or *source folder*.
- whether the section is written to a *public rivt file* 

They only need to be specified when different from defaults.

============= ============================
API function    default write parameters       
============= ============================
rv.R             nowrite, private
rv.I             print, private
rv.V             rvsource, private
rv.T             nowrite, private
rv.D             nowrite, private
rv.S             nowrite, private
rv.Q             nowrite, private
============= ============================

Sections are numbered, bookmarked and linked when output to *doc*. If the
*section label* is preceeded by two dashes (*--section label*) the section
output is merged with the prior section, instead of starting a new one.

**[02]** Tags and Commands
----------------------------

Section content is indented four spaces (for legibility and code folding) and
includes *tags* for text formatting and *commands* for file operations. Any
text not defined by *commands* or *tags* is passed through unchanged to
intermediate files for further PDF and HTML processing, or formatted to a utf-8
*doc*. *rivt markup* wraps and extends *restructuredText* and provides a
unified markup that can generate text, PDF or HTML docs from the same file.

:doc:`Tags </dv03-markup/rv0310-quick>`

*rivt tags* come *Line tags* format a line of text and are denoted
with _[**TAG**], typically added at the end of the line.

*Block tags* evaluate a multi-line text block that starts
with _[[**TAG**]] and ends with _[[**Q**]].

:doc:`Commands </dv03-markup/rv0310-quick>`

*Commands* read and write files and assign values to variables. They start in
the first column with a vertical bar, followed by the command name, the
relative file path, file path and parameters. The exceptions are the assign (=)
and define (:=) commands, related to equations.

`RestructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

Text in a *rivt string* not defined by *commands* or *tags* is passed through
to the intermediate *restructuredText (reST)* file that is used to write PDF
and HTML *docs*. In addition, *commands* and *tags* are generally converted to
*reST* when processing a *rivt file*. Common *restructuredText* that is useful
in a *rivt string* include:

- surrounding text with * for italics and ** for bold.


*rivt markup* includes sets of *tags* and *commands* for each API function.
When writing PDF and HTML *docs*, text that is not a *tag* or *command* is
passed to an intermediate *.rst* file which allows for embedding
`restructuredText markup
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ in a *rivt
string*.

**Tags**

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 

**Commands**

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name, file path and parameters. 



The general syntax of a *rivt string* is text enclosed in triple quotes. The
first line is a section header. Subsequent lines are indented 4 spaces and
define the section content.
  
.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section content
        ...
        
        """)


For the Values API the header options are

.. code-block:: python

    rv._("""Section Label | rvsource; rvlocal, public; private

        section content
        ...
        
        """)




.. toctree::
    :maxdepth: 1
    :hidden:

    rv0301-tagr.rst
    rv0302-tagi.rst
    rv0303-tagv.rst
    rv0304-tagt.rst
    rv0305-cmdr.rst
    rv0306-cmdi.rst
    rv0307-cmdv.rst
    rv0308-cmdt.rst
    rv0309-cmdprc.rst
    rv0310-quick.rst
    rv0311-example1.rst
