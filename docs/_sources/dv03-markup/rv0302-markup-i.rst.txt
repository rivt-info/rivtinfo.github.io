3.2 rv. **I** - Insert
========================


**[01]** TAG KEY
--------------------------------------

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 

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

**[03]** _[D] :  footnote text
-------------------------------------------    

.. raw:: html

    <hr>

.. topic:: *endnote* _[D]

   endnote - assigned in order _[D]

text, pdf, html


**[04]** _[B] :  center, bold
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[B]

    This text will be bold and centered _[B]

pdf, html


**[05]** _[C] :   center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    This text will be centered _[C]

pdf, html


**[06]** _[E] : label equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   An autonumbered equation label _[E]

text, pdf, html


**[07]** _[F] : label figure 
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

.. topic:: *text* _[LD] doc link
    
    text at end of line _[LD] section number, link label

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


**[15]** __ : line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 4 or more underscores ____ 

   ____    
    
text, pdf, html


**[16]** _[[B]] : indent bold
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


**[17]** _[[C]] : code or literal text
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


**[18]** _[[L]] : LaTeX
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


**[19]** _[[T]] : topic
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



**[20]** _[[C]] : code or literal
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


**[21]** _[[I]] : indent italic
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


**[22]** _[[L]] : LaTeX
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

**[23]** _[[N]] :  indent
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


**[24]** _[[T]] : topic
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


**[25]** COMMAND KEY
----------------------

*Command* parameter options are separated with commas and parameter elements by
semicolons. Path names can be directly specified relative to the project
*source folder* or specified with an alias:

    *rvsource* : this alias directs *rivtlib* to look for the file in the
    default *source* folder. For example if the *rivt file* is in Division 1 and
    the API function is *Insert* the *i01* subfolder in the *source* folder is
    searched.

    *rvlocal* : this alias directs *rivtlib* to look for the file in the *rivt
    file* directory. It is used when a *single doc*, rather than a *report
    doc* is processed.

The *rivt report* folders are described 
:doc:`here. </dv04-reports/rv0402-folders>`


.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

  example

file types


**[26]** | IMG | - insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | path | filename | scale, caption (_[F])

    | IMG | rvsource | file1.png | .50, Map _[F]


reads PNG and JPEG files (.png, jpg)

text, PDF, HTML


**[27]** | IMG2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | path | fname1, fname2 | cap1 (_[F]), cap2 (_[F]), sc1, sc2 

    | IMG | rvsource | file1.png, file2.png | .50, .40, Map, Plan


reads PNG and JPEG files (.png, jpg)

text, PDF, HTML


**[28]** | TABLE | - format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title (_[T])

    | TABLE | rvsource | file1.csv | Forces _[T]


reads text, csv and EXCEL files (.txt, .csv, .xls)

PDF, HTML, text


**[29]** | TEXT | - format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | path | filename | normal, literal

    | TABLE | rvsource | file1.txt | normal

reads text, text and reST files (.txt, .tex, .rst)

PDF, HTML, text

