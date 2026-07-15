**D.1 | rivt Markup**
======================

.. _API functions:

**[1]** API functions
--------------------------------------------------------------------- 

*rivt* has six API functions. The name *rivt* is an acronym taken from 
four functions that process content. The remaining three functions are used for
document generation and debugging.

.. raw:: html

    <b>Content APIs</b>
    <ol style="border: 2px; 
            border-color: #49b2c3; 
            border-style: solid; 
            padding: 2em;
            margin: 2em">
        <li><b>[R]un</b> Runs Python scripts and markup.</li>
        <li><b>[I]nsert</b> Adds static tables, images and equations.</li>
        <li><b>[V]alues</b> Evaluates equations and functions.</li>
        <li><b>[T]ools</b> Executes shell scripts and external programs.</li>
    </ol>

    <br>

    <b>Publish APIs</b>
    <ol style="border: 2px; 
            border-color: #49b2c3; 
            border-style: solid; 
            padding: 2em;
            margin: 2em">
        <li><b>[D]oc</b> specifies the <i>doc</i> type and style.</li>
        <li><b>[S]kip, e[X]it</b> can be used for interactive debugging and comments.</li>
    </ol>

================ =============== ================================================
API Function         Name             Purpose
================ =============== ================================================
**rv.R** (rS)         Run            Run scripts and markup
**rv.I** (rS)         Insert         Insert static sources 
**rv.V** (rS)         Values         Calculate values
**rv.T** (rS)         Tools          Shell scripts and external programs
**rv.D** (rS)         Doc            Publish docs 
**rv.S,X** (rS)    Skip, Exit        Skip section, exit (comments and debugging)
================ =============== ================================================

API functions define doc sections. The available *rivt markup* commands and
tags depend on the API funciton. If interactive IDEs are used, API functions
can be processed individually using the standard notebook cell percent
notation:

.. code-block:: python

    # %% optional label for navigation
    rv._(r"""rivt string""")


------------------------------------------------

.. _rivt string:

**[2]** rivt string
----------------------------------

Each :doc:`API function <rvA01-start>` takes a raw, triple quoted 
:term:`rivt string` composed of a :term:`header substring` line followed 
by a multiple-line :term:`content substring`. The *header substring* defines 
section processing parameters.  The *content substring* includes  
:term:`rivt markup` and is indented four spaces for improved readability 
and navigation (e.g. section folding).

.. _Header substring:

**Header substring**

The :term:`header substring` starts with a *section label*, used as the
section title, followed by a vertical bar and three comma separated
*section parameters* that override default behavior.

.. code-block:: python

    rv._(r"""Section Label | doc;stored, private;public, section;merge

         Content substring indented 4 spaces
        
        ...
        
        """)

The header parameters include the following comma separated values in any
order:

*private/public* 
    Determines whether the API section text is copied to the the *Public* folder
    *rivt file* for potentinal sharing. Actually sharing this folder is a 
    separate step.

*doc/stored*
    Determines whether the *rivt string* is formatted and printed in the doc, 
    or just annotated in the doc and written to a file in the *Stored* folder 
    for optional inclusion as an appendix.

*section/merge* 
    Determines whether the API starts a new *doc* section
    or is merged into the previous section.   

*script type* 
    For the rv.R API only, the markup script type is specified 
    in the header substring. 

Default settings in the *header substring* do not need to be specified. The
default setting for each API is listed first (in bold) in the table below.
The default privacy settings for all sections in a rivt file may be reversed by
including it in the *comment settings* immediately following the  
*rivlib import statement*.  File default settings are in parenthsis.


.. code-block:: python

    import rivtlib.rvapi as rv

    # rv private = false ; default section parameter changed to public (true)
    # rv no_tag = true ; API type is added to section number (true)
    # rv set_width = true character width of text output (80

Individual sections may be set back to private in the header substring after
changing the default. 

**Header substring defaults**

====== =================== =============== =================== ================== ===========
API      private; public     doc; stored      section; merge     pdfpage; nopage    markup
====== =================== =============== =================== ================== ===========
rv.R    **private**         **stored**       **section**          **nopage**       **type**
rv.I    **private**         **doc**          **section**          **nopage**         NA
rv.V    **private**         **doc**          **section**          **nopage**         NA
rv.T    **private**         **stored**       **merge** [1]        **nopage**         NA
rv.D    **private**         stored only          NA                  NA              NA
rv.S         NA                 NA               NA                  NA              NA
rv.X         NA                 NA               NA                  NA              NA
====== =================== =============== =================== ================== ===========

[1] Summary of tool execution added to prior section

Examples of *header substring* settings are shown below.

- An example with explicit defaults (they do not have to be declared).

.. code-block:: python

    # This
    
    rv.I(r"""A New Section | private, doc, section

        Content text
        ...
        
        """)
    
    # is equivalent to:

    rv.I(r"""A New Section  

        Content text
  
        ...
        
        """)


- An example that merges a section into the previous section.

.. code-block:: python

    rv.I(r"""A Merged Section | merge

        Content text

        ...
        
        """)

.. _Content substring:

**Content substring**

The :term:`content substring` is indented four spaces for legibility and 
code folding. It includes :doc:`line tags<rvD03-linetags>`, 
:doc:`block tags<rvD04-blocktags>` and  :doc:`commands<rvD05-commands>` 
along with  text.

.. code-block:: python

    rv._(r"""Section Label  

        Content text indented 4 spaces.
        ...
        
        """)

Content is converted line by line into formatted text and 
`RestructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`__,
and then further processed into HTML or PDF. If a line does not contain 
a *command*, *tag* or *assignment* it is passed through as is. This allows the 
*Insert* function (rv.I) to include some *restructured text* directly i.e. 
surrounding words with * or ** will format a word as italic or bold.

In addition block tags in the *Tools function* (rv.R) directly supports
processing HTML, LaTeX and reStructuredText scripts.

-------------------------------------------------

.. _markup:

**[3]** Tags and Commands
----------------------------


:doc:`Line Tags <rvD03-linetags>`

    A :term:`line tag` formats a line of text and is denoted with a single
    **_[LETTER]**, placed at or near the end of the line, depending on the tag.

:doc:`Block Tags <rvD04-blocktags>`

    A :term:`block tag` formats a block of text and begins with
    **_[[TAGNAME]]** and terminates with **_[[END]]**.

:doc:`Commands <rvD05-commands>`

    *rivt commands* read and write external files. They typically start in the
    first column with a vertical bar ( | ) followed by the command name, file
    path, and parameters.

    The exceptions are the definition (**==:**), assignment (**<=:**), 
    function (**:=:**) and compare (**<>**) commands that are used to 
    define, assign and compare values.

    .. code-block:: bash  
        
        | COMMAND | relative path | parameters

    File paths are specified relative to the *rivt root folder*. The *rivt
    report* folder structure is described :ref:`here<rivt-folders>`.

    If the path is ommitted the default path for each command is applied. If
    the *singledoc* parameter is set, the *resource files* and *docs* are
    stored in the *rivt root folder*.

Tag and Command syntax for each API type is defined and described 
using the following format:

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Markup Key<br>
    <br>
    _[TAG] or | COMMAND |</b><br>
    <br>
    Description<br>
    <br>
    <pre>
        Syntax:
            _[TAG] or | COMMAND | syntax

        Example:
            This is a sentence. _[C]
    </pre> 
    </p>

-----------------------------------------------

**[4]** Folders
---------------------------

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Names</b><br>
    <br>
    
    A report folder can contain any set of files and folders but the following
    structure is required for <i>doc</i> processing. Files and folders are
    organized under a root folder with the prefix <i>rivt-</i> e.g.
    <i>rivt-Report-Label</i>. <br> <br>
    
    <i>report folders</i> (root folders) include at least the <i>rivt files</i> 
    and the five required subfolders. Required folders and prefixes are 
    shown in brackets. Folders preceded by an underscore contain rivt outputs. 
    Folders requiring author input are capitalized. <br> <br>

The top level folder structure is shown below. A more detailed description of
the folder structure is :ref:`here<report-folders>`.

**Top Level Folders** 

.. code-block:: bash

.. code-block:: bash

      rivt-Report-Label/           Report Folder                
        ├── .vscode/                  optional VSCode settings 
        ├── rivt-public_/             rivt-generated public files
            ├── rvsrc/                     source files
            ├── README.txt                public text report or doc
            ├── rv-101-filename1.py       public rivt file
            ├── rv-102-filename2.py       public rivt file       
            ├── rv-201-filename3.py       public rivt file          
            ...
        └── rivt-report/               rivt files and docs               
            ├── _published/               published docs and reports
            ├── _rstdocs/                 intermediate restructured text files               
            ├── rv_stor/                  rivt generated stored files
            ├── rvsrc/                    author source files
            ├── rivt-report.py            report generating script
            ├── rv101-filename1.py        rivt file
            ├── rv102-filename2.py        rivt file       
            ├── rv201-filename3.py        rivt file          
            ...    
        └── README.txt                 text report or doc  

------------------------------------


.. toctree::
    :maxdepth: 2
    :hidden:

    rvD02-apiscope.rst
    rvD03-linetags.rst
    rvD04-blocktags.rst
    rvD05-commands.rst    
    rvD06-assign.rst    

    