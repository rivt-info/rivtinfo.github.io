3.4 Tags in [V]alues
======================

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 


**KEY**  
--------------------------------------------


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

**[03]** _[E] : label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   An autonumbered equation label _[E]

text, pdf, html

**[04]** _[F] : label figure 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[F]

   An autonumbered figure label _[E]

text, pdf, html

**[05]** _[LS] :  section link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LD] doc link
    
    text at end of line _[LD] section number, link label

text, pdf, html

**[06]** _[LR] :  doc link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LR] doc link 
    
    text at end of line _[LR] doc-file-name, link label

text, pdf, html

**[07]** _[LU] :  url link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[LU] url link  
    
    text at end of line _[LU] urlname, link label

text, pdf, html

**[08]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    this will start a new page _[P]

text, pdf, html


**[09]** _[S] : sympy equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[S]

    f(x) = sin(x) + y/5 _[S]

text, pdf, html

**[10]** _[T]  label table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

   An autonumbered table title _[T]

text, pdf, html


**[11]** __ : line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 4 or more underscores ____ 

   ____    
    
text, pdf, html


**[12]** _[[C]] : code or literal text
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


**[13]** _[[L]] : LaTeX
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


**[14]** _[[T]] : topic
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

  

**[15]** _[[V]] : values
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[V]] *title*

    ::
        
        _[[V]] First Floor Framing
        I_1 = 100 | IN^3, CM^3, 2 | moment of intertia
        L_1 = 10*1.5 | FT, M, 2| beam length
        ...
        _[[Q]]

text, pdf, html  
