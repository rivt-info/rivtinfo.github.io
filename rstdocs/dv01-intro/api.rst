1.1 API
================

**[01]** import rivtlib
------------------------------

.. raw:: html

    <hr>

Python combines new functions and libraries using *import* statements
and *namespaces*. A **rivt** file is a Python file (.py) that *imports* the
**rivtlib** library and assigns the *namespace* **rv**::

    import rivtlib.rvapi as rv

rivtlib exposes 7 API functions which may be run in a script or interactively
as notebook cells in an IDE (e.g. VSCode).

**[02]** API functions
----------------------------

.. raw:: html

    <hr>

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

API functions may be arbitrarily ordered. Each function evaluates a *rivt
string* (a triple-quoted string argument, rS). 

The first four functions in the table (**R I V T**) output formatted utf-8 text
to the terminal and generate *doc* content. 

The last three functions (**D S Q**) process files or sections. The *Docs*
function writes a doc as a text, PDF or HTML file. The *Skip* and *Quit*
functions are used primarily in interactive editing and processing.


**[03]** rivt string
----------------------------

An API function starts in the first column. Its *rivt string* argument is
enclosed in triple quotes and begins with a header that specifies section
labeling and processing. The section content follows the header on subsequent
lines and is indented four spaces for legibility and section folding.

Section content includes rivt-markup tags and commands and may include
arbitrary utf-8 text. See :doc:`Markup </dv03-markup/_dv03-markup>` for further
details.

.. code-block:: python

    rv._("""Header

        section content
        ...
        
        """)


**[04]** Docs
----------------------------

Docs are formatted output files specified by the *Doc* function. Docs include
text (.txt), HTML (.html) and PDF (.pdf) files. Each output type is generated
from the same *rivt file*.

PDF files are produced in two ways, referred to as *rpdf* and *tpdf*.An *rpdf*
doc is formatted using the rst2pdf library, a susbset of the larger ReportLab
library. Its advantage includes a much smaller library size and it is the
default PDF Doc for the rivt framework. A PDF doc produced using *tpdf*
requires a separate installation of the large texlive LaTeX library. Its
advantage is extensive control over the Doc appearance.

**[05]** Command Line 
------------------------

rivtlib is generally run in an IDE. If run from the command line the command
takes one of two forms depending on whether the file is part of a report. If
part of a report the form is:

    python -m rivtlib rvddss-filename.py

where *rvddss-* is the doc number and*dd* and *ss* are integers identifying the
report division and subdivision respectively. 
