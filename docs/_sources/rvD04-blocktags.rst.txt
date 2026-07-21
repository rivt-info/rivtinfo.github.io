**D.3 |** Block Tags
========================

.. _block summary:

**[1]** Block Tag Summary
-------------------------------------

**Format or run blocks of text or scripts**

========== ========================================= ===============================
API Scope         Block Tag                                Description 
========== ========================================= ===============================
rv.R        **_[[WRITE]]** var name                   :ref:`Write block`
rv.R        **_[[SHELL]]** os, *wait;nowait*          :ref:`Shell script`
rv.I,V      **_[[TABLE]]** label                      :ref:`Table block`
rv.I,V      **_[[ENDNOTES]]**                         :ref:`Endnotes block`
rv.V        **_[[ARGS]]** arg dict name               :ref:`Arg block`
rv.D        **_[[METADATA]]** label                   :ref:`Meta block` 
all         **_[[END]]**                              :ref:`End block`
========== ========================================= ===============================


.. _Endnotes block:

**[2]** Endnotes Block
------------------------------------------------

.. topic:: _[[ENDNOTES]] 

    Inserts endnotes at end of document. One block is used per document. 
    
    .. code-block:: text 

            Syntax:
                _[[ENDNOTES]] 
                endnote 1

                endnote 2

                endnote 3
                ...
                _[[END]]  
        
            Example:
                _[[ENDNOTES]] 
                Timoshenko, Stephen P. (1983). History of strength of
                materials: with a brief account of the history of theory of
                elasticity and theory of structures. Dover Books on Physics.
                Dover Publications.

                Truesdell, C. (1960). The rational mechanics of flexible or
                elastic bodies 1638–1788. Venditioni Exponunt Orell Fussli
                Turici.
                _[[END]]

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------


.. _Table block:

**[3]** Table Block
------------------------------------------------

 

.. topic:: _[[TABLE]] 

    Reads and formats restructured text table and writes contents
    to csv file in the _rvstor/data folder.
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
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------

.. _Arg block:

**[4]** Argument block
---------------------------------------

.. topic:: _[[ARG]] arg_name
        
    Organizes function arguments into a dictionary that may be passed
    to the FUNCTION command.

    .. code-block:: text
            
        Syntax:    
            _[[ARGS]] arg_dictionary_name | list of units
            arg1 = A # label
            arg2 = B # label
            ...
            _[[END]]

        Example:    
            _[[ARGS]] beam1 | units: inch, pounds
            ln_1 = 10*12 # beam length
            P_1 = 1.1*1000 # beam load
            ...
            _[[END]]

=========== ==========================
API Scope     Values
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------


.. _Write block:

**[5]** Write 
------------------------------------------------

.. topic:: _[[WRITE]] rel file path

    Updates variables in templates and writes file to report folder. 

    .. code-block:: text

            Syntax:    
                _[[WRITE]] relative file path
                text or script
                ...
                _[[END]]

            Example:    
                _[[WRITE]] rvsrc/script.py
                for i in range(2):
                    print(f"{vars}",i) 
                _[[END]]

=========== ==========================
API Scope     Run
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------


.. _Shell script:

**[6]** Shell script
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
API Scope     Run
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------


.. _Meta block:

**[7]** Metadata
-------------------

 
.. topic:: _[[METADATA]]
    
    Each keyword is required and is followed by an equal sign and a value. The
    keywords are case insensitive.

    ..  code-block:: text

        Synatax - defaults:

            _[[METADATA]] 
            [doc]
            ;-----------------------------------------
            authors = --
            version = --
            repo = --
            license = --
            copyright = --
            fork1_authors = --
            fork1_version = --
            fork1_repo = --
            fork1_license = --
            [layout]
            ;----------------------- cover page and runner settings
            ;--- add logo files to rvsrc/image folder, size is % page width
            subtitle =  --
            copyright = --
            client =  --
            coverpage = --
            coverlogo_size = --
            coverlogo = --
            runninglogo = --
            runninglabel = --
            project_ref = --
            ;------------------------ PDF settings
            ;--- colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
            pdf_link_color = --
            pdf_link_underline = --
            pdf_pagesize = -- ; letter, legal, A4
            pdf_margins = -- ; top, right, bottom, left
            pdf_page = -- ; if true, start sections on new page 
            ;----------------------- TOC levels
            ;--- 1: include subdivisions   2: include subdivisions and sections
            toc_level = --
            [process]
            ;-----------------------------------------
            doc_verbose = true; if false minmize output during doc processing
            auto_cfg = true ; if false, config files are not updated from rivt file
            _[[END]]   

        Example:
            _[[METADATA]] 
            [doc]
            ;-----------------------------------------
            authors = R Holland
            version = 1.0.0a17
            repo = https://github.com/rivt-info/rivt-example-01
            license = https://opensource.org/license/mit/
            copyright = --
            fork1_authors = --
            fork1_version = --
            fork1_repo = --
            fork1_license = https://opensource.org/license/mit/
            [layout]
            ;----------------------- cover page and runner settings
            ;--- add logo files to rvsrc/image folder, size is % page width
            subtitle =  UDL Beam
            copyright = --
            client = user example
            coverpage = true
            coverlogo_size = 30
            coverlogo = logo1.png
            runninglogo = logo2.png
            runninglabel = rivt
            project_ref = proj. 0001
            ;------------------------ PDF settings
            ;--- colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
            pdf_link_color = brown
            pdf_link_underline = false
            pdf_pagesize = letter ; letter, legal, A4    
            pdf_margins = 1in, 1in, 1in, 1in ; top, right, bottom, left
            pdf_page = false ; if true, start sections on new page 
            ;----------------------- TOC levels
            ;--- 1: include subdivisions   2: include subdivisions and sections
            toc_level = 2
            [process]
            ;-----------------------------------------
            doc_verbose = true; if false minmize doc processing output
            auto_cfg = true ; if false, config files are not updated from rivt file
            _[[END]]

=========== ==========================
API Scope     Docs
Doc Types     text, PDF, HTML
=========== ==========================

-----------------------

.. _End block:

**[8]** End block
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
