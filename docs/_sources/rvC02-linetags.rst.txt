**C.2 Line Tags**
========================

**[1t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>

**Format a line or partial line of text**
  
============= =========================================== ===============================
API Scope             Line Tags                            Description 
============= =========================================== ===============================
rv.I                        text _[#] text                    :ref:`Endnote number`  
rv.I                        text _[D] file_name text          :ref:`Doc link`
rv.I                        text _[C]                         :ref:`Center text` 
rv.I                        text _[R]                         :ref:`Right justify text`
rv.I                  ASCII math _[M]                         :ref:`ASCII math` 
rv.I                  LaTeX math _[L]                         :ref:`LaTeX math` 
rv.I                        text _[G] glossary link term      :ref:`Term reference`
rv.I                        text _[S] section label           :ref:`Section link`
rv.I                        text _[U] label, external_url     :ref:`URL link`   
rv.V, I                     text _[V] var_name text           :ref:`Variable value`
rv.V, I          assign or label _[E]                         :ref:`Equation label`
rv.V, I        valtable or title _[T]                         :ref:`Table title`
============= =========================================== ===============================

..  _Endnote number:

**[2t]**  Endnote number
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

..  _Center text:

**[3t]** Center text
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


.. _Right justify text:

**[4t]** Right justify text
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

.. _LaTeX math:

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


.. _ASCII math:

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

.. _Term reference:

**[7t]** Term reference
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

.. _Section link:

**[8t]** Section link
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

.. _Doc link:

**[9t]** Doc link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[D] doc number
    
    The phrase following the comma will be linked to the doc 
    **_[D]** rA01-myfile, received yesterday.

Links to a *doc* in a *report*. The tag must be at the end of a line. Text will be
continued and wrapped when formatted. 

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _URL link:

**[10t]** URL link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[U] external url, label 
    
    The  phrase following the comma will be linked to the specified url 
    **_[U]** https://myurl.com, my link 

External url link. The tag must be at the end of a line. Text will be
continued and wrapped when formatted.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Variable value:

**[11t]** Variable value
------------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[V] var_name text

   This tag inserts the value of **_[V] my_var** in the sentence.

Insert variable value.

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

.. _Equation label:

**[12t]** Equation label 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: assign command or label _[E]

   math text or label **_[E]**

   equation assignment command **_[E]**

If the line of text is math text or a label, the text is assigned an equation
number and right justified. If the line is an equation assignment the equation
label is used for the label text.

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

.. _Table title:

**[13t]** Table title
------------------------------------------

.. raw:: html

    <hr>

.. topic:: Table Title  _[T]

   A New Table **_[T]**

Labels and numbers tables.

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================



