3.3 Tags in [I]nsert
=====================

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 


**KEY**  
--------------------------------------------

_[TAG] : line tag description

_[[TAG]] : block tag description

.. raw:: html

    <hr>

.. topic::  syntax

    types of output

.. raw:: html

    <hr>


**[01]** _[B] :  center, bold
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[B]

   pdf, html

**[02]** _[C] :   center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

   pdf, html

**[03]** _[D] :  footnote description
-------------------------------------------    

.. raw:: html

    <hr>

.. topic:: *text* _[D]

    text, pdf, html

**[04]** _[E] : number, label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    text, pdf, html

**[05]** _[F] : number, label figure 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *caption* _[F]

    pdf, html

**[06]** _[LD] :  doc link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LD] doc link *text*
    
    text, pdf, html

**[07]** _[LR] :  report link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LR] report link *text*
    
    text, pdf, html

**[08]** _[LU] :  url link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LU] url link *text*
    
    text, pdf, html

**[09]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    pdf, html


**[10]** _[S] : sympy equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[S]

    text, pdf, html

**[11]** _[T]  label table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

    text, pdf, html


**[12]** _[V] : label values table 
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[V]
    

    text, pdf, html

**[13]** _[#] :  numbered footnote
----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[#] text
    
   text, pdf, html


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

    text, pdf, html

**[15]** _[[C]] : code or literal
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

**[16]** _[[I]] : indent italic
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

**[17]** _[[L]] : LaTeX
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

**[18]** _[[N]] :  indent
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

**[19]** _[[T]] : topic
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

**[20]** __ : horizontal line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic::  more than 4 underscores  ___ 

    text, pdf, html
