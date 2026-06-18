
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


*rivt* is a lightweight, interactive and extensible open source Python tool 
for writing, organizing and sharing engineering production documents. 
It compiles and formats naturally readable text files (*.py* files) into formatted 
**text, HTML or PDF document files** (*rivt docs*).  

There are four types of rivt documents:

.. code-block:: text

   rivt file   | A Python file that imports the rivtlib package 
               | and includes document content and rivt markup
   
   rivt doc    | A formatted text, PDF or HTML file output from 
               | a rivt file

   rivt report | A group of rivt files output as a linked and
               | collated text, PDF or HTML doc file

   rivt book   | A collection of rivt files orgainzed around a common 
               | subject matter and arranged for individual export 

 
An interface for finding public *rivt files* on **GitHub** is 
:doc:`here<rvE02-ghsearch>`. A collection of open source models and documents, 
including *rivt*, is at **Google Drive** `here <https://www.openmodels.info>`__ . 

For an overview of *rivt* and *AI* see :ref:`here<rivt-context>`.
*rivt* is effective in organizing *AI* outputs into documents and reports with a
high degree of user control.

*rivt* produces clear, organized engineering documents using reasonable default
formats that can be customized. *rivt markup* uses about 3 dozen commands and
tags to format and build documents. If journal articles or books with 
higher production values are needed `Quarto <https://quarto.org/>`__ is a 
better tool. Further discussion of avaialble scientific and engineering 
document tools is :ref:`here <motivation>`.

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