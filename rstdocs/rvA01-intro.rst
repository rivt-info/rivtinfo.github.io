**A.1 Introduction**
=================================================================

**[1t]** Summary
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source software project that simplifies sharing and reuse of 
engineering documents. It can reduce repetitive work and improve document 
quality. 

Engineering documents may include text, images, tables, calculations, computer
code and models. Although a number of document programs are available, reuse
and sharing are restricted by the software design, terms of use and
licenses. In general,

- documents may come from many incompatible programs
- frequent software updates are needed to maintain document access
- update costs are high
- newer document formats become inaccessible without upgrades
- software is limited to specific platforms
- document version control is limited
- report generation features are limited
- collaboration features are limited

The table below summarizes and compares limitations between different software
programs.

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


**[2t]** rivt API 
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

The *rivtlib* package implements an API designed to be:

- **lightweight** - *rivt markup syntax* is made up of 3 dozen tags 
    and commands.

- **flexible** - it produces single *docs* or large reports in text, HTML and
    PDF formats from the same rivt file or files.

- **extensible** - it is written in Python with direct access to 
    thousands of Python packages.

The *rivt API* publishes documents using a lightweight 
:term:`rivt markup` language that combines text, tables, diagrams, models 
and calculations with a standard :ref:`folder structure <top-folders>` and 
file naming system that organizes documents into reports.

The API implements seven functions. The name *rivt* is an acronym formed from 
the four functions that generate document content. 

=============== =============== ===========================================
API Function        Name             Purpose
=============== =============== ===========================================
rv.R(rS)           **R** un          Run shell commands
rv.I(rS)           **I** nsert       Insert static resources 
rv.V(rS)           **V** alues       Calculate values
rv.T(rS)           **T** ools        Python and markup scripts
rv.D(rS)           Doc               Publish docs 
rv.S(rS)           Skip              Skip section
rv.X(rS)           Exit              Exit rivt (rivt string not processed)
=============== =============== ===========================================

Each API function takes a single :term:`rivt string` argument (rS) as input and
outputs text or restructuredText that is further processed into a
text, HTML and PDF output file, referred to as :term:`rivt doc`. Indiviudal 
API functions can also be processed interactively as cells in an IDE e.g. 
VSCode or Spyder.

The four functions that generate *doc* content are:

    The *Run API* which executes shell commands. 
    
    The *Insert API* which adds static table, image, equation and text content. 

    The *Value API* which evaluates equations and functions. 

    The *Tool API* which runs reStructuredText,HTML, LaTeX and Python scripts.

The remaining three functions are for processing and debugging:

    The *Doc API* specifies *doc* type and style and generates the *doc* file. 
    
    The *Skip API* can be used for interactive debugging and comments.

    The *Exit API* can be used for interactive debugging.

Most of a docs's content is written using the Insert and Value API's.


**[3t]** rivt String
------------------------------------------------------------------------ 

.. raw:: html

    <hr>

An API function starts in the first column and takes a triple quoted
:term:`rivt string` (rS) argument. The first line of a *rivt string* is a
header, followed by content text indented 4 spaces for improved readability 
and section folding. 

The :term:`header` specifies the section title and other
processing parameters. The :term:`content text`` may include 
:term:`rivt markup` and other arbitrary text. For further details 
see :doc:`here <rvC01-markup>`.

.. code-block:: python

    rv._("""Section Label | parameters

         Content text indented four spaces
        
        ...
        
        """)



**[4t]** rivt File
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A :term:`rivt file` is a Python plain text file (.py) that includes *rivt
markup* and imports the :term:`rivtlib` API into the *rv* :term:`namespace`:

.. code-block:: python

    import rivtlib.rvapi as rv


Each *rivt file* outputs a formatted rivt :term:`doc` file as an text, PDF or
HTML document. Reports are organized collections of *docs*.



.. _folderstruc:

**[5t]**  Report Folder Structure
-----------------------------------

.. raw:: html

    <hr>

Reports are organized under a single root report folder with the prefix
*rivt-*. *rivt files* are contained in the root folder and *rivt markup* 
file paths used in *commands* are relative to the root. 

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


**Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 

        ...

        ├── [public]/                   || public rivt files 
        ├── [publish]/                  || doc and report files
        ├── [src]/                      |  source files 
        ├── [stored]/                   || stored files from rivt
        └── README.txt                  || searchable text report 


Resource files are stored in four primary subfolders:

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
   *hidden*, and *metadata*. They may be appended to a report.

The complete folder structure is shown :ref:`here <report-folders>`.

**[6t]** *Single docs*
------------------------

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

**[7t]** Metadata
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

