**C.2 Line Tags**
========================

**[1t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>

**Format a line or partial line of text**
  
========== ================================================= ===============================
API Scope             Line Tags                                     Description 
========== ================================================= ===============================
rv.I                          text _[C]                         :ref:`Center text` 
rv.I                          text _[R]                         :ref:`Right justify text`
rv.I                    text  math _[M]                         :ref:`Text math` 
rv.I                    LaTeX math _[L]                         :ref:`LaTeX math` 
rv.I                   label, url  _[U]                         :ref:`URL link`   
rv.I                          text _[G] glossary term           :ref:`Term reference`
rv.I                          text _[S] section label           :ref:`Section link`
rv.I                          text _[#] more text               :ref:`Endnote number`  
rv.I                text rivt_file _[D] more text               :ref:`Doc link`
rv.V, I              text var_name _[V] more text               :ref:`Variable value`
rv.V, I            assign or label _[E]                         :ref:`Equation label`
rv.V, I          valtable or title _[T]                         :ref:`Table title`
========== ================================================= ===============================

..  _Center text:

**[2t]** Center text
-------------------------------------------

.. raw:: html

    <hr>

Centers line of text within the page margins.

.. topic:: _[C]
    
    .. code-block:: text

        Syntax:
            text **_[C]**

        Example:
            This text wil be centered. _[C]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================


.. _Right justify text:

**[3t]** Right justify text
-----------------------------------------

.. raw:: html

    <hr>

Right justifies line of text within the page margins.

.. topic:: _[R]

    .. code-block:: text

        Syntax:
            text **_[R]**

        Example:
            This text wil be centered. _[R]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Text math:

**[4t]** Text math
-----------------------------------------

.. raw:: html

    <hr>

Formats a utf-8 math expression.

.. topic:: _[M]

    .. code-block:: text

        Syntax:
            text math expression  **_[M]**

        Example:
            f(x,y) = sin(x)**2 + y/5 _[M]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _LaTeX math:

**[5t]** LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

Formats a LaTeX math expression in the font specified in the style files.

.. topic:: _[L]

    .. code-block:: text

        Syntax:
            LaTeX math expression  **_[L]**

        Example:
            \frac{1}{\sqrt{x}} _[L]

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _URL link:

**[6t]** URL link
-----------------------------------------

.. raw:: html

    <hr>

.. topic::  external url, label  _[U] 
    
    The  phrase following the comma will be linked to the specified url 
    **_[U]** https://myurl.com, my link 


=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
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
    
    Link to  _[S] My Section

Creates a link to a section label defined in the API header.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

..  _Endnote number:

**[2t]**  Endnote number
-------------------------------------

.. raw:: html

    <hr>

This tag assigns an endnote number to the text in order of processing. Endnotes
are defined with the block tag _[[ENDNOTE]] and are listed at the end of the
*doc*. 
    
.. topic:: _[#] 

    .. code-block:: text

        Syntax:
            text _[#] more text

        Example:
            This is a sentence with an endnote _[#] tag.



=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
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



