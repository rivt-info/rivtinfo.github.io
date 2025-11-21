**A.2 Terms**
=====================

.. raw:: html

    <p id="api">&lt;t&gt;</p>


**[1]** rivt Terms
-----------------------------

.. raw:: html

    <hr>


.. glossary::
  :sorted: 

  doc
  docs
    A formatted document file output using the rivtlib package. 
    A doc is a text, PDF or HTML file with the default name of the *rivt file* 
    and file type suffix.


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

  API header
  API headers
    The first line of a  *rivt string*. It includes a section title, followed 
    by comma separated parameters.
    
  header
  headers
    The first line of a  *rivt string*. It includes a section title, followed 
    by comma separated parameters.

  rivt doc
  rivt docs
    A formatted document file output from a *rivt file* using the rivtlib package. 
    A doc is a text, PDF or HTML file with the default name of the *rivt file* 
    and file type suffix.
  
  rivtlib
    Python package that generates docs and reports from 
    a `rivt file. <https://rivtlib.dev>`_

  rivt string
    Triple quoted string argument to an API function.

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

  rivt framework
  framework
    The *rivt-framework* includes installation of the following programs:

    #. `VSCode <https://code.visualstudio.com/>`_ and 
       `VSCode extensions <https://marketplace.visualstudio.com/vscode>`_. 
       *rivt* extensions and snippets are :doc:`here <rvB03-vscode>`.
    #. `Git <https://git-scm.com>`_ and set up a `GitHub <hhttps://github.com>`_ 
    #. `LaTeX <https://www.tug.org/texlive/>`_ 
    #. `QCAD <https://qcad.io/en/>`_ 

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
    published using the local folder  rather than the *src* subfolder. In 
    this case command files and *docs*  are read and written to 
    the *rivt file* folder.

  report
  reports
    A group of compiled *docs* organized by rivt file number. 

  report folder
  report folders
    The folder structure for producing a report is described 
    :doc:`here. <rvD03-folders>`

  section parameter 
  section parameters 
    Comma separated parameters in a *header* that specify the section processing.

  section text
    The content of a *rivt string* minus the *header*. 

  api-history 
    API excecution history written to log folder as the file *rvDss-api.rst*. 
    For the complete execution history see the rivt log file *rvDss-log.txt*.

  rivt log file
    *rivt file* execution log written to the *log folder* as *rvDss-log.txt*.

  report script
    A Python script that assembles *docs* into a *report*.

  stand-alone doc
    A single document that is not part of a report. It uses
    the local rivt file folder for reading and writing files. *doc* 
    styling control is limited compared to a *report*.

  rv-namespace
  rv-space
    rivt alias name for the global rivt file namespace. Other user namespaces may be 
    specified

  rv_authD
    Defined in rv.M(). Specifies the author, version, email, repository and 
    license information and lists the forks. *rv_forknD* specifies data for 
    the forked file. 

  rv_fork1D 
    Defined in rv.M(). Example name of a *doc* fork specified in the *forks* 
    list of rv_authD.

  rv_localB 
    Defined in rv.M(). Overrides the default report structure and specifies 
    that the *values* and *ouput* files are written to the rivt file folder.

  rv_docnameS
    Defined in rv.M(). Overrides the default doc title derived from 
    the rivt file name.

  rv_headerL
    Defined in rv.M(). Specfies the contents and order of *doc* page headings.

.. raw:: html

    <p id="api">&lt;t&gt;</p>

**[2]** Python Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 

  
  Python
    A language
  
  docutils
    A Python package that processes `restructured text <https://docutils.sourceforge.io/>`_
    files into HTML, LaTeX, and other formats.

  restructuredtext
  restructuredtext markup
    A lightweight markup language designed to be processed by document software 
    including `docutils, <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ 
    Sphinx and rivt.

  namespace
    Provides `scope <https://en.wikipedia.org/wiki/Namespace>`_ for functions 
    and variables. 

.. raw:: html

    <p id="api">&lt;t&gt;</p>


**[3]** GitHub Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 


  repository 
    a storage location for software packages

.. raw:: html

    <p id="api">&lt;t&gt;</p>

  
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

