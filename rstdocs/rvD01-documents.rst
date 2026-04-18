**D.1 Docs**
========================

**[1t]** rivt Files
-----------------------------

.. raw:: html

    <hr>

Each :term:`rivt file` outputs a corresponding formatted :term:`doc`. A doc
number has the form

.. code-block:: text

    rvAnn-filename.py

where rv is a required prefix, A is an alphanumeric character and nn are
non-negative integers.

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


**[2t]** Docs and Reports
-----------------------------

.. raw:: html

    <hr>

Each :term:`rivt file` outputs a corresponding formatted :term:`doc` written to
the *publish* folder unless it is a :term:`single doc`. 

*Docs* may be text, HTML or PDF. PDF and HTML *doc* files are produced using
using the *rst2pdf* and *Sphinx* Python libraries. The *report folder*
structure for *docs* is described in :ref:`report-folders`. Reports are
assembled from by the *rivt-report.py* script in the *Rst_Docs* folder.


**[3t]** Single docs
----------------------------------------------------------

.. raw:: html

    <hr>

A single doc that will not be part of a report may use a simplified folder
structure. A single *doc* is formatted by setting the comment variable,
immediately following the *rivtlib* import statement.
  
.. code:: python

    from rivtlib import rivtlib.rvapi as rv

    # rv singledoc=True

The folder structure for *single docs* is simmilar to the structure for
*report* folders described in :ref:`report-folders` but without the *Src* and
*_stored* folders. Files in those folders are stored or written in the root
folder.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvD02-files.rst
    rvD03-folders.rst
    rvD04-setting.rst
    rvD05-docex.rst
    rvD06-reportex.rst
