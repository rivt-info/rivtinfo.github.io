**D.3 Block Tags**
========================

**[1]** Block Tag Summary
-------------------------------------

**Run Format blocks of text or scripts**

========== ========================================= ===============================
API Scope         Block Tag                                Description 
========== ========================================= ===============================
rv.R        **_[[MARKUP]]** type                      :ref:`Markup block`
rv.R        **_[[PYTHON]]** label                     :ref:`Python block`
rv.I        **_[[BOX]]** label                        :ref:`Box block`
rv.I        **_[[TOPIC]]** topic                      :ref:`Topic block`
rv.V        **_[[TABLE]]** label                      :ref:`Table block`
rv.T        **_[[SHELL]]** os, *wait;nowait*          :ref:`Shell script`
rv.D        **_[[METADATA]]** label                   :ref:`Meta block` 
all         **_[[END]]**                              :ref:`End block`
========== ========================================= ===============================

.. _Shell script:

**[2]** Shell script
------------------------------------
Runs shell scripts that run external programs. The shell parameters include
specifying the operating system, process control and terminal window control.
The os parameter specifies the terminal type. The wait parameter specifies
whether rivt file processing waits for the script to complete before
continuing. The open parameter specifies whether to keep the shell window open
after execution.

.. topic:: _[[SHELL]] 

    .. code-block:: text
        
        Syntax:
            _[[SHELL]] win;mac;linux,wait; nowait,open; close
            shell command
            ...
            _[[END]]
    
        
        Example:
            _[[SHELL]] win,nowait,open
            dir
            path
            _[[END]]

=========== ==========================
API Scope     Tools
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------

.. _Endnotes block:

**[3]** Endnotes 
-------------------------------------------    

 

.. topic:: _[[ENDNOTES]] 

    Assigns numbers and formats endnotes in order of processing. Each endnote is
    separated by a blank line and is numbered in order of occurrence.
    
    .. code-block:: text

            Syntax:
                _[[ENDNOTES]] label
                Endnote 1.

                Endnote 2. 
                ...
                _[[END]]    
    
            Example:
                _[[ENDNOTES]] ACI citations
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

-----------------------------

.. _Table block:

**[4]** Table Block
------------------------------------------------

 

.. topic:: _[[TABLE]] 

    Reads and formats restructured text table and writes contents
    to csv file in the _stored/Vals folder.
    .. code-block:: text 

            Syntax:
                _[[TABLE]] label
                reST table
                ...
                _[[END]]  
        
            Example:
                _[[TABLE]] my_table
                =====  ======
                Name   Age
                =====  ======
                John   25
                Jane   30
                =====  =====
                _[[END]]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------

.. _Topic block:

**[5]** Topic 
------------------------------------------------

 

.. topic:: _[[TOPIC]] 

    Formats a topic block.

    .. code-block:: text

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

-----------------------

.. _Box block:

**[6]** Box 
------------------------------------------------

.. topic:: _[[BOX]] 

    Draws a box around the block of text.

    .. code-block:: text

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

-----------------------

.. _Python block:

**[7]** Python 
------------------------------------------------
.. topic:: _[[PYTHON]] 

    Executes Python script in the *rivt namespace* or a user specified namespace.
    File paths in the script are relative to the *rivt file* folder.

    .. code-block:: python

            Syntax:    
                _[[Python]] topic title
                code
                ...
                _[[END]]

            Example:    
                _[[PYTHON]] *rvspace*; user namespace
                b = 1*inch + 2.2*ft
                print(b)
                _[[END]]

=========== ==========================
API Scope     Value, Run
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------

.. _Markup block:

**[8]** Markup block
---------------------------------------

Inserts formatted text into doc. 

    - *literal*
    - *rst*
    - *html*
    - *endnote*
    - *center*
    - *bold*
    - *italic*
    - *latex* (texlive must be installed)


.. topic:: _[[MARKUP]] type
        
    .. code-block:: text
            
        Syntax:    
            _[[MARKUP]] 
            markup
            ...
            _[[END]]

        Example:    
            _[[MARKUP]] rst
            This is **bold** and 
            this is *italic* in 
            reStructuredtext
            ...
            _[[END]]

=========== ==========================
API Scope     Run
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------

.. _Meta block:

**[9]** Metadata
-------------------

 
.. topic:: _[[METADATA]]
    
    *Metadata* is written to the *rvAnn-apilog.py* file and is converted
    internally to a Python dictionary rvmetaD with key name taken from the
    label e.g. *docnameS* or *authorsD*.

    ..  code-block:: text

        Synatax - defaults:
            _[[METADATA]] optional label
            docname = ""
            authors = "" 
            version = 0.0.0
            email = ""
            repo = ""
            license = https://opensource.org/license/mit
            fork1 = author, version, email, repo
            fork2 = author, version, email, repo
            _[[END]]

        Example:
            _[[METADATA]]
            docname = Bearing Pressures 
            authors = rholland, rward
            version = 0.1.1
            email = rholland@email.com
            repo = https://github.com/rivt-info/rivt-simple-doc
            license = https://opensource.org/license/mit
            _[[END]]

=========== ==========================
API Scope     Docs
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------

.. _End block:

**[10]** End block
------------------------------------------------

 

.. topic:: _[[END]] 
    
    Terminates a block tag.

    .. code-block:: text

        Syntax:
            _[[NEWPAGE]] optional label 

        Example:    
            _[[END]] 


=========== ==========================
API Scope     All
Doc Types     text, PDF, HTML
=========== ==========================
