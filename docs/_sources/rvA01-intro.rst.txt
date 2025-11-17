**A.1 Introduction**
=================================================================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Summary
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source software project that simplifies reuse and sharing of
engineering documents. Reuse and sharing provides opportunities for continual
improvement. Although a number of document programs are curently available,
reuse and sharing is generally difficult because of limitations in the
software and its distribution:

- documents are divided among many incompatible programs
- document formats become obsolete an inaccessible
- frequent software updates are needed
- update costs are high
- software is limited to specific platforms
- version control is limited
- report generation features are limited
- collaboration features are limited

The table below summarizes these limitations and compares *rivt* with other
software programs.

.. rst-class:: center


Table 1 - **Document Limitations - Comparison**

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


**[2]** rivt Files
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A :term:`rivt file` is a Python plain text file (.py) that imports the 
:term:`rivtlib` library into the :term:`rv-namespace`:

.. code-block:: python

    import rivtlib.rvapi as rv

*rivtlib* includes 6 primary and 2 auxilliary API functions that may be run as
a script or interactively as notebook cells in *VSCode* or other *IDE*.

Engineering documents and reports typically combine text, tables, diagrams,
models and calculations to describe and justify decisions and designs. The
*rivt API* is designed to simplify the document organization and publishing
process through the use of half a dozen API functions that process 
:term:`rivt markup`, along with a pre-defined :ref:`folder structure <report-folders>`. 

Each *rivt file* outputs a formatted rivt :term:`doc` as a text, PDF or HTML
document. Reports are organized assemblies of *docs*.

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[3]** rivt API 
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

=============== =============== ===========================================
API Function        Name             Purpose
=============== =============== ===========================================
rv.M(rS)           Meta              Meta data 
rv.R(rS)           Run               Run shell commands
rv.I(rS)           Insert            Insert static resources 
rv.V(rS)           Value             Calculate values
rv.T(rS)           Tool              Import Python and Markup functions
rv.D(rS)           Doc               Publish docs 
rv.S(rS)           Skip              Skip section
rv.X(rS)           Quit              Exit rivt 
=============== =============== ===========================================

Each function takes a single *rivt string* (triple quoted string) argument.

The four content functions (**R I V T**) output formatted utf-8 text to the
terminal and generate *doc* content. The *Run API* executes shell commands.
The *Insert API* adds table, image, equation and text (static) content. The
*Value API* evaluates equations and functions. The *Tool API* extends *rivt* by
importing and processing raw HTML, LaTeX, and Python scripts.

The four processing functions (**M D S Q**) are related to processing and output.
The *Meta* function specifies *rivt file* author and version information and
sets processing variables. The *Doc* function controls publishing formatted
dcouments (*doc* files) as text, PDF or HTML . The *Skip* and *Exit* functions
are used for interactive editing and debugging.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** rivt Strings
------------------------------------------------------------------------ 

.. raw:: html

    <hr>

An API function starts in the first column and takes a single 
:term:`rivt string` (rS) argument. The first line of a *rivt string* is a header
that specifies section labeling and processing. The :term:`header` is followed 
byvthe section text, indented four spaces for legibility and section folding.

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
    