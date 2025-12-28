**C.3 Insert - rv.I**
========================

**Summary**

**[1t]** Summary
-------------------------------------

.. raw:: html

    <hr>

The *Insert* API function inserts static resources into the *doc* including
images, tables and formatted text.

============================= =======================================
        Line Tags              Description (doc scope)
============================= =======================================
    text _[#] text             :ref:`endnote` number (all)
    text _[C]                  :ref:`center` text (all)
    text _[R]                  :ref:`right` justify text (all)
    math _[A]                  format ASCII math (all) 
    math _[L]                  format LaTeX math (all) 
   label _[E]                  equation number and label (all)
 caption _[I]                  image number and caption (all)[1]
   title _[T]                  table number and title (all)[1]
    text _[D] term link        link to defined term in report (all)
    text _[S] section link     link to section in doc (all)
    text _[R] report link      link to doc in report (all)
    text _[U] external url     external url link (all)
    \-\-\-\-\-                 >4 dashes inserts line (all)[2]
    \=\=\=\=\=                 >4 underscores inserts page (all)[2]
============================= =======================================

[1] tag may be added to the label parameter in the IMAGE and TABLE commands

[2] must start in first indented column (absolute column 4)

======================================= ==============================
       Block Tags                        Description (doc scope)
======================================= ==============================
 _[[INDENT]] spaces (4 default)          Indent (all)
 _[[ITALIC]] spaces (4 default)          Italic indent - (all)
 _[[ENDNOTES]] optional label            Endnote descriptions (all)
 _[[TEXT]] optional language             *literal*, code language (all)
 _[[TERMS]] label                        Glossary of terms
 _[[TOPIC]] topic                        Topic (all)
 _[[END]]                                End block (all)
======================================= ==============================

======================================================== ===== ==================
         | Command | path | parameters                    R/W   input types
======================================================== ===== ==================
 \| IMAGE | relative path |  scale, caption (_[I])        R     *.png, .jpg*
 \| IMAGE2 | relative path | s1, s2, c1, c2 (_[I])        R     *.png, jpg*
 \| TABLE | relative path | width, l;c;r, title           R     *csv, txt, xlsx*
 \| TEXT | relative path |  *normal;literal* ;code        R     *txt, code*
======================================================== ===== ==================

..  _endnote:


**[2t]** _[#] : endnote number
-------------------------------------

.. raw:: html

    <hr>


.. topic:: text _[#] 
    
   Text is wrapped when formatted. _[#]

This tag assigns an endnote number to the text. Endnotes are defined with the
block tag _[[NOTE]] and are listed at the end of the *doc*. Numbers are
assigned in the order they are processed.

outputs: text, pdf, html

..  _center:


**[3t]** _[C] :  center text
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[C]

    This text will be centered _[C]

Center text within the page margins.

outputs: text, pdf, html

.. _right:


**[4t]** _[R] : right justify text
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[L]

    \frac{1}{\sqrt{x}} _[L]

The LaTeX math expression will be formatted in PDF and HTML.

outputs: pdf, html


.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[5]** _[L] : LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[L]

    \frac{1}{\sqrt{x}} _[L]

The LaTeX math expression will be formatted in PDF and HTML.

outputs: pdf, html


.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[6]** _[A] : ASCII math
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[A]

    f(x,y) = sin(x)**2 + y/5 _[A]

The math expression will be formated in ASCII text.

outputs: text, pdf, html


.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[7]** _[E] : equation label 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: equation label _[E]

   Equation label  _[E]

Labels and numbers equation.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[8]** _[I] : image label 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[I]

   Image label _[I]

Labels and numbers images.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[9]** _[T] : table label
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

   Table Title _[T]

Labels and numbers tables.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[10]** _[S] : section link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[S] 
    
    text at end of line _[s] section number, link label

Links *sections* within a *doc*. Text will be continued and wrapped when
formatted.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[11]** _[D] : doc link
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[D] doc link
    
    text at end of line _[S] doc number, link label

Links *docs* within a *report*. Text will be continued and wrapped when
formatted.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[12]** _[U] : url - external
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[U] url link  
    
    text at end of line _[U] urlname, link label

External url link. Text will be continued and wrapped when formatted.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[13]** ______ : horizontal line
------------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 5 or more underscores

    ___________     
    


Draws a horizontal line the width of the page.
    
outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[14]** ======== : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: 5 or more double dashes

     =======

Starts a new page.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[15]** _[[INDENT]] : indent text
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[INDENT]] spaces

    ::

        _[[INDENT]] 4
        text
        text
        ...
        _[[QUIT]]

Indents text four spaces.


.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[16]** _[[ITALIC]] : indent italic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[I]] spaces

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


**[17]** _[[NOTE]] : endnote text
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


.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>



**[18]** _[[TEXT]] : literal text or code
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[TEXT]] language or *literal*

    ::
        
        _[[TEXT]] python
        print("some text")
        b = 3 + 5
        ...
        _[[QUIT]]

This block formats text as literal or code. The parameters specify formatting
and syntax coloring. Languages include: - *python* - *bash* - *sh* - *cmd*

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[19]** _[[TOPIC]] : topic
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

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[20]** | IMAGE | : insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | relative path | scale, caption (_[I])

    | IMG | src/file1.png | .50, Map _[I]

Reads PNG and JPEG files (.png, jpg) and inserts them in the *doc*. The *Image
tag* may be added to the captions. 

outputs: PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[21]** | IMAGE2 | : insert adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | rel path1, rel path2| sc1, sc2, cap1 (_[I]), cap2 (_[I])  

    | IMAGE2 | src/file1.png, src/file2.png | .50, .40, Map _[I], Plan _[I]

Reads PNG and JPEG files (.png, jpg) and inserts them side by side in the
document. The *Image tag* may be added to the captions.

outputs: PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[22]** | TABLE | : format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | relative path | width, l;c;r, title  (_[T])

    | TABLE | src/file1.csv | 30, c, Forces _[T]

Reads text, csv and EXCEL files (.txt, .csv, .xls) and outputs formatted
tables. The width parameter specifies the maximum column width. The l,c,r
parameter specifies cell justification (left, center, right). The *Table tag*
may be added to the caption.

outputs: text, PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[23]** | TEXT | : format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TEXT | relative path | *literal*; code 

    | TEXT | src/file1.py  | python

Reads and formats text and code files. The parameters specify formatting and
syntax coloring.  Languages include:

    - *python*
    - *bash*
    - *sh*
    - *cmd*

outputs: text, PDF, HTML

