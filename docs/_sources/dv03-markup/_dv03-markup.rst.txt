3. Markup
==================

*rivt markup*,  within a *rivt string*, provides a common language to generate
text, PDF or HTML *docs* from the same *rivt file*. *rivt strings* are the
argument to *rivt* API functions. 

=============== =============== ===================================
API Function        Name             Purpose
=============== =============== ===================================
rv.R(rs)         Run               Run shell commands
rv.I(rs)         Insert            Insert static sources 
rv.V(rs)         Value             Calculate values
rv.T(rs)         Tool              Functions and scripts
rv.D(rs)         Doc               Write docs
rv.M(rs)         Meta              Meta data for rivt file 
rv.S(rs)         Skip              Skip section
rv.Q(rs)         Quit              Exit rivt 
=============== =============== ===================================

Each API function starts in the first column (Python syntax) and defines a *doc
section*. The first line in a *rivt string* is a *section header*. Subsequent
lines are indented 4 spaces and include *tags* and *commands*.

.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private; (rvsource, rvlocal)

        section content (utf-8 text)
        ...
        
        """)


**[01]** Header 
------------------

A header starts with a *section label* followed by a vertical separator bar and
*parameters* that override the section write behavior. The *section label* is
typically the section title, and the write *parameters* specify:

- whether the section output is written to the *doc* 
- whether the function and *rivt string* are written to a *public rivt file* 
- where the *value file* is written (rv.V only)

They only need to be specified when different from defaults.

============= ==============================
API function    default write parameters       
============= ==============================
rv.R             nowrite, private
rv.I             write, private
rv.V             write, private, rvsource
rv.T             nowrite, private
rv.D             nowrite, private
rv.S             nowrite, private
rv.Q             nowrite, private
============= ==============================

Sections are numbered, bookmarked and linked when output to *doc*. If the
*section label* is preceeded by two dashes (*--section label*) the section
output is merged with the prior section, instead of starting a new one.


**[02]** Section Content 
--------------------------

Section content is indented four spaces (for legibility and code folding) and
includes *tags* for text formatting and *commands* for file operations.



.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section content
        ...
        
        """)

Text in a *rivt string* not defined by *commands* or *tags* is passed through
to an intermediate `RestructuredText file
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ used to publish
PDF and HTML *docs*. *commands* and *tags* are also converted to *reST* when
processing a *rivt file*. This allows for embedded *restructured text*, e.g.
surrounding text with * for italics or ** for bold. *Text docs* are formatted
separately.


**[03]** Tags and Commands
----------------------------

:doc:`Tags </dv03-markup/rv0312-quick>`

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 

*rivt tags* come *Line tags* format a line of text and are denoted
with _[**TAG**], typically added at the end of the line.

*Block tags* evaluate a multi-line text block that starts
with _[[**TAG**]] and ends with _[[**Q**]].

:doc:`Commands </dv03-markup/rv0312-quick>`

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name, file path and parameters. 

*Commands* read and write files and assign values to variables. They start in
the first column with a vertical bar, followed by the command name, the
relative file path, file path and parameters. The exceptions are the equations
assign (=) and define (:=) commands.


.. toctree::
    :maxdepth: 1
    :hidden:

    rv0301-tagr.rst
    rv0302-tagi.rst
    rv0303-tagv.rst
    rv0304-tagt.rst
    rv0305-tagm.rst
    rv0306-cmdr.rst
    rv0307-cmdi.rst
    rv0308-cmdv.rst
    rv0309-cmdt.rst
    rv0310-cmdd.rst
    rv0311-example1.rst
    rv0312-quick.rst