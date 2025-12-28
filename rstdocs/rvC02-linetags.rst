**C.12 Line Tags**
========================

**[1t]** Summary
-------------------------------------

.. raw:: html

    <hr>

Format a line of text.
  
=============  ======================================= =======================
API Scope             Line Tags                            Description 
=============  ======================================= =======================
rv.I, V                    text _[#] text               :ref:`notetag`  
rv.I, V                    text _[C]                    :ref:`centertag` 
rv.I, V                    text _[R]                    :ref:`righttag` 
rv.I                 latex math _[L]                    :ref:`latextag` 
rv.I                 ascii math _[A]                    :ref:`asciitag`
rv.I, V          equation label _[E]                    :ref:`equatag`
rv.I, V                   title _[T]                    :ref:`tabletag` [1]
rv.I, V          section anchor _[N]                    :ref:`anchortag`
rv.I, V                    text _[M] term link          :ref:`termtag`
rv.I, V                    text _[S] section link       :ref:`sectiontag`
rv.I, V                    text _[D] doc link           :ref:`doctag`
rv.I, V                    text _[U] external url       :ref:`urltag`   
rv.I, V          \-\-\-\-\-                             :ref:`linetag` [2]
rv.I, V          \=\=\=\=\=                             :ref:`pagetag` [2]
=============  ======================================= =======================

[1] tag may be added to the label parameter in the TABLE commands

[2] must start in first indented column (absolute column 4)


..  _notetag:

**[2t]**  endnote number
-------------------------------------

.. raw:: html

    <hr>


.. topic:: _[#] 
    
   Text is wrapped when formatted. _[#]

This tag assigns an endnote number to the text. Endnotes are defined with the
block tag _[[NOTE]] and are listed at the end of the *doc*. Numbers are
assigned in the order they are processed.

outputs: text, pdf, html

..  _centertag:

**[3t]** center text
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[C]

    some text _[C]

Center text within the page margins.

outputs: text, pdf, html

.. _righttag:

**[4t]** right justify text
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[R]

    some text _[R]

The LaTeX math expression will be formatted in PDF and HTML.

outputs: pdf, html

.. _latextag:

**[5t]** LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[L]

    \frac{1}{\sqrt{x}} _[L]

The LaTeX math expression will be formatted in PDF and HTML.

outputs: pdf, html

.. _asciitag:

**[6t]** ASCII math
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[A]

    f(x,y) = sin(x)**2 + y/5 _[A]

The math expression will be formated in ASCII text.

outputs: text, pdf, html

.. _equatag:

**[7t]** equation label 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[E]

   equation label  _[E]

Labels and numbers equation.

outputs: text, pdf, html

.. _tabletag:

**[8t]** table label
------------------------------------------

.. raw:: html

    <hr>

.. topic:: Table Title

   Table Title _[T]

Labels and numbers tables.

outputs: text, pdf, html

.. _termtag:

**[9t]** term reference
------------------------------------------

.. raw:: html

    <hr>

.. topic:: _[M]

   term in glossary _[M]

link to term in glossary

outputs: text, pdf, html

.. _anchortag:

**[10t]** link anchor
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[N] 
    
    anchorname _[N] 

Inserts reference anchor at this location in the *doc*. Typically inserted
before a section title.

outputs: text, pdf, html

.. _sectiontag:

**[11t]** section link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: anchorname _[S] 
    
    text anchorname _[S] text

Replaces anchorname with Section title and link to Section. 

outputs: text, pdf, html

.. _doctag:

**[10t]** doc link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[D] doc link
    
    text at end of line _[D] doc number, link label

Links *docs* within a *report*. Text will be continued and wrapped when
formatted.

outputs: text, pdf, html

.. _urltag:

**[11t]** external url
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[U] 
    
    text at end of line _[U] urlname, link label

External url link. Text will be continued and wrapped when formatted.

outputs: text, pdf, html

..  _linetag:

**[13]** horizontal line
------------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 5 or more underscores

    ___________     
    


Draws a horizontal line the width of the page.
    
outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

.. _pagetag:

**[14t]** new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: 5 or more double dashes

     =======

Starts a new page.

outputs: text, pdf, html

