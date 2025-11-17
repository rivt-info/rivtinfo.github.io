**C.1 Markup**
==================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** rivt String
----------------------------------

.. raw:: html

    <hr>

A :term:`rivt string`  is a utf-8 text triple quoted string argument to an 
:doc:`API function <rvA01-intro>`. It may include :term:`rivt markup`, 
a readable, plain text language that generates formatted text, PDF or 
HTML :term:`docs`. The different *doc* types are generated from the 
same *rivt file*. 

The first line of a *rivt string* is a header, followed by lines that are
indented 4 spaces for improved readability and section folding.

.. code-block:: python

    rv._("""Section Label | print;noprint, private;public, section;merge

        section text (utf-8 text)
        
        ...
        
        """)

The *rivt string* begins with an *API header* that includes a "section
label" and section formatting parameters.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** API Header 
-------------------------

.. raw:: html

    <hr>

An :term:`API header` starts with a *section label* followed by a vertical
separator bar and comma separtaed *section parameters* that may override the
default behavior. The *section label* is the section title. *Header*
paramaters include the following:

- private/public : determines whether the API markup is copied to the
    *rivt file* in the */public* folder intended for sharing. 

- print/noprint : determines whether the *rivt string* is formatted and printn 
    in the doc or just annotated. 

- section/merge : determines whether the API starts a new *doc* section
    or is merged into the previous section.   


Default settings do not need to be specified in the *header*. In the table
below, the default setting for each API is listed first in bold.
 
========== ===================== ==================== =====================
API          private/public        print/noprint           section/merge         
========== ===================== ==================== ===================== 
rv.M        **private**; public   **noprint**; print   **merge**; section
rv.R        **private**; public   **noprint**; print   **merge**; section
rv.I        **private**; public   **print**; noprint   **section**; merge   
rv.V        **private**; public   **print**; noprint   **section**; merge    
rv.T        **private**; public   **noprint**; print   **merge**; section
rv.D        **private**; public   **noprint**; print   **merge**; section
rv.S        **private**; public   **noprint**; print   **merge**; section
rv.Q        **private**; public   **noprint**; print   **merge**; section
========== ===================== ==================== ===================== 


Examples of *header* settings are shown below.

.. code-block:: python

    rv.I("""A New Section | private, print, section

        section content (utf-8 text)
  
        ...
        
        """)

As defaults are specified in the prior example, the following syntax is
equivalent:

.. code-block:: python

    rv.I("""A New Section

        section content (utf-8 text)

        ...
        
        """)


.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[3]** Section Text 
--------------------------

.. raw:: html

    <hr>

Section text is indented four spaces for legibility and code folding. It 
includes *rivt tags* for text formatting and *rivt commands* for file operations.

.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section text
        ...
        
        """)


A section is processed line by line to formatted text and a
`RestructuredText string <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_,
and then further processed to an HTML or PDF file. If a line does not 
contain a *command* or *tag* it is passed through as is, which allows for 
including *restructured text* directly. For example surrounding text 
with * for italics  or ** for bold. *Text docs* are formatted separately.

In addition the *Tools API function* (rv.T) supports inserting raw Python,
HTML, LaTex and resTructuredText that is isolated from the primary textual
content of the file which improves readability.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Tags and Commands
----------------------------

.. raw:: html

    <hr>

:doc:`Tags <rvC08-quick>`

A :term:`line tag` formats a line of text and is denoted with **_[TAG]**, usually 
at the end of the line.

A :term:`block tag` formats a block of text that begins with **_[[TAG]]**
and terminates with **_[[Q]]**. 

:doc:`Commands <rvC08-quick>`

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


.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[5]** Syntax Key
----------------------------------

.. raw:: html

    <hr>

_[TAG] : :term:`line tag` description


.. topic::  syntax : description

   example

outputs: types of output


.. raw:: html

    <hr>


_[[TAG]] : :term:`block tag` description
        

.. topic::  syntax : description

  example

file types

.. raw:: html

    <hr>

**[#]** | Command | : description


.. topic:: | COMMAND | relative path | parameters

  example

file types

.. raw:: html

    <hr>



.. toctree::
    :maxdepth: 1
    :hidden:

    rvC02-markup-m.rst
    rvC03-markup-r.rst
    rvC04-markup-i.rst
    rvC05-markup-v.rst
    rvC06-markup-t.rst
    rvC07-markup-d.rst
    rvC08-quick.rst
    rvC09-example1.rst
