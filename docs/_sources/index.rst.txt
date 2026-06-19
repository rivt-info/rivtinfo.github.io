
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


*rivt* is a lightweight, extensible open source Python tool 
for writing, organizing and sharing engineering documents. 
It takes readable, interactive text files and compiles them into 
formatted **text, HTML or PDF document files**.  

There are four types of rivt files:

.. code-block:: text

               | A rivt file is the basic file that produces a publication. 
   rivt file   | It is a Python file (.py) that imports the rivtlib Python
               | package and includes document content and markup.

               | A rivt doc is the basic publication of a rivt file. 
   rivt doc    | It is a formatted text, PDF or HTML output file compiled
               | from a rivt file.

               | A rivt report is the published output from a
   rivt report | collection of rivt files organized and compiled into
               | a single text, PDF or HTML report file.


               | A rivt book is a collection of rivt files sharing a common 
   rivt book   | topic and organized for efficient search and porting
               | to rivt files that are part of a doc or report.
   

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started see 
:ref:`here <rivt-start>`. For *rivt* and *AI*  see :ref:`here<rivt-context>`. 
*rivt* works naturally with *AI* tools.

An interface for finding public *rivt files* on **GitHub** is 
:doc:`here<rvE02-ghsearch>`. A collection of open source models and documents, 
including *rivt*, is at **Google Drive** `here <https://www.openmodels.info>`__ . 

*rivt* produces clear, organized engineering documents using reasonable default
formats that can be customized. *rivt markup* uses about 3 dozen commands and
tags to format and assemble documents. If journal articles or books with 
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