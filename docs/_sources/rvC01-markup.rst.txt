**C.1 Markup**
==================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** rivt String
----------------------------------

.. raw:: html

    <hr>

:term:`rivt markup` provides a readable, plain text language that generates
formatted text, PDF or HTML :term:`docs` from the same *rivt file*. The markup
is processed in a *rivt string* - a utf-8 text string argument to a 
:doc:`API function<rvA01-intro>`.

The API function and header start in the first column (standard Python syntax),
with subsequent lines indented 4 spaces for improved readability and section
folding in IDEs.

.. code-block:: python

    rv._("""Section Label | hide;print, public;private; (rvsource, rvlocal)

        section content (utf-8 text)
        ...
        ...
        
        """)

The :term:`rivt string` begins with a *section header* that includes a "section
label" and parameters that define the section behavior. 

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Header 
------------------

.. raw:: html

    <hr>

A header starts with a *section label* followed by a vertical separator bar and
*section parameters* that override the section default behavior. The *section
label* is the section title.

.. code-block:: python

    rv._("""Section Label | hide;print, public;private;

        section content (utf-8 text)
        ...
        ...
        
        """)
 
*Section parameters* specify the following settings:

- *print*: formats :term:`section content` to *doc* 
- *public*: copies *section content* to *public rivt file* 
- *merge*: merges formatted *section content* to previous section
- *history*: writes *section label and parameters* to :term:`api-history` file

The table below summarizes the section parameter settings, with the default
setting shown first. A parameter only needs to be specified if different from
the default.

====== ============= ================= ================ ============== 
API         print        public            merge          history                         
====== ============= ================= ================ ============== 
rv.R   hide, print   private, public   section, merge    record, skip                 
rv.I   print, hide   private, public   section, merge    record, skip
rv.V   print, hide   private, public   section, merge    record, skip                                
rv.T   hide, print   private, public   section, merge    record, skip                 
rv.D   hide, print   private, public   section, merge    record, skip                 
rv.M   hide, print   private, public   section, merge    record, skip                 
rv.S   hide, print   private, public   section, merge    record, skip                 
rv.Q   hide, print   private, public   section, merge    record, skip                                                                                                                                                                                                                                    
====== ============= ================= ================ ============== 


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


A section is processed line by line to a
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

:doc:`Tags <rvC08-quick>`

A :term:`line tag` formats a line of text and is denoted with **_[TAG]**, usually 
at the end of the line.

A :term:`block tag` formats a block of text that begins with **_[[TAG]]**
and terminates with **_[[Q]]**. 

:doc:`Commands <rvC08-quick>`

*rivt commands* read and write external files and assign values to variables.
They typically start in the first column with a vertical bar ( | ) followed by
the file path, name and parameters. 

.. code-block:: bash  
    
    | COMMAND | relative path | filename | parameters

*Commands* specify the file location and processing parameters. Parameter
options are separated by commas. File paths are specified relative to the
report *source folder* or with the alias *rvlocal* to specify the local
directory. *rvlocal* is typically used for *single docs*. The standard *rivt
report* folder structure is described :doc:`here. <rvD02-folders>`

The exceptions to this pattern are the assignment (**<=** ) and definition
(**:=**) commands, which are used to assign values to equation results and
define variables.


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
