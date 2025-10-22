**C.5 Values - rv.V**
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

**[2]** _[#] : endnote number
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

.. topic:: _[H] or 4 or more underscores

    ___________  or _[H]
    
outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[4]** _[A] : ASCII math
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[A]

    f(x,y) = sin(x)**2 + y/5 _[A]

Math expression will be formated in ASCII text.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[5]** _[L] : LaTeX math 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation* _[L]

    \frac{1}{\sqrt{x}} _[L]

Math expression will be formated in LaTeX, even if LaTeX is not installed.

outputs: pdf, html


.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[6]** _[C] :  center 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[C]

    *This text will be centered* _[C]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[7]** _[E] : equation label 
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *equation label* _[E]

   *Label assigned an equation number*  _[E]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[8]** _[F] : figure label 
-----------------------------------------

.. raw:: html

    <hr>   

.. topic:: *caption* _[F]

   *Caption assigned a figure number* _[F]

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[9]** _[T] : table label
------------------------------------------

.. raw:: html

    <hr>

.. topic:: *title* _[T]

   *An autonumbered table title* _[T]

Table title will be assigned a table number.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[10]** _[D] : link docs
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[D] report link 
    
    *text at end of line* _[D] doc-file-name, link label

Links *docs* within a report

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[11]** _[S] : link sections
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[S] doc link
    
    *text* _[S] section number, link label

Links *sections* within a *doc*

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[12]** _[U] : link urls
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: *text* _[U] url link  
    
    *text at end of line* _[U] urlname, link label

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[13]** _[P] : new page
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: _[P]

     _[P]

This starts a new page.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


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

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

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

Formats LaTeX, which needs to be installed.

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[16]** _[[E]] : endnote text
-------------------------------------------    

.. raw:: html

    <hr>


.. topic:: _[[E]] 
    
    ::
   
        _[[E]]
        this is an endnote - assigned to an endnote tag [#] in order of
        of processing.
        _[[Q]] 

Formats an endnote.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


**[17]** _[[T]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[T]] *topic title*

    ::
        
        _[[T]] topic title
        text
        text
        ...
        _[[Q]]

Formats a colored highlight block with a title.

outputs: pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[18]** _[[V]] : values
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[V]] 

    ::
        
        _[[T]] topic title
        a := 1*IN  | IN, M, 2 | thickness
        b := 10*IN  | IN, M, 2 | length
        _[[Q]]

Reads values from a block and writes values to a file *vnum-s.csv* where *num*
is the *doc number* and *s* is the section number.

outputs: text, pdf, html

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[19]** **COMMAND KEY**
---------------------------

.. raw:: html

    <hr>

.. topic:: | COMMAND | relative path | parameters

  example

outputs: types of outputs

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[20]** | FUNC | Python functions 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | FUNC | relative path |  user-namespace; rvnamespace
   
    | FUNC | src/tools/functions.py | f1

Imports .py files. Functions (methods) are stored. If the parameter is
*rvnamespace* the module is imported into the rivt file namespace.
Otherwise the module is imported into a user specified namespace.

Functions are evaluated using the assigne (<=) command in the *Value API
function*.

outputs: text, pdf, html


**[21]** | IMG | : insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG | relative path | scale, caption (_[F])

    | IMG | src/file1.png | .50, Map _[F]

Reads PNG and JPEG files (.png, jpg). The file path is relative to
the report folder. 

outputs: PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[22]** | IMG2 | : adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMG2 | rel path1, rel path2| sc1, sc2, cap1 (_[F]), cap2 (_[F])  

    | IMG | src/file1.png, src/file2.png | .50, .40, Map, Plan

Reads PNG and JPEG files (.png, jpg) and places them side by side in the
document. The file path is relative to the report folder.

outputs: PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[23]** | TABLE | : format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | relative path | width, l;c;r, title  (_[T])

    | TABLE | src/file1.csv | 30, c, Forces _[T]

Reads text, csv and EXCEL files (.txt, .csv, .xls) and outputs formatted
tables. The file path is relative to the report folder. The width parameter
specifies the maximum column width. The l,c,r parameter specifies cell
justification (left, center, right).

outputs: text, PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[24]** | VALUES | : format values
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | VALUE | rel path | hide; insert

    | VALUE | src/file1.csv  | hide; insert

Reads a value file (.csv). The file path is relative to the report folder. The
insert parameter specifies whether the value table is visible in the doc.  

outputs: text, PDF HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[25]** **<=** : assign equation value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b <= a * 10 | unit1, unit2, decimals | reference

    b_1 <= E_1 * 12.1*IN^2 | KIP, kN, 2 | Std. 123
  
Assigns a variable or variables to an equation or function value and writes the
values to a file *vnum-s.csv* where *num* is the *doc number* and *s* is the
section number. The file is written to the folder *src/values* unless
*rvsource* is set to *True* in the *Meta API function*.
  
outputs: text, PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[26]** **:=** : define value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: c := 5*unit1 | unit1, unit2, decimals | description

    D_1 = 10*IN | IN, M, 3 | beam depth
  
Defines a variable value and writes values to a file *vnum-s.csv* where *num*
is the *doc number* and *s* is the section number.
  
outputs: text, PDF, HTML