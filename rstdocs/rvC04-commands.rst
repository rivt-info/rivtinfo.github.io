**C.3 Commands**
========================

**Summary**

**[1t]** Summary
-------------------------------------

.. raw:: html

    <hr>

Read, write and format files.

========== ======================================================== ===== ==================
API Scope           | Command | path | parameters                    R/W   input types
========== ======================================================== ===== ==================
rv.R       \| LINUX | relative path | *wait;nowait*                  R     *.sh*
rv.R       \| MACOS | relative path | *wait;nowait*                  R     *.sh*
rv.R       \| WIN | relative path   | *wait;nowait*                  R     *.bat, .cmd*
rv.I,V     \| FIGURE | relative path |  scale, caption               R     *.png, .jpg*
rv.I,V     \| FIGURE2 | relative path | s1, s2, c1, c2               R     *.png, jpg*
rv.I,V     \| IMAGE | relative path |  scale                         R     *.png, .jpg*
rv.I,V     \| IMAGE2 | relative path | scale1, scale2                R     *.png, jpg*
rv.I,V     \| TABLE | relative path | width, l;c;r, title            R     *csv, txt, xlsx*
rv.I,V     \| TEXT | relative path |  *normal;literal* ;code         R     *txt, code*
rv.V       \| VALUES | relative path | title, rows (_[T])            R     *csv*
rv.V       a := 1*IN  | unit1, unit2, decimal | label   (_[E])       W     define a value
rv.V       b <= a + 3*FT | unit1, unit2, decimal | label  (_[E])     W     assign a value
rv.V       c <= func1(x,y) | unit1, unit2, decimal | label (_[E])    W     assign a value
rv.V,T     \| PYTHON | relative path | *rvspace*; userspace          R     *py*
rv.T       \| HTML | relative path | reference                       R     *html*
rv.T       \| LATEX | relative path | reference                      R     *tex*
rv.T       \| RST | relative path | reference                        R     *tex*
rv.D       \| PREPEND | relative path | *none*;title                 W     *pdf*
rv.D       \| APPEND | relative path | *none*,title                  W     *pdf*
rv.D       \| PUBLISH | ini rel. path | *rst2pdf;pdftex;text;html*   W     *pdf, html, txt*
========== ======================================================== ===== ==================



**[20t]** | IMAGE | : insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | relative path | scale, caption (_[I])

    | IMG | src/file1.png | .50, Map _[I]

Reads PNG and JPEG files (.png, jpg) and inserts them in the *doc*. The *Image
tag* may be added to the captions. 

outputs: PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[21t]** | IMAGE2 | : insert adjacent images 
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | rel path1, rel path2| sc1, sc2, cap1 (_[I]), cap2 (_[I])  

    | IMAGE2 | src/file1.png, src/file2.png | .50, .40, Map _[I], Plan _[I]

Reads PNG and JPEG files (.png, jpg) and inserts them side by side in the
document. The *Image tag* may be added to the captions.

outputs: PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[22t]** | TABLE | : format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | relative path | width, l;c;r, title  (_[T])

    | TABLE | src/file1.csv | 30, c, Forces _[T]

Reads text, csv and EXCEL files (.txt, .csv, .xls) and outputs formatted
tables. The width parameter specifies the maximum column width. The l,c,r
parameter specifies cell justification (left, center, right). The *Table tag*
may be added to the caption.

outputs: text, PDF, HTML

.. raw:: html

    <p style="text-align: right;"> &lt;i&gt; </p>

**[23]** | TEXT | : format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TEXT | relative path | *literal*; code 

    | TEXT | src/file1.py  | python

Reads and formats text and code files. The parameters specify formatting and
syntax coloring.  Languages include:

    - *python*
    - *bash*
    - *sh*
    - *cmd*

outputs: text, PDF, HTML

**[23t]** | VALUES | : table title
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  | VALUES | relative path | *show;hide*

        
    | VALUES | src/data/newvals.csv | show

Defines values and writes them to *out* folder.

outputs: pdf, html

**[24t]** **:=** : define value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: c := 5*unit | unit1, unit2, decimals | label

    D_1 := 10*IN | IN, M, 3 | beam depth
  
Defines a value and writes to a file *vnum-s.csv* where *num* is the *doc
number* and *s* is the section number. The file is written to the folder
*out/values* unless *rv_localB* is set to *True* in the *Meta API function*.
  
outputs: text, PDF, HTML

**[25t]** **<=** : assign value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b <= a * 10*FT | unit1, unit2, decimals | label (_[E])

    b_1 <= E_1 * 12.1*IN^2 | KIP, KN, 2 | Std. 123

    c <= func1(a,b) | KIP, KN, 2 | ACI 318-19 Table 22.5.5.1 

Assigns a value to an equation or function variable and writes the
values to a file *vnum-s.csv* where *num* is the *doc number* and *s* is the
section number. The file is written to the folder *out/values* unless
*rv_localB* is set to *True* in the *Meta API function*.
  
outputs: text, PDF, HTML


**[6t]** | HTML | HTML markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | HTML | src/path | label

    | HTML | src/tools/page1.html | code excerpt

Reads and inserts .html and .htm files into *doc*. 

outputs: text, pdf, html

**[7t]** | LATEX | LaTeX markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | src/path | label

    | LATEX | src/tools/page1.tex | frame analysis

Reads and inserts .tex files into *doc*. May require installation of LaTeX.

outputs: text, pdf, html

**[8t]** | RST | reStructuredText markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | src/path | label

    | LATEX | src/tools/page1.tex | frame analysis

Reads and inserts .tex files into *doc*. May require installation of LaTeX.

outputs: text, pdf, html


**[9t]** | PYTHON | Python script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PYTHON | src/path | *rv-space*; user space
   
    | PYTHON | src/tools/script1.py | rv-space

Executes Python code in the *rivt namespace* or user specified namespace. File
paths used in the script are relative to the *rivt file* folder.

outputs: text, pdf, html

**[5]** | WIN | - command script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | WIN | relative path | nowait;wait

  | WIN | src/run/file.cmd | nowait


reads .txt, .cmd, .bat  files

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[6]** | MACOS | - shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | relative path | nowait;wait

  | MACOS | src/run/file.cmd | nowait

reads .sh files

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[7]** | LINUX | - shell script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LINUX | relative path | nowait;wait

  | LINUX | src/run/file.cmd | nowait

reads .sh files
