3.2 Line Tags
===================

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. Tags have a function and output scope.


**KEY**  
--------------------------------------------

_[TAG] : description

.. raw:: html

    <hr>

.. topic::  line syntax

    - function scope
    - applicable output

_[B] :  center, bold
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[B]

    - rv.I, rv.V
    - pdf, html

_[C] :   center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    - rv.I, rv.V
    - pdf, html

_[D] :  footnote description
-------------------------------------------    

.. raw:: html

    <hr>

.. topic:: *text* _[D]

    rv.I, rv.V
    text, pdf, html

_[E] : number, label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    *label* _[C]
    rv.I, rv.V
    text, pdf, html

_[F] : number, label figure 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *caption* _[F]

    rv.I, rv.V
    pdf, html

_[LD] :  doc link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LD] doc link *text*
    
    rv.I, rv.V
    text, pdf, html

_[LR] :  report link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LR] report link *text*
    
    rv.I, rv.V
    text, pdf, html

_[LU] :  url link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LU] url link *text*
    
    rv.I, rv.V
    text, pdf, html

_[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    rv.I, rv.V
    pdf, html


_[S] : sympy equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[S]

    rv.I, rv.V
    text, pdf, html

_[T]  number, label table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

    rv.I, rv.V
    text, pdf, html


_[V] : number, label values table 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[V]
    
    rv.I, rv.V
    text, pdf, html

_[#] :  numbered footnote
----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[#] text
    
    rv.I, rv.V
    text, pdf, html

**horizontal line**
--------------------------------------- 
.. raw:: html

    <hr>

.. topic::  5 or more underscores  _____

    rv.I, rv.V
    text, pdf, html
