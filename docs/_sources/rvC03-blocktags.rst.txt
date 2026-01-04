**C.3 Block Tags**
========================

**[1t]** Block Tag Summary
-------------------------------------

.. raw:: html

    <hr>


**Format blocks of text**

========== ========================================= =======================================
API Scope         Block Tags                           Description 
========== ========================================= =======================================
rv.R        _[[SHELL]] os,wait,open                    :ref:`Shell scripts`
rv.I        _[[INDENT]] spaces (4 default)             :ref:`Indent text block`
rv.I        _[[ITALIC]] spaces (4 default)             :ref:`Indent italic block`
rv.I        _[[ENDNOTES]] optional label               :ref:`Endnotes block`
rv.I        _[[TEXT]] optional language                :ref:`Text block`
rv.I        _[[TOPIC]] topic                           :ref:`Topic block`
rv.T, V     _[[PYTHON]] namespace                      :ref:`Python block`
rv.T        _[[MARKUP]] type                           :ref:`Markup block`
rv.D        _[[META]] label                            :ref:`Meta block`
rv.D        _[[LAYOUT]] label                          :ref:`Layout block` 
all         _[[END]]                                   :ref:`End block`
========== ========================================= =======================================

.. _Shell scripts:

**[2t]** Shell scripts
------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
    Syntax:
    _[[SHELL]] *win;mac;linux,wait;nowait,open;close*
    shell command
    shell command
    ...
    _[[END]]
  
    Example:
    _[[SHELL]] win,nowait,open
    dir
    _[[END]]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

The shell command runs shell scripts and is used for external program
processing. The os parameter specifies the terminal type. The wait parameter
specifies whether rivt file processing waits for the script to complete before
continuing. The open parameter specifies whether to keep the shell window open
after execution.

.. _Indent text block:

**[3t]** Indent text block
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[INDENT]] spaces

    ::

        _[[INDENT]] 4
        text
        text
        ...
        _[[END]]

Indents block text four spaces.

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Indent italic block:

**[4t]** Indent italic block
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[ITALIC]] spaces

    ::
        
        _[[ITALIC]] 4
        text
        text
        ...
        _[[END]]

Indents the specified number spaces and italicizes block.

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Endnotes block:

**[5t]** Endnotes block
-------------------------------------------    

.. raw:: html

    <hr>


.. topic:: _[[ENDNOTE]] label
    
    ::
   
        _[[NOTE]] aci endnotes
        this is an endnote - assigned to an endnote tag [#] in order of
        of processing.

        this is a second endnote separated by a blank line.
        ...
        _[[END]] 

Formats and numbers an endnote in order of processing. Each endnote is
separated by a blank line. They are numbered in order.

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Text block:

**[6t]** Text block
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TEXT]] language

    ::
        
        _[[TEXT]] python
        print("some text")
        b = 3 + 5
        ...
        _[[END]]

The TEXT command reads and formats text and code files. The language parameter
specifies formatting and syntax coloring.  Languages include:

    - *literal*
    - *python*
    - *bash*
    - *sh*
    - *cmd*

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Topic block:

**[7t]** Topic block
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TOPIC]] topic title

    ::
        
        _[[TOPIC]] topic title
        text
        text
        ...
        _[[END]]

Formats a highlighted topic block.

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Python block:

**[8t]** Python block
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
     
      _[[PYTHON]] *rvspace*; user namespace
      code
      code
      ...
      _[[END]]

Executes Python script in the *rivt namespace* or a user specified namespace.
File paths in the script are relative to the *rivt file* folder.

=========== ==========================
API Scope     Value, Tool
Doc Types     text, PDF, HTML
=========== ==========================

.. _Markup block:

**[9t]** Markup block
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[MARKUP]] *html;latex;rst*
     markup
     markup
     ...
     _[[END]]

Inserts HTML into an HTML *doc*, LaTeX into a PDF *doc*, and reStructuredText
into either PDF or HTML. 
 

=========== ==========================
API Scope     Tool
Doc Types     text, PDF, HTML
=========== ==========================

.. _Layout block:

**[10t]** Layout block
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LAYOUT]] optional label
    docnameS = ""
    pdfheaderL = []
    footerL = []    
    _[[END]]


Overrides default layout settings.

=========== ==========================
API Scope     Doc
Doc Types     text, PDF, HTML
=========== ==========================


.. _metablk:

**[11t]** Metadata
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


.. _endblk:


=========== ==========================
API Scope     Doc
Doc Types     text, PDF, HTML
=========== ==========================


**[12t]** End
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[END]] optional label

Terminates a block tag.

=========== ==========================
API Scope     All
Doc Types     text, PDF, HTML
=========== ==========================