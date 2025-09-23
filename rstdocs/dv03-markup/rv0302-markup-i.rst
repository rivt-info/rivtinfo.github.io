3.3 **rv.I** - Insert
=======================


**TAG KEY**  
--------------------------------------


_[TAG] : line tag description

.. raw:: html

    <hr>

.. topic::  syntax : description

   example

types of output


_[[TAG]] : block tag description
        
.. raw:: html

    <hr>

.. topic::  syntax : description

    example

types of output



**COMMAND KEY**  
------------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

  example

file types




**[01]** _[#] :  numbered endnote
----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[#] text
    
   end of text with auto endnote. _[#]

text, pdf, html

**[02]** _[D] :  footnote text
-------------------------------------------    

.. raw:: html

    <hr>

.. topic:: *endnote* _[D]

   endnote - assigned in order _[D]

text, pdf, html


**[03]** _[B] :  center, bold
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[B]

    This text will be bold and centered _[B]

pdf, html


**[04]** _[C] :   center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    This text will be centered _[C]

pdf, html


**[05]** _[E] : label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   An autonumbered equation label _[E]

text, pdf, html


**[06]** _[F] : label figure 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[F]

   An autonumbered figure label _[E]

text, pdf, html


**[07]** _[LS] :  section link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LD] doc link
    
    text at end of line _[LD] section number, link label

text, pdf, html


**[08]** _[LR] :  doc link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LR] doc link 
    
    text at end of line _[LR] doc-file-name, link label

text, pdf, html


**[09]** _[LU] :  url link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LU] url link  
    
    text at end of line _[LU] urlname, link label

text, pdf, html


**[10]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    this will start a new page _[P]

text, pdf, html


**[11]** _[S] : sympy equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[S]

    f(x) = sin(x) + y/5 _[S]

text, pdf, html


**[12]** _[T]  label table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

   An autonumbered table title _[T]

text, pdf, html


**[13]** _[V] : label values table 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[V]
    
   An autonumbered value table title _[V]

text, pdf, html


**[14]** __ : line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 4 or more underscores ____ 

   ____    
    
text, pdf, html


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

text, pdf, html


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

text, pdf, html


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

pdf, html


**[18]** _[[T]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[T]] *topic*

    ::
        
        _[[T]] this a topic title : after colon will be italic
        This is a topic description.
        ...
        _[[Q]]


text, pdf, html



**[19]** _[[C]] : code or literal
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

text, pdf, html


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

text, pdf, html


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

    pdf, html

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

text, pdf, html


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


text, pdf, html


**[24]** | IMAGE | 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | path | filename | caption _[F], scale

    example

reads PNG and JPEG files (.png, jpg)

PDF, HTML


**[25]** | IMAGE2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | path | fname1, fname2 | cap1 _[F], cap2 _[F], sc1, sc2 

    example

reads PNG and JPEG files (.png, jpg)

PDF, HTML


**[26]** | TABLE | 
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title _[T]

    example

reads text, csv and EXCEL files (.txt, .csv, .xls)

PDF, HTML, text


**[27]** | TEXT | 
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | path | filename | title _[T]


    example

reads text, text and reST files (.txt, .tex, .rst)

PDF, HTML, text

