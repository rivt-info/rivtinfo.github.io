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

The first line of a *rivt string* is a header, followed by text 
indented 4 spaces for improved readability and section folding.

.. code-block:: python

    rv._("""Section Label | show;hide, private;public, section;merge

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

An :term:`API header` starts with a *section label* followed by comma separated
*section parameters* that may override default behavior. The *section label* is
the section title and is separated from the *section header* paramaters by a
vertical bar. Parameters include the following:

- private/public : determines whether the API section text is copied to the
    the */public* folder *rivt file* for sharing. 

- show/hide : determines whether the *rivt string* is formatted and printed 
    in the doc or just annotated and written to a file for optional inclusion 
    as an appendix. 

- section/merge : determines whether the API starts a new *doc* section
    or is merged into the previous section.   


Default settings do not need to be specified in the *header*. In the table
below, the default setting for each API is listed first in bold.
 
========== ===================== ==================== =====================
API          private/public         show/hide           section/merge         
========== ===================== ==================== ===================== 
rv.M        **private**; public   **hide**; show       **merge**; section
rv.R        **private**; public   **hide**; show       **merge**; section
rv.I        **private**; public   **show**; hide       **section**; merge   
rv.V        **private**; public   **show**; hide       **section**; merge    
rv.T        **private**; public   **hide**; show       **merge**; section
rv.D        **private**; public   **hide**; show       **merge**; section
rv.S        **private**; public   **hide**; show       **merge**; section
rv.Q        **private**; public   **hide**; show       **merge**; section
========== ===================== ==================== ===================== 


Examples of *header* settings are shown below.

.. code-block:: python

    rv.I("""A New Section | private, show, section

        section content (utf-8 text)
  
        ...
        
        """)

For the *Insert API* - rv.I(), the following syntax is equivalent:

.. code-block:: python

    rv.I("""A New Section

        section text (utf-8)

        ...
        
        """)


.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[3]** Section Text 
--------------------------

.. raw:: html

    <hr>

Section text is indented four spaces for legibility and code folding. It
includes *rivt tags* that format lines of text and *rivt commands* that operate
on files.

.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section text
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

**[4]** Tags and Commands
----------------------------

.. raw:: html

    <hr>

:doc:`Tags <rvC07-quick>`

A :term:`line tag` formats a line of text and is denoted with **_[TAG]**, usually 
at the end of the line.

A :term:`block tag` formats a block of text that begins with **_[[TAG]]**
and terminates with **_[[Q]]**. 

:doc:`Commands <rvC07-quick>`

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

**| COMMAND |** :term:`command` descripion


.. topic:: | COMMAND | relative path | parameters

  example

file types

.. raw:: html

    <hr>

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[6]** Metadata
----------------------------------

.. raw:: html

    <hr>

.. toctree::
    :maxdepth: 1
    :hidden:

    rvC02-markup-r.rst
    rvC03-markup-i.rst
    rvC04-markup-v.rst
    rvC05-markup-t.rst
    rvC06-markup-d.rst
    rvC07-quick.rst
    rvC08-example1.rst
