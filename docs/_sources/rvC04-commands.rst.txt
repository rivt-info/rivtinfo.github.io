**C.4 Commands**
========================

**[1t]** Summary
-------------------------------------

.. raw:: html

    <hr>

**Read, write and format files**

========== ============================================================== =====================
API Scope           | Command | path | parameters                          Description
========== ============================================================== =====================
rv.R       \| SHELL | relative path | os, wait                             :ref:`shellcmd`
rv.I,V     \| IMAGE | relative path |  scale, caption, figure              :ref:`imgcmd`
rv.I,V     \| IMAGE2 | rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2   :ref:`img2cmd`
rv.I,V     \| TABLE | relative path | width, align, title (_[T]) [1]       :ref:`tablecmd`     
rv.I,V     \| TEXT | relative path |  language                             :ref:`textcmd`
rv.V       \| VALUES | relative path | title, rows                         :ref:`valcmd` 
rv.V       a := 1*IN  | unit1, unit2, decimal | label                      :ref:`defcmd`
rv.V       c <= expression | unit1, unit2, decimal | label (_[E]) [1]      :ref:`asscmd`
rv.V,T     \| PYTHON | relative path | namespace                           :ref:`pycmd`
rv.T       \| SCRIPT | relative path | type                                :ref:`scriptcmd`
rv.D       \| PDFAPPEND | relative path | place, cover                     :ref:`appcmd`   
rv.D       \| PUBLISH | ini rel. path | type                               :ref:`pubcmd` 
========== ============================================================== =====================

.. highlight:: none

::

    [1] optional tags number the equation or table

.. _shellcmd:

**[2t]** run shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | SHELL | relative path | os, *nowait; wait*

    | SHELL | file.cmd | win, nowait

The SHELL command runs shell scripts including .cmd, .bat and .sh files. 
The *os* parameter specifies the operating system: *win*, *mac* or *linux*. 
The *wait; nowait* specifies whether rivt file processing waits for the
script to complete before continuing.

If the doc is part of a report and no path is specified, the file is assumed to
be in the default folder */src/run/* . Otherwise the path is specified relative
to the report root (rivt file folder) If the doc is a single doc the file is
read from the rivt file folder.

API: Run
file types: .cmd, .bat, .sh
docs: text, PDF, HTML

.. _imgcmd:

**[3t]** insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | relative path | scale, caption, figure

    | IMAGE | file1.png | .5, Map, fig 

The IMAGE command reads a PNG or JPEG file and centers it in the *doc*. The
scale parameter is a decimal fraction of the page width. The caption may be
ommited by using a single hyphen. The *fig;nofig* parameter specifies whether
to assign a figure number.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/img/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

API: Insert, Values
file types: .png, .jpg
docs: text, PDF, HTML

.. _img2cmd:

**[4t]** insert adjacent images
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | rel path1, rel path2 | sc1, sc2, cap1, cap2, fig1, fig2

    | IMAGE2 | file1.png, file2.png | .5, Map, fig 

The IMAGE2 command reads two PNG or JPEG file and center them side by side in
the *doc*. The scale parameters are a decimal fraction of the page width. The
captions may be ommited by using a single hyphen for either or both images. The
*fig;nofig* parameters specify whether to assign a figure number to either or
both images.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/img/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

For text docs the image file path is inserted. 

API: Insert, Values
file types: .png, .jpg
docs: text, PDF, HTML

.. _tablecmd:

**[5t]** format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | relative path | width, *l;c;r*, title  (_[T])

    | TABLE | file1.csv | 30, c, Forces _[T]

The TABLE command reads csv and EXCEL files and outputs formatted
tables. The width parameter specifies the maximum character width of a column. 
The align parameter specifies the cell justification (left, center, right). 
The *Table tag* may be added to the caption.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.


API: Insert, Values
file types: .csv, .xls
docs: text, PDF, HTML

.. _textcmd:

**[6t]** format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TEXT | relative path | *literal*; code 

    | TEXT | src/file1.py  | python

The TEXT command reads and formats text and code files. The language parameter
specifies formatting and syntax coloring.  Languages include:

    - *literal*
    - *python*
    - *bash*
    - *sh*
    - *cmd*

The *literal* type inserts text into the *doc* without formatting.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.


API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML

.. _valcmd:

**[7t]**  import values
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  | VALUES | relative path | *show;hide*

        
    | VALUES | src/data/newvals.csv | show

Defines values and writes them to */store/vals* folder.

API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML

.. _defcmd:

**[8t]** **:=** : define value
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: c := 5*unit | unit1, unit2, decimals | label

    D_1 := 10*IN | IN, M, 3 | beam depth
  
Defines a value and writes to a file *vnum-s.csv* where *num* is the *doc
number* and *s* is the section number. The file is written to the folder
*out/values* unless *rv_localB* is set to *True* in the *Meta API function*.
  
API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML

.. _asscmd:

**[9t]** **<=** : assign value
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
  
API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML


.. _pycmd:

**[10t]** import Python script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PYTHON | src/path | *rv-space*; user space
   
    | PYTHON | script1.py | rv-space

Executes Python code in the *rivt namespace* or user specified namespace. File
paths used in the script are relative to the *rivt file* folder.

API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML

.. _scriptcmd:

**[11t]**  import tool script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | SCRIPT | relative path | *rst, html, latex*

    | SCRIPT | page1.html | code excerpt

Reads and inserts .tex files into *doc*. May require installation of LaTeX.

API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML

.. _appcmd:

**[12t]** append PDF
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | SCRIPT | relative path | *rst, html, latex*

    | SCRIPT | page1.html | code excerpt

Reads and inserts .html and .htm files into *doc*. 

API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML

.. _pubcmd:

**[13t]** publish doc
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | SCRIPT | relative path | *rst, html, latex*

    | SCRIPT | page1.html | code excerpt

Reads and inserts .html and .htm files into *doc*. 

API: Insert, Values
file types: .txt, .py, .cmd, .sh, .bash
docs: text, PDF, HTML

