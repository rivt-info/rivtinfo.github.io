**C.5 Values - rv.V**
========================

**Summary**

============================= =======================================
        Line Tags              Description (doc scope)
============================= =======================================
    text _[#]                  endnote number (all)
    text _[C]                  center text (all)
    text _[R]                  right justify text (all)
    math _[L]                  format LaTeX math (all) 
    math _[A]                  format ASCII math (all) 
   label _[E]                  equation number and label (all)
 caption _[I]                  image number and caption (all)[1]
   title _[T]                  table number and title (all)[1]
    text _[S] section link     link section within doc (all)
    text _[D] report link      link doc within report (all)
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
 _[[NOTES]] optional label               Endnote descriptions (all)
 _[[TEXT]] optional language             *literal*, code (all)
 _[[TOPIC]] topic                        Topic (all)
 _[[VALUES]] table title (_[T])          Define values(all)
======================================= ==============================

[1] LaTeX processing requires the installation of *Texlive*


======================================================== ===== ==================
         | Command | path | parameters                    R/W   input types
======================================================== ===== ==================
 \| IMAGE | relative path |  scale, caption (_[I])        R     *.png, .jpg*
 \| IMAGE2 | relative path | s1, s2, c1, c2 (_[I])        R     *.png, jpg*
 \| TABLE | relative path | width, l;c;r, title           R     *csv, txt, xlsx*
 \| TEXT | relative path |  *normal;literal* ;code        R     *txt, code*
 \| VALUES | relative path | *visible;hide* (_[T])        R     *csv*
a := 1*IN  | unit1, unit2, decimal | descrip (_[E])[1]    W     define a value
b <= a + 3*FT | unit1, unit2, decimal | descrip (_[E])    W     assign a value
c <= func1(x,y) | unit1, unit2, decimal | descrip (_[E])  W     assign a value
======================================================== ===== ==================

[1] Values are usually defined in a block where the equation tag (_[E]) 
would not apply and will be disregarded.


.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[2]** _[#] : endnote number
-------------------------------------

.. raw:: html

    <hr>


.. topic:: text _[#] 
    
   Text is wrapped when formatted. _[#]

This tag assigns an endnote number to the text. Endnotes are defined with the
block tag _[[NOTE]] and are listed at the end of the *doc*. Numbers are
assigned in the order they are processed.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[3]** _[H] or ______ : horizontal line
------------------------------------------- 
.. raw:: html

    <hr>

.. topic:: _[H] or 4 or more underscores

    ___________     
    

    or some text _[H]

Draws a horizontal line the width of the page.
    
outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[4]** _[A] : ASCII math
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[A]

    f(x,y) = sin(x)**2 + y/5 _[A]

The math expression will be formated in ASCII text.

outputs: text, pdf, html

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

**[6]** _[C] :  center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[C]

    This text will be centered _[C]

Center text within the page margins.

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

**[10]** _[S] : link sections
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

**[11]** _[D] : link docs
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

**[12]** _[U] : external url
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[U] url link  
    
    text at end of line _[U] urlname, link label

External url link. Text will be continued and wrapped when formatted.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[13]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: text _[P]

     end of line. _[P]

Starts a new page. Pages indicated with double dashed line in text output.

outputs: text, pdf, html



.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[14]** _[[TEXT]] : literal text or code
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

**[15]** _[[LATEX]] : LaTeX
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[L]] 
    
    ::
        
        _[[L]]
        \frac{\alpha}{\beta}
        \sum_{n=1}^{10} n
        ...
        _[[QUIT]]

Formats LaTeX, which needs to be installed.

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[16]** _[[NOTE]] : endnote text
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

**[17]** _[[ITALIC]] : indent italic
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

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[18]** _[[INDENT]] : indent text
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

**[21]** | IMAGE | : insert image
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

**[22]** | IMAGE2 | : insert adjacent images 
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

**[23]** | TABLE | : format table
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

**[24]** | TEXT | : format text
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

**[25]** | VALUES | : format values
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | VALUE | rel path | hide; insert

    | VALUE | src/file1.csv  | hide; insert

Reads a value file (.csv). The file path is relative to the report folder. The
insert parameter specifies whether the value table is visible in the doc.  

outputs: text, PDF HTML


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[26]** **<=** : assign equation value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b <= a * 10 | unit1, unit2, decimals | reference (_[E])

    b_1 <= E_1 * 12.1*IN^2 | KIP, KN, 2 | Std. 123
  
Assigns a variable or variables to an equation or function value and writes the
values to a file *vnum-s.csv* where *num* is the *doc number* and *s* is the
section number. The file is written to the folder *src/values* unless
*rvsource* is set to *True* in the *Meta API function*.
  
outputs: text, PDF, HTML


**[27]** **<=** : assign function value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: c <= func1(a,b) | unit1, unit2, decimals | reference (_[E])

    c <= func1(a,b) | KIP, KN, 2 | Std. A-1
  
Assigns a variable or variables to an equation or function value and writes the
values to a file *vnum-s.csv* where *num* is the *doc number* and *s* is the
section number. The file is written to the folder *src/values* unless
*rvsource* is set to *True* in the *Meta API function*.
  
outputs: text, PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[28]** **:=** : define value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: c := 5*unit1 | unit1, unit2, decimals | description

    D_1 = 10*IN | IN, M, 3 | beam depth
  
Defines a variable value and writes its value to a file *vnum-s.csv* where
*num* is the *doc number* and *s* is the section number. *unit1* is the primary
unit used in *doc*. *unit2* is also printed int he values table. the The file is written to the folder *src/values*
  
outputs: text, PDF, HTML
