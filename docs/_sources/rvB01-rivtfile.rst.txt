**B.1 |** R-I-V-T
=================================  

.. _rivt-summary:

**[1]** Summary
-------------------------------------------------------------------------------- 

*rivt* uses a wide variety of source materials when publishing *docs*. They
include external programs, images, functions, equations, data files and Python
scripts. To assemble a *doc* it uses four primary API functions:

.. raw:: html

    <p style="border-width:2px; border-style:solid; border-color:#49b2c3;padding: 1em;">

    <b>R():</b> Processes internal scripts and block text, e.g. Python, LaTeX, rst <br>

    <b>I():</b> Inserts static sources e.g. images, text, and PDF files <br>

    <b>V():</b> Imports data and calculates values from equations and functions <br>

    <b>T(): </b> Runs external binary programs <br>

A fourth **rv.D API**  for publishing the *doc* is documented 
:ref:`here <rivt-publish>`. Examples of a *rivt file* with text, PDF and 
HTML *docs* are here:

- :ref:`a rivt file <example-file>` 
- :ref:`a text doc <text-doc>`
- :ref:`a PDF doc <pdf-doc>`
- :ref:`a HTML doc <html-doc>`

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

There are several comment settings that apply to the entire rivt file. They
are specified in the *comment settings* immediately following the import
statement. Default settings shown in parentheses and do not need to be specified.


.. code-block:: python

    import rivtlib.rvapi as rv

    # rv pub_folder = true, false; create _rvpublic folder in project root (false)
    # rv toggle_pub = true, false; toggles default section setting from private to public (false)
    # rv set_width = 80; character width of text output (80)
    # rv no_tag = true; false ; the API type symbol is added to section number (false)


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

Individual *API methods* define sections.  Each :doc:`API function <rvB01-rivtfile>` 
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
need to be overriden. *The rv.D API* header does not have modification settings.

**Section Headers**

.. code-block:: python

    rv._("""Section Label 

        Default header for Insert and Values sections.
        Content text and rivt markup, indented four spaces.
        
        """)

    rv._("""Section Label | shmpn 

        Header with modifications for Insert and Values sections.
        Content text and rivt markup, indented four spaces.
        
        """)

The first parameter list in the *header substring* specifies handling of the
*content substring*. The second and third parameters, where applicable, specify 
a type and file that is processed by the API method before processing 
any *content*.

**Parameters**

Section parameters may be specified in any order or ommitted if defaults are
acceptable. 

- s | store - stores the section content in *_rvstored/sect* as a *.rvt file.*
- h | hide - processes the section but suppresses the *doc* output.
- m | merge - merges the section with the previous section.
- n | new page - Starts a new pdf page.
- p | public - toggles the default public/private status of the section 

Note that the default publication status for a *doc* is private. The default
setting can be switched to public using a 
:ref:`comment setting <rivt-settings>`. The *p* parameter toggles the 
setting from whichever default is currently in effect.

The default parameters, when ommitted, are as follows:

- section is not stored
- section content is published
- section not merged
- section is private
- pages are continuous 

Note: that section breaks at the *doc* level are specified in the 
:ref:`METADATA block <publish-settings>`. 

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


.. _rivt-tips:

**[6]** Tips 
---------------------------------

Where interactive IDEs are used **rv.S** and **rv.X** can be used for
debugging. Cell notation can be used for the navigation panels generated
rivtStudio. Note that Ctrl+Alt+C inserts a cell label (# %%) followed by the
section title if the cursor is on the first line of the section.

.. toctree::
    :maxdepth: 2
    :hidden:

    rvB02-markup.rst
    rvB03-linetags.rst
    rvB04-blocktags.rst
    rvB05-assigntags.rst    
    rvB06-commands.rst    





