**C.3 Block Tags**
========================

**[1t]** Summary
-------------------------------------

.. raw:: html

    <hr>


Format blocks of text.

========== ======================================= ==============================
API Scope         Block Tags                        Description (doc scope)
========== ======================================= ==============================
rv.R        _[[WIN]] label, *wait;nowait*           Windows command script (all)
rv.R        _[[MACOS]] label, *wait;nowait*         Mac shell script (all)
rv.R        _[[LINUX]] label, *wait;nowait*         Linux shell script (all)
rv.I, V     _[[INDENT]] spaces (4 default)          Indent (all)
rv.I, V     _[[ITALIC]] spaces (4 default)          Italic indent - (all)
rv.I, V     _[[ENDNOTES]] optional label            Endnote descriptions (all)
rv.I, V     _[[TEXT]] optional language             *literal*, code (all)
rv.I, V     _[[TOPIC]] topic                        Topic (all)
rv.V        _[[VALUES]] table title, rows (_[T])    Define values(all)
rv.T        _[[PYTHON]] label, *rvspace*;newspace   Python script (all)
rv.T        _[[LATEX]] label                        LaTeX markup (pdf)[1]
rv.T        _[[HTML]] label                         HTML markup (html)
rv.D        _[[LAYOUT]] label                       Doc format settings (all)
all         _[[END]]                                End block (all)
========== ======================================= ==============================

[1] LaTeX processing requires the installation of *Texlive*


.. _indenttag:

**[15t]** indent text block
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[INDENT]] number of spaces

    ::

        _[[INDENT]] 4
        text
        text
        ...
        _[[QUIT]]

Indents text four spaces.

.. _italictag:

**[16t]** indent italic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[ITALIC]] spaces

    ::
        
        _[[ITALIC]] 4
        text
        text
        ...
        _[[QUIT]]

Indents the specified number spaces and italicizes block.

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[17t]** endnote text
-------------------------------------------    

.. raw:: html

    <hr>


.. topic:: _[[NOTE]] 
    
    ::
   
        _[[NOTE]]
        this is an endnote - assigned to an endnote tag [#] in order of
        of processing.
        _[[QUIT]] 

Formats and numbers an endnote in order of processing.

outputs: text, pdf, html

**[18t]** literal text or code
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TEXT]] language;*literal*

    ::
        
        _[[TEXT]] python
        print("some text")
        b = 3 + 5
        ...
        _[[QUIT]]

This block formats text as literal or code. The parameters specify formatting
and syntax coloring. Languages include: - *python* - *bash* - *sh* - *cmd*

outputs: text, pdf, html

**[19t]** _[[TOPIC]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TOPIC]] topic title

    ::
        
        _[[TOPIC]] topic title
        text
        text
        ...
        _[[QUIT]]

Formats a highlighted block.

outputs: pdf, html

**[2t]** _[[HTML]] : HTML markup
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[HTML]] label
     markup
     markup
     ...
     _[[QUIT]]

Inserts HTML into *doc*. 

outputs: text, pdf, html

**[3t]** _[[LATEX]] : LaTeX markup
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LATEX]] label
    markup
    markup
    ...
    _[[END]]


Inserts TeX into *doc*.  May require installation of LaTeX.

outputs: text, pdf, html

**[4t]** _[[RST]] : reStructuredText code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[RST]] label
    markup
    markup
    ...
    _[[END]]


Inserts TeX into *doc*.  May require installation of LaTeX.

outputs: text, pdf, html

**[5t]** _[[PYTHON]] : Python code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
     
      _[[PYTHON]] *rv-namespace*; user namespace
      code
      code
      ...
      _[[END]]

Executes Python script in the *rivt namespace* or a user specified namespace.
File paths in the script are relative to the *rivt file* folder.

outputs: text, pdf, html

**[2]** _[[WIN]] : batch commands
------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[WIN]] *nowait;wait*
  batch command
  batch command
  ...
   _[[Q]]

text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** _[[MACOS]] : shell commands
--------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[MACOS]] *nowait;wait*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** _[[LINUX]] : shell commands 
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *nowait;wait*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html

**[17t]** endnote text
-------------------------------------------    

.. raw:: html

    <hr>


.. topic:: _[[NOTE]] 
    
    ::
   
        _[[NOTE]]
        this is an endnote - assigned to an endnote tag [#] in order of
        of processing.
        _[[QUIT]] 

Formats and numbers an endnote in order of processing.

outputs: text, pdf, html

**[18t]** literal text or code
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TEXT]] language;*literal*

    ::
        
        _[[TEXT]] python
        print("some text")
        b = 3 + 5
        ...
        _[[QUIT]]

This block formats text as literal or code. The parameters specify formatting
and syntax coloring. Languages include: - *python* - *bash* - *sh* - *cmd*

outputs: text, pdf, html

**[19t]** _[[TOPIC]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TOPIC]] topic title

    ::
        
        _[[TOPIC]] topic title
        text
        text
        ...
        _[[QUIT]]

Formats a highlighted block.

outputs: pdf, html

**[2t]** _[[HTML]] : HTML markup
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[HTML]] label
     markup
     markup
     ...
     _[[QUIT]]

Inserts HTML into *doc*. 

outputs: text, pdf, html

**[3t]** _[[LATEX]] : LaTeX markup
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LATEX]] label
    markup
    markup
    ...
    _[[END]]


Inserts TeX into *doc*.  May require installation of LaTeX.

outputs: text, pdf, html

**[4t]** _[[RST]] : reStructuredText code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[RST]] label
    markup
    markup
    ...
    _[[END]]


Inserts TeX into *doc*.  May require installation of LaTeX.

outputs: text, pdf, html

**[5t]** _[[PYTHON]] : Python code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
     
      _[[PYTHON]] *rv-namespace*; user namespace
      code
      code
      ...
      _[[END]]

Executes Python script in the *rivt namespace* or a user specified namespace.
File paths in the script are relative to the *rivt file* folder.

outputs: text, pdf, html

**[2]** _[[WIN]] : batch commands
------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[WIN]] *nowait;wait*
  batch command
  batch command
  ...
   _[[Q]]

text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** _[[MACOS]] : shell commands
--------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[MACOS]] *nowait;wait*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** _[[LINUX]] : shell commands 
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *nowait;wait*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html