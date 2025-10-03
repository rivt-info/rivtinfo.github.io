**1.1** API
================

**[1]** import rivtlib :literal:`                                          <i>`
-------------------------------------------------------------------------------

.. raw:: html

    <hr>

A *rivt file* is a Python file (.py) that imports the *rivtlib* library
into the *rv namespace*::

    import rivtlib.rvapi as rv

*rivtlib* includes 8 API functions which may be run in a script or interactively
as notebook cells in *VSCode* or other *IDE*.

**[2]** API functions :literal:`                                           <i>`
-------------------------------------------------------------------------------

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
functions (**R I V T**) output formatted utf-8 text to the terminal and can
generate *doc* content.

The last four functions (**D M S Q**) are related to processing and output. The
*Doc* function writes text, PDF or HTML *doc* files. The *Meta* function
contains *rivt file* author and version information. The *Skip* and *Quit*
functions are used for interactive editing and debugging.

**3** <i> rivt Strings
----------------------------

An API function starts in the first column and takes a *rivt string* (rS)
argument enclosed in triple quotes. The first line is a header that specifies
overall section labeling and processing. The header is followed by the section
content, indented four spaces for legibility and section folding.

.. code-block:: python

    rv._("""Header

        section content
        ...
        ...
        
        """)

Section content includes arbitrary utf-8 text and may include *rivt tags and
commands*. See :doc:`Markup </dv03-markup/rv00-markup>` for further details.




**4** <i>  Docs
----------------------------

*rivt files* are compiled into *docs* that are formatted as text (.txt), HTML
(.html) and PDF (.pdf) files. Each output type is generated from the same *rivt
file*. Output types are specified in the 
:doc:`Doc function </dv03-markup/rv06-markup-d>` (*rv.D*).

