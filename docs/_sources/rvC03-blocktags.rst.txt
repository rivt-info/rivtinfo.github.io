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
rv.R        _[[SHELL]] os,wait,open                    :ref:`shellblk`
rv.I        _[[INDENT]] spaces (4 default)             :ref:`indentblk`
rv.I        _[[ITALIC]] spaces (4 default)             :ref:`italicbllk`
rv.I        _[[NOTES]] optional label                  :ref:`notesblk`
rv.I        _[[TEXT]] optional language                :ref:`codeblk`
rv.I        _[[TOPIC]] topic                           :ref:`topicblk`
rv.T, V     _[[PYTHON]] namespace                      :ref:`pythonblk`
rv.T        _[[MARKUP]] type                           :ref:`markupblk`
rv.D        _[[META]] label                            :ref:`metablk`
rv.D        _[[LAYOUT]] label                          :ref:`layoutblk` 
all         _[[END]]                                   :ref:`endblk`
========== ========================================= ==============================

.. _shellblk:

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

API Scope: Run
Doc Types: text, PDF, HTML

The shell command runs shell scripts and is used for external program
processing. The os parameter specifies the terminal type. The wait parameter
specifies whether rivt file processing waits for the script to complete before
continuing. The open parameter specifies whether to keep the shell window open
after execution.

.. _indentblk:

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

API Scope: Insert, Values
Doc Types: text, PDF, HTML

.. _italicblk:

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

API Scope: Insert, Values
Doc Types: text, PDF, HTML

.. _notesblk:

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

API Scope: Insert, Values
Doc Types: text, PDF, HTML

.. _codeblk:

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

API Scope: Insert, Values
Doc Types: text, PDF, HTML

.. _topicblk:

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

API Scope: Insert, Values
Doc Types: text, PDF, HTML

.. _pythonblk:

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

API Scope: Value, Tool
Doc Types: text, PDF, HTML

.. _markupblk:

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
 

API Scope: Tool
Doc Types: PDF, HTML

.. _layoutblk:

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

API Scope: Doc
Doc Types: text, PDF, HTML


.. _metablk:

**[8t]** Metadata
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

**[11t]** End
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[END]] optional label

Terminates a block tag.

API Scope: Doc
Doc Types: text, PDF, HTML