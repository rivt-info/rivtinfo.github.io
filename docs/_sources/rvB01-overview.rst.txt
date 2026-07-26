**B.1 |** Overview
=================================  

.. _rivt-overview:

**[1]** Summary
--------------------------------------------------------------------- 

*rivt* is designed to assemble calculation documents from a wide variety of
sources including engineering programs, data files, Python scripts,
image files and single purpose programs like Excel, Mermaid, Graphviz, and
LaTeX. It accomplishes this using four API functions:

.. raw:: html

    <p style="border-width:2px; border-style:solid; border-color:#49b2c3;padding: 1em;">

    <b>R():</b> Runs external binary programs <br>

    <b>I():</b> Inserts static sources e.g. images, text, and PDF files <br>

    <b>V():</b> Imports data and calculates values from equations and functions <br>

    <b>T():</b> Processes scripts and block text, e.g. Python, LaTeX, rst <br> 

`rivtlib <https://pypi.org/project/rivtlib/>`__ is the Python library that 
compiles a *rivt file* to a text, PDF or HTML doc. A *rivt file* is a 
Python file (.py) that imports the *rivtlib* Python package and includes 
*rivt markup*. *rivt* dependencies are listed `:ref:here <vscode-settings>`. 

A *public rivt file* is a subset of a *rivt file*, made up of sections the
author chooses to share under an `Open Source license
<https://opensource.org/licenses>`__. *rivt* is designed to seamlessly extract
public files, allowing the author discretion in choosing which file 
sections to make public.

Groups of *rivt files* may be compiled and linked into a single 
:ref:`rivt report <rivt-report>`. Collections of *rivt files* with related 
subject matter may be grouped together as a :ref:`rivtbook <rivt-books>`.

*rivt files* are generally edited and run in an IDE. The lightweight 
`Pyzo <https://pyzo.org/>`__ IDE is installed by rivtlib. The 
`VSCode IDE <https://code.visualstudio.com/>`__ is a full featured IDE 
with rivt profiles and extensions documented :ref:`here <vscode-settings>`. 
*VSCode* is installed with the portable :ref:`rivt-code <rivt-code>` installation.

*rivt file* examples are illustrated :ref:`here <rivt-tutor>`. Additional  
*rivt files* may be downloaded from *Google Drive* at 
`OpenModels.info <https://www.openmodels.info/>`__.  An interface for searching 
*public rivt files* on *GitHub* is :doc:`here <rvE02-github>`. 

*rivt* is distributed under the
`MIT open source license <https://opensource.org/license/mit>`__. 
(see:ref:`Licenses`).

.. _rivt-api:

**[3]** API
------------------------------------------------------------------------------- 

The *rivt API* includes :ref:`API methods <API methods>`, 
:ref:`markup <Line Tags>` and structured 
:ref:`folders and files <file-folder>`.

The API is designed to be:

- lightweight
    :term:`rivt markup` wraps :term:`reStructuredText` and uses fewer than
    three dozen tags and commands. *rivt tags* format lines and blocks of text 
    and *commands* read and write files.

- extensible 
    *rivtlib* is written in Python with direct access to the large 
    library of Python packages and functions. Python scripts and external 
    programs can be integrated into a *rivt doc*.

- versatile 
    A *rivt file* produces a text, HTML or PDF *doc* from the same file. 
    Multiple *docs* can be organized into reports. *rivtbooks* provide a 
    convenient way to organize files around a subject matter for insertion into
    reports. *rivt* can be run within a variety of IDEs.

- efficient
    The file and folder settings produce clear, organized documents with 
    default settings. Settings may be customized via *conf.py* and *yaml* files.

The API methods are listed in the table below, where (rS) is a triple quoted 
:term:`rivt string` argument.

================= =============== ==============================================
API Function         Name             Purpose
================= =============== ==============================================
**rv.R** (rS)         Run          Run external programs
**rv.I** (rS)         Insert       Insert static sources 
**rv.V** (rS)         Values       Calculate values
**rv.T** (rS)         Text         Process scripts and text blocks
**rv.D** (rS)         Doc          Publish docs 
**rv.S** (rS)         Skip         Skip section 
**rv.X** ()           Exit         Exit rivt file
================= =============== ==============================================

An API function starts in the first column and takes a triple quoted
:term:`rivt string` argument containing a *header and content substring*.
The first line of the *rivt string* is the header substring, 
followed by a :term:`content substring` indented 4 spaces 
for readability and section folding. See :ref:`here <rivt-header>` for 
*rivt string* details.


.. _rivt-docs:

**[2]** Docs
-------------------------------------------------------------------------------


.. image:: _static/img/process2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: rivt flow chart 

.. rst-class:: center

    **rivt Doc Processing**

Each :term:`rivt file` outputs a corresponding :term:`doc` with the format
specified in | PUBLISH | command of the *rv.D()* API. A rivt file number has the
form:

.. code-block:: text

    rvAnn-filename.py

where rvAnn is a required file number prefix with A an alphanumeric character and nn a two
digit non-negative integer. Corresponding rivt docs are output as:

.. code-block:: text

    rvAnn-filename.txt, pdf or html

A *rivt report* is organized using the *file numbers*. The file numbers are
used to organize reports into divisions and subdivisions. Each *rivt file* or
*doc* is a report subdivision. If the *rivt filenames* are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

the corresponding *doc numbers* in a report would be: 

- A.1 (division A, subdivision 1)
- 1.5 (division 1, subdivision 5)
- 2.12 (division 2, subdivision 12)

--------------------------------


.. _file-folder:

**[4]** Files / Folders
------------------------------------------------------------------------------- 


A :term:`rivt file` is a Python plain text file ( *.py* ) that includes API
functions and imports the :term:`rivtlib` package into the *rv*
:term:`namespace`:

.. code-block:: python

    import rivtlib.rvapi as rv

*rivt files* are stored in either a *rivt* or *rivtbk* folder. Each *rivt file*
and corresponding *rivt doc* has a prefix used for document organization. The
top level folder structures are shown below. The difference in folder structure
facilitates copying docs from rivtbooks into report. A more detailed
description of the folder structure is :ref:`here <report-folders>`.
    
A report folder can contain any set of files and folders but the following
structure is required for <i>doc</i> processing. Files and folders are
organized under a root folder with the prefix rivt- e.g. rivt-Report-Label. 

report folders (root folders) include at least the rivt files
and the five required subfolders. Required folders and prefixes are 
shown in brackets. Folders preceded by an underscore contain rivt outputs. 
Folders requiring author input are capitalized.

The top level folder structure is shown below. More detailed descriptions of
the folder structures are :ref:`here <rivt-report>`.

.. code-block:: bash
    
    Report Folders
    --------------

    [rivt-]Report-Label/           Report Folder                
        ├── .help/                     help files
        ├── .vscode/                   optional VSCode settings 
        ├── [_rivt-public]/            rivt-generated public files
        └── [README.txt]               text doc or report
            ├── [rvsrc]/                    source files
            ├── [README.txt]                public text report or doc
            ├── [rv-101-]filename1.py       public rivt file
            ├── [rv-102-]filename2.py       public rivt file       
            ├── [rv-201-]filename3.py       public rivt file          
            ...
        └── [rivt-report]/               rivt files and docs               
            ├── [_published]/               published docs and reports
            ├── [_rstdocs]/                 rivt generated rst files               
            ├── [_rvstor]/                  rivt generated stored files
            ├── [_rvsrc]/                   author source files
            ├── [rivt-]report.py            report generating script
            ├── [rv101-]filename1.py        rivt file
            ├── [rv102-]filename2.py        rivt file       
            ├── [rv201-]filename3.py        rivt file          
            ...    

    rivtbook Folders
    ----------------

    [rivtbk-]Book-Label/            rivtbook folder
        ├── .help/                      help files
        ├── .vscode/                    optional VSCode settings   
        ├── [README.txt]                rivt-generated book as text       
        ├── [_rstdocs]/                 restructured text files
        ├── [_pdfdocs]/                 PDF docs and report         
        ├── [rvbk101-]folder name       rivtbook folder
        ├── [rvbk102-]folder name       rivtbook folder        
        ├── [rvbk201-]folder name       rivtbook folder           
             ...            


--------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    rvB02-motivation.rst
    rvB03-framework.rst
