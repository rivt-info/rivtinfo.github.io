
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

*rivt* is an extensible, open-source program for writing and assembling 
calculation documents with a focus on reuse [1]_. Python knowledge is not
required but *rivt* capabilities can be extended with Python scripts that
access scientific and engineering libraries.

There are four types of rivt document files:

.. code-block:: text

                    | A rivt file is the basic input file that
      rivt file     | compiles to a text, PDF or HTML document. 
                    | It is a Python file (.py) that imports the 
                    | rivtlib Python package.

                    | A rivtbook is a collection of rivt files with
      rivtbook      | common subject matter and a folder structure
                    | that makes it easy to select files with related
                    | resources for inclusion in documents and reports.

                    | A rivt doc is the published output of a rivt
      rivt doc or   | file. A doc (or chapter in the context of a  
      chapter       | rivt report) is the output of a rivt file
                    | formatted as text, PDF or HTML.  

                    | A rivt report is the collated output of multiple
                    | docs into a single text file, PDF file or HTML site.
      rivt report   | Each doc is a chapter in a report. Chapters are
                    | grouped into divisions using file doc numbers. 


Examples of a :ref:`rivt file <example-file>` with its :ref:`text <text-doc>`,
:ref:`PDF <pdf-doc>`, and :ref:`HTML <html-doc>` docs are provided in a
:ref:`tutorial <rivt-tutor>`

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started with 
running examples see :ref:`install <rivt-start>`.  For *rivt* and *AI* see 
:ref:`here <rivt-context>`.

The *rivtlib* `Python package <https://pypi.org/project/rivtlib/>`__ formats
and compiles a *rivt file* to a text, PDF or HTML document (*doc*) in about a
second. *rivt file* sections may be interactively executed in an IDE. Multiple
*rivt files* may be compiled into a collated *rivt report*.  *rivt files* may 
be organized into  *rivtbooks*, collections around a common subject matter 
and organized for efficient selection and inclusion in reports.  This website is 
an example of an HTML *rivt report*.

A convenient interface for searching and downloading public *rivt files* on
*GitHub* is :doc:`here. <rvE02-github>` Open source engineering models,
documents and examples, including *rivt*, may be downloaded from 
`Google Drive. <https://www.openmodels.info>`__

*rivt* produces clear, organized engineering documents from active calculations
using reasonable defaults. Use cases are listed :ref:`here <use-case>`.
Document tools like `Quarto <https://quarto.org/>`__ are likely better tools
for static documents including journal articles and books that do
not need recalculation. A brief discussion of current engineering document
tools and their strengths relative to the objectives of *rivt* is :ref:`here
<motivation>`.

.. [1] rivt includes the built-in capability to selectively export 
    sections of a *rivt file* to a *public rivt report* for open-source 
    reuse.

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