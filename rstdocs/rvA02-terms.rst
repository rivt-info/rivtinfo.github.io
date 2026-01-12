**A.2 Terms**
=====================

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

  single doc 
  single docs 
    A single doc is a rivt file that publishes a doc that is not part of 
    a report and is used for quick docs that only require limited formatting. 
    
    It is specified in a comment variable directly after the *rivtlib* 
    import statement.

    # rv singledoc = True
  
    The default setting is False. The rivt file folder is used for 
    source and output files. A folder structure is not used. 

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
  header text
  header substring
    The first line of a  *rivt string*. It includes a section title, followed 
    by comma separated parameters.

  content
  content text
  content substring
    The text in a *rivt string* that follows the *header substring*. The text is 
    utf-8 (Unicode Transformation Format - 8-bit), a character encoding 
    standard that is a superset of ASCII, handles text from any language, 
    and is constant across all platforms.
  
  rivt
    An open source Python project that includes :term:`rivtlib` and approximately 
    two dozen :doc:`Python packages <rvB02-python>`. When *rivt* is installed
    :term:`docs` and :term:`reports` may be edited and published using a text
    editor.
  
  rivt doc
  rivt docs
    A formatted document file output from a *rivt file* using the rivtlib package. 
    A doc is a text, PDF or HTML file with the default name of the *rivt file* 
    and file type suffix.
  
  rivtlib
    Open source `Python package <https://www.rivtlib.dev>`_ that generates docs 
    and reports from a :term:`rivt file`  

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
    The recommended *rivt-framework* includes the
    following separately installed programs:

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
    variables. They start in the initial columns with a 
    vertical bar ( | ) followed by the file path, name and parameters. The path
    is relative to the rivt report root folder. If the metadata variable
    *rv_localB* is set to true resources will be read from and written to the 
    local *rivt file* folder.

    .. code-block:: bash

      | COMMAND | relative path | parameters
    

  report
  reports
  rivt report
    A group of compiled *docs* organized by rivt file number. 

  report folder
  report folders
    The folder structure for producing a report is described 
    :doc:`here. <rvD03-folders>`

  section parameter 
  section parameters 
    Comma separated parameters in a *header* that specify the section processing.

  API log
    API excecution history written to log folder as the file *rvDss-api.rst*. 
    For the complete execution history see the rivt log file *rvDss-log.txt*.

  rivt log file
    *rivt file* execution log written to the *log folder* as *rvDss-log.txt*.

  report script
    A Python script that assembles *docs* into a *report*.

  rvspace
    rivt alias name for the global rivt file namespace. Other user namespaces may be 
    specified


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

  fork
    duplicate of a software project's code to create a new, 
    independent version


.. raw:: html

    <p id="api">&lt;t&gt;</p>

  
**[4]** VSCode Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 

  profile
    Allows VSCode users to customize their environment for different workflows, 
    projects, or tasks. This feature provides a way to manage distinct 
    configurations of settings, extensions, keyboard shortcuts, snippets, 
    and tasks.

  IDE
    Integrated Development Environment. A software application that provides 
    comprehensive facilities to computer programmers for software development. 
    An IDE typically includes a code editor, build automation tools, 
    and a debugger. *rivt extensions* are mostly developed for VSCode. 
    Other examples include PyCharm, Spyder, and JupyterLab.

