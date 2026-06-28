
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
documents, with a focus on document reuse and privacy controls. Python
knowledge is not needed to use rivt but Python scripts can provide access to,
and automation of, a large collection of scientific and engineering libraries.

There are four types of rivt document files:

.. code-block:: text

               | A rivt file is the basic input file that produces a publication 
   rivt file   | document. It is a Python file (.py) that imports the rivtlib 
               | Python package and includes plain text content and rivt markup.

               | A rivt doc is the published output of a rivt file. A doc
   rivt doc    | is a formatted text, PDF or HTML output file compiled from
               | a rivt file. The same rivt file produces each type of doc.

               | A rivt report is the published output from a group of
   rivt report | rivt files organized and collated into a single text,
               | PDF or HTML report file. Each rivt doc is a chapter in the report/


               | A rivt book is an organized collection of rivt files with  
   rivt book   | a common subject matter organized for efficient selection
               | and insertion into docs and reports.
   

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started using
*rvit* see :ref:`here <rivt-start>`. For using *AI* with *rivt* see 
:ref:`here <rivt-context>`.  

An interface for finding public *rivt files* on **GitHub** is 
:doc:`here. <rvE02-ghsearch>` A collection of open source models and documents 
on **Google Drive**, including *rivt*, is `here. <https://www.openmodels.info>`__

*rivt* produces clear, organized engineering documents through a fast
compilation process that can process a complete *doc* or *report*, or executed 
section by section interactively similar to `Jupyter notebook. <https://jupyter.org/>`__
A typical complete *doc* takes a second or two to compile.

*rivt markup* formats documents using about 3 dozen commands and tags with
reasonble defaults. If more control is needed to publiish formal journal
articles or books, `Quarto <https://quarto.org/>`__ will be a better tool.
A brief discussion of other engineering document tools and their
strengths relative to the objectives of *rivt* is :ref:`here <motivation>`.

.. raw:: html

   <hr>

   <p style="color:rgb(63,177,197);">ver: 1.0.0a12 
   (Note: rivt is <i>alpha sofware</i>. Some features are incomplete 
   and the user API may change.)</p>

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