**C.2 Line Tags**
========================

**[1t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>

**Format a line of text**
  
=============  ========================================= =======================
API Scope             Line Tags                            Description 
=============  ========================================= =======================
rv.I                 latex math _[L]                      :ref:`latextag` 
rv.I                 ascii math _[M]                      :ref:`asciitag`
rv.I, V                    text _[#] text                 :ref:`notetag`  
rv.I, V                    text _[C]                      :ref:`centertag` 
rv.I, V                    text _[R]                      :ref:`righttag` 
rv.I, V          equation label _[E]                      :ref:`equatag`
rv.I, V             table title _[T]                      :ref:`tabletag` 
rv.I, V             anchor_name _[A]                      :ref:`anchortag`
rv.I, V                    text _[N] anchor_name link     :ref:`linktag`
rv.I, V                    text _[G] glossary link term   :ref:`termtag`
rv.I, V                    text _[D] doc link             :ref:`doctag`
rv.I, V                    text _[U] external url         :ref:`urltag`   
rv.I, V          \-\-\-\-\-                               :ref:`linetag` [1]
rv.I, V          \=\=\=\=\=                               :ref:`pagetag` [1]
=============  ========================================= =======================

.. highlight:: none

::

    [1] must start in first indented column (absolute column 4)


.. _latextag:

**[2t]** LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[L]

    \frac{1}{\sqrt{x}} **_[L]**

The LaTeX math expression will be formatted in the specified font.

API: Insert
docs: text, PDF, HTML


.. _asciitag:

**[3t]** ASCII math
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[M]

    f(x,y) = sin(x)**2 + y/5 **_[M]**

The math expression will be formated in ASCII text.

API: Insert
docs: text, PDF, HTML


..  _notetag:

**[4t]**  endnote number
-------------------------------------

.. raw:: html

    <hr>


.. topic:: _[#] 
    
   Text is wrapped when formatted. **_[#]**

This tag assigns an endnote number to the text. Endnotes are defined with the
block tag _[[NOTE]] and are listed at the end of the *doc*. Numbers are
assigned in the order they are processed.

API: Insert, Value
docs: text, PDF, HTML

..  _centertag:

**[5t]** center text
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[C]

    some text **_[C]**

Center text within the page margins.

API: Insert, Value
docs: text, PDF, HTML

.. _righttag:

**[6t]** right justify text
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[R]

    some text **_[R]**

The LaTeX math expression will be formatted in PDF and HTML.

API: Insert, Value
docs: text, PDF, HTML

.. _equatag:

**[7t]** equation label 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[E]

   equation label  **_[E]**

Labels and numbers equation.

API: Insert, Value
docs: text, PDF, HTML

.. _tabletag:

**[8t]** table title
------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[T]

   Table Title **_[T]**

Labels and numbers tables.

outputs: text, PDF, HTML

.. _termtag:

**[9t]** term reference
------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[G]

   term in glossary **_[G]**

link to term in glossary

API: Insert, Value
docs: text, PDF, HTML

.. _anchortag:

**[10t]** link anchor
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[A] 
    
     **_[A]** anchorname

Inserts reference anchor at this location in the *doc*. Typically inserted
before a section title. If inserted before a section title, the section title
is inserted as the link text.

API: Insert, Value
docs: text, PDF, HTML

.. _linktag:

**[11t]** anchor reference
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[N] 
    
    text **_[N]** anchorname

Replaces anchorname with the section title that follows, and links to the
anchor.

API: Insert, Value
docs: text, PDF, HTML

.. _doctag:

**[12t]** doc link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[D] doc link
    
    text at end of line **_[D]** doc number, link label

Links *docs* within a *report*. Text will be continued and wrapped when
formatted.

API: Insert, Value
docs: text, PDF, HTML

.. _urltag:

**[13t]** external url
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[U] 
    
    text at end of line **_[U]** urlname, link label

External url link. Text will be continued and wrapped when formatted.

API: Insert, Value
docs: text, PDF, HTML

..  _linetag:

**[14t]** horizontal line
------------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 5 or more underscores

    ___________     
    


Draws a horizontal line the width of the page.
    
API: Insert, Value
docs: text, PDF, HTML

.. _pagetag:

**[15t]** new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: 5 or more double dashes

     =======

Starts a new page.

API: Insert, Value
docs: text, PDF, HTML

