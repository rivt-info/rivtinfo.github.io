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
rv.I       \| TEXT | relative path |  language                             :ref:`textcmd`
rv.I       \| TABLE | rel path | title, width, rows, align, head           :ref:`tablecmd`     
rv.V, I    \| IMAGE | relative path |  scale, caption, figure              :ref:`imgcmd`
rv.V, I    \| IMAGE2 | rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2   :ref:`img2cmd`
rv.V       \| VALTABLE | rel path | title, width, rows                     :ref:`valtablecmd`     
rv.V       a =: 1*IN  | unit1, unit2, decimal | label                      :ref:`defcmd`
rv.V       c <=: expression | unit1, unit2, decimal | label                :ref:`asscmd`
rv.V       a < c  | decimal | text, align, color                           :ref:`compcmd`
rv.T,V     \| PYTHON | relative path | namespace                           :ref:`pycmd`
rv.T       \| MARKUP | relative path | type                                :ref:`scriptcmd`
rv.D       \| PDFATTACH | relative path | place,title                      :ref:`attcmd`   
rv.D       \| PUBLISH | ini rel. path | type                               :ref:`pubcmd` 
========== ============================================================== =====================

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

If the *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/run/* . Otherwise the path is specified relative
to the report root (rivt file folder). If the doc is a single doc the file is
read from the rivt file folder.

=========== ==========================
API Scope     Run
File Types   .cmd, .bat, .sh 
Doc Types     text, PDF, HTML
=========== ==========================

.. _imgcmd:

**[3t]** insert image
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE | relative path | scale, caption, *fig;nofig*

    | IMAGE | file1.png | .5, Map, fig 

The IMAGE command reads a PNG or JPEG file and centers it in the *doc*. The
scale parameter is a decimal fraction of the page width. The caption may be
ommited by using a single hyphen. The *fig;nofig* parameter specifies whether
to assign a figure number. The image path is inserted in the text *doc* instead
of the image.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/img/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

=========== ==========================
API Scope     Insert, Values
File Types    PNG, JPG 
Doc Types     PDF, HTML
=========== ==========================

.. _img2cmd:

**[4t]** insert adjacent images
--------------------------------------------------

.. raw:: html

    <hr>

.. topic:: | IMAGE2 | rel path1, rel path2 | sc1, sc2, cap1, cap2, fig, fig

    | IMAGE2 | file1.png, file2.png | .5,.5, Map, Photo, fig, fig 

The IMAGE2 command reads two PNG or JPEG file and places them side by side in
the *doc*. The scale parameters are a decimal fraction of the page width. The
captions may be ommited by using a single hyphen for either or both images. The
*fig;nofig* parameters specify whether to assign a figure number to either or
both images. The image path is inserted in the text *doc* instead
of the image.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/img/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

=========== ==========================
API Scope     Insert, Values
File Types    PNG, JPG 
Doc Types     PDF, HTML
=========== ==========================

.. _textcmd:

**[5t]** format text
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TEXT | relative path | language

    | TEXT | file1.py  | python

The TEXT command reads and formats text and code files. The language parameter
specifies formatting and syntax coloring.  Languages include:

    - *literal*
    - *python*
    - *bash*
    - *sh*
    - *cmd*
    - *reStructuredText*

The *literal* type inserts text into the *doc* without formatting.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

=========== ==========================
API Scope     Insert, Values
File Types    txt, .py, .cmd, .bat, .sh, .rst 
Doc Types     text, PDF, HTML
=========== ==========================

.. _tablecmd:

**[6t]** format table
------------------------------------------

.. raw:: html

    <hr>

.. topic:: | TABLE | rel path | title, width, rows, *l;c;r*, *head;nohead*, *num,nonum*  

    | TABLE | file1.csv | Forces, 30, c, nohead, num 

The TABLE command reads csv, xls, and rst files and outputs formatted tables.
The title may be ommited by inserting a hyphen "-". The width parameter
specifies the maximum character width of a column. The align parameter
specifies the cell justification (left, center, right). The head parameter
specifies whether the first row is a column header.The number parameter
specifies whether the table is numbered.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

=========== ==========================
API Scope     Insert, Values
File Types    csv, xls, rst
Doc Types     text, PDF, HTML
=========== ==========================

.. _valtablecmd:

**[7t]**  read values
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  | VALTABLE| relative path | title, width, rows, *num,nonum*

    If read from the default folder:

    | VALTABLE | newvals.csv | Beam Properties, 30, 1-10, num

    If read from the stored folder:

    | VALTABLE | /stored/vals/vA01-2.csv | Beam Properties, 30, 1-10, num

The VALTABLE command imports and defines values from a *csv* or *xls* file. 
The file format is:: 

    var = value, unit1, unit2, decimal, label

The path variable is either from *src* or *stored* depending on if the values
were generated by rivtlib or provided by the author. The *rows* parameter
specifies the rows to import. The title parameter is the table title. A hyphen
omits the title. The *num; nonum* parameter specifies whether to assign a table
number to the values table.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/vals/* . Otherwise the path needs to be
specified relative to the report root (rivt file folder). If the values are
read from prior calculated values, they will be found in the */stored/vals*
folder. If the doc is a :term:`single doc` the file is read from the rivt file
folder.

=========== ==========================
API Scope     Values
File Types    .csv, .xls, 
Doc Types     text, PDF, HTML
=========== ==========================

.. _defcmd:

**[8t]** define variable
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: c =: 5*unit | unit1, unit2, decimals | label, *num,nonum*

    D_1 =: 10*IN | IN, M, 3 | beam depth, num
  
Defines a value and writes it to the file *vdocnum-s.csv* where *num* is the 
*docnumber* and *s* is the section number. The file is written to the folder
*stored/vals* unless *singledocB* is set to *True* in the comment variable.

The stored values can read and defined in other rivt files using the VALUES
command.
  
=========== ==========================
API Scope     Values
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _asscmd:

**[9t]** assign variable
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: b <=: a * 10*FT | unit1, unit2, decimals | label, *num;nonum*

    b_1 <=: E_1 * 12.1*IN^2 | KIP, KN, 2 | Std. 123, num

    c_1 <=: func1(a,b) | KIP, KN, 2 | ACI 318-19 Table 22.5.5.1, num 

Assigns a value to an equation or function variable and writes the values to a
file *vdocnum-s.csv* where *num* is the *doc number* and *s* is the section
number. The file is written to the folder *stored/vals* unless *singledocB* is
set to *True* in the comment variable.

The label is a reference printed with the equation. The units specify the
result expressed in two different units. The integer specifies the number of
places after the decimals.

=========== ==========================
API Scope     Values
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _compcmd:

**[10t]** compare
-----------------------------------------

.. raw:: html

    <hr>

.. topic:: expression | decimal | text, align, color

   a < b **_[S]** text, r, red

Inserts a text stamp, alignment and color on the following line if the
expression evaluates to true. Alignment can be *r;l;c* for right, left or
center. Colors can be *red;blue;yellow;green;black;gray* defined in the *style
files*.

=========== ==========================
API Scope     Values
Doc Types     text, PDF, HTML
=========== ==========================



.. _pycmd:

**[11t]** import Python script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PYTHON | relative path | *rvspace*; user space
   
    | PYTHON | script1.py | rv-space

Executes Python code in the *rivt namespace* or user specified namespace. File
paths used in the script are relative to the *rivt file* folder.

=========== ==========================
API Scope     Values, Tools
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _markupcmd:

**[12t]**  import Markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | MARKUP | relative path | *rst, html, latex*

    | SCRIPT | page1.html | html

Inserts HTML into an HTML *doc*, LaTeX into a PDF *doc*, and reStructuredText
into either PDF or HTML. LaTeX requires the installation of *texlive*.

=========== ==========================
API Scope     Tools
File Types    html, rst, tex
Doc Types     text, PDF, HTML
=========== ==========================

.. _attcmd:

**[12t]** attach PDF
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PDFATTACH | relative path | *front;back*, title

    | ATTACHPDF | file.pdf | back, -

Appends or prepends a PDF file to the *doc*. The title parameter generates an
Appendix cover page with the specified title. A "-" omits the over page. For
HTML *docs* the file is inserted as a donwload link.

=========== ==========================
API Scope     Values, Tools
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _pubcmd:

**[13t]** publish doc
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PUBLISH | ini relative path | *rst2pdf, texpdf, tex, hmtl* 

    | PUBLISH | ini relative path | *rst2pdf, texpdf, tex, hmtl* 

Reads and inserts .html and .htm files into *doc*. 

=========== ==========================
API Scope     Values, Tools
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

