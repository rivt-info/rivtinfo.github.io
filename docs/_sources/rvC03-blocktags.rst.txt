**C.3 Block Tags**
========================

**[1t]** Block Tag Summary
-------------------------------------

.. raw:: html

    <hr>


**Format blocks of text**

========== ========================================= ==============================
API Scope         Block Tags                           Description 
========== ========================================= ==============================
rv.R        _[[SHELL]] os,wait,open                    :ref:`shelltag`
rv.I, V     _[[INDENT]] spaces (4 default)             :ref:`indenttag`
rv.I, V     _[[ITALIC]] spaces (4 default)             :ref:`italictag`
rv.I, V     _[[NOTES]] optional label                  :ref:`notestag`
rv.I, V     _[[TEXT]] optional language                :ref:`codetag`
rv.I, V     _[[TOPIC]] topic                           :ref:`topictag`
rv.T        _[[PYTHON]] namespace                      :ref:`pythontag`
rv.T        _[[SCRIPT]] type                           :ref:`scripttag` [1]
rv.D        _[[LAYOUT]] label                          :ref:`layouttag` 
all         _[[END]]                                   :ref:`endblk`
========== ========================================= ==============================

::

    [1] LaTeX processing requires the installation of Texlive

.. _shelltag:

**[2t]** shell commands
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

API: Run
docs: text, PDF, HTML

The shell command runs shell scripts and is used for external program
processing. The os parameter specifies the terminal type. The wait parameter
specifies whether rivt file processing waits for the script to complete before
continuing. The open parameter specifies whether to keep the shell window open
after execution.

.. _indenttag:

**[3t]** indent text
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

API: Insert, Values
docs: text, PDF, HTML

.. _italictag:

**[4t]** indent italic text
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

API: Insert, Values
docs: text, PDF, HTML

.. _notestag:

**[5t]** endnote text
-------------------------------------------    

.. raw:: html

    <hr>


.. topic:: _[[NOTE]]  reference label
    
    ::
   
        _[[NOTE]] aci endnotes
        this is an endnote - assigned to an endnote tag [#] in order of
        of processing.

        this is a second endnote separated by a blank line.
        ...
        _[[END]] 

Formats and numbers an endnote in order of processing.

API: Insert, Values
docs: text, PDF, HTML

.. _codetag:

**[6t]** literal text or code
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

API: Insert, Values
docs: text, PDF, HTML

.. _topictag:

**[7t]** topic
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

API: Insert, Values
docs: text, PDF, HTML

.. _pythontag:

**[8t]** Python code
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

API: Value, Tool
docs: text, PDF, HTML

.. _scripttag:

**[9t]** markup scripts
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[SCRIPT]] *html;latex;rst*
     markup
     markup
     ...
     _[[END]]

Inserts HTML into an HTML *doc*, LaTeX into a PDF *doc*, and reStructuredText
into either PDF or HTML. 
 

API: Tool
docs: PDF, HTML

.. _layouttag:

**[10t]** Layout 
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

API: Doc
docs: text, PDF, HTML

.. _endblk:

**[11t]** End
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[END]] optional label

Terminates a block tag.

API: Doc
docs: text, PDF, HTML