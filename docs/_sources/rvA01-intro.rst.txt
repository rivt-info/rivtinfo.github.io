**A.1 Introduction**
=================================================================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Summary
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source software project that simplifies reuse of shared 
engineering documents. Collaboration reduces repetitive work and
improves quality. Although a number of document software programs are
available, reuse and sharing is generally difficult because of limitations in
the software terms of use and distribution:

- documents come from many incompatible programs
- document formats become obsolete and inaccessible
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


**[2]** rivt file
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A :term:`rivt file` is a Python plain text file (.py) that imports the 
:term:`rivtlib` library into the :term:`rv-namespace` and defines an API:

.. code-block:: python

    import rivtlib.rvapi as rv


Each *rivt file* outputs a formatted rivt :term:`doc` file as a text, PDF or
HTML document. Reports are organized assemblies of *docs*.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

The *rivt API* is designed to simplify document organization and publishing
by implementing a flexible :term:`rivt markup` language and standard
:ref:`folder structure <top-folders>`. It is designed to combine text, 
tables, diagrams, models and calculations that are typically part of engineering
documents.

**[3]** API 
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivtlib* includes 8 API functions that may be run as a script or interactively
as notebook cells in *VSCode* or other *IDE*.

The four content functions (**R I V T**) output formatted utf-8 text to the
terminal and generate formatted *doc* content. 

    The *Run API* executes shell commands. 
    
    The *Insert API* adds static table, image, equation and text content. 

    The *Value API* evaluates equations and functions. 

    The *Tool API* imports HTML, LaTeX, and Python scripts.

The three processing functions (**D S X**) are related to processing and
output. The *Doc* API specifies settings for publishing formatted :term:`docs`. 
The *Skip* and *Exit* functions are used for interactive editing and debugging.

=============== =============== ===========================================
API Function        Name             Purpose
=============== =============== ===========================================
rv.R(rS)           Run               Run shell commands
rv.I(rS)           Insert            Insert static resources 
rv.V(rS)           Value             Calculate values
rv.T(rS)           Tool              Import Python and Markup functions
rv.D(rS)           Doc               Publish docs 
rv.S(rS)           Skip              Skip section
rv.X(rS)           Exit              Exit rivt 
=============== =============== ===========================================


Each function takes a single *rivt string* (triple quoted string) argument.


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** rivt string
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
:doc:`here. <rvC07-quick>`  See :doc:`Markup</rvC01-markup>` for further 
details. 


.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-terms.rst
    rvA03-faq.rst
    rvA04-docex.rst


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]**  Report Folders
-------------------------------

.. raw:: html

    <hr>

Reports are organized under a single root report folder with the prefix
*rivt-*. *rivt files* are stored in the root folder and *rivt markup* file paths
are relative to the roo.  Resource files are stored in four primary subfolders:

*public* 
    Includes *rivt files* written by *rivtlib* intended for upload to 
    a public repository.

*publish*
    Includes formatted *docs* and *reports* written by *rivtlib*.

*src*
    Includes author provided content, style and generating files for *docs* 
    and *reports*.

*stored*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden*, and *metadata*.

.. _top-folders:

**Folder Key**

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    Required names or prefixes are shown in brackets [ ]. <br>
    <br>
    Folders (including subfolders) that contain author generated files 
    are marked with a single vertical bar ( | ).<br>  
    <br>
    Folders (including subfolders) that contain rivtlib generated files are 
    marked with double vertical bars ( || ).</p>


**Top Level Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 

        ...

        ├── [public]/                   || public rivt files 
        ├── [publish]/                  || report and doc files
        ├── [src]/                      |  source files 
        ├── [stored]/                   || stored rivt files
        └── README.txt                  || searchable text report 

An example of a complete folder structure is :ref:`here <report-folders>`.


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** Metadata
-------------------

.. raw:: html

    <hr>

*Metadata* is specified before any API functions are called and uses standard
Python dictionaries, lists and strings. It is specified outside the *rivtlib*
API functions and provides author information and global file path handling. 
See :doc:`here <rvC01-markup>` for further details.
    
=================== ==========================================================
    Variable                        Description
=================== ==========================================================
:term:`rv_authD`     specifies author information
:term:`rv_forknD`    specifies author fork information - n is a number
:term:`rv_localB`    true; false [default] - resource files are local
=================== ==========================================================

*rv_authD* specifies the author, version, email, repository and license
information and lists the forks. *rv_forknD* specifies data for the forked
file. The *rv_authD* is always included.

*rv_localB* overrides the default report structure and specifies that all
resource files are read from and written to the *rivt file* folder instead of
*rivt folders*.  It is intended for simple, *single docs*.
