**D.1 Markup**
==================

.. _API functions:

**[1]** API functions
--------------------------------------------------------------------- 

*rivt* has six API functions. The name *rivt* is an acronym taken from the
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

API functions define doc sections. If interactive IDEs are used, API functions
can be processed individually using the standard notebook cell percent
notation:

.. code-block:: python

    # %% optional label
    rv.API("""rivt string""")


------------------------------------------------

.. _rivt string:

**[2]** rivt string
----------------------------------

Each :doc:`API function <rvA01-start>` takes a triple quoted :term:`rivt string` 
argument composed of a :term:`header substring` line followed 
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

    rv._("""Section Label | doc;stored, private;public, section;merge

         Content substring indented 4 spaces
        
        ...
        
        """)

The header parameters include the following comma separated values in any
order:

*private/public* 
    Determines whether the API section text is copied to the
    the *Public* folder *rivt file* for sharing. 

*doc/stored*
    Determines whether the *rivt string* is formatted and printed in the doc, 
    or just annotated in the doc and written to a file in the *Stored* folder 
    for optional inclusion as an appendix.

*section/merge* 
    Determines whether the API starts a new *doc* section
    or is merged into the previous section.   

Default settings in the *header substring* do not need to be specified. The
default setting for each API is listed first (in bold) in the table below.
The default privacy settings for all sections in a rivt file may be reversed by
including the *public comment setting* immeditely following the 
*rivlib import statement*. 

.. code:: python

    import rivtlib.rvapi as rv

    # rv setpublic = true

Individual sections may still be set as private in the header substring.
 
========== ===================== ===================== =====================
API          private; public         doc; stored           section; merge         
========== ===================== ===================== ===================== 
rv.R        **private**; public     **stored**; doc       **merge**; section
rv.I        **private**; public     **doc**; stored       **section**; merge   
rv.V        **private**; public     **doc**; stored       **section**; merge    
rv.T        **private**; public     **stored**; doc       **merge**; section
rv.S        **private**; public     **stored**            **merge**
rv.D        **public**              **stored**            **merge**
rv.X         -                       -                    -
========== ===================== ===================== =====================

Examples of *header substring* settings are shown below.

- An example with explicit defaults (they do not have to be declared).

.. code-block:: python

    # This
    
    rv.I("""A New Section | private, doc, section

        Content text
        ...
        
        """)
    
    # is equivalent to:

    rv.I("""A New Section  

        Content text
  
        ...
        
        """)


- An example that merges a section into the previous section.

.. code-block:: python

    rv.I("""A Merged Section | merge

        Content text

        ...
        
        """)

.. _Content substring:

**Content substring**

 

The :term:`content substring` is indented four spaces for legibility and 
code folding. It includes :doc:`line tags<rvD02-linetags>`, 
:doc:`block tags<rvD03-blocktags>` and  :doc:`commands<rvD04-commands>` 
along with  text.

.. code-block:: python

    rv._("""Section Label  

        Content text indented 4 spaces.
        ...
        
        """)

Content is converted line by line into formatted text and `RestructuredText
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_, and then
further processed into HTML or PDF. If a line does not contain a *command* or
*tag* it is passed through as is, which allows for the *Insert* function (rv.I) 
including some *restructured text* directly i.e. 
surrounding words with * or ** will format a word as italic or bold respectively.

In addition block tags in the *Tools function* (rv.T) directly supports
processing HTML, LaTeX and reStructuredText scripts.

-------------------------------------------------

.. _markup:

**[3]** Tags and Commands
----------------------------


:doc:`Line Tags <rvD02-linetags>`

    A :term:`line tag` formats a line of text and is denoted with a single
    **_[LETTER]**, placed at or near the end of the line, depending on the tag.

:doc:`Block Tags <rvD03-blocktags>`

    A :term:`block tag` formats a block of text and begins with
    **_[[TAGNAME]]** and terminates with **_[[END]]**.

:doc:`Commands <rvD04-commands>`

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
    
    A rivt folder can contain any set of files and folders but the following
    structure is required for <i>doc</i> processing. Files and folders are
    organized under a root folder with the prefix <i>rivt-</i> e.g.
    <i>rivt-Report-Label</i>. <br> <br>
    
    <i>rivt folders</i> (root folders) include at least the <i>rivt files</i> 
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

    rvD02-linetags.rst
    rvD03-blocktags.rst
    rvD04-commands.rst    
    rvD05-apimarkup.rst
    