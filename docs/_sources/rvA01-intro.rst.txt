**A.1 Introduction**
=================================================================

**[1t]** Motivations
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source software project that simplifies sharing and reuse of
engineering documents. Engineering documents are more complex than typical word
and image documents. They need to combine text, images, tables, calculations,
models and computer code in an organized report. As open source, *rivt* is
designed to reduce repetitive work and improve document quality through sharing
and reuse.

Although a number of engineering document programs are available, sharing is
restricted by software design and terms of use in the following way:

- documents written with incompatible programs
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

**Software Comparison**

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


**[2t]** Overview
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A document (:term:`rivt doc`) is published from a :term:`rivt file` 
written in :term:`rivt markup` and processed by the :term:`rivtlib` Python
package. A collection of *rivt docs* may be collated as a :term:`rivt report`.

As an open source project *rivt files* may be collaberatively shared and *rivt*
may be integrated with other programs. *rivt* is distributed under the 
`MIT open source license. <https://opensource.org/license/mit>`_ 
The parts of a *rivt file* that are shared in *public rivt files* under an 
`Open Source license <https://opensource.org/licenses>`_ are selected 
by the author when the *doc* is published. The *MIT license* is the default.

.. rst-class:: center

**rivt Doc Processing**

.. image:: _static/img/rivtflow2.png
    :scale: 70%
    :alt: rivt flow chart 
    :align: center

.. raw:: html

    <br>

The *rivt API* includes  :ref:`API functions`, :ref:`Markup` and
:ref:`Files and folders`. The API is designed to be:

- lightweight
    :term:`rivt markup` is made up of about 3 dozen tags 
    and commands, and wraps :term:`reStructuredText`.

- flexible 
    A *rivt file* produces a *doc* that can be formatted as 
    text, HTML and PDF.that can be part of a large report 

- extensible 
    *rivtlib* is written in Python with direct access to thousands of 
    Python packages.


.. _API functions:

**[3t]** API functions
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

The name *rivt* is an acronym formed from four content generating
functions. 

=============== =============== ===========================================
API Functions        Name             Purpose
=============== =============== ===========================================
rv.R(rS)           **R** un          Run shell commands
rv.I(rS)           **I** nsert       Insert static resources 
rv.V(rS)           **V** alues       Calculate values
rv.T(rS)           **T** ools        Python and markup scripts
rv.S(rS)           Skip              Skip section (comments and debugging)
rv.D(rS)           Doc               Publish docs 
rv.X(rS)           Exit              Exit rivt (debugging)
=============== =============== ===========================================

Most of a docs' content is written using the *Insert* (rv.I) and *Value* (rv.v)
API's.

.. raw:: html

    <p style="border-width:1px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Content Functions</b> <br>
    The <i>Run API</i> executes shell commands.<br> 
    The <i>Insert API</i> adds static table, image, equation and text content.<br> 
    The <i>Value API</i> evaluates equations and functions.<br> 
    The <i>Tool API</i> runs reStructuredText, HTML, LaTeX and Python scripts.<br>
    <br>
    <b>Processing and interactive Functions</b> <br>
    The <i>Doc API</i> specifies <i>doc</i> type and style and generates the file.<br>  
    The <i>Skip API</i> can be used for interactive debugging and comments.<br> 
    The <i>Exit API</i> can be used for interactive debugging.<br> 
    </p>

Within an interactive IDE like *VSCode* and *Spyder*, indiviudal functions
can be processed interactively as cells using the standard prefix notation:

.. code-block:: python

    # %% optional label

Refer to :doc:`rvB03-vscode` for further details.

Each API function takes a single :term:`rivt string` argument as input (rS),
and outputs formatted text or restructuredText that is further processed 
into a text, HTML and PDF :term:`doc`. The *rivt string* is written 
in *rivt markup*.

.. _Markup:

**[4t]** Markup Overview
------------------------------------------------------------------------ 

.. raw:: html

    <hr>

An API function starts in the first column and takes a triple quoted
:term:`rivt string` (rS) argument. The first line of a *rivt string* is a
:term:`header`, followed by :term:`content` indented 4 spaces for 
improved readability and section folding. 

The *header* specifies the section title and other
processing parameters. The content text may include 
:term:`rivt markup` and other arbitrary text. For further details 
see :doc:`here <rvC01-markup>`.

.. code-block:: python

    rv._("""Section Label | parameters

         Content text indented four spaces
        
        ...
        
        """)

.. _Files and folders:

**[4t]** Folder/Files overiew
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

A :term:`rivt file` is a Python plain text file ( *.py* ) that includes *rivt
markup* and imports the :term:`rivtlib` API into the *rv* :term:`namespace`:

.. code-block:: python

    import rivtlib.rvapi as rv

*rivt files* are stored in the root folder designated with the prefix *rivt-*.
Each *rivt file* and corresponding *rivt doc* has a prefix that is used to
organize the report. The file names have the form

.. code-block::

    rvANN-filename.py

where A is an alpha-numeric character used for organizing report divisions, and
NN is a two digit number used to organize sub-divisions. The file name is used
as the *doc* title unless overridden. Use underscores or hyphens rather than
spaces to seprate words in the name.

.. _top-folders:

.. raw:: html

    <p style="border-width:1px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Key</b> <br>
    Required names or prefixes are shown in brackets [ ].
    Required folders start with a capital letter. <br>
    Folders that contain author provided files are marked with a 
    single vertical bar ( | ).<br>  
    Folders that contain <i>rivtlib</i> generated files are 
    marked with double vertical bars ( || ).</p>


**Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 

        ...

        ├── [Public]/                   || public rivt files 
        ├── [Publish]/                  || doc and report files
        ├── [Src]/                      |  source files from author
        ├── [Stored]/                   || stored files from rivtlib
        └── README.txt                  || searchable text report 


The four rivt subfolders are:

*Public*
    Stores public *rivt files* generated by *rvitlib*. File content intended for 
    sharing is defined by *section headers*. Public *rivt files* 
    are identified by a hyphen after  the *rv* prefix e.g. *rv-101-filename1*. 
    
*Publish*
    Stores *docs* and *reports* generated by *rvitlib*
    
*Src*
    Stores images, data, code and text provided by the author.

*Stored*
    Stores files generated by *rvitlib*. Files include stored
    sections identified in headers, api log files and processing log files. Files
    may be attached to a report.

The complete folder structure is shown :ref:`here <report folders>`.

.. _Reports and single docs:

**[5t]** Doc/report overview
-----------------------------------------------------------------------

.. raw:: html

    <hr>

.. raw:: html

    <hr>

Each :term:`rivt file` outputs a corresponding :term:`doc` in the specified
format. A doc number
has the form:

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

Note that leading zeroes are dropped.  *Docs* are sorted alpha-numerically into
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

:doc:`here <rvD01-documents>`.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-terms.rst
    rvA03-faq.rst

