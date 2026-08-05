
.. raw:: html

   <div style="display:none">

Home
=================

.. raw:: html

   </div>


.. figure::  _static/img/rivt-finalb.png
    :class: dark-light
    :scale: 20%
    :align: center
    :alt: rivt logo
    
.. raw:: html

   <hr>
    

*rivt* is an open-source program for writing and assembling calculation
documents with a focus on reuse [#]_.  The large ecosystem of engineering 
analysis software often requires organizing and combining their output into a 
single, systematic project document.

*rivt* is designed to write, assemble and link calculation documents and code
into live, editable and organized *rivt files*  prior to publishing text, PDF or
HTML *docs* or *reports*. *rivt markup* facilitates converting any PDF or text
document to, or directly writing, a live calculation document that can be 
easily modified and extended. Python knowledge is not required to use *rivt* but 
incorporating Python scientific and engineering libraries increases its capabilities.

The primary purpose of *rivt* is providing a stable file format that
can be shared, edited, and maintained as a live calculation document, and that 
produces text, PDF and HTML engineering reports as output.  *rivt files* and 
can be organized in three ways, that differ only in their folder structure and 
publication processing.

.. code-block:: text

                    | A rivt file is the basic input file that
      rivt file     | compiles to a text, PDF or HTML document. 
                    | It is a Python file (.py) that imports the 
                    | rivtlib Python package and uses rivt markup.

                    | A rivt doc is the published output of a rivt
      rivt doc      | file. A doc may be formatted as text, PDF
                    | or HTML from the same rivt file.

                    | A rivtbook is a collection of rivt files with
      rivtbook      | common subject matter and a folder structure
                    | that makes it easy to select files and resources
                    | for inclusion in documents and reports.

                    | A rivt report is the collated output of multiple
      rivt report   | docs into a single text or PDF file, or an HTML
                    | site. A Python script links and organizes docs 
                    | into a structured report using rivt file numbering. 

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started with
running examples see :ref:`install <rivt-start>`. For *rivt* and *AI* see
:ref:`here <rivt-context>`. Examples of a :ref:`rivt file <example-file>` with
:ref:`text <text-doc>`, :ref:`PDF <pdf-doc>`, and :ref:`HTML <html-doc>`
output *docs* are provided in this :ref:`tutorial <rivt-tutor>`. Other documents 
and examples may be downloaded from `Google Drive. <https://www.openmodels.info>`__ 

The *rivtlib* `Python package <https://pypi.org/project/rivtlib/>`__ formats
and compiles a *rivt file* to a text, PDF or HTML document (*doc*) in a few
seconds. *rivt file* sections may be interactively executed, top down, in an
IDE. Multiple *rivt files* may be compiled into a collated :ref:`rivt report
<rivt-reports>`. This website is an example of an HTML *rivt report*. *rivt
files* may be organized into :ref:`rivtbooks <rivt-books>` with a common
subject matter for efficient selection and inclusion in reports. A convenient
interface for searching and downloading public *rivt files* on *GitHub* is
:doc:`here. <rvE02-github>` . *rivt reports* and examples are also available at
`openmodels.info <https://www.openmodels.info/models>`__.

*rivt* produces organized, formatted engineering documents from active
calculation files using reasonable defaults. Use cases are listed :ref:`here
<use-case>`. For static documents with rigid format requirements, including
journal articles and books that do not need recalculation, `Quarto
<https://quarto.org/>`__ is likely a better fit. For interactive calculation 
documents not intended for organized report publication 
`Jupyter Notebooks <https://jupyter.org/>`__ is likely a better fit. A brief 
discussion of current engineering document tools and their strengths relative 
to the objectives of *rivt* is :ref:`here <motivation>`.

.. [#] rivt includes switches that selectively export *rivt file* sections
    to a *public rivt report folder* for open-source reuse.

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