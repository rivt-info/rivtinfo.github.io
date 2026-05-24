**B.1 Overview**
=================================  

**[1]** Summary
--------------------------------------------------------------------- 

 

*rivt* is an open source Python project that imports 
the `rivtlib Python package <https://pypi.org/project/rivtlib/>`__
and dependencies (see :ref:`Project requirements`).  A :term:`rivt file` 
publishes a formatted :term:`rivt doc` as a text, PDF or HTML file. 
A *rivt file* is a Python file (.py) that imports the
:term:`rivtlib` Python package and includes :term:`rivt markup`. A collection
of *rivt docs* may be assembled into a :term:`rivt report`.

*rivt files* are generally edited and run in an IDE. The lightweight 
`Pyzo <https://pyzo.org/>`__ IDE is installed with rivtlib. The 
`VSCode IDE <https://code.visualstudio.com/>`__ is a full featured IDE that 
is part of the :ref:`rivt framework` and included 
with :ref:`rivt-portable`. 

*rivt file* examples are provided `here <https://openmodels.info>`__.
An interface for searching *public rivt files* on *GitHub* is :doc:`here <rvE04-ghsearch>`. 
A *public rivt file* is are the parts of a *rivt file* the author chooses to 
share under an `Open Source license <https://opensource.org/licenses>`__. 
*rivt* itself is distributed under the 
`MIT open source license <https://opensource.org/license/mit>`__. (see :ref:`Licenses`). 

.. _rivt docs:

**[2]** Docs
-------------------------------------------------------------------------------


.. image:: _static/img/process2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: rivt flow chart 

.. rst-class:: center

    **rivt Doc Processing**

Each :term:`rivt file` outputs a corresponding :term:`doc` in the 
format specified in *rv.D()* API. A rivt file number has the form:

.. code-block:: text

    rvAnn-filename.py

where rv is a required prefix, A is an alphanumeric character and nn are two
digit non-negative integers. The prefix is used to organize reports
into divisions and subdivisions.

Corresponding rivt docs are output as:

.. code-block:: text

    rvAnn-filename.txt
    rvAnn-filename.pdf
    rvAnn-filename.html

A *rivt report* is organized using the *rivt file numbers*. If the rivt file
names are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

the corresponding *doc numbers* in the would be: 

- A.1 (division A, subdivision 1)
- 1.5 (division 1, subdivision 5)
- 2.12 (division 2, subdivision 12)

*Docs* are sorted alpha-numerically into divisions and subdivisions. A *doc
number* corresponds to a report subdivision. Note that leading zeroes are
dropped in the formatted output.

--------------------------------

.. _rivt API:

**[3]** API
------------------------------------------------------------------------------- 


The *rivt API* includes half a dozen :ref:`API functions <API functions>`, 
:ref:`markup` and :ref:`files <Files-folders>`.  The API is designed 
to be:

- lightweight
    :term:`rivt markup` wraps :term:`reStructuredText` and uses fewer than
    three dozen tags and commands. *rivt* tags format lines or blocks of text 
    and commands read and write files.

- extensible 
    *rivtlib* is written in Python with direct access to the very large 
    library of Python packages and functions. Python scripts and external 
    programs can be integrated into a *rivt doc*.

- versatile 
    A *rivt file* produces a text, HTML or PDF *doc*. Multiple *docs* can be 
    organized into reports. *rivt* can be run within a variety of IDEs.

================= =============== ================================================
API Function         Name             Purpose
================= =============== ================================================
**rv.R** (rS)         Run          Run scripts and markup
**rv.I** (rS)         Insert       Insert static sources 
**rv.V** (rS)         Values       Calculate values
**rv.T** (rS)         Tools        Execute shell scripts and external programs
**rv.D** (rS)         Doc          Publish docs 
**rv.S,X** (rS)       Skip         Skip section or exit (comments and debugging)
================= =============== ================================================

An API function starts in the first column and takes a triple quoted
:term:`rivt string` (rS) containting :term:`rivt markup` as the argument. The
first line of a *rivt string* is a :term:`header substring`, followed by a
:term:`content substring` indented 4 spaces for improved readability and
section folding.

The *header substring* specifies the section title and other
processing parameters. The content substring includes 
:term:`rivt markup` and other arbitrary text. For further details 
see :doc:`here <rvD01-markup>`.

.. code-block:: python

    rv._("""Section Label | parameters

         Content text that is 
         indented four spaces.
        
        ...
        
        """)

--------------------------------

.. _Files-folders:

**[4]** Files / Folders
------------------------------------------------------------------------------- 


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
as the *doc* title unless overridden in *rv.D*. Use hyphens rather than spaces
to separate words in a file name. They are replaced with spaces when a *doc*
title is extracted.

The top level folder structure is shown below. A more detailed description of
the folder structure is :ref:`here <report-folders>`.

.. code-block:: bash

      rivt-Report-Label/           Report Folder                
        ├── .vscode/                  optional VSCode settings 
        ├── rivt-public_/             rivt-generated public files
            ├── src/                     source files
            ├── README.txt                public report   
            ├── rv-101-filename1.py       public rivt file
            ├── rv-102-filename2.py       public rivt file       
            ├── rv-201-filename3.py       public rivt file          
            ├── rv-202-filename4.py       public rivt file
            ...
        └── rivt-report/               rivt files and docs               
            ├── _published/               published docs and reports
            ├── _rstdocs/                 restructured text files               
            ├── _stored/                  stored files
            ├── src/                      source files
            ├── rivt-report.py            report generating script
            ├── rv101-filename1.py        rivt file
            ├── rv102-filename2.py        rivt file       
            ├── rv201-filename3.py        rivt file          
            ├── rv202-filename4.py        rivt file
            ...    

--------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    rvB02-framework.rst
