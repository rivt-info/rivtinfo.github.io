3.4 Tags in [V]alues
======================

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


**[01]** _[#] :  numbered footnote
----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[#] text
    
    text, pdf, html

**[02]** _[D] :  footnote description
-------------------------------------------    

.. raw:: html

    <hr>

.. topic:: *text* _[D]

    text, pdf, html

**[03]** _[E] : label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[E]

    text, pdf, html

**[04]** _[F] : number, label figure 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *caption* _[F]

    pdf, html

**[05]** _[LD] :  doc link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LD] doc link *text*
    
    text, pdf, html

**[06]** _[LR] :  report link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LR] report link *text*
    
    text, pdf, html

**[07]** _[LU] :  url link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LU] url link *text*
    
    text, pdf, html

**[08]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    pdf, html


**[09]** _[S] : sympy equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[S]

    text, pdf, html

**[10]** _[T]  label table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

    text, pdf, html


**[11]** _[V] : label values table 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[V]
    

    text, pdf, html


**[12]** __ : line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic::  more than 4 underscores  ____

    text, pdf, html


**[13]** _[[C]] : code or literal
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


**[14]** _[[L]] : LaTeX
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


**[15]** _[[T]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[T]] *topic*

    ::
        
        _[[N]] topic
        text
        text
        ...
        _[[Q]]


    text, pdf, html

  

**[16]** _[[V]] : values
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[V]] *title*

    ::
        
        _[[V]] topic
        values1
        values2
        ...
        _[[Q]]

    - rv.I, rv.V
    - text, pdf, html  
