**B.1 Overview**
=================================  

**[1t]** Summary
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source Python project that imports 
the `rivtlib Python package <https://pypi.org/project/rivtlib/>`__
and dependencies (:ref:`Project requirements`). The lightweight 
`Pyzo <https://pyzo.org/>`__  IDE is also installed for editing and 
publishing *rivt file* examples. The `VSCode IDE <https://code.visualstudio.com/>`__ 
is a more full featured IDE that is part of the *rivt framework* and 
installed separately.

A :term:`rivt file` publishes a formatted :term:`rivt doc` as a text, PDF or
HTML file. A *rivt file* is a Python file (.py) that imports the
:term:`rivtlib` Python package and includes :term:`rivt markup`. A collection
of *rivt docs* may be collated as a :term:`rivt report`.

*rivt file* examples are provided 
`here <https://drive.google.com/drive/folders/1jsYQizu7RbTHks1WbtbM_oR8z0IRIzub?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto>`__.
An interface for searching *public rivt files* on *GitHub* is :doc:`here <rvE03-ghsearch>`. 
A *public rivt file* is all or parts of a *rivt file* the author chooses to 
share under an `Open Source license <https://opensource.org/licenses>`__. 
*rivt* itself is distributed under the `MIT open source license <https://opensource.org/license/mit>`__. 
(see :ref:`Licenses`). 

.. _rivt docs:

**[2t]** rivt docs
------------------------------------------------------------------------

.. raw:: html

    <hr>

.. image:: _static/img/process2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: rivt flow chart 

.. rst-class:: center

    **rivt Doc Processing**

Each :term:`rivt file` outputs a corresponding :term:`doc` in the 
format specified in *rv.D*. A doc number has the form:

.. code-block:: text

    rvAnn-filename.py

where rv is a required prefix, A is an alphanumeric character and nn are two
digit non-negative integers.  

A *rivt report* is organized using the rivt *doc numbers*. If the *rivt file*
names are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

the *report numbers* would be: 

- A.1 (division A, subdivision 1)
- 1.5 (division 1, subdivision 5)
- 2.12 (division 2, subdivision 12)

Note that leading zeroes are dropped. *Docs* are sorted alpha-numerically into
divisions and subdivisions in the *report*.

*Docs* are assembled from sources and published using a specified folder
structure. The *singledocB* variable overrides the default report structure and
specifies that resource files and *docs* are read from and written to the *rivt
file* folder. It is intended for simpler, standalone *docs* with more limited
format control. The comment variable is specified immediately after the import
statement:

.. code:: python

    import rivtlib.rvapi as rv

    # rv singledocB = True

The default setting is False.

.. _rivt API:

**[2t]** rivt API
------------------------------------------------------------------------ 

The *rivt API* includes  :ref:`API functions <API functions>`, 
:ref:`markup` and :ref:`files <Files and folders>`.  The API is designed 
to be:

- lightweight
    :term:`rivt markup` is made up of about 3 dozen tags 
    and commands, and wraps :term:`reStructuredText`.

- flexible 
    A *rivt file* produces a text, HTML or PDF *doc*. 
    Multiple *docs* can be organized into a report. 

- extensible 
    *rivtlib* is written in Python with direct access to thousands of 
    Python packages.


.. _Markup:

**[3t]** Markup
------------------------------------------------------------------------ 

.. raw:: html

    <hr>

An API function starts in the first column and takes a triple quoted
:term:`rivt string` (rS) argument. The first line of a *rivt string* is a
:term:`header substring`, followed by a :term:`content substring` 
indented 4 spaces for improved readability and section folding.

The *header substring* specifies the section title and other
processing parameters. The content substring includes 
:term:`rivt markup` and other arbitrary text. For further details 
see :doc:`here <rvC01-markup>`.

.. code-block:: python

    rv._("""Section Label | parameters

         Content text that is 
         indented four spaces.
        
        ...
        
        """)

.. _Files and folders:

**[4t]** Folder/Files
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A :term:`rivt file` is a Python plain text file ( *.py* ) that includes *rivt
markup* and imports the :term:`rivtlib` package and API into the *rv*
:term:`namespace`:

.. code-block:: python

    import rivtlib.rvapi as rv

*rivt files* are stored in a root folder designated with the prefix *rivt-*.
Each *rivt file* and corresponding *rivt doc* has a prefix that is used to
organize the report. The  prefix has the form

.. code-block::

    rvANN-filename.py

where A is an alpha-numeric character used for organizing report divisions, and
NN is a two digit number used to organize sub-divisions. The file name is used
as the *doc* title unless overridden in *rv.D*. Use underscores or hyphens
rather than spaces to seprate words in the file name. They are replaced with
spaces when a *doc* title is extracted.

.. _top-folders:

.. raw:: html
    
    <b>Folder Key</b>
    <ol style="border: 2px; 
            border-color: #49b2c3; 
            border-style: solid; 
            padding: 2em;
            margin: 2em">
        <li> Required names or prefixes are shown in brackets [ ].</li>
        <li> Folders containing input files edited by author start with a capital letter. </li>
               and are marked with a single bar ( | ).</li>
        <li> Folders/files generated by <i>rivtlib</i> start with a lowercase
               letter and are marked with a double bar</li>
    </ol>


**Top-Level Single Doc Folders** (see :ref:`single-doc`)

.. code-block:: bash

    [rivt-]single-doc-label/                 Single doc Folder            
        ├── [rv101-]filename.py              |  rivt file
        ├── multiple source files            |  data, image and function files
        ├── addunits.py                      |  define new units
        ├── rv-101-log.txt                   || log file                          
        ├── rv-101-docname.py                || public rivt file
        ├── README.txt                       || searchable text doc 
        ├── [.vscode]/                       |  optional VSCode settings            
        ├── [rstdocs]/                       |  rst style input  
        ├── [pdfdocs]/                       |  pdf output
        ├── [htmldocs]/                      || html output 
        ├── [latexdocs]/                     || latex output
        └── [textdocs]/                      || text output 

**Top-Level Report Folders** (see :ref:`report-describe`)

.. code-block:: bash

    [rivt-]Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt files
        ├── [rv102-]filename2.py        
        ├── [rv201-]filename3.py        
        ├── [rv202-]filename4.py        
        ...
        ├── [.vscode]/                  |  optional VSCode settings   
        ├── [Files]/                    |  files provided by authors
        ├── [publish]/                  || doc and report files
        ├── [stored]/                   || files written by rivtlib
        └── README.txt                  || searchable text report 


The three primary rivt folders are:

*Files*
    Images, data, code and text provided by the author.
    
*publish*
    Final *docs*, *reports* and *public rivt files* generated by *rvitlib*

*stored* 
    Intermediate files generated by *rivtlib*. Files include excluded sections,
    logs, value files and results from scripts. Stored files may be 
    referenced in multiple docs.

The complete folder structure is shown :ref:`here <report-folders>`.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvB02-framework.rst

