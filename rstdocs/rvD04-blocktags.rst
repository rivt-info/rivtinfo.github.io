**D.3 | Block Tags**
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
