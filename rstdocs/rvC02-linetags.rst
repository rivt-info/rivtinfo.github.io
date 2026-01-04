**C.2 Line Tags**
========================

**[1t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>

**Format a line of text**
  
============= =========================================== =======================
API Scope             Line Tags                            Description 
============= =========================================== =======================
rv.I                        text _[#] text                    :ref:`notetag`  
rv.I                        text _[C]                         :ref:`centertag` 
rv.I                        text _[R]                         :ref:`righttag`
rv.I                  latex math _[L]                         :ref:`latextag` 
rv.I                  ascii math _[M]                         :ref:`asciitag` 
rv.I                        text _[S] section label           :ref:`Section link`
rv.I                        text _[G] glossary link term      :ref:`termtag`
rv.I                        text _[D] doc number              :ref:`doctag`
rv.I                        text _[U] external url            :ref:`urltag`   
rv.V, I        equation or label _[E]                         :ref:`Equation label`
rv.V, I          values or title _[T]                         :ref:`Table title`
============= =========================================== =======================

..  _notetag:

**[2t]**  endnote number
-------------------------------------

.. raw:: html

    <hr>


.. topic:: text _[#] text 
    
   Some text. **_[#]**  Some more text.

This tag assigns an endnote number to the text in order of processing. Endnotes
are defined with the block tag _[[ENDNOTE]] and are listed at the end of the
*doc*. 

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

..  _centertag:

**[3t]** center text
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[C]

    Some text. **_[C]**

Centers line of text within the page margins.

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================


.. _righttag:

**[4t]** right justify text
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[R]

    Some text. **_[R]**

Right justifies line of text within the page margins.

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _latextag:

**[5t]** LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: LaTeX math _[L]

    \frac{1}{\sqrt{x}} **_[L]**

Formats LaTeX math expression in the font specified in the style files.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================


.. _asciitag:

**[6t]** ASCII math
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: math _[M]

    f(x,y) = sin(x)**2 + y/5 **_[M]**

Formats math expression in ASCII text.

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Section link:

**[7t]** Section link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[S] section label
    
    Link to  _[S] My Section.

Creates a link to a section label defined by the API header.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _termtag:

**[8t]** term reference
------------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[G] term

    This is a rivt **_[G]** doc. 

Links term to the glossary term.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _doctag:

**[9t]** doc link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[D] doc number
    
    The last word in this phrase will be linked to the doc **_[D]** rA01

Links to *docs* in a *report*. Text will be continued and wrapped when
formatted.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _urltag:

**[10t]** External url
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[U] 
    
    The last word in this phrase will be linked to the url **_[U]** urlname

External url link. Text will be continued and wrapped when formatted.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Equation label:

**[11t]** Equation label 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: equation or math _[E]

   math text or label **_[E]**

   equation assignment command **_[E]**

If the line of text is math text or a label, the text is assinged an equation
number and right justified. If the line of 

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

.. _Table title:

**[12t]** Table title
------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[T]

   Table Title **_[T]**

Labels and numbers tables.

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

