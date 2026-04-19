**B.1 Overview**
=================================  

**[1t]** Summary
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source Python project that imports 
the `rivtlib Python package <https://pypi.org/project/rivtlib/>`__
and dependencies (:ref:`Project requirements`).  A :term:`rivt file` publishes a 
formatted :term:`rivt doc` as a text, PDF or HTML file. 
A *rivt file* is a Python file (.py) that imports the
:term:`rivtlib` Python package and includes :term:`rivt markup`. A collection
of *rivt docs* may be assembled into a :term:`rivt report`.

*rivt files* are generally edited and run in an IDE. The lightweight `Pyzo
<https://pyzo.org/>`__ IDE is installed with rivtlib. The `VSCode IDE
<https://code.visualstudio.com/>`__ is a full featured IDE that is part of
the :ref:`rivt framework<framework>` and included with :ref:`rivt-portable`. 

*rivt file* examples are provided `here <https://openmodels.info>`__.
An interface for searching *public rivt files* on *GitHub* is :doc:`here <rvE03-ghsearch>`. 
A *public rivt file* is are the parts of a *rivt file* the author chooses to 
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

.. _Files and folders:

**[3t]** Files/Folders
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
as the *doc* title unless overridden in *rv.D*. Use hyphens rather than spaces
to separate words in a file name. They are replaced with spaces when a *doc*
title is extracted.

The top level folder structure is shown below. A more detailed description of
the folder structure is :ref:`here <report-folders>`.

.. code-block:: bash

    [rivt-]Report-Label/            Report Folder
        ├── conf.py                   configuration file
        ├── rv101-filename1.py        rivt file
        ├── rv102-filename2.py        rivt file
        ├── rv201-filename3.py        rivt file
        ├── rv202-filename4.py        rivt file 
        ...
        ├── .vscode/                  optional VSCode settings   
        ├── _publish/                 published docs and reports
        ├── _rstdocs/                 restructured text files 
        ├── _shared/                  public rivt files
        ├── _stored/                  stored files
        ├── Src/                      author source files        
        └── README.txt                searchable text report 


.. _framework:

**[5t]** Framework
----------------------------------------------------------------------

.. raw:: html

    <hr>

The *rivt framework* includes separate programs that provide additional editing ,
formatting, version control, and diagramming tools.

======================= ==========================================================================
Purpose                  Link
======================= ==========================================================================
Editing                   `VSCode <https://code.visualstudio.com/>`_  
Editing Extensions         :ref:`VSCode settings`
Added Formatting          `LaTeX <https://www.tug.org/texlive/>`_
Version Control           `Git <https://git-scm.com>`_
2D Diagramming            `QCAD <https://qcad.org/en/85-new-community-edition-open-source>`_
3D Diagramming            `FreeCad <https://www.freecad.org/>`_
======================= ==========================================================================

.. toctree::
    :maxdepth: 1
    :hidden:

    rvB02-framework.rst
