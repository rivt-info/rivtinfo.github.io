**D.1 |** rivt Markup
======================

.. _API methods:

**[1]** API methods
--------------------------------------------------------------------- 

*rivt* has seven *API methods*. The name *rivt* is an acronym taken from 
four functions that process content. The remaining functions are used for
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
**rv.R** (rS)         Run            Run external binary programs
**rv.I** (rS)         Insert         Insert static sources 
**rv.V** (rS)         Values         Calculate values
**rv.T** (rS)         Tools          Process text scripts
**rv.D** (rS)         Doc            Publish docs 
**rv.S,X** (rS)     Skip, Exit       Skip section, exit (comments, debugging)
================ =============== ================================================

There are several settings that a apply to the entire rivt file. 
These are specified in the *comment settings* immediately following the
import statement. Default settings do not need to be specified - only variants. 


.. code-block:: python

    import rivtlib.rvapi as rv

    # rv private = false ; default section parameter changed to public (true)
    # rv no_tag = true ; API type is added to section number (true)
    # rv set_width = true character width of text output (80


If interactive IDEs are used **rv.S** and **rv.X** can be used for debugging
and cell notation can be used for navigation. Note that Ctrl+Alt+C inserts the
navigation cell label (# %%) if the cursor is on the first line of the cell and
the *rivt Profile* is installed in VSCode.


.. code-block:: python

    # %% My Section Label
    rv._(r"""My Section Label
    
            Content text and rivt markup - indented four spaces.
        
        ...
        
        """)

------------------------------------------------


.. _rivt-header:

**[2]** rivt string Header
----------------------------------

Individual *API methods* define sections.  Each :doc:`API function <rvA01-start>` 
takes a raw, triple quoted :term:`rivt string` composed of a 
:term:`header substring` on the first line followed by a multi-line 
:term:`content substring`. The *header line* defines section processing 
parameters. The *content substring* includes :term:`rivt markup` and is indented 
four spaces for improved readability and navigation (e.g. section folding). 
*rivt markup* commands and tags will vary depending on the API function.

The :term:`header substring` starts with a *section label*, also used as the
section title, followed by *section parameters* that override default behavior.
All parameters are optional and may be omitted if defaults are acceptable. If any
parameters are specified the vertical bars bracketing the file name are required.  

The *header substring* specifies the section title and other processing
parameters. The first set of parameters modify section processing. The
second parameter provides the option for a template file or script that
is processed in addition to the *content substring* if provided. 

The *API method header* has two general forms: *Default* and *Modified*. The
default form is used when the *header substring* accepts default parameters. It
only requires a section label. The modified form is used when default parameters
need to be modified.


**Header Defaults**

.. code-block:: python

    rv._(r"""Section Label 

         Content text and rivt markup - indented four spaces.
        
        ...
        
        """)


**Header Modifications**

.. code-block:: python

    rv._(r"""Section Label | shmpn | type | template or script file


         Content text and rivt markup - indented four spaces. 
         Content may be ommitted if a template file or script 
         is specified.
        
        ...
        
        """)


The first set of parameters in the *header substring* specify handling of the
*content substring*. The second and third parameters specify a type and file or
script that is processed by the API method before processing any *content*.

**Parameters**

Section parameters may be specified in any order or ommitted if defaults are
acceptable. The default parameters are shown in the

- s
  stores the section content in *_rvstored/sect* as a *.rvt file.*

- h
  processes the section but suppresses the *doc* output.
   
- m
  merges the section with the previous section.

- p 
  toggles the public/private status of the section. The rivt file default is
  private unless overridden by a :ref:`comment settings <comment-settings>`

- n 
  Starts a new pdf page.

**File and Type Settings**

The second parameter specifies a template file or script that is processed by
the API method before processing any *content*. The file is read from the
rvsrc/data folder unless a relative path is specified. The file type is
determined by the API method. The type setting for all
API methods, except rv.T, is *rvt*. A *rvt* file type is a section content
string stored as a file. It is written by the **s** parameter.

For the rv.T method the type settings are:

 #. **PYTHON** - run Python script
 #. **python** - insert Python script
 #. **text** - literal text
 #. **rst** - reStructuredText
 #. **html** - HTML markup
 #. **mermaid** - Mermaid diagram (requires mermaid installation)
 #. **latex** - LaTeX (requires LaTeX installation)

.. _rivt-content:

**[3]** rivt String Content
---------------------------------

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


------------------------------------


.. toctree::
    :maxdepth: 2
    :hidden:

    rvD02-apiscope.rst
    rvD03-linetags.rst
    rvD04-blocktags.rst
    rvD05-commands.rst    
    rvD06-assign.rst    

    