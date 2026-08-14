
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
documents with a focus on reuse [#]_. The extensive and expanding collections of 
engineering and scientific software often require that outputs be organized
into systematic project documents. *rivt markup* is used to write live, linked
and editable *rivt files* that organize text, calculations, images, code and 
output from different sources. *rivt* publishes *rivt files* as text, PDF or HTML 
*docs*. Python knowledge is not required but incorporating Python scientific 
and engineering libraries into a *rivt file* increases its capabilities.

The primary purpose of *rivt* is providing a stable file format that can be
shared, edited, and maintained as a live calculation document that
produces formatted text, PDF and HTML engineering reports as output. 
*rivt files* can be organized in two ways:

.. code-block:: text

                    | A rivt file is the basic input file that
      rivt file     | compiles to a text, PDF or HTML document (doc). 
                    | It is a Python file (.py) that imports the 
                    | rivtlib Python package and uses rivt markup.

                    | A rivtbook is a collection of rivt files with
      rivtbook      | common subject matter and a folder structure
                    | that makes it easy to select files and resources
                    | for inclusion in docs and reports.

                    | A rivt report is the collated output of one or more 
                    | rivt docs into a single text or PDF file, or an HTML
      rivt report   | site. A rivt doc is the published output of a rivt  
                    | file. A Python script links and organizes multiple 
                    | docs into a report using rivt file numbers. 

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started with
running examples see :ref:`install <rivt-start>`. For *rivt with AI* see
:ref:`here <rivt-context>`. Examples of a :ref:`rivt file <example-file>` with
:ref:`text <text-doc>`, :ref:`PDF <pdf-doc>`, and :ref:`HTML <html-doc>` *docs* 
are provided in this :ref:`tutorial <rivt-tutor>`.

*rivtlib* is the `Python package <https://pypi.org/project/rivtlib/>`__ that formats
and compiles a *rivt file* to *doc* in a second or two. A *rivt file* may 
be interactively executed into text from the top down in an IDE, or as a whole 
from the command line. Multiple *rivt files* may be compiled into a collated 
:ref:`rivt report  <rivt-reports>`.  This website is an example of an HTML 
*rivt report*.  *rivt files* may also be  collected into 
:ref:`rivtbooks <rivt-books>` that address  a common subject matter. 
*rivtbooks* are organized for efficient selection and inclusion of chapters into 
a report. 

*rivt files and reports* may be shared and distributed through any cloud
storage service. *rivt report* examples on *Google Drive* are available at 
`openmodels.info <https://www.openmodels.info/models>`__. If collaboration and 
version control are needed `GitHub <https://github.com/>`__ may be used. 
*rivt files and reports* are organized in top level 
:ref:`rivt project <rivt-folders>` or :ref:`rivtbook <rivt-books>` folders which
work well as *GitHub repositories*. *rivt* also generates a text report as a 
*GitHub README* file. A convenient interface for searching public *rivt file* 
READMEs  on *GitHub* is :doc:`here. <rvE02-github>`. 

*rivt* produces organized, formatted engineering documents from active
calculation files using reasonable defaults. Use cases are listed :ref:`here
<use-case>`. A brief discussion of current engineering document tools and their 
strengths relative to *rivt* objectives is :ref:`here <motivation>`.
For documents with rigid format requirements, including
journal articles and books that do not need active recalculation, `Quarto
<https://quarto.org/>`__ is likely a better fit. For interactive calculation 
documents that do not need an organized published report,
`Jupyter Notebooks <https://jupyter.org/>`__ is likely a better fit. 

.. [#] rivt includes switches that selectively export *rivt file* sections
    to a *public rivt report folder* for open-source reuse.

.. raw:: html

   <hr>

   <p style="color:rgb(63,177,197);">ver: 1.0.0a18 
   (Note: rivt is currently <i>alpha sofware</i>. Some features are 
   incomplete and program structure, markup and assignment tags, and commands may change.)</p>

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