**C.4 Insert - rv.I**
========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** **TAG KEY**
--------------------------------------

.. raw:: html

    <hr>

*line tags* format a line of text and are denoted with _[TAG] at the end of the
line. *Block tags* format a block of text that begin with _[[TAG]] on the first
line and end with _[[Q]] after the last line.

_[TAG] : line tag description

.. raw:: html

    <hr>

.. topic::  syntax : description

   example

outputs: types of output


_[[TAG]] : block tag description
        
.. topic::  syntax : description

    example

outputs: types of output


.. raw:: html

    <hr>

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[2]** _[#] :  endnote number
-------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>


.. topic:: *text* _[#] 
    
   end of line - text is wrapped when formatted. _[#]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[3]** __ : horizontal line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 4 or more underscores ____ 

    ___________  

    
outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[4]** _[B] :  center, bold
-------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

.. topic:: *text* _[B]

    This text will be bold and centered _[B]

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[5]** _[C] :   center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    This text will be centered _[C]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[6]** _[E] : label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   This label will be assigned an equation number  _[E]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[7]** _[F] : label figure 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[F]

   This caption will be assigned a figure number _[F]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[8]** _[L] : LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[L]

    \frac{1}{\sqrt{x}} _[L]

This math expression will be formated in LaTeX.

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[9]** _[M] : math equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[M]

    f(x,y) = sin(x) + y/5 _[M]

This math expression will be formated in ASCII text.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[10]** _[T] : table label
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

   An autonumbered table title _[T]

This table title will be assigned a table number.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[11]** _[L] : link *sections* 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[L] doc link
    
    *text* _[L] section number, link label

Links *sections* within a *doc*

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[12]** _[D] : link *docs*
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[D] report link 
    
    text at end of line _[D] doc-file-name, link label

Links *docs* within a report

outputs: text, pdf, html


**[13]** _[U] : link *urls*
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[U] url link  
    
    text at end of line _[U] urlname, link label

outputs: text, pdf, html


**[14]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    this will start a new page _[P]

outputs: text, pdf, html


**[15]** _[[B]] : indent bold
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[B]] 

    ::
        
        _[[B]]
        text
        text
        ...
        _[[Q]]

outputs: text, pdf, html


**[16]** _[[C]] : code or literal text
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[C]] *language*

    ::
        
        _[[C]] python
        print("some text")
        b = 3 + 5
        ...
        _[[Q]]

outputs: text, pdf, html


**[17]** _[[L]] : LaTeX
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[L]] 
    
    ::
        
        _[[L]]
        \frac{\alpha}{\beta}
        \sum_{n=1}^{10} n
        ...
        _[[Q]]

outputs: pdf, html


**[18]** _[[E]] : endnote text
-------------------------------------------    

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

.. topic:: _[[E]] 
    ::
   
        _[[E]]
        this is an endnote - assigned in order of
        of endnote line tags [#]
        _[[Q]] 

outputs: text, pdf, html


**[19]** _[[I]] : indent italic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[I]] 

    ::
        
        _[[I]]
        text
        text
        ...
        _[[Q]]

outputs: pdf, html


**[20]** _[[L]] : LaTeX
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[L]] 
    
    ::
        
        _[[L]]
        text
        text
        ...
        _[[Q]]

outputs: pdf, html


**[21]** _[[N]] :  indent
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[N]]

    ::

        _[[N]] title
        text
        text
        ...
        _[[Q]]

outputs: text, pdf, html


**[22]** _[[T]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[T]] *topic*

    ::
        
        _[[T]] topic
        text
        text
        ...
        _[[Q]]


outputs: text, pdf, html


**[23]** **COMMAND KEY**
---------------------------



.. raw:: html

    <hr>


.. topic:: | COMMAND | relative path | filename | parameters

  example

outputs: types of outputs


**[24]** | IMG | - insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | path | filename | scale, caption (_[F])

    | IMG | img1 | file1.png | .50, Map _[F]

    Where *img1* references the *i-img1* subfolder of the *source* folder. 

reads PNG and JPEG files (.png, jpg)

outputs: PDF, HTML


**[25]** | IMG2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | path | fname1, fname2 | cap1 (_[F]), cap2 (_[F]), sc1, sc2 

    | IMG | rvsource | file1.png, file2.png | .50, .40, Map, Plan


reads PNG and JPEG files (.png, jpg)

outputs: PDF, HTML


**[26]** | TABLE | - format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title (_[T])

    | TABLE | rvsource | file1.csv | Forces _[T]


reads text, csv and EXCEL files (.txt, .csv, .xls)

outputs: text, PDF HTML


**[27]** | TEXT | - format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | path | filename | normal, literal

    | TABLE | rvsource | file1.txt | normal

reads text, text and reST files (.txt, .tex, .rst)

outputs: text, PDF HTML

