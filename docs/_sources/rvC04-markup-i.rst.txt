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

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[2]** _[#] :  endnote number
-------------------------------------

.. raw:: html

    <hr>


.. topic:: *text* _[#] 
    
   end of line - text is wrapped when formatted. _[#]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[3]** __ : horizontal line
--------------------------------------- 
.. raw:: html

    <hr>

.. topic:: 4 or more underscores ____ 

    ___________  

    
outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[4]** _[B] :  bold, center
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[B]

    This text will be bold and centered _[B]

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[5]** _[C] :  center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    This text will be centered _[C]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[6]** _[E] : equation label 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   This label will be assigned an equation number  _[E]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[7]** _[F] : figure label 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[F]

   This caption will be assigned a figure number _[F]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[8]** _[L] : LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[L]

    \frac{1}{\sqrt{x}} _[L]

This math expression will be formated in LaTeX.

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[9]** _[D] : link docs
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[D] report link 
    
    text at end of line _[D] doc-file-name, link label

Links *docs* within a report

outputs: text, pdf, html


**[10]** _[S] : link sections
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[S] doc link
    
    *text* _[S] section number, link label

Links *sections* within a *doc*

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[11]** _[U] : link urls
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[U] url link  
    
    text at end of line _[U] urlname, link label

outputs: text, pdf, html


**[12]** _[M] : math equation
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[M]

    f(x,y) = sin(x) + y/5 _[M]

This math expression will be formated in ASCII text.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[13]** _[T] : table label
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

   An autonumbered table title _[T]

This table title will be assigned a table number.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[14]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

    this will start a new page _[P]

outputs: text, pdf, html


**[15]** _[[B]] : bold indent
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

outputs: text, pdf, html


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

outputs: pdf, html


**[18]** _[[E]] : endnote text
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


**[19]** _[[I]] : indent italic
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


**[20]** _[[N]] :  indent
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


**[21]** _[[T]] : topic
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


**[22]** **COMMAND KEY**
---------------------------

.. raw:: html

    <hr>

.. topic:: | COMMAND | relative path | parameters

  example

outputs: types of outputs


**[23]** | IMG | - insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | relative path | scale, caption (_[F])

    | IMG | src/file1.png | .50, Map _[F]

The command reads PNG and JPEG files (.png, jpg). The file path is relative to
the report folder. 

outputs: PDF, HTML


**[24]** | IMG2 | - adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | rel path1, rel path2| sc1, sc2, cap1 (_[F]), cap2 (_[F])  

    | IMG | src/file1.png, src/file2.png | .50, .40, Map, Plan

The command reads PNG and JPEG files (.png, jpg). The file path is relative to
the report folder. 

outputs: PDF, HTML


**[25]** | TABLE | - format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | rel path | title (_[T])

    | TABLE | src/file1.csv | Forces _[T]

The command reads reads text, csv and EXCEL files (.txt, .csv, .xls). The file
path is relative to the report folder.

outputs: text, PDF HTML


**[26]** | TEXT | - format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | text | rel path | normal, literal

    | TABLE | src/file1.txt  | normal

The command reads text and reST files (.txt, .tex, .rst). The parameters
specify whether the text is wrapped or treated as a literal. The file path is
relative to the report folder.

outputs: text, PDF HTML

