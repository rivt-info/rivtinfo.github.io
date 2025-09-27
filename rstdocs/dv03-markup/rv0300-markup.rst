3. Markup
==================

*rivt* uses *rivt markup* to provide a readable, common language that generates
text, PDF or HTML *docs* from the same *rivt file*. *rivt markup" is used
within a *rivt string*. A *rivt string* is the utf-8 text argument to a *rivt*
API function.

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

Each API function starts in the first column (standard Python syntax) and defines
a *doc section*. The first line in a *rivt string* is a *section header*.
Subsequent lines are indented 4 spaces and include *tags* and *commands*.

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
- whether the API with its *rivt string* is written to a *public rivt file* 
- for *rv.V* only - where the *value file* is written

They only need to be specified when different from defaults.

============= ==============================
API function    default write parameters       
============= ==============================
rv.R             nowrite, private
rv.I             write, private
rv.V             write, private, rvsource
rv.T             nowrite, private
rv.D             nowrite, private
rv.M             nowrite, private
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

:doc:`Tags </dv03-markup/rv0307-quick>`

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 

*rivt tags* come *Line tags* format a line of text and are denoted
with _[**TAG**], typically added at the end of the line.

*Block tags* evaluate a multi-line text block that starts
with _[[**TAG**]] and ends with _[[**Q**]].

:doc:`Commands </dv03-markup/rv0307-quick>`


*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name and parameters. The exceptions to this pattern are the
assignment ( = ) and definition ( := ) commands which are used to assign values
and evaluate equations. 

Parameter options are separated with commas and parameter elements by
semicolons. Path names can be directly specified (relative to the project
*source folder*) or specified with an alias:

    *rvsource* : this alias directs *rivtlib* to look for the file in the
    source folder. For example if the *rivt file* is in division 1
    and the API function is *Insert* the folder *i01* in *source* is searched.

    *rvlocal* : this alias directs *rivtlib* to look for the file in the *rivt
    file* directory. It is used when a *single doc*, ratherh than a *report
    doc* is processed.

The *rivt project* folders are described 
:doc:`here. </dv04-reports/rv0402-folders>`


.. toctree::
    :maxdepth: 1
    :hidden:

    rv0301-markup-r.rst
    rv0302-markup-i.rst
    rv0303-markup-v.rst
    rv0304-markup-t.rst
    rv0305-markup-m.rst
    rv0306-markup-d.rst
    rv0307-quick.rst
    rv0308-example1.rst
