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


**[2]** _[#] :  endnote number
-------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>


.. topic:: *text* _[#] 
    
   end of text with auto endnote. _[#]

outputs: text, pdf, html


**[3]** __ : horizontal line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 4 or more underscores ____ 

    ____    
    
outputs: text, pdf, html


**[4]** _[B] :  center, bold
-------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

.. topic:: *text* _[B]

    This text will be bold and centered _[B]

outputs: pdf, html


**[5]** _[C] :   center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    This text will be centered _[C]

outputs: text, pdf, html


**[6]** _[E] : label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   An autonumbered equation label _[E]

outputs: text, pdf, html


**[7]** _[F] : label figure 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[F]

   An autonumbered figure label _[E]

outputs: text, pdf, html


**[8]** _[M] : math equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[S]

    f(x) = sin(x) + y/5 _[S]


outputs: text, pdf, html


**[9]** _[T]  table label
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

   An autonumbered table title _[T]

outputs: text, pdf, html


**[10]** _[L] :  link *sections* 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[L] doc link
    
    *text* _[L] section number, link label

Links *sections* within a *doc*

outputs: text, pdf, html


**[11]** _[D] :  link *docs*
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[D] report link 
    
    text at end of line _[D] doc-file-name, link label

Links *docs* within a report

outputs: text, pdf, html


**[12]** _[U] :  link *urls*
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[U] url link  
    
    text at end of line _[U] urlname, link label

outputs: text, pdf, html


**[13]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    this will start a new page _[P]

outputs: text, pdf, html


**[14]** _[[B]] : indent bold
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


**[15]** _[[C]] : code or literal text
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


**[16]** _[[L]] : LaTeX
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


**[17]** _[[T]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[T]] *topic*

    ::
        
        _[[T]] this a topic title : after colon will be italic
        This is a topic description.
        ...
        _[[Q]]


outputs: text, pdf, html



**[18]** _[[C]] : code or literal
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[C]] *language*

    ::
        
        _[[C]]
        text
        text
        ...
        _[[Q]]

outputs: text, pdf, html


**[19]** _[[E]] :  endnote text
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


**[20]** _[[I]] : indent italic
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


**[21]** _[[L]] : LaTeX
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


**[22]** _[[N]] :  indent
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


**[23]** _[[T]] : topic
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


**[24]** **COMMAND KEY**
---------------------------



.. raw:: html

    <hr>


.. topic:: | COMMAND | relative path | filename | parameters

  example

outputs: types of outputs


**[25]** | IMG | - insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | path | filename | scale, caption (_[F])

    | IMG | img1 | file1.png | .50, Map _[F]

    Where *img1* references the *i-img1* subfolder of the *source* folder. 

reads PNG and JPEG files (.png, jpg)

outputs: PDF, HTML


**[26]** | IMG2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | path | fname1, fname2 | cap1 (_[F]), cap2 (_[F]), sc1, sc2 

    | IMG | rvsource | file1.png, file2.png | .50, .40, Map, Plan


reads PNG and JPEG files (.png, jpg)

outputs: PDF, HTML


**[27]** | TABLE | - format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title (_[T])

    | TABLE | rvsource | file1.csv | Forces _[T]


reads text, csv and EXCEL files (.txt, .csv, .xls)

outputs: text, PDF HTML


**[28]** | TEXT | - format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | path | filename | normal, literal

    | TABLE | rvsource | file1.txt | normal

reads text, text and reST files (.txt, .tex, .rst)

outputs: text, PDF HTML

