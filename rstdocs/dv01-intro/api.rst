1.1 API
================

**[01]** import rivtlib
------------------------------

.. raw:: html

    <hr>

A *rivt file* is a Python file (.py) that *imports* the **rivtlib** library
into the *namespace* **rv**::

    import rivtlib.rvapi as rv

rivtlib includes 8 API functions which may be run in a script or interactively
as notebook cells in an IDE (e.g. VSCode).

**[02]** API functions
----------------------------

.. raw:: html

    <hr>

=============== =============== ===================================
API              Name             Purpose
=============== =============== ===================================
rv.R(rs)           Run               Run shell commands
rv.I(rs)           Insert            Insert static resources 
rv.V(rs)           Value             Calculate values
rv.T(rs)           Tool              Run Python functions
rv.D(rs)           Doc               Write docs 
rv.M(rs)           Meta              Meta data 
rv.S(rs)           Skip              Skip section
rv.Q(rs)           Quit              Exit rivt 
=============== =============== ===================================

Each function evaluates a triple-quoted string argument (rS). The first four
functions (*R I V T*) output formatted utf-8 text to the terminal and can
generate *doc* content.

The last four functions (*D M S Q*) are related to processing and management.
The *Doc* function writes text, PDF or HTML *doc* files. The *Meta* function
contains information related to file sharing. The *Skip* and *Quit* functions
are used for interactive editing and debugging.

**[03]** API argument
----------------------------

An API function starts in the first column. Its argument is a *rivt string*
(rS) enclosed in triple quotes. The first line is a header that specifies
overalll section labeling and processing. The header is followed by the section
content. Content is indented four spaces for legibility and section folding.

Section content includes *rivt tags and commands* may include
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

PDF files are produced in two ways, referred to as *rpdf* and *tpdf*. An *rpdf*
doc is formatted using the *rst2pdf* library, a susbset of the larger
*ReportLab* library. It is the default *rivt PDF doc*. Its advantage is a much
smaller library compared to other PDF libraries. A *rivt LaTeX doc* (*tpdf*)
requires a separate installation of the large texlive LaTeX library. Its
advantage is extensive control over *doc* formatting and appearance.

**[05]** Command Line 
------------------------

rivtlib is generally run interactilvey in an IDE. If run from the command line
the command is

.. code-block:: bash

    python rvddss-filename.py

where *rvddss-* is the doc number and*dd* and *ss* are integers identifying the
report division and subdivision respectively. See 
:doc:`here </dv04-reports/rv0402-folders>` for further details.
