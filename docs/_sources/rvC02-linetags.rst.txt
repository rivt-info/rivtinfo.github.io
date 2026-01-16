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
rv.I                          text **_[C]**                     :ref:`Center text` 
rv.I                          text **_[R]**                     :ref:`Right justify text`
rv.I                    text  math **_[M]**                     :ref:`Text math` 
rv.I                    LaTeX math **_[L]**                     :ref:`LaTeX math` 
rv.I                          text **_[#]** more text           :ref:`Endnote number`  
rv.I                          text **_[G]** glossary term       :ref:`Term reference`
rv.I                          text **_[S]** section label       :ref:`Section link`
rv.I                          text **_[D]** rivt_file text      :ref:`Doc link`
rv.I                          text **_[U]** label, url          :ref:`URL link`   
rv.V, I                       text **_[V]** var_name text       :ref:`Variable value`
rv.V, I            assign or label **_[E]**                     :ref:`Equation number`
rv.V, I                      title **_[T]**                     :ref:`Table number`
rv.V, I                    caption **_[F]**                     :ref:`Figure number`
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
            text _[C]

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
            text _[R]

        Example:
            This text wil be right justified _[R]

=========== ==========================
API Scope     Insert
Doc Types     text, PDF, HTML
=========== ==========================

.. _Text math:

**[4t]** Text math
-----------------------------------------

.. raw:: html

    <hr>

Formats a text math expression.

.. topic:: _[M]

    .. code-block:: text

        Syntax:
            text math expression  _[M]

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
            LaTeX math expression  _[L]

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

.. topic::  _[U] 

    .. code-block:: text

        Syntax:
            external url, label  _[U]

        Example:
            https://www.github.com, github _[U]
    
=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Term reference:

**[7t]** Glossary link
------------------------------------------

.. raw:: html

    <hr>

Links a term to the glossary.

.. topic:: _[G] 

    .. code-block:: text

        Syntax:
            text _[G] glossary term

        Example:
            Links to the glossary term _[G] doc. 

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Section link:

**[8t]** Section link
-----------------------------------------

.. raw:: html

    <hr>

Creates a link to a section label defined in the API header.

.. topic:: _[S]

        .. code-block:: text

        Syntax:
            text _[S] section title

        Example:
            This creates a link to _[S] My Section Title

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

..  _Endnote number:

**[9t]**  Endnote number
-------------------------------------

.. raw:: html

    <hr>

Assigns endnote number to the text in order of processing. Endnotes
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

**[10t]** Doc link
-----------------------------------------

.. raw:: html

    <hr>

Links to a *doc* in a *report*. The *doc* title will be inserted as the
link term.

.. topic:: _[D]

    .. code-block:: text

        Syntax:
            text rivt_file _[D] more text

        Example:
            This is a link to the rv101-filename1 _[D] doc.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Variable value:

**[11t]** Variable value
------------------------------------------

.. raw:: html

    <hr>

Inserts the value of  var_name _[V] in the sentence.

.. topic:: _[V]

    .. code-block:: text

        Syntax:
            text var_name _[V] more text

        Example:
            The value of my_var is my_var _[V].

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

.. _Equation number:

**[12t]** Equation number
-----------------------------------------

.. raw:: html

    <hr>

If the line of text is math text or a label, the text is assigned an equation
number and right justified. If the line is an equation assignment the equation
label is used for the label text.

.. topic:: _[E]

    .. code-block:: text

        Syntax:
            math text or label _[E]

            assignment command _[E]

        Example:
            3x * 4/(1+n) _[E]

            x <= 3*IN + 4.1*FT | inch, cm, 2 | example 1 _[E]

=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

.. _Table number:

**[13t]** Table number
------------------------------------------

.. raw:: html

    <hr>

    Labels and numbers tables.

.. topic:: _[T]

    .. code-block:: text

        Syntax:
            Table Title  _[T]

        Example:
            A New Table _[T]


=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================

.. _Figure number:

**[14t]** Figure number
------------------------------------------

.. raw:: html

    <hr>

    Labels and numbers figures.

.. topic:: _[F]

    .. code-block:: text

        Syntax:
            Figure caption _[F]

        Example:
            Stress Distribution _[F]


=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================


