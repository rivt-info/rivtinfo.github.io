**A.1 Introduction**
=================================================================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Summary
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source software project that faciliates reuse and shared
improvement of engineering documents. Engineering documents typically combine
text, tables, diagrams, equations and calculations from a variety of sources.
Although writing software combining these elements is available, document reuse
is generally difficult because of limitations in the software and its
distribution:

- documents are divided among many incompatible programs
- documents are inaccessible without frequently updating software
- update costs are high
- software is limited to specific platforms
- version controls are limited
- report generation features are limited
- collaboration features are limited

The table below summarizes these limitations and compares *rivt* with other
software programs.

.. rst-class:: center


Table 1 - **Reuse Limitations - Comparison**

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

*rivtlib* includes 8 API functions that may be run as a script or interactively
as notebook cells in *VSCode* or other *IDE*.

=============== =============== ===================================
API Function        Name             Purpose
=============== =============== ===================================
rv.M(rS)           Meta              Meta data 
rv.R(rS)           Run               Run shell commands
rv.I(rS)           Insert            Insert static resources 
rv.V(rS)           Value             Calculate values
rv.T(rS)           Tool              Run Python functions
rv.D(rS)           Doc               Write docs 
rv.S(rS)           Skip              Skip section
rv.Q(rS)           Quit              Exit rivt 
=============== =============== ===================================


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** rivt Strings and Docs
------------------------------------------------------------------------ 

.. raw:: html

    <hr>

The first four functions (**R I V T**) output formatted utf-8 text to the
terminal and may generate *doc* content. The *Run API* executes shell commands.
The *Insert API* adds static table, image, equation and text content. The
*Value API* evaluates equations and functions. The *Tool API* extends *rivt* by
importing raw HTML and LaTeX and executing *Python scripts* inside or out of
the *rivt namespace*.

The last four functions (**D M S Q**) are related to processing and output. The
*Doc* function writes formatted text, PDF or HTML *doc* files. The *Meta*
function contains *rivt file* author and version information and sets
processing variables. The *Skip* and *Quit* functions are used for interactive
editing and debugging.

An API function starts in the first column and takes a single 
:term:`rivt string` (rS) argument. The first line of a *rivt string* is a 
header that specifies section labeling and processing. The 
:term:`section header` is followed by the section text, indented four 
spaces for legibility and section folding.

.. code-block:: python

    rv._("""Header

        section text
        ...
        ...
        
        """)

Section text includes :term:`rivt markup` - a plain text language that
generates *doc* files formatted as text, HTML or PDF. *rivt markup* includes
:term:`line tags`, :term:`block tags` and :term:`commands` summarized 
:doc:`here. <rvC08-quick>`  See :doc:`Markup</rvC01-markup>` for further 
details. 


.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-terms.rst
    rvA03-faq.rst
    rvA04-docex.rst
    