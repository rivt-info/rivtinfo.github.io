**C.1 Markup**
==================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** rivt String
----------------------------------

.. raw:: html

    <hr>

:term:`rivt markup` is a readable, plain text language that generates
formatted text, PDF or HTML :term:`docs` from the same *rivt file*. The markup
is included in a *rivt string* - a utf-8 text string argument of a 
:doc:`API function<rvA01-intro>`.

The API function and header start in the first column (standard Python syntax),
with subsequent lines indented 4 spaces for improved readability and section
folding in IDEs.

.. code-block:: python

    rv._("""Section Label | print;hide, private;public, section;merge

        section text (utf-8 text)
        ...
        ...
        
        """)

The :term:`rivt string` begins with a *section header* that includes a "section
label" and parameters that define the section behavior. 

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** API Header 
------------------

.. raw:: html

    <hr>

An :term:`API header` starts with a *section label* followed by a vertical
separator bar and comma separtaed *section parameters* that may override the
default behavior. The *section label* is the section title. *Header*
paramaters include the following:

- private/public : determines whether the API markup is copied to the
    *rivt file* in the */public* folder intended for sharing. 

- show/hide : determines whether the API markup is formatted and shown 
    in the output doc.

- section/merge : determines whether the API markup starts a new section
    in the output doc or is merged into the previous section.   


Default settings do not need to be specified in the *header*. In the table
below, the default setting for each API is listed first in bold.
 
========== ===================== ================= =====================
API          private/public        show/hide           section/merge         
========== ===================== ================= ===================== 
rv.M        **private**; public   **hide**; show     **merge**; section
rv.R        **private**; public   **hide**; show     **merge**; section
rv.I        **private**; public   **show**; hide     **section**; merge   
rv.V        **private**; public   **show**; hide     **section**; merge    
rv.T        **private**; public   **hide**; show     **merge**; section
rv.D        **private**; public   **hide**; show     **merge**; section
rv.S        **private**; public   **hide**; show     **merge**; section
rv.Q        **private**; public   **hide**; show     **merge**; section
========== ===================== ================= ===================== 


Examples of *header* settings are shown below.

.. code-block:: python

    rv.I("""A New Section | private, show, section

        section content (utf-8 text)
        ...
        ...
        
        """)

As defaults are specified in the prior example, the following syntax is
equivalent:

.. code-block:: python

    rv.I("""A New Section

        section content (utf-8 text)
        ...
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
