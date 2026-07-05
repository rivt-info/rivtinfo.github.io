
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


*rivt* is an open source Python tool for writing and sharing engineering
documents, with a focus on document reuse. Python knowledge is not required but
*rivt* capabilities are extended by Python scripts that access scientific and
engineering libraries.

There are four types of rivt document files:

.. code-block:: text

               | A rivt file is the basic input file that produces a publication 
   rivt file   | document. It is a Python file (.py) that imports the rivtlib 
               | Python package and includes plain text content and rivt markup.

               | A rivt doc is the basic published output of a rivt file. A doc
   rivt doc    | is a formatted text, PDF or HTML output file compiled from
               | a rivt file. The same rivt file produces each type of doc.

               | A rivt report is the published output from a group of rivt files
   rivt report | organized and collated into a single text, PDF or HTML report
               | file. Each doc is a chapter in the report,


               | A rivt book is a collection of rivt files with a common
   rivt book   | subject matter organized for efficient selection and inclusion
               | in docs and reports.
   

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started see
:ref:`here <rivt-start>`. For *rivt* and *AI* see :ref:`here
<rivt-context>`.

The *tivtlib* package formats and compiles a *rivt file* to a text, PDF or HTML
document in a second or two. *rivt file* sections may be Interactively executed
in and IDE, similar to a `Jupyter notebook. <https://jupyter.org/>`__

A convenient interface for searching public *rivt files* on **GitHub** is 
:doc:`here. <rvE02-github>` A collection of donwloadable open source models 
and documents on **Google Drive**, including *rivt*, is 
`here. <https://www.openmodels.info>`__

*rivt* produces clear, organized engineering documents from active calculations
using reasonable defaults. Use cases are listed :ref:`here <use-case>`. For
formatted documents that are typically static, including journal articles and
books, `Quarto <https://quarto.org/>`__ is likely a better tool. A brief
discussion of engineering document tools and their strengths relative to the
objectives of *rivt* is :ref:`here <motivation>`.

.. raw:: html

   <hr>

   <p style="color:rgb(63,177,197);">ver: 1.0.0a12 
   (Note: rivt is currently <i>alpha sofware</i>. Some features are incomplete 
   and markup *tags and commands* may change.)</p>

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