
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


*rivt* is an extensible, open-source Python tool for writing engineering
documents with a focus on reuse [1]_. Python knowledge is not required but
*rivt* capabilities can be extended with Python scripts that access scientific
and engineering libraries.

There are four types of rivt document files:

.. code-block:: text

                    | A rivt file is the basic input file that
      rivt file     | compiles to a text, PDF or HTML document. 
                    | It is a Python file (.py) that imports the 
                    | rivtlib Python package.

                    | A rivt doc is the published output of a
      rivt doc      | rivt file. A doc is an output file in 
      rivt chapter  | formatted text, PDF or HTML. In the context
                    | of a report or book a doc is a chapter. All 
                    | formats are compiled from the same rivt file. 

                    | A rivt report is the published output 
                    | of multiple docs collated into a single 
      rivt report   | text, PDF or HTML file. Each doc is a
                    | chapter in the report. Chapters are
                    | grouped together in divisions.

                    | A rivtbook is a collection of rivt files
      rivtbook      | with a common subject matter and
                    | organized for efficient selection and 
                    | inclusion in docs and reports.


For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started using
*rivt* see :ref:`here <rivt-start>` and :ref:`here <rivt-tutor>` for 
installation and tutorials. For *rivt* and *AI* see :ref:`here <rivt-context>`.

The *rivtlib* Python package formats and compiles a *rivt file* to a text, PDF
or HTML document ( *doc* ) in about a second. *rivt file* sections may be
interactively executed in an IDE, similar to a `Jupyter notebook.
<https://jupyter.org/>`__ Multiple *rivt files* may be compiled into a collated
*rivt report*. This website is an example of an HTML *rivt report*. *rivtbooks*
are collections of *rivt files* about a common subject matter and organized for
efficient selection and inclusion in reports.

A convenient interface for searching and downloading public *rivt files* on
*GitHub* is :doc:`here. <rvE02-github>` Open source engineering models,
documents and examples, including *rivt*, may be downloaded from 
`Google Drive. <https://www.openmodels.info>`__

*rivt* produces clear, organized engineering documents from active calculations
using reasonable defaults. Use cases are listed :ref:`here <use-case>`.
Document tools like `Quarto <https://quarto.org/>`__ are likely better tools
for static, formatted documents including journal articles and books that do
not need recalculation. A brief discussion of engineering document
tools and their strengths relative to the objectives of *rivt* is :ref:`here
<motivation>`.

.. [1] rivt includes the built-in capability to export selected
    sections of a *private rivt file* to a *public rivt file* for sharing 
    and reuse.

.. raw:: html

   <hr>

   <p style="color:rgb(63,177,197);">ver: 1.0.0a12 
   (Note: rivt is currently <i>alpha sofware</i>. Some features are 
   incomplete and markup tags, commands and assignments may change.)</p>

.. toctree::
    :maxdepth: 1
    :hidden:

    rvA00-start.rst
    rvB00-overview.rst
    rvC00-documents.rst
    rvD00-markup.rst
    rvE00-collab.rst
    rvF00-aiintro.rst
    rvG00-quickref.rst