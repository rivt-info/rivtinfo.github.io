**A.2 Terms**
=====================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** rivt Terms
-----------------------------

.. raw:: html

    <hr>


.. glossary::
  :sorted: 

  doc
  docs
    A formatted document file output by rivt. The file is a text, 
    PDF or HTML file.


  doc number 
    Prefix of a rivt and doc file name and used to organize a report. 
    It has the form *rvDss-filename.py* where D is a capital alphanumeric 
    division number and ss is the subdivision number.


  division 
    A group of related rivt files organized in a report and labeled in
    the rivt file name. Optionally organized in a division folder.


  rivt markup  
    A light weight markup that wraps restructuredText and outputs reports in
    text, PDF and HTML. Markup is included in string arguments to rivt 
    API functions. 


  rivtlib
    Python package that generates docs and reports from 
    a `rivt file. <https://rivtlib.dev>`_


  rivt string
    Triple quoted string argument to an API function.


  rivt file
  rivt files
    A Python file that imports *rivtlib* and includes *rivt markup*.  

  rivt file
  rivt files
    A Python file that imports *rivtlib* and includes *rivt markup*.  

  rivt file number 
    Prefix of rivt file name used to organize a report (rvDss-). It has the form 
    *rvDss-filename.py* where D is a capital alphanumeric division number 
    and ss is the subdivision number.


  rivt folder
    A folder containing a rivt file and all of its resources in the same folder. 
    Generally used 

  rivt report folder  
    A folder containing multiple rivt files to be organized in a report 
    and resources organized in subfolders

  line tag
  line tags
    A line tag has the form **_[TAG]** and formats a line of text. 


  block tag
  block tags
    A block tag formats a block of text that begins with **_[[TAG]]**
    and terminates with **_[[Q]]**. 


  command
  commands 
    *rivt commands* read and write external files and assign values to
    variables. They typically start in the first column with a 
    vertical bar ( | ) followed by the file path, name and parameters:

    .. code-block:: bash

      | COMMAND | rel path | filename | parameters
    
    For *reports* the relative path is a subfolder of the *source* folder. If 
    the file is a  *single doc* the alias *rvlocal* specifies that the 
    sources are stored in the same folder as the *rivt file*. 


  single doc 
  single docs 
    A document that is not part of a report. It may be
    published using the local folder alias (*rvlocal*) for the relative path 
    rather than the *source* subfolder. In this case command files and *docs* are
    are read and written to the *rivt file* folder.


  report
  reports
    A report is a group of compiled *docs* organized by rivt file number. 


  report folder
  report folders
    The folder structure for producing a report is described :doc:`here. <rvD02-folders>`


  section parameter 
  section parameters 
    Comma separated parameters in a *header* that specify the section processing.


  section content
    The content of a *rivt string* minus the *header*. 


  api-history 
    API excecution history written to log folder as the file *rvDss-api.rst*. For the complete 
    execution history see the rivt log file *rvDss-log.txt*.


  rivt log file
    *rivt file* execution log written to the *log folder* as *rvDss-log.txt*.

**[2]** Python Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 

  docutils
    A Python package that processes `restructured text <https://docutils.sourceforge.io/>`_
    files into HTML, LaTeX, and other formats.

  restructured text
    A lightweight markup language designed to be processed by document software 
    including `docutils, <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ 
    Sphinx and rivt.

  namespace
    Provides `scope <https://en.wikipedia.org/wiki/Namespace>`_ for functions 
    and variables. 


**[3]** GitHub Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 


  repository 
    a storage location for software packages


  
**[4]** VSCode Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 

  profile
    Allows users to customize their VS Code environment for different workflows, 
    projects, or tasks. This feature provides a way to manage distinct 
    configurations of settings, extensions, keyboard shortcuts, snippets, 
    and tasks.

