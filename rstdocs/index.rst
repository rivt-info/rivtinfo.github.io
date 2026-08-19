
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
    

*rivt* is an open-source project for writing and assembling calculation
documents with a focus on file reuse [#]_. It is designed to work with the 
extensive collection of individual engineering and scientific software packages 
that often require organization into systematic project documents. 
*rivt markup* is used in *rivt files* to write and organize text, calculations, 
images, code and output from different sources. The *rivtlib* Python package 
compiles and publishes a *rivt file* as a text, PDF or HTML *doc*.

The primary purpose of *rivt* is to provide a stable file and folder format that 
can be shared, edited, and maintained as a live calculation file that
produces formatted reports.  *rivt files* are organized in *rivt project*
or *rivtbook* folders. 

.. code-block:: text

                        | A rivt file is the input file that compiles
   rivt file            | to a text, PDF or HTML document (doc). 
                        | It is a Python file (.py) that imports the 
                        | rivtlib Python package and uses rivt markup.

                        | A rivtbook folder is a collection of rivt files with
   rivtbook folder      | common subject matter, and a folder structure
                        | that makes it easy to select files and resources
                        | for inclusion in rivt docs.

                        | A rivt project folder is a collection of one or
   rivt project folder  | more rivt files and resources. rivt files in the
                        | project folder are compiled into a text, PDF or
                        | HTML doc and assembled into a report. 

For an overview of *rivt* see :ref:`here <rivt-overview>`. To get started with
running examples see :ref:`install <rivt-start>`. For *rivt with AI* see
:ref:`here <rivt-context>`. Examples of a :ref:`rivt file <example-file>` with 
the associated :ref:`text <text-doc>`, :ref:`PDF <pdf-doc>`, and 
:ref:`HTML <html-doc>` *docs* are provided in this :ref:`tutorial <rivt-tutor>`.

*rivtlib* is the `Python package <https://pypi.org/project/rivtlib/>`__ that formats
and compiles a *rivt file* to a *doc* in a second or two. Python knowledge is not 
required to use *rivt* but incorporating Python scientific and engineering 
libraries into a *rivt file* increases its capabilities. A *rivt file* may 
be interactively executed from the top down in an IDE, or from the command line. 
Multiple *rivt files* may be compiled into a :ref:`rivt report  <rivt-reports>`.  
This website is an example of an *HTML report*. *rivt files* may also be collected 
into a :ref:`rivtbook <rivt-books>` organized around a common subject matter. 
*rivtbooks* are organized for efficient file selection and inclusion in reports. 

*rivt files and reports* may be shared and distributed through any cloud
storage service. Examples are available on *Google Drive* at 
`openmodels.info <https://www.openmodels.info/models>`__. If collaboration and 
version control are needed `GitHub <https://github.com/>`__ may be used for development
and distribution. *rivt files and reports* are organized in top level folders  
( :ref:`rivt project <rivt-folders>` or :ref:`rivtbook <rivt-books>` ) which
work well as *GitHub* repositories. *rivt* also generates a *GitHub* README file 
from a *rivt report*. A convenient interface for searching  public *rivt* READMEs 
is :doc:`here. <rvE02-github>`. 

*rivt* produces organized, formatted engineering documents from active
calculation files using reasonable defaults. Use cases are listed :ref:`here
<use-case>`. A brief discussion of current engineering document tools and their 
strengths and weaknesses relative to *rivt* objectives is :ref:`here <motivation>`.
For documents with rigid format requirements, including
journal articles and books that do not need active recalculation, `Quarto
<https://quarto.org/>`__ is likely a better fit. For interactive calculation 
documents that do not need an organized published report,
`Jupyter Notebooks <https://jupyter.org/>`__ is likely a better tool. 

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