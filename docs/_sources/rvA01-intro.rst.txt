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
available, reuse and sharing is generally not possible because of limitations 
in software terms of use and distribution:

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


Table 1 - **Software Comparison**

============ ========= ======== ======== ========= ========= ============= 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_  CP [5]_   Collab [6]_  
============ ========= ======== ======== ========= ========= ============= 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS    limited  limited     no      no          yes      limited  
Jupyter        no       no         no      yes         yes      yes  
**rivt**      **yes**  **yes**   **yes**  **yes**   **yes**    **yes**
============ ========= ======== ======== ========= ========= ============= 


.. rst-class:: left

    .. [1] Report generation
    .. [2] Native version control
    .. [3] Plain text, readable input files
    .. [4] Forward and backward compatibility
    .. [5] Cross-platform
    .. [6] Collaboration support


.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[2]** rivt File
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A :term:`rivt file` is a Python plain text file (.py) that imports the 
:term:`rivtlib` library and includes *rivt markup*:

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

*rivtlib* includes 7 API functions that may be run as a script or interactively
as notebook cells in *VSCode* or other *IDE*.

Four content functions (**R I V T**) output formatted utf-8 text to the
terminal and write formatted *docs*. 

    The *Run API* executes shell commands. 
    
    The *Insert API* adds static table, image, equation and text content. 

    The *Value API* evaluates equations and functions. 

    The *Tool API* imports HTML, LaTeX, and Python scripts.

Three processing functions (**D S X**) specify the publication format. The
*doc* API specifies the publication type of the :term:`doc` as text, HTML or
PDF. The *Skip* and *Exit* APIs are used in interactive editing and debugging.

=============== =============== ===========================================
API Function        Name             Purpose
=============== =============== ===========================================
rv.R(rS)           Run               Run shell commands
rv.I(rS)           Insert            Insert static resources 
rv.V(rS)           Values            Calculate values
rv.T(rS)           Tools             Python and markup scripts
rv.D(rS)           Doc               Publish docs 
rv.S(rS)           Skip              Skip section
rv.X(rS)           Exit              Exit rivt without processing section
=============== =============== ===========================================

Each API function takes a single *rivt string* (triple quoted string) argument.


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** rivt String
------------------------------------------------------------------------ 

.. raw:: html

    <hr>

An API function starts in the first column and takes a triple quoted
:term:`rivt string` (rS) argument. The first line of the string is a header
that specifies section labeling and processing. The :term:`header` is followed 
by section text indented four spaces for legibility and section folding.

.. code-block:: python

    rv._("""Header

        section text
        ...
        
        """)

Section text is plain text that includes :term:`rivt markup` and
:term:`reStructuredText`. *rivt markup* includes :term:`line tags`, 
:term:`block tags` and :term:`commands` summarized :doc:`here. <rvC07-quick>` 
See :doc:`Markup</rvC01-markup>` for further details.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]**  Report Folders
-------------------------------

.. raw:: html

    <hr>

Reports are organized under a single root report folder with the prefix
*rivt-*. *rivt files* are stored in the root folder and *rivt markup* file paths
are relative to the root.  Resource files are stored in four primary subfolders:

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
    Folders and subfolders that contain author generated files 
    are marked with a single vertical bar ( | ).<br>  
    <br>
    Folders and subfolders that contain *rivtlib* generated files are 
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

**[5]** Single *docs*
---------------------

.. raw:: html

    <hr>

The *rv_localB* variable overrides the default report structure and specifies
that resource files and *docs* are read from and written to the *rivt file*
folder. It is intended for simple, standalone *docs* with limited, built-in
formatting options.

The variable is specified immediately after the import statement as a comment:

.. code:: python

    import rivtlib.rvapi as rv

    # rv_localB = True


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[6]** Metadata
-------------------

.. raw:: html

    <hr>

*rivt* file metadata can be specified in the *Tools API* as a Python dictionary. 
*rv_authD* is a dictionary that specifies the author, version, email, repository
and license information and forks. The data is written to the API log file.

.. code:: python

    _[[PYTHON]] Author data
    rv_authD = {
    "authors": ["rholland"],
    "version": "0.7.1",
    "email": "rod.h.holland@gmail.com",
    "repo": "https://github.com/rivt-info/rivt-simple-single-doc",
    "license": "https://opensource.org/license/mit/",
    "fork1": ["author", "version", "email", "repo"],
    "fork2": [],
    }
    _[[END]]


.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-terms.rst
    rvA03-faq.rst
    rvA04-docex.rst

