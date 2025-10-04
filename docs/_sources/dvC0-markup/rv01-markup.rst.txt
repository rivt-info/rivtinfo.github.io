**C.1** Markup
==================

*rivt markup* provides a readable, common language that generates text, PDF or
HTML *docs* from the same *rivt file*. It is used in a *rivt string* - a
utf-8 text string argument to a *rivtlib* API function.

The first line in a *rivt string* is a *section header* that defines a section
label and its visibility. The API function and header starts in the first
column (standard Python syntax), with subsequent lines indented 4 spaces for
improved readability and code folding.

.. code-block:: python

    rv._("""Section Label | hide;print, public;private; (rvsource, rvlocal)

        section content (utf-8 text)
        ...
        ...
        
        """)

A *rivt doc* is defined by 8 API functions. The first four functions **(R, I,
V, T)** defined the *doc* content. The last four **(D, M, S, Q)** define *doc*
processing. API functions may be used in any order and number with the
exception of *rv.M*, which is the first function in a *doc* if used.

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
rv.Q(rs)         Quit              Exit rivtlib
=============== =============== ===================================


**[01]** Header 
------------------

A header starts with a *section label* followed by a vertical separator bar and
*parameters* that override the section write behavior. 

.. code-block:: python

    rv._("""Section Label | hide;print, public;private; (rvsource, rvlocal)

        section content (utf-8 text)
        ...
        ...
        
        """)


The *section label* is the section title. If the *section label* is preceeded
by two dashes (*--section label*) the section output is merged with the prior
section, instead of starting a new one. Sections are numbered, bookmarked and
linked when output to *doc*. The write *parameters* specify:

- whether the section output is written to the *doc* 
- whether the API with its *rivt string* is written to a *public rivt file* 
- where the *value file* is exported (for *rv.V* only)

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


**[02]** Section Content 
--------------------------

Section content is indented four spaces (for legibility and code folding) and
includes *tags* for text formatting and *commands* for file operations.

.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section content
        ...
        
        """)


As a section is processed, line by line, it is passed to a 
`RestructuredText string <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_,
which is then further processed to an HTML or PDF file. If a line does not 
contain a *command* or *tag* it is passed through as is. This allows for 
embedded *restructured text*, e.g. surrounding text with *  for italics 
or ** for bold. 

*Text docs* are formatted separately.


**[03]** Tags and Commands
----------------------------

:doc:`Tags </dv03-markup/rv07-quick>`

*Line tags* format a line of text and are denoted with **_[TAG]**, usually at
the end of the line.

*Block tags* format a block of text that begin with **_[[TAG]]**
on the first line and end with **_[[Q]]** after the last line. 

:doc:`Commands </dv03-markup/rv07-quick>`

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name and parameters. The exceptions to this pattern are the
assignment (**<=** ) and definition (**:=**) commands, which are used to assign
values to equation results and define variables.


.. toctree::
    :maxdepth: 1
    :hidden:

    rv01-markup-r.rst
    rv02-markup-i.rst
    rv03-markup-v.rst
    rv04-markup-t.rst
    rv05-markup-m.rst
    rv06-markup-d.rst
    rv07-quick.rst
    rv08-example1.rst
