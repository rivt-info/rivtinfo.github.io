
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


*rivt* is a lightweight, extensible open source Python tool for writing,
organizing and sharing engineering documents. It compiles markup text
in rivt files into formatted **text, HTML or PDF documents**.

There are four types of rivt and document files:

.. code-block:: text

               | A rivt file is the basic input file that produces a publication 
   rivt file   | document. It is a Python file (.py) that imports the rivtlib 
               | Python package and includes plain text content and markup.

               | A rivt doc is the published output of a rivt file. A doc
   rivt doc    | is a formatted text, PDF or HTML output file compiled from
               | a rivt file. The same rivt file produces each type of doc.

               | A rivt report is the published output from a group of
   rivt report | rivt files organized and collated into a single text,
               | PDF or HTML report file.


               | A rivt book is an organized collection of rivt files with  
   rivt book   | a common subject matter and organized for efficient selection
               | and insertion into docs and reports.
   

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started see 
:ref:`here <rivt-start>`. For *rivt* and *AI*  see :ref:`here <rivt-context>`. 
*rivt* works seamlessly with *AI* tools while maintaining user control of the
final document.

An interface for finding public *rivt files* on **GitHub** is 
:doc:`here<rvE02-ghsearch>`. A collection of open source models and documents, 
including *rivt*, is at **Google Drive** `here <https://www.openmodels.info>`__ . 

*rivt* produces clear, organized engineering documents using reasonable default
formats that can be customized. *rivt markup* uses about 3 dozen commands and
tags to format and compile documents and reports. For formal journal articles or 
books needing higher production values `Quarto <https://quarto.org/>`__  is a 
better tool. Further discussion of available scientific and engineering 
document tools and their strengths realtive to the objectives of *rivt* 
is :ref:`here <motivation>`.

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