**C.5 rv.V - Values**
========================


**[1]** TAG KEY
--------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

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



**[2]** _[#] :  numbered endnote
----------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

.. raw:: html

    <hr>

.. topic:: *text* _[#] text
    
   end of text with auto endnote. _[#]

text, pdf, html


**[3]** _[D] :  endnote text
-------------------------------------------    

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

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


**[14]** _[[C]] : code or literal text
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


**[15]** _[[L]] : LaTeX
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


**[16]** _[[T]] : topic
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


**[17]** COMMAND KEY
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
:doc:`here. </dv04-reports/rv02-folders>`


.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

  example

file types


**[18]** | IMG | - insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | path | filename | scale, caption (_[F])

    | IMG | rvsource | file1.png | .50, Map _[F]


reads PNG and JPEG files (.png, jpg)

text, PDF, HTML


**[19]** | IMG2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | path | fname1, fname2 | cap1 (_[F]), cap2 (_[F]), sc1, sc2 

    | IMG | rvsource | file1.png, file2.png | .50, .40, Map, Plan


reads PNG and JPEG files (.png, jpg)

text, PDF, HTML


**[20]** | TABLE | - format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | path | filename | title (_[T])

    | TABLE | rvsource | file1.csv | Forces _[T]


reads text, csv and EXCEL files (.txt, .csv, .xls)

PDF, HTML, text


**[21]** | TEXT | - format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | path | filename | normal, literal

    | TABLE | rvsource | file1.txt | normal

reads text, text and reST files (.txt, .tex, .rst)

PDF, HTML, text

**[22]** **<=** - assign equation value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b <= a * 10 | unit1, unit2, decimals | reference

    b_1 <= E_1 * 12.1*IN^2 | KIP, kN, 2 | Std. 123
  
  assigns a variable to an equation value
  
  text, PDF, HTML


**[23]** **:=** - define value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: c := 5*unit1 | unit1, unit2, decimals | description

    D_1 = 10*IN | IN, M, 3 | beam depth
  
  defines the value of a variable 
  
  text, PDF, HTML