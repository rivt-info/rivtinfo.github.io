**C.1 Markup**
==================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** rivt String
----------------------------------

.. raw:: html

    <hr>

*rivt markup* provides a readable, plain text language that generates formatted
text, PDF or HTML *docs* from the same *rivt file*. The markup is processed in
a *rivt string* - a utf-8 text string argument to a *rivtlib* 
:doc:`API function</dv-A-intro/rv-A01-intro>`.

The API function and header start in the first column (standard Python syntax),
with subsequent lines indented 4 spaces for improved readability and section
folding in IDEs.

.. code-block:: python

    rv._("""Section Label | hide;print, public;private; (rvsource, rvlocal)

        section content (utf-8 text)
        ...
        ...
        
        """)

The *rivt string* begins with a *section header* that includes a "section
label" and parameters that define the section behavior. 

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Header 
------------------

.. raw:: html

    <hr>

A header starts with a *section label* followed by a vertical separator bar and
*parameters* that override the section write behavior. 

.. code-block:: python

    rv._("""Section Label | hide;print, public;private; (rvsource, rvlocal)

        section content (utf-8 text)
        ...
        ...
        
        """)

The *section label* is the section title. If the *section label* is preceeded
by two dashes (*--section label*) the section output is merged with the prior
section, instead of starting a new one. Sections are numbered, bookmarked and
linked when output to *doc*. The write *parameters* specify:

- whether the section output is written to the *doc* 
- whether the API with its *rivt string* is written to a *public rivt file* 
- where the *value file* is exported (for *rv.V* only)

They only need to be specified when different from defaults.

============= ==============================
API function    default write parameters       
============= ==============================
rv.R             nowrite, private
rv.I             write, private
rv.V             write, private, rvsource
rv.T             nowrite, private
rv.D             nowrite, private
rv.M             nowrite, private
rv.S             nowrite, private
rv.Q             nowrite, private
============= ==============================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[3]** Section Content 
--------------------------

.. raw:: html

    <hr>

Section content is indented four spaces (for legibility and code folding) and
includes *tags* for text formatting and *commands* for file operations.

.. code-block:: python

    rv._("""Section Label | write; nowrite, public; private

        section content
        ...
        
        """)


A section is processed, line by line, to a
`RestructuredText string <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_,
and then further processed to an HTML or PDF file. If a line does not 
contain a *command* or *tag* it is passed through as is. This allows for 
including *restructured text* directly, e.g. surrounding text with * for italics 
or ** for bold. *Text docs* are formatted separately.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Tags and Commands
----------------------------

.. raw:: html

    <hr>

:doc:`Tags </dv-C-markup/rv-C08-quick>`

*Line tags* format a line of text and are denoted with **_[TAG]**, usually at
the end of the line.

*Block tags* format a block of text that begin with **_[[TAG]]**
on the first line and end with **_[[Q]]** after the last line. 

:doc:`Commands </dv-C-markup/rv-C08-quick>`

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the command name and parameters. The exceptions to this pattern are the
assignment (**<=** ) and definition (**:=**) commands, which are used to assign
values to equation results and define variables.


.. toctree::
    :maxdepth: 1
    :hidden:

    rv-C02-markup-m.rst
    rv-C03-markup-r.rst
    rv-C04-markup-i.rst
    rv-C05-markup-v.rst
    rv-C06-markup-t.rst
    rv-C07-markup-d.rst
    rv-C08-quick.rst
    rv-C09-example1.rst
