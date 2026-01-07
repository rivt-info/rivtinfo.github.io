**D.1 Docs**
========================

**[1t]** rivt Files
-----------------------------

.. raw:: html

    <hr>

Each :term:`rivt file` outputs a corresponding formatted :term:`doc`. A *rivt
report* is organized using the rivt *doc numbers*. A doc number has the form

.. codeblock:: text

    rvAnn-filename.py

where rv is a required prefix, A is an alphanumeric character and nn are two
digit non-negative integers. If the *rivt file* names are:

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


**[2t]** Docs
-----------------------------

.. raw:: html

    <hr>

Each :term:`rivt file` outputs a corresponding formatted :term:`doc` written to
the *publish* folder unless it is a :term:`stand-alone doc`. 

*Docs* may be text, HTML or PDF. PDF *doc* files are produced by two different
libraries, referred to as *pdf* and *pdftex*. A *pdf* doc is formatted using
the *rst2pdf* library, a subset of the larger *ReportLab* library. It is the
default PDF *doc*. Its advantage is a small library that has been incorporated
into *rivt*.

A *pdftex doc* requires separate installation of the much larger *texlive*
LaTeX library (approx. 3GB). Its advantage is additional control over *doc*
formatting and appearance.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3t]** Single docs
----------------------------------------------------------

.. raw:: html

    <hr>

A document that will not be part of a :ref:`report <report-describe>` may use
the local rivt file folder for reading and writing files, without referencing
the *rivt report folders*. A single *doc* is formatted by setting the
*rv_local* variable in a comment, immediately following the *rivtlib* import
statement. 
  
.. code:: python

    # rv singledocS=True

The text, PDF or HTML *doc* will be written to the local file folder using
simple style settings built into *rivtlib*. *Single docs* require less
setup but also offer less formatting control.

.. toctree::
    :maxdepth: 1
    :hidden:

    rvD02-files.rst
    rvD03-folders.rst
    rvD04-setting.rst
    rvD05-docex.rst
    rvD06-reportex.rst
