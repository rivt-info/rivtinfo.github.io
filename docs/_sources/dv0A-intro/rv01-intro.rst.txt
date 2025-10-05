
**A.1 Introduction**
=================================================================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Summary
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source software project that faciliates the reuse and
improvement of engineering documents. Writing engineering documents typically
involves combining text, tables, diagrams, equations and calculations from a
variety of sources. Although software combining these elements is available,
reusing a document is generally difficult because of the following limitations:

- documents are divided among many incompatible programs
- documents are inaccessible without frequently updating software
- update costs are high
- software is limited to specific platforms
- version controls are limited
- report generation features are limited
- collaboration features are limited

The table below compares *rivt* with other representative software and
summarizes how it addresses these limitations:

.. rst-class:: center


Table 1 - **Reuse Features**

============ ========= ======== ======== ========= ========= ============= 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_  CP [5]_   Collab [6]_  
============ ========= ======== ======== ========= ========= ============= 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS     some     some       no      no          yes      some  
Jupyter        no       no         no      yes         yes      yes  
**rivt**      **yes**  **yes**   **yes**  **yes**   **yes**    **yes**
============ ========= ======== ======== ========= ========= ============= 


.. rst-class:: left

    .. [1] Report generation
    .. [2] Version control
    .. [3] Plain text input files
    .. [4] Forward and backward compatibility
    .. [5] Cross-platform
    .. [6] Collaboration support


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** import rivtlib 
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A *rivt file* is a Python plain text file (.py) that imports the *rivtlib*
library into the *rv namespace*:

.. code-block:: python

    import rivtlib.rvapi as rv

*rivtlib* includes 8 API functions run as a script or interactively as notebook
cells in *VSCode* or other *IDE*.

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


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** rivt Strings and Docs
------------------------------------------------------------------------ 

.. raw:: html

    <hr>

The first four functions (**R I V T**) output formatted utf-8 text to the
terminal and can generate *doc* content. The last four functions (**D M S Q**)
are related to processing and output. The *Doc* function writes text, PDF or
HTML *doc* files. The *Meta* function contains *rivt file* author and version
information. The *Skip* and *Quit* functions are used for interactive editing
and debugging.

An API function starts in the first column and takes a *rivt string* (rS)
argument enclosed in triple quotes. The first line is a header that specifies
overall section labeling and processing, followed by the section
content. Content is indented four spaces for legibility and section folding.

.. code-block:: python

    rv._("""Header

        section content
        ...
        ...
        
        """)

Section content includes *rivt markup* - a plain text, light weight language
that generates *docs* from the same *rivt file* in different formats. See
:doc:`Markup</dv0C-markup/rv01-markup>` for further details. *rivt files* are
compiled into *docs* that are formatted as text (.txt), HTML (.html) or PDF
(.pdf) files.

.. toctree::
    :maxdepth: 1
    :hidden:

    rv02-terms.rst
    rv03-faq.rst
    rv04-smallex1.rst
    rv05-smallex2.rst