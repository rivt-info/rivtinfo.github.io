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

_[F] : number, label figure 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *caption* _[F]

    pdf, html

_[LD] :  doc link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LD] doc link *text*
    
    text, pdf, html

_[LR] :  report link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LR] report link *text*
    
    text, pdf, html

_[LU] :  url link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LU] url link *text*
    
    text, pdf, html

_[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    pdf, html


_[S] : sympy equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[S]

    text, pdf, html

_[T]  number, label table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

    text, pdf, html


_[V] : number, label values table 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[V]
    

    text, pdf, html

_[#] :  numbered footnote
----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[#] text
    
   text, pdf, html


_[[B]] : indent bold
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

_[[C]] : code or literal
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

_[[I]] : indent italic
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

_[[L]] : LaTeX
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

_[[N]] :  indent
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

_[[T]] : topic
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

_ : horizontal line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic::  4 or more underscores  ___ 

    text, pdf, html
