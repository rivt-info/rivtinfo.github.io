**C.4 Commands**
========================

**[1t]** Command Summary
-------------------------------------

.. raw:: html

    <hr>

========== ============================================================== ========================
API Scope           | Command | path | parameters                          Description
========== ============================================================== ========================
rv.R        **| SHELL |** rel path | os, wait                               :ref:`Shell file`
rv.I        **| TEXT |** rel path |  language                               :ref:`Text file`
rv.V, I     **| TABLE |** rel path | title, width, rows, align, head        :ref:`Table file`     
rv.V, I     **| IMAGE |** rel path | caption, scale, number                 :ref:`Image file`
rv.V, I     **| IMAGE2 |** rel path1, rel path2 | caption, scale number     :ref:`Adjacent images`
rv.V        **| VALTABLE |** rel path | title, rows, number                 :ref:`Values file`     
rv.V        a **=:** 1*IN  | unit1, unit2, decimal | label                  :ref:`Define variable`
rv.V        c **<=:** expression | unit1, unit2, decimal | label            :ref:`Assign value`
rv.V        a **<** c  | decimal | text, align, color                       :ref:`Compare values`
rv.T, V     **| PYTHON |** rel path | namespace                             :ref:`Python file`
rv.T        **| MARKUP |** rel path | type                                  :ref:`Markup file`
rv.D        **| ATTACHPDF |** rel path | place, title                       :ref:`Attach PDF`   
rv.D        **| PUBLISH |** rel path (ini) | type                           :ref:`Publish doc` 
========== ============================================================== ========================

**Default command paths**

See :ref:`here <report folders>` for the folder structure. If files
are in the default path only the file name needs to be provided.

================ =========================
   Command         Default Path
================ =========================
\| SHELL |          **/Src/Shell/**
\| TEXT |           **/Src/Data/**
\| TABLE |          **/Src/Data/**
\| IMAGE |          **/Src/Image/**
\| IMAGE2 |         **/Src/Image/**
\| VALTABLE |       **/Src/Data/**   [1]    
\| PYTHON |         **/Src/Scripts/**
\| MARKUP |         **/Src/Scripts/**
\| ATTACHPDF |      **/Src/Gendocs/**  
\| PUBLISH |        **/Src/Gendocs/**
================ =========================

[1]  use /stored/data/filename to read values previously defined and stored


.. _Shell file:

**[2t]** Shell file
-------------------------------------------

.. raw:: html

    <hr>

The SHELL command runs shell scripts including .cmd, .bat and .sh files. 
The *os* parameter specifies the operating system: *win*, *mac* or *linux*. 
The *wait; nowait* specifies whether rivt file processing waits for the
script to complete before continuing.

If the *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/run/* . Otherwise the path is specified relative
to the report root (rivt file folder). If the doc is a single doc the file is
read from the rivt file folder.

.. topic:: | SHELL | 

    .. code-block:: text

        Syntax:
            | SHELL | relative file path | win;mac;linux,wait;nowait

        Example:
            | SHELL | file1.cmd | win, nowait

=========== ==========================
API Scope     Run
File Types   .cmd, .bat, .sh, .bsh 
Doc Types     text, PDF, HTML
=========== ==========================


.. _Text file:

**[3t]** Text file
------------------------------------------

.. raw:: html

    <hr>

The TEXT command reads and formats text and code files. The language parameter
specifies formatting and syntax coloring.  Language types include:

- *literal*
- *python*
- *text*
- *sh*
- *cmd*
- *reStructuredText*

The *literal* type inserts text into the *doc* without formatting.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

.. topic:: | TEXT | 

    .. code-block:: text

        Syntax:
            | TEXT | relative file path | language - see list above

        Example:
            | TEXT | file1.txt | literal

=========== =====================================
API Scope     Insert
File Types    txt, .py, .cmd, .bat, .sh, .rst 
Doc Types     text, PDF, HTML
=========== =====================================

.. _Table file:

**[4t]** Table file
------------------------------------------

.. raw:: html

    <hr>

The TABLE command reads csv, xls, and rst files and outputs formatted tables.
The title may be ommited by inserting a hyphen "-". The width parameter
specifies the maximum character width of a column. The align parameter
specifies the cell justification - left, center, right. The number parameter
specifies whether the table is numbered. For csv files, the head parameter
specifies whether the first row is a column header.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
:term:`single doc` the file is read from the rivt file folder.

.. topic:: | TABLE |   

    .. code-block:: text

        Syntax:
            | TABLE | rel path | title, max width, rows, l;c;r, head;nohead, num;nonum 

        Example:
            | TABLE | file1.csv | Forces, 30, 0:0, c, nohead, num 

=========== ==========================
API Scope     Insert, Values
File Types    csv, xls, rst
Doc Types     text, PDF, HTML
=========== ==========================

.. _Image file:

**[5t]** Image file
-------------------------------------------

.. raw:: html

    <hr>

The IMAGE command reads a PNG or JPEG file and centers it in the *doc*. The
scale parameter is a decimal fraction of the page width. The caption may be
ommited by using a single hyphen. The *num;nonum* parameter specifies whether
to assign a figure number. The image path is inserted in the text *doc* instead
of the image.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/img/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a :term:`single doc` 
the file is read from the rivt file folder.

.. topic:: | IMAGE | 

    .. code-block:: text

        Syntax:
            | IMAGE | relative path | caption, scale, num;nonum

        Example:
            | IMAGE | file1.png | Map, 0.5, num

=========== ==========================
API Scope     Insert, Values
File Types    PNG, JPG 
Doc Types     PDF, HTML
=========== ==========================

.. _Adjacent images:

**[6t]** Adjacent images
--------------------------------------------------

.. raw:: html

    <hr>

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

.. topic:: | IMAGE2 | 

    .. code-block:: text

        Syntax:
            | IMAGE2 | relative path | cap1, cap2, scale1, scale2, num;nonum, num;nonum

        Example:
            | IMAGE2 | file1.png, file2.png | Map, Photo, .5,.5, num, num

=========== ==========================
API Scope     Insert, Values
File Types    PNG, JPG jenn
Doc Types     PDF, HTML
=========== ==========================

.. _Values file:

**[7t]**  Valtable file
------------------------------------------------

.. raw:: html

    <hr>

The VALTABLE command imports and defines values from a *csv* or *xls* file. 
The file format is:: 

    var = value, unit1, unit2, decimal, label

The path variable is either from *src* or *stored* depending on if the values
were generated by rivtlib or provided by the author. The title parameter is the
table title. A hyphen omits the title. The *rows* parameter specifies the rows
to import. The *num; nonum* parameter specifies whether to assign a table
number to the values table.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/vals/* . Otherwise the path needs to be
specified relative to the report root (rivt file folder). If the values are
read from prior calculated values, they will be found in the */stored/vals*
folder. If the doc is a :term:`single doc` the file is read from the rivt file
folder.

.. topic::  | VALTABLE | 

    .. code-block:: text

        Syntax:
            | VALTABLE | relative path | title, rows, *num;nonum*

        Example:
            If read from the default folder:
            | VALTABLE | newvals.csv | Beam Properties, 1:10, num
            If read from the stored folder:
            | VALTABLE | /stored/vals/vA01-2.csv | Beam Properties, 1-10, num

=========== ==========================
API Scope     Values
File Types    .csv, .xls, 
Doc Types     text, PDF, HTML
=========== ==========================

.. _Define variable:

**[8t]** Define variable
-------------------------------------------

.. raw:: html

    <hr>

Defines a value and writes it to the file *vdocnum-s.csv* where *num* is the 
*docnumber* and *s* is the section number. The file is written to the folder
*stored/vals* unless *singledocB* is set to *True* in the comment variable.

The stored values can read and defined in other rivt files using the VALUES
command.

.. topic:: =: 

    .. code-block:: text

        Syntax:
            c =: 5*unit | unit1, unit2, decimals | label, *num,nonum*
    
        Example:
            D_1 =: 10*IN | IN, M, 3 | beam depth, num
  
=========== ==========================
API Scope     Values
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _Assign value:

**[9t]** Assign value
-------------------------------------------

.. raw:: html

    <hr>

Assigns a value to an equation or function variable and writes the values to a
file *vdocnum-s.csv* where *num* is the *doc number* and *s* is the section
number. The file is written to the folder *stored/vals* unless *singledocB* is
set to *True* in the comment variable.

The label is a reference printed with the equation. The units specify the
result expressed in two different units. The integer specifies the number of
places after the decimals.

.. topic:: <=: 

    .. code-block:: text

        Syntax:
            b <=: a * 10*FT | unit1, unit2, decimals | label, *num;nonum*
    
        Example:
            b_1 <=: E_1 * 12.1*IN^2 | KIP, KN, 2 | Std. 123, num

            c_1 <=: func1(a,b) | KIP, KN, 2 | ACI 318-19 Table 22.5.5.1, num 


=========== ==========================
API Scope     Values
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _Compare values:

**[10t]** Compare values
-----------------------------------------

.. raw:: html

    <hr>

Inserts a text with alignment and color on the following line if the
expression evaluates to true. Alignment can be *r;l;c* for right, left or
center. Colors can be *red;blue;yellow;green;black;gray* defined in the *style
files*. 

Comparison operators:

- ==	Equal	x == y	
- !=	Not equal	x != y	
- >	Greater than	x > y	
- <	Less than	x < y	
- >=	Greater than or equal to	x >= y	
- <=	Less than or equal to	x <= y

.. topic:: <> 

    .. code-block:: text

        Syntax:  
            a < b **_[S]** text, r, red
    
        Example:
           a < b **_[S]** text, r, red
  
=========== ==========================
API Scope     Values
Doc Types     text, PDF, HTML
=========== ==========================


.. _Python file:

**[11t]** Python file
-------------------------------------------

.. raw:: html

    <hr>

Executes Python code in the *rivt namespace* or user specified namespace. File
paths used in the script are relative to the root *rivt* folder.

.. topic:: | PYTHON |

    .. code-block:: text

        Syntax:
            | PYTHON | relative path | *rvspace*; user space
  
        Example:
            | PYTHON | script1.py | rv-space

=========== ==========================
API Scope     Values, Tools
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _Markup file:

**[12t]**  Markup file
-------------------------------------------

.. raw:: html

    <hr>

Inserts HTML into an HTML *doc*, LaTeX into a PDF *doc*, and reStructuredText
into either PDF or HTML. LaTeX requires the installation of *texlive*.

.. topic:: | MARKUP |

    .. code-block:: text

        Syntax:
            | MARKUP | relative path | *rst, html, latex*
  
        Example:
            | MARKUP | script.rst | rst

=========== ==========================
API Scope     Tools
File Types    html, rst, tex
Doc Types     text, PDF, HTML
=========== ==========================

.. _Attach PDF:

**[13t]** Attach PDF
-------------------------------------------

.. raw:: html

    <hr>

Appends or prepends a PDF file to the *doc*. The title parameter generates an
Appendix cover page with the specified title. A "-" omits the over page. For
HTML *docs* the file is inserted as a donwload link.

.. topic:: | ATTACHPDF |

    .. code-block:: text

        Syntax:
            | ATTACHPDF | relative path | *front;back*, title
  
        Example:
            | ATTACHPDF | relative path | *front;back*, title
 



=========== ==========================
API Scope     Doc
File Types    tex, html, text, pdf
Doc Types     text, PDF, HTML
=========== ==========================

.. _Publish doc:

**[14t]** Publish doc
-------------------------------------------

.. raw:: html

    <hr>

Publishes a *doc*. 

.. topic:: | PUBLISH |

    .. code-block:: text

        Syntax:
            | PUBLISH | ini relative path | rst2pdf, texpdf, tex, hmtl
    
        Example:
            | PUBLISH | ini relative path | rst2pdf

=========== ==========================
API Scope     Doc
File Types    tex, html, text, pdf
Doc Types     text, PDF, HTML
=========== ==========================

