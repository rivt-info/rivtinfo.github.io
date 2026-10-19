**B.1 |** R-I-V-T
=================================  

.. _rivt-summary:

**[1]** Summary
-------------------------------------------------------------------------------- 

*rivt* is designed to publish engineering documents using a wide variety of
source materials including external programs, images, functions, equations,
data files and Python scripts. To assemble a *doc* it uses four primary API
functions:

.. raw:: html

    <p style="border-width:2px; border-style:solid; border-color:#49b2c3;padding: 1em;">

    <b>R():</b> Processes internal scripts and block text, e.g. Python, LaTeX, rst <br>

    <b>I():</b> Inserts static sources e.g. images, text, and PDF files <br>

    <b>V():</b> Imports data and calculates values from equations and functions <br>

    <b>T(): </b> Runs external binary programs <br>

A fourth API for publishing the doc is documented :ref:`here <rivt-docs>`:

.. raw:: html

    <b>D(): </b> Publishes documents <br>

Examples of a complete rivt file with text, PDF and HTML docs are here:

- :ref:`rivt file <example-file>` 
- :ref:`text doc <text-doc>`, 
- :ref:`PDF doc <pdf-doc>`
- :ref:`HTML doc <html-doc>`

------------------------------------------------

.. _rivt-api:

**[2]** API
------------------------------------------------------------------------------- 

The API is designed to be:

- lightweight
    :term:`rivt markup` wraps :term:`reStructuredText` and uses fewer than
    three dozen tags and commands. *rivt tags* format lines and blocks of text 
    and *commands* read and write files.

- extensible 
    *rivtlib* is written in Python with direct access to the large 
    library of Python packages and functions. Python scripts and external 
    programs can be integrated into a *rivt doc* throught the Run and Tools APIs.

- versatile 
    A *rivt file* produces a text, HTML or PDF *doc* from the same file. 
    Multiple *docs* can be organized into reports. *rivtbooks* provide a 
    convenient way to organize files around a subject matter for insertion into
    reports. *rivt* can be run within a variety of IDEs.

- efficient
    The file and folder organization is intuitive and it produces clear, organized 
    documents with default settings. Settings may be customized via *conf.py* 
    and *yaml* files. A *rivt doc* can be generated with a 
    single file or, using the same folder structure extendec to a large report
    involving  hundreds of files.

The API methods are listed in the table below, where (rS) is a triple quoted 
:term:`rivt string` argument.

================= =============== ========================================
API Function         Name             Purpose
================= =============== ========================================
**rv.R** (rS)        Run           Run Python scripts and markup
**rv.I** (rS)        Insert        Insert static sources 
**rv.V** (rS)        Values        Calculate values
**rv.T** (rS)        Tools         Execute shell scripts and programs
**rv.D** (rS)        Doc           Publish docs 
**rv.S; X** (rS)     Skip; Exit    Editing - Skip section or exit program 
================= =============== ========================================

An API function starts in the first column and takes a triple quoted
:term:`rivt string` argument containing a *header and content substring*.
The first line of the *rivt string* is the header substring, 
followed by a :term:`content substring` indented 4 spaces 
for readability and section folding. See :ref:`here <rivt-header>` for 
*rivt string* details.

The *rivt API* also provides scope for :ref:`rivt markup <rivt-markup>` 

---------------------------------------------------


.. _rivt-settings:

**[3]** File Settings
----------------------------------

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
    rv._("""My Section Label
    
            Content text and rivt markup - indented four spaces.
        ...
        
        """)

------------------------------------------------

.. _rivt-header:

**[4]** String Header
----------------------------------

Individual *API methods* define sections.  Each :doc:`API function <rvB01-rivt>` 
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

    rv._("""Section Label 

         Content text and rivt markup - indented four spaces.
        
        ...
        
        """)


**Header Modifications**

.. code-block:: python

    rv._("""Section Label | shmpn | type | template or script file


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

------------------------------------------------

.. _rivt-content:

**[5]** String Content
---------------------------------

The :term:`content substring` is indented four spaces for legibility and 
code folding. It includes :ref:`line tags <line summary>`, 
:doc:`block tags<rvB04-blocktags>` and  :ref:`commands <command-summary>` 
along with  text.

.. code-block:: python

    rv._("""Section Label  

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


.. toctree::
    :maxdepth: 2
    :hidden:

    rvB02-markup.rst
    rvB03-linetags.rst
    rvB04-blocktags.rst
    rvB05-assigntags.rst    
    rvB06-commands.rst    





