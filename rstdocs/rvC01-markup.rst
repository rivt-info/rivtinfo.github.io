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

- print/store : determines whether the *rivt string* is formatted and printed 
    in the doc or just annotated and written to a file for optional inclusion 
    as an appendix. eps

- section/merge : determines whether the API starts a new *doc* section
    or is merged into the previous section.   


Default settings do not need to be specified in the *header*. In the table
below, the default setting for each API is listed first (in bold).
 
========== ===================== ==================== =====================
API          private;public         print;store           section;merge         
========== ===================== ==================== ===================== 
rv.R        **private**;public      **store**;print     **merge**;section
rv.I        **private**;public      **print**;store     **section**;merge   
rv.V        **private**;public      **print**;store     **section**;merge    
rv.T        **private**;public      **store**;print     **merge**;section
rv.D        **private**;public      **store**;print     **merge**;section
rv.S        **private**;public      **store**;print     **merge**;section
rv.X        **private**;public      **store**;print     **merge**;section
========== ===================== ==================== ===================== 


Examples of *header* settings are shown below.

.. code-block:: python

    rv.I("""A New Section | private, show, section

        Section text (utf-8 text)
  
        ...
        
        """)

For the *Insert API* - rv.I(), the following syntax is equivalent:

.. code-block:: python

    rv.I("""A New Section

        Section text (utf-8)

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

        Section text
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

A :term:`line tag` formats a line of text and is denoted with **_[LETTER]**,
generally placed at the end of the line for readability.

A :term:`block tag` formats a block of text and begins with **_[[TAGNAME]]**
and terminates with **_[[END]]**. 

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


**[5]** Markup Key
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

**[6]** Metadata
-------------------

.. raw:: html

    <hr>

*Metadata* is stored in the file *rivtmeta.py*. If used, it is imported prior
to *rivtlib* and provides author information and specifies whether the *rivt
file* is a single doc or part of report. Metadata is specified using standard
Python data types. See :doc:`here <rvC01-markup>` for further details.
    
=================== ==========================================================
    Variable                        Description
=================== ==========================================================
:term:`rv_authD`     specifies author information
:term:`rv_localB`    True; False [default] if True resource files are local
=================== ==========================================================

*rv_authD* is a dictionary that pecifies the author, version, email, repository
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

*rv_localB* overrides the default report structure and specifies that all
resource files are read from and written to the *rivt file* folder instead of
*rivt folders*. It is intended for simple, *single docs* with more limited
formatting options.

..  code-block:: python

     # default setting uses report folders
     rv_localB = false
     
     # resource files are read from and written to the rivt file folder
     rv_localB = true

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
