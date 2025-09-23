3.3 rv. **V** - Values
========================


**[01]** TAG KEY
--------------------------------------

_[TAG] : line tag description

.. raw:: html

    <hr>

.. topic::  syntax : description

   example

types of output


_[[TAG]] : block tag description
        
.. topic::  syntax : description

    example

types of output


.. raw:: html

    <hr>



**[02]** _[#] :  numbered endnote
----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[#] text
    
   end of text with auto endnote. _[#]

text, pdf, html

**[03]** _[D] :  endnote text
-------------------------------------------    

.. raw:: html

    <hr>

.. topic:: *endnote* _[D]

   endnote - assigned in order _[D]

text, pdf, html

**[04]** _[E] : label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   An autonumbered equation label _[E]

text, pdf, html

**[05]** _[F] : label figure 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[F]

   An autonumbered figure label _[E]

text, pdf, html

**[08]** _[L] :  section link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[L] doc link
    
    text at end of line _[L] section number, link label

text, pdf, html


**[09]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    this will start a new page _[P]

text, pdf, html



**[10]** _[R] :  report link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[R] report link 
    
    text at end of line _[R] doc-file-name, link label

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


**[13]** _[U] :  url link 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[U] url link  
    
    text at end of line _[U] urlname, link label

text, pdf, html



**[14]** _[V] : label values table 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[V]
    
   An autonumbered value table title _[V]

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



**[16]** | IMAGE | 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | path | filename | caption _[F], scale

    - reads PNG and JPEG files (.png, jpg)
    - PDF, HTML

**[17]** | IMAGE2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | path | fname1, fname2 | cap1 _[F], cap2 _[F], sc1, sc2 

    - reads PNG and JPEG files (.png, jpg)
    - PDF, HTML

**[18]** | TABLE | 
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title _[T]

    - reads text, csv and EXCEL files (.txt, .csv, .xls)
    - PDF, HTML, text


**[19]** | VALUES | 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | VALUES | relative path | filename | title _[V], [rows]

    - reads values.txt file
    - PDF, HTML

**[20]** **=** - assign value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: a = 10*IN | unit1, unit2, decimals | description

    - assigns value to a variable
    - PDF, HTML

**[21]** **:=** - define equation
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b := a * 10 | unit1, unit2, decimals | reference

    - defines a variable in terms of expression
    - PDF, HTML
