**C.1 Markup**
==================

.. _API functions:

**[1t]** API functions
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* has seven API functions. The name *rivt* is an acronym taken from the
four functions that process content. The remaining three functions are used for
document generation and debugging.

.. raw:: html

    <b>Content APIs</b>
    <ol style="border: 2px; 
            border-color: #49b2c3; 
            border-style: solid; 
            padding: 2em;
            margin: 2em">
        <li><b>[R]un</b> executes shell commands.</li>
        <li><b>[I]nsert</b> adds static table, image, equation and text content.</li>
        <li><b>[V]alues</b> evaluates equations and functions.</li>
        <li><b>[T]ools</b> runs reStructuredText, HTML, LaTeX and Python scripts.</li>
    </ol>

    <br>

    <b>Publish APIs</b>
    <ol style="border: 2px; 
            border-color: #49b2c3; 
            border-style: solid; 
            padding: 2em;
            margin: 2em">
        <li><b>Doc</b> specifies the <i>doc</i> type and style.</li>
        <li><b>Skip</b> can be used for interactive debugging and comments.</li>
        <li><b>Exit</b> can be used for interactive debugging.</li>
    </ol>

=============== =============== ===========================================
API Function         Name             Purpose
=============== =============== ===========================================
**rv.R** (rS)         Run            Run shell commands
**rv.I** (rS)         Insert         Insert static sources 
**rv.V** (rS)         Values         Calculate values
**rv.T** (rS)         Tools          Python and markup scripts
**rv.D** (rS)         Doc            Publish docs 
**rv.S** (rS)         Skip           Skip section (comments and debugging)
**rv.X** (rS)         Exit           Exit rivt (debugging)
=============== =============== ===========================================

API functions define doc sections. If interactive IDEs like *VSCode* or
*Spyder* are used to edit and run *rivt files*, functions can be processed
individually as cells by using the standard notebook hash notation:

.. code-block:: python

    # %% optional label
    rv.API_FUNCTION("""rivt string""")

.. _rivt string:

**[2t]** rivt string
----------------------------------

.. raw:: html

    <hr>

Each :doc:`API function <rvA01-start>` takes a triple quoted :term:`rivt string` 
argument composed of a line :term:`header substring` line followed 
by a multiple-line :term:`content substring`.

The *header substring* defines section processing parameters.
The *content substring* includes :term:`rivt markup` and is indented 
four spaces for improved readability and navigation (e.g. section folding).

.. _Header substring:

**Header substring**

.. raw:: html

    <hr>

The :term:`header substring` starts with a *section label* that is used as the
section title, followed by a vertical bar and three comma separated
*section parameters* that override default behavior.

.. code-block:: python

    rv._("""Section Label | doc;stored, private;public, section;merge

         Content substring indented 4 spaces
        
        ...
        
        """)

The parameters include the following, in any order:

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
 
========== ===================== ===================== =====================
API          private;public         doc;stored           section;merge         
========== ===================== ===================== ===================== 
rv.R        **private**;public     **stored**;doc       **merge**;section
rv.I        **private**;public     **doc**;stored       **section**;merge   
rv.V        **private**;public     **doc**;stored       **section**;merge    
rv.T        **private**;public     **stored**;doc       **merge**;section
rv.S        **private**;public     **stored**           **merge**
rv.D        **public**             **stored**           **merge**
rv.X         -                      -                   -
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

.. raw:: html

    <hr>

The :term:`content substring` is indented four spaces for legibility and 
code folding. It includes :doc:`line tags<rvC02-linetags>`, 
:doc:`block tags<rvC03-blocktags>` and  :doc:`commands<rvC04-commands>` 
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



**[3t]** Tags and Commands
----------------------------

.. raw:: html

    <hr>

:doc:`Line Tags <rvC02-linetags>`

    A :term:`line tag` formats a line of text and is denoted with a single
    **_[LETTER]**, placed at or near the end of the line, depending on the tag.

:doc:`Block Tags <rvC03-blocktags>`

    A :term:`block tag` formats a block of text and begins with
    **_[[TAGNAME]]** and terminates with **_[[END]]**.

:doc:`Commands <rvC04-commands>`

    *rivt commands* read and write external files. They typically start in the
    first column with a vertical bar ( | ) followed by the command name, file
    path, and parameters.

    The exceptions are the definition (**==:**), assignment (**<=:**), 
    function (**:=:**) and compare (**<>**) commands that are used to 
    define, assign and compare values.

    .. code-block:: bash  
        
        | COMMAND | relative path | parameters

    File paths are specified relative to the *rivt root folder*. The *rivt
    report* folder structure is described :doc:`here. <rvD03-folders>`.

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


**[4t]** Folders
---------------------------

.. raw:: html

    <hr>

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b> Folder Names</b> <br> 
    <br>
    A rivt report folder can contain any files and
    folders, but the following structure is required for doc processing. Files
    and folders are organized under a root folder with the prefix <i>rivt-</i>
    e.g. <i>rivt-Report-Label</i>. The root folder includes the <i>rivt
    files</i> and five subfolders.<br> 
    <br> 

    Required folders are capitalized or preceded by an underscore. Folders
    preceded by an underscore are rivt outputs. Folder names that include both
    output and author input begin with a capital letter and also include an
    underscore.<br>

For :term:`single docs` the folder structure is the same as a *report* folder
but simplified by omitting the *Src* and *_stored* folders. The files normally
stored there are stored in the root folder. The *report script* is not used for
single docs.

The top level folder structure is shown below. A more detailed description of
the folder structure is :doc:`here <rvD03-folders>`.

.. code-block:: bash

    [rivt-]Report-Label/                Report Folder
        ├── [rv101-]filename1.py        rivt file
        ├── [rv102-]filename2.py        rivt file
        ├── [rv201-]filename3.py        rivt file
        ├── [rv202-]filename4.py        rivt file 
        ...
        ├── [.vscode]/                  optional VSCode settings   
        ├── [_public]/                  public rivt files
        ├── [_publish]/                 published docs and reports
        ├── [_stored]/                  stored files
        ├── [Rst_docs]/                 restructured text files               
        ├── [Src]/                      source files        
        └── README.txt                  searchable text report 


.. toctree::
    :maxdepth: 1
    :hidden:

    rvC02-linetags.rst
    rvC03-blocktags.rst
    rvC04-commands.rst    
    rvC05-markup-r.rst
    rvC06-markup-i.rst
    rvC07-markup-v.rst
    rvC08-markup-t.rst
    rvC09-markup-d.rst
