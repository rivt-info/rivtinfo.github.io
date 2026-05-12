**C.1 Docs**
========================

**[1]** Doc Files
-----------------------------

.. raw:: html

    <hr>

A *rivt doc* is the output of a *rivt file* processed by *rivtlib*. Each 
*rivt file* outputs a corresponding formatted :term:`doc` with a *doc number* derived
from the rivt file name. A *rivt report* is organized using the rivt *doc
numbers*. The rivt file name has the form:

.. code-block:: text

    rvAnn-filename.py

where *rv* is a required prefix, *A* is an alphanumeric character and *nn* are
non-negative integers. 

.. code:: python

    import rivtlib.rvapi as rv

    # rv public=True

If the *rivt file* names are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

the corresponding *doc* references would be: 

.. code-block:: bash

    doc file names
    rvA01-filename.type
    rv105-filename.type
    rv212-filename.type  
    
    doc references
    A.1 (division A, subdivision 1)
    1.5 (division 1, subdivision 5)
    2.12 (division 2, subdivision 12)

Note that leading zeroes are dropped.  *Docs* are sorted alpha-numerically into
divisions and subdivisions in the *report*.


**[2]** Reports
-----------------------------

.. raw:: html

    <hr>

Each :term:`rivt file` outputs a corresponding :term:`doc` written to the
*publish* folder in the specified format. A *rivt report* is assembled from a
set of *docs* using the *rivt-report.py* script. The *report folder structure*
is described in :ref:`rivt-folders`.

*Docs* may be output as text, HTML or PDF. PDF and HTML *docs* are produced
using the *rst2pdf* and *Sphinx* Python libraries. 

*Reports* are assembled from docs using the *rivt-report.py* script in the
*Src/Tools* folder. A single doc that is notpart of a report does not
require running the rivt-report.py script. 

.. toctree::
    :maxdepth: 1
    :hidden:

    rvC03-files.rst
    rvC02-folders.rst
    rvC04-report.rst
    rvC05-docex.rst
