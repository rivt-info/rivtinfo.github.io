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
    A Python file that imports *rivtlib* and includes rivt markup.  

  rivt file number 
    Prefix of rivt file name used to organize a report. It has the form 
    *rvDss-filename.py* where D is a capital alphanumeric division number 
    and ss is the subdivision number.

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
    ``| COMMAND | rel path | filename | parameters``. The relative path is 
    a subfolder of the *source* folder, or the alias *rvlocal* if 
    the rivt file is for a *single doc* where the sources are stored in the same 
    folder as the *rivt file*. 

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
  The folder structure for producing a report, described :doc:`here. <rvD02-folders>`


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
    such as Docutils and rivt, and readable by humans.

  namespace
    provides `scope <https://en.wikipedia.org/wiki/Namespace>`_ for functions 
    and variables 


**[3]** GitHub Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 

  docutils1
    A Python package that processes `restructured text <https://docutils.sourceforge.io/>`_
    files into HTML, LaTeX, and other formats.

  repository 
    a storage location for software packages


  
**[4]** VSCode Terms
-----------------------------

.. raw:: html

    <hr>

.. glossary::
  :sorted: 

  docutils2
    A Python package that processes `restructured text <https://docutils.sourceforge.io/>`_
    files into HTML, LaTeX, and other formats.