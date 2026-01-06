**C.3 Block Tags**
========================

**[1t]** Block Tag Summary
-------------------------------------

.. raw:: html

    <hr>


**Format blocks of text**

========== ========================================= ===============================
API Scope         Block Tags                           Description 
========== ========================================= ===============================
rv.R        _[[SHELL]] process parameters              :ref:`Shell script`
rv.I        _[[INDENT]] spaces (4 default)             :ref:`Indent text block`
rv.I        _[[ITALIC]] spaces (4 default)             :ref:`Indent italic block`
rv.I        _[[ENDNOTES]] optional label               :ref:`Endnotes block`
rv.I        _[[TEXT]] optional language                :ref:`Text block`
rv.I        _[[TOPIC]] topic                           :ref:`Topic block`
rv.I        _[[BOX]] label                             :ref:`Box block`
rv.V, T     _[[PYTHON]] namespace                      :ref:`Python block`
rv.T        _[[MARKUP]] type                           :ref:`Markup block`
rv.T        _[[METADATA]] label                        :ref:`Meta block`
rv.D        _[[LAYOUT]] label                          :ref:`Layout block` 
all         _[[END]]                                   :ref:`End block`
all         _[[NEW PAGE]]                              :ref:`Start new page`
========== ========================================= ===============================

.. _Shell script:

**[2t]** Shell script
------------------------------------

.. raw:: html

    <hr>

Runs shell scripts that run external programs. The shell parameters include
specifying the operating system, process control and terminal window control.
The os parameter specifies the terminal type. The wait parameter specifies
whether rivt file processing waits for the script to complete before
continuing. The open parameter specifies whether to keep the shell window open
after execution.

.. topic::  _[[SHELL]] process parameters



    .. code-block:: bash
        
        Syntax:
            _[[SHELL]] win;mac;linux,wait;nowait,open;close
            shell command
            ...
            _[[END]]
    
        
        Example:
            _[[SHELL]] win,nowait,open
            dir
            path
            _[[END]]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================


.. _Indent text block:

**[3t]** Indent text block
----------------------------------------------

.. raw:: html

    <hr>

Indents text block the specified number of spaces.

.. topic::  _[[INDENT]] spaces

    .. code-block:: bash

            Syntax:
                _[[INDENT]] number of spaces
                text
                text
                ...
                _[[END]]

            Example:
                _[[INDENT]] 8
                This is a sentence that will be 
                indented 8 spaces.
                _[[END]]



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

    Italicizes and indents the text block the specified number of spaces.

    .. code-block:: bash

            Syntax:
                _[[ITALIC]] number of spaces
                text
                ...
                _[[END]]

            Example:
                _[[ITALIC]] 4
                This is a sentence that will be 
                italicized and indented 4 spaces.
                _[[END]]



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

    Assigns numbers and formats endnotes in order of processing. Each endnote is
    separated by a blank line and is numbered in order of occurrence.
    
    .. code-block:: bash

            Syntax:
                _[[ENDNOTE]] label
                Endnote 1.

                Endnote 2. 
                ...
                _[[END]]    
    
            Example:
                _[[ENDNOTE]] ACI citations
                This endnote is assigned to the first endnote tag (_[#]) in order of
                of processing.

                This second endnote is separated by a blank line and assigned
                to the second

                This is a third endnote.
                _[[END]] 



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

    Reads and formats text and code. The language parameter
    specifies formatting and syntax coloring.  Languages include:

    - *literal*
    - *python*
    - *bash*
    - *sh*
    - *cmd*

    .. code-block:: bash

            Syntax:
                _[[TEXT]] language
                text and code
                ...
                _[[END]]  
        
            Example:
                _[[TEXT]] python
                # some code
                print(1)
                a = 1 + 3
                _[[END]]


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

    Formats a topic block.

    .. code-block:: bash

            Syntax:    
                _[[TOPIC]] topic title
                text
                ...
                _[[END]]

            Example:    
                _[[TOPIC]] topic title
                Text related to the topic.
                _[[END]]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Box block:

**[8t]** Box block
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[BOX]] label

    Draws a box around the block of text.

    .. code-block:: bash

            Syntax:    
                _[[BOX]] optional label
                text
                ...
                _[[END]]

            Example:    
                _[[BOX]] 
                This is a sentence.
                A second sentence.
                A box is drawn around the sentences.
                _[[END]]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Python block:

**[9t]** Python block
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[PYTHON]] topic title

    Executes Python script in the *rivt namespace* or a user specified namespace.
    File paths in the script are relative to the *rivt file* folder.

    .. code-block:: python

            Syntax:    
                _[[TOPIC]] topic title
                text
                _[[END]]

            Example:    
                _[[PYTHON]] *rvspace*; user namespace
                code
                code
                ...
                _[[END]]


=========== ==========================
API Scope     Value, Tool
Doc Types     text, PDF, HTML
=========== ==========================

.. _Markup block:

**[10t]** Markup block
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


.. _Meta block:

**[11t]** Metadata
-------------------

.. raw:: html

    <hr>
.. topic:: _[[METADATA]] label
    
   Some text. **_[#]**  Some more text.

..  code-block:: bash

    # defaults
    _[[METADATA]] meta
    authors: 
    version: 0.0.0
    email:
    repo:
    license: https://opensource.org/license/mit
    fork1: author, version, email, repo
    fork2: author, version, email, repo
    _[[END]]

    # example - author dicitionary
    _[[METADATA]] authors
    authors: rholland, rward
    version: 0.1.1
    email: rholland@email.com
    repo: https://github.com/rivt-info/rivt-simple-doc
    license: https://opensource.org/license/mit
    fork1: author, version, email, repo
    fork1: author, version, email, repo
    _[[END]]

*Metadata* is written to the *api-log.py* file and is converted internally to
Python dictionaries with a name taken from the label e.g. *rvmeta_D* or 
*rvmeta_authorsD*/

=========== ==========================
API Scope     Tools
Doc Types     text, PDF, HTML
=========== ==========================



.. _Layout block:

**[12t]** Layout block
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

.. _End block:

**[13t]** End block
------------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[[END]] optional label
    
    Terminates a block tag.

.. code-block:: text
        
    _[[END]] 


=========== ==========================
API Scope     All
Doc Types     text, PDF, HTML
=========== ==========================

.. _Start new page:

**[14t]** Start new page
------------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[[NEWPAGE]] optional label
    
    Starts new page.

.. code-block:: text
        
    _[[NEWPAGE]] 


=========== ==========================
API Scope     All
Doc Types     text, PDF, HTML
=========== ==========================