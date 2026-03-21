**C.2 Line Tags**
========================

**[1t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>

**Format a line of text**
  
========== ==================================================== ===============================
API Scope             Line Tag                                      Description 
========== ==================================================== ===============================
rv.I                      text **_[C]**                          :ref:`Center text` 
rv.I                      text **_[R]**                          :ref:`Right justify text`
rv.I                 **text math _[M]**                          :ref:`Text math` 
rv.I                **LaTeX math _[L]**                          :ref:`LaTeX math` 
rv.I                      text **_[#]** text                     :ref:`Endnote number`  
rv.I                      text **_[G] glossary term |** text     :ref:`Term link`
rv.I                      text **_[S] label, section |** text    :ref:`Section link`
rv.I                      text **_[D] label, file name |** text  :ref:`Doc link`
rv.I                      text **_[U] label, url |** text        :ref:`URL link`   
rv.V, I                   text **_[V] var_name |** text          :ref:`Variable value`
rv.V, I                   **text _[E]**                          :ref:`Number equation`
rv.V, I                  **title _[T]**                          :ref:`Number table`
rv.V, I                **caption _[F]**                          :ref:`Number figure`
rv.V, I                        **_[P]**                          :ref:`New page`
========== ==================================================== ===============================

..  _Center text:

**[2t]** Center text
-------------------------------------------

.. raw:: html

    <hr>

Center line of text within the page margins.

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

Right justify line of text within the page margins.

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

Format math expression into text.

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

Format LaTeX math expression.

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


..  _Endnote number:

**[6t]**  Endnote number
-------------------------------------

.. raw:: html

    <hr>

Assign endnote number to the text in order of processing. Endnotes
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


.. _Term link:

**[7t]** Glossary link
------------------------------------------

.. raw:: html

    <hr>

Link a term to the glossary.

.. topic:: _[G] 

    .. code-block:: text

        Syntax:
            text _[G] glossary term

        Example:
            A definition of _[G] namespace
            is provided in the glossary.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Section link:

**[8t]** Section link
-----------------------------------------

.. raw:: html

    <hr>

Create a link to the section label defined in the API header with optional
link text. If the text is ommitted the section label is used for the link.

.. topic:: _[S]

        .. code-block:: text

        Syntax:
            text _[S] link text, section title

        Example:
            This creates a link to _[S] Section Title, actual section label
            which provides more detail.

=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Doc link:

**[9t]** Doc link
-----------------------------------------

.. raw:: html

    <hr>

Link to a *doc* in a *report* with an optional link text. If the link text is 
ommitted the *doc* title will be inserted as the link term.

.. topic:: _[D]

    .. code-block:: text

        Syntax:
            text _[D] text, rivt_file

        Example:
            This is a link to _[D] rv101-filename1 
            for reference.


=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _URL link:

**[10t]** URL link
-----------------------------------------

.. raw:: html

    <hr>

Link to a an external site with optional link text. If the link text is 
ommitted the url will be inserted as the link term.

.. topic::  _[U] 

    .. code-block:: text

        Syntax:
            text _[U] link label ,external url 

        Example:
            text _[U]  github, https://www.github.com 

   
=========== ==========================
API Scope     Insert
Doc Types     PDF, HTML
=========== ==========================

.. _Variable value:

**[11t]** Variable value
------------------------------------------

.. raw:: html

    <hr>

Insert the value of  var_name _[V] in the sentence.

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

.. _Number equation:

**[12t]** Equation number
-----------------------------------------

.. raw:: html

    <hr>

Assign equation number to a line of text. 

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

.. _Number table:

**[13t]** Table number
------------------------------------------

.. raw:: html

    <hr>

    Label and number tables.

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

.. _Number figure:

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

.. _New Page:

**[15t]** New Page
------------------------------------------

.. raw:: html

    <hr>

    Insert a page break in the document.

.. topic:: _[P]

    .. code-block:: text

        Syntax:
            text _[P]

        Example:
            Preceded by text or stand alone. _[P]
            _[P]


=========== ==========================
API Scope     Insert, Values
Doc Types     text, PDF, HTML
=========== ==========================


