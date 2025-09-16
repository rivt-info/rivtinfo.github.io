3. Markup
==================

*rivt markup* provides a unified language that generates text, PDF or HTML
*docs* from the same file. The *markup* is enclosed in a *rivt string* which
includes a header line followed by lines of text, all enclosed in triple
quotes. A *rivt string* is the argument to each of the 7 *rivt* API functions.

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

Each function starts in column one and defines a *doc section*. The first line
in the *rivt string* is a *section header*. Subsequent lines define *section
content* and are indented 4 spaces.

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


**[02]** Section Content 
--------------------------

Section content is indented four spaces (for legibility and code folding) and
includes *tags* for text formatting and *commands* for file operations.
*commands* and *tags* are generally converted to *reST* when processing a *rivt
file*. *Text docs* are formatted separately.


.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section content
        ...
        
        """)

Text in a *rivt string* not defined by *commands* or *tags* is passed through
to an intermediate `RestructuredText file 
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ used to
write PDF and HTML *docs*.  Embedded *restructuredText* that commonly used
in a *rivt string* includes:

- surrounding text with * for italics or ** for bold.


**[03]** Tags and Commands
----------------------------

:doc:`Tags </dv03-markup/rv0310-quick>`

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 

*rivt tags* come *Line tags* format a line of text and are denoted
with _[**TAG**], typically added at the end of the line.

*Block tags* evaluate a multi-line text block that starts
with _[[**TAG**]] and ends with _[[**Q**]].

:doc:`Commands </dv03-markup/rv0310-quick>`

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name, file path and parameters. 

*Commands* read and write files and assign values to variables. They start in
the first column with a vertical bar, followed by the command name, the
relative file path, file path and parameters. The exceptions are the assign (=)
and define (:=) commands, related to equations.


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
