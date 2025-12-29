**C.3 Block Tags**
========================

**[1t]** Block Tag Summary
-------------------------------------

.. raw:: html

    <hr>


Format blocks of text.

========== ======================================= ==============================
API Scope         Block Tags                        Description 
========== ======================================= ==============================
rv.R        _[[WIN]] label, *wait;nowait*           :ref:`wintag`
rv.R        _[[MACOS]] label, *wait;nowait*         :ref:`mactag`
rv.R        _[[LINUX]] label, *wait;nowait*         :ref:`linuxtag`
rv.I, V     _[[INDENT]] spaces (4 default)          :ref:`indenttag`
rv.I, V     _[[ITALIC]] spaces (4 default)          :ref:`italictag`
rv.I, V     _[[ENDNOTES]] optional label            :ref:`notestag`
rv.I, V     _[[TEXT]] optional language             :ref:`codetag`
rv.I, V     _[[TOPIC]] topic                        :ref:`topictag`
rv.V        _[[VALUES]] table title, rows (_[T])    Define values(all)
rv.T        _[[PYTHON]] label, *rvspace*;newspace   :ref:`pythontag`
rv.T        _[[LATEX]] label                        :ref:`latexblktag` [1]
rv.T        _[[HTML]] label                         :ref:`htmltag`
rv.T        _[[RST]] label                          :ref:`rsttag`
rv.D        _[[LAYOUT]] label                       :ref:`layouttag` 
all         _[[END]]                                End block (all)
========== ======================================= ==============================

[1] LaTeX processing requires the installation of *Texlive*

.. _wintag:

**[2t]** Windows batch commands
------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[WIN]] *nowait;wait*
  batch command
  batch command
  ...
   _[[END]]

API: Run
docs: text, pdf, html

.. _mactag:

**[3t]** Mac shell commands
--------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[MACOS]] *nowait;wait*
  shell command
  shell command
  ...
   _[[END]]

API: Run
docs: text, pdf, html

.. _linuxtag:

**[4t]** Linux shell commands 
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *nowait;wait*
  shell command
  shell command
  ...
   _[[END]]

API: Run
docs: text, pdf, html


.. _indenttag:

**[5t]** indent text
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

Indents text four spaces.

API: Insert, Values
docs: text, pdf, html

.. _italictag:

**[6t]** indent italic text
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

outputs: pdf, html

.. _notestag:

**[7t]** endnote text
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

outputs: text, pdf, html

.. _codetag:

**[8t]** literal text or code
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TEXT]] language;*literal*

    ::
        
        _[[TEXT]] python
        print("some text")
        b = 3 + 5
        ...
        _[[END]]

This block formats text as literal text or code. The parameters 
specify formatting and syntax coloring. Languages 
include: - *python* - *bash* - *sh* - *cmd*

outputs: text, pdf, html

.. _topictag:

**[9t]** topic
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

Formats a highlighted topic block.

outputs: text, pdf, html

.. _htmltag:

**[10t]** HTML markup
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

.. _latexblktag:

**[11t]** LaTeX markup
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

.. _rsttag:

**[12t]** reStructuredText code
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

.. _pythontag:

**[13t]** Python code
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

.. _layouttag:

**[11t]** Layout 
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LAYOUT]] label
    markup
    markup
    ...
    _[[END]]


Inserts TeX into *doc*.  May require installation of LaTeX.

outputs: text, pdf, html