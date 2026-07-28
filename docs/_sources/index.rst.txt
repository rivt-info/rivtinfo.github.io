
.. raw:: html

   <div style="height: 0; visibility: hidden;">

   Home
   ========

   </div>

.. figure::  _static/img/rivt-finalb.png
    :class: dark-light
    :scale: 20%
    :align: center
    :alt: rivt logo
    
.. raw:: html

   <hr>

*rivt* is an open-source program for writing and assembling calculation
documents with a focus on reuse [#]_. The large ecosystem of engineering calculation
tools often requires organizing their output into a single project document.
*rivt* is designed to write, assemble and link calculation documents and code 
into a live, editable and organized format prior to publishing to a text, PDF or HTML
static format. 

The *rivt markup* language also facilitates conversion of any PDF or text
document into a live calculation document that can then be modified or extended.
Python knowledge is not required to use *rivt* but its capabilities are
increased when Python scientific and engineering libraries and scripts are used.
For further details refer to the `rivt user manual <https://rivt.info>`__.

The primary use case for *rivt* is producing organized, live calculation
documents that can be easily shared, reused and maintained. There are four 
types of rivt files:

.. code-block:: text

                    | A rivt file is the basic input file that
      rivt file     | compiles to a text, PDF or HTML document. 
                    | It is a Python file (.py) that imports the 
                    | rivtlib Python package.

                    | A rivt doc is the published output of a rivt
      rivt doc      | file. A doc may be formatted as text, PDF
                    | or HTML from the same rivt file.

                    | A rivtbook is a collection of rivt files with
      rivtbook      | common subject matter and a folder structure
                    | that makes it easy to select files and resources
                    | for inclusion in documents and reports.

                    | A rivt report is the collated output of multiple
                    | docs into a single text or PDF file or HTML
      rivt report   | site. Docs are linked and grouped into divisions
                    | using doc file name conventions.

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started with
running examples see :ref:`install <rivt-start>`. For *rivt* and *AI* see
:ref:`here <rivt-context>`. Examples of a :ref:`rivt file <example-file>` with
:ref:`text <text-doc>`, :ref:`PDF <pdf-doc>`, and :ref:`HTML <html-doc>`
output docs are provided in this :ref:`tutorial <rivt-tutor>`. Other documents 
and examples may be downloaded from `Google Drive. <https://www.openmodels.info>`__ 

The *rivtlib* `Python package <https://pypi.org/project/rivtlib/>`__ formats
and compiles a *rivt file* to a text, PDF or HTML document (*doc*) in a
few seconds. *rivt file* sections may be interactively executed in an IDE. Multiple
*rivt files* may be compiled into a collated *rivt report*.  *rivt files* may 
be organized into  *rivtbooks*. These are rivt file collections around a 
common subject matter and organized for efficient selection and inclusion in 
reports.  This website is an example of an HTML *rivt report*. A convenient 
interface for searching and downloading public *rivt files* on *GitHub* is 
:doc:`here. <rvE02-github>` 

*rivt* produces organized, formatted engineering documents from active
calculation files using reasonable defaults. Use cases are listed :ref:`here
<use-case>`. For static documents with rigid format requirements, including
journal articles and books that do not need recalculation, tools like `Quarto
<https://quarto.org/>`__ are likely a better fit. A brief discussion of current
engineering document tools and their strengths relative to the objectives of
*rivt* is :ref:`here <motivation>`.

.. [#] rivt includes switches that selectively export sections
    of a *rivt file* to a *public rivt report* for open-source reuse.

.. raw:: html

   <hr>

   <p style="color:rgb(63,177,197);">ver: 1.0.0a12 
   (Note: rivt is currently <i>alpha sofware</i>. Some features are 
   incomplete and markup tags, commands and assignments may change.)</p>

.. toctree::
    :maxdepth: 1
    :hidden:

    rvA01-start.rst
    rvB01-overview.rst
    rvC01-documents.rst
    rvD01-markup.rst
    rvE01-collab.rst
    rvF01-aiintro.rst
    rvG01-quickref.rst