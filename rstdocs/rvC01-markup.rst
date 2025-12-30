**C.1 Markup**
==================

**[1t]** rivt String
----------------------------------

.. raw:: html

    <hr>

A :term:`rivt string` is a utf-8 text triple quoted string argument to an
:doc:`API function <rvA01-intro>`. It is composed of two parts - a header that
specifies section processing and content text. 

The first line of a *rivt string* is the header, followed by text 
indented 4 spaces for improved readability and section folding.
Content may include :term:`rivt markup`, a readable, plain text language
that generates formatted text, PDF or HTML :term:`docs` and other arbitrary text. 


.. code-block:: python

    rv._("""Section Label | include;store, private;public, section;merge

         Content text indented 4 spaces (utf-8 text)
        
        ...
        
        """)


**[2t]** API Header 
-------------------------

.. raw:: html

    <hr>

An :term:`API header` starts with a *section label* followed by comma separated
*section parameters* that may override default behavior. The *section label* is
the section title and is separated from the *section header* paramaters by a
vertical bar. Parameters include the following:

- private/public : determines whether the API section text is copied to the
    the */public* folder *rivt file* for sharing. 

- print/store : determines whether the *rivt string* is formatted and printed 
    in the doc or just annotated and written to a file for optional inclusion 
    as an appendix. eps

- section/merge : determines whether the API starts a new *doc* section
    or is merged into the previous section.   


Default settings do not need to be specified in the *header*. In the table
below, the default setting for each API is listed first (in bold).
 
========== ===================== ==================== =====================
API          private;public         include;store        section;merge         
========== ===================== ==================== ===================== 
rv.R        **private**;public     **store**;include     **merge**;section
rv.I        **private**;public     **include**;store     **section**;merge   
rv.V        **private**;public     **include**;store     **section**;merge    
rv.T        **private**;public     **store**;include     **merge**;section
rv.D        **private**;public     **store**             **merge**
rv.S        **private**;public     **store**;include     **merge**;section
rv.X        **private**            **store**             **merge**
========== ===================== ==================== ===================== 


Examples of *header* settings are shown below.

**An example with explicit defaults that do not have to be declared**

.. code-block:: python

    rv.I("""A New Section | private, include, section

        Content text
        ...
        
        """)
    
    # Equivalent to:

    rv.I("""A New Section | 

        Content text
  
        ...
        
        """)


**An example that merges a section to the previous section**

.. code-block:: python

    rv.I("""A Merged Section | merge

        Content text

        ...
        
        """)

**[3t]** Content Text 
--------------------------

.. raw:: html

    <hr>

:term:`Content text` is indented four spaces for legibility and code folding.
It arbitrary text along with :doc:`line tags<rvC02-linetags>`, 
:doc:`block tags<rvC03-blocktags>` and 
:doc:`commands<rvC04-commands>`.

.. code-block:: python

    rv._("""Section Label | 

        Content text indented 4 spaces (utf-8).
        ...
        
        """)


A section is processed line by line into formatted text and `RestructuredText
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_, and then
further processed to an HTML or PDF file. If a line does not contain a
*command* or *tag* it is passed through as is, which allows for including some
*restructured text* directly. For example surrounding words with * for italics
or ** for bold. 

In addition the *Tools API function* (rv.T) supports inserting raw Python,
HTML and LaTex. Since it can be hid from the primary textual
content of the file rv.T() improves readability.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4t]** Tags and Commands
----------------------------

:doc:`Line Tags <rvC04-commands>`

A :term:`line tag` formats a line of text and is denoted with **_[LETTER]**,
generally placed at the end of the line for readability.

:doc:`Block Tags <rvC04-commands>`

A :term:`block tag` formats a block of text and begins with **_[[TAGNAME]]**
and terminates with **_[[END]]**. 

:doc:`Commands <rvC04-commands>`

*rivt commands* read and write external files. They typically start in the
first column with a vertical bar ( | ) followed by the file path, name and
parameters. The exceptions to this pattern are the assignment (**<=** ) and
definition (**:=**) commands, which are used to assign values to equation
results and define variables.

.. code-block:: bash  
    
    | COMMAND | relative path | parameters

File paths are specified relative to the *report folder* or *rivt file* folder.  
The  typical *rivt report* folder structure is described 
:doc:`here. <rvD03-folders>`

**[5t]** Markup Key
----------------------------------

.. raw:: html

    <hr>

Tag and Command syntax for each API type is defined and described using the
following format.


_[TAG] : description of :term:`line tag` 


.. topic::  syntax : description

   example

outputs: types of output


.. raw:: html

    <hr>


_[[TAG]] :  description of :term:`block tag`
        

.. topic::  syntax : description

  example

file types

.. raw:: html

    <hr>

| COMMAND |  description of :term:`command`

.. topic:: | COMMAND | relative path | parameters

  example

file types

.. raw:: html

    <hr>

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[6t]** Metadata
-------------------

.. raw:: html

    <hr>

*Metadata* is written to the *api-log.py* file. Metadata is specified using
standard Python data types. 

*rv_authD* is a dictionary that specifies the author, version, email, repository
and license information and forks. 

..  code-block:: python

    # default - author dictionary
    rv_authD = {
            "authors": "",
            "version": "0.0.0",
            "email": "",
            "repo": "",
            "license": "https://opensource.org/license/mit/",
            "fork1": ["author", "version", "email", "repo"],
            "fork2": ["author", "version", "email", "repo"],
            }

    # example - author dicitionary
    rv_authD = {
            "authors": "rholland",
            "version": "0.6.1",
            "email": "rod.h.holland@gmail.com",
            "repo": "https://github.com/rivt-info/rivt-simple-doc",
            "license": "https://opensource.org/license/mit/",
            }

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
    rvC10-api-summary.rst

