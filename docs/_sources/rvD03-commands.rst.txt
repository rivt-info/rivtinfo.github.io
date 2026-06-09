**D.3 | Commands**
========================


.. _command-summary:

**[1]** Command Summary
-------------------------------------


**Commands format files and equations**

========== =============================================================== ========================
API Scope           Command                                                        Description
========== =============================================================== ========================
rv.R        **| MARKUP |** rel path | type                                   :ref:`Markup file`
rv.V, I     **| TABLE |** rel path | title,width,head;nohead,num;non         :ref:`Table file`     
rv.V, I     **| IMAGE |** rel path | caption, scale, num;non, time;not       :ref:`Image file`
rv.V, I     **| IMAGE2 |** rel path1, rel path2 | c1,c2,s1,s2,n1,n2          :ref:`Adjacent images`
rv.V, R     **| PYTHON |** rel path | rivt;namespace                         :ref:`Python file`
rv.V        **| VALTABLE |** rel path | title, width, num;non                :ref:`Values file`   
rv.V        a **==:** 1*IN  | unit1, unit2, decimal | label                  :ref:`Define value`
rv.V        c **<=:** expression | unit1, unit2, decimal | label             :ref:`Assign value`
rv.V        c **:=:** func(x,y) | unit1, unit2, decimal | label              :ref:`Inline function`
rv.V        a **<** c | unit, decimal, text1, text2 | label                  :ref:`Compare value`
rv.V        **| FUNCTION |** function, arg, var, type | label                :ref:`Function value`  
rv.T        **| COPY |** abs src path | abs dest path | file pattern         :ref:`Copy file`
rv.T        **| SHELL |** abs path | os, wait                                :ref:`Shell file`
rv.D        **| ATTACHPDF |** rel path | front;back, title                   :ref:`Attach PDF`   
rv.D        **| PUBLISH |** doc title | type                                 :ref:`Publish doc` 
========== =============================================================== ========================


**Parent paths for commands**

See :ref:`here <report-folders>` for the folder structure. 

================ ========================= ======
   Command           Parent Path [1]        R/W
================ ========================= ======
\| SHELL |          **rivt-report/**           R
\| IMAGE |          **rivt-report/**           R
\| IMAGE2 |         **rivt-report/**           R
\| TABLE |          **rivt-report/**           R
\| VALTABLE |       **rivt-report/**   [2]     R
\| VALTABLE |       **rivt-report/**   [3]     R
\| PYTHON |         **rivt-report/**           R
\| MARKUP |         **rivt-report/**           R
\| ATTACHPDF |      **rivt-report/**           R
\| PUBLISH |        **/_published/**   [4]     W
================ ========================= ======

[1} file paths begin with rvsrc/ and may include subdirectories 
[2] values are read from *rvsrc/* and its subdirectories
[3] values written by *rivt* are read from *rv_stor/vals*  
[4] *docs* are written to subdirectories of *_published*

.. _Shell file:

**[2]** Shell file
-------------------------------------------

The SHELL command runs shell scripts including .cmd, .bat and .sh files. 
The *os* parameter specifies the operating system: *win*, *mac* or *linux*. 
The *wait; nowait* specifies whether rivt file processing waits for the
script to complete before continuing.

If the *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/run/* . Otherwise the path is specified relative
to the report root (rivt file folder). If the doc is a single doc the file is
read from the rivt file folder.

.. code-block:: text

    Syntax:
        | SHELL | relative file path | file name

    Example:
        | SHELL | rvsrc | sap.cmd

=========== ==========================
API Scope     Tools
File Types    .cmd, .bat, .sh, .bsh 
Doc Types     text, PDF, HTML
=========== ==========================


.. _Markup file:

**[3]** Text file
------------------------------------------

The TEXT command reads and formats text and code files. The language parameter
specifies formatting and syntax coloring.  Language types include:

Inserts formatted text into doc. 

- *literal*
- *html*
- *reST*
- *python*
- *endnote*
- *center*
- *bold*
- *italic*
- *mermaid* (node and mermaid-cli must be installed)
- *latex*   (texlive must be installed)  

The *literal* type inserts text into the *doc* without formatting.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
single doc the file is read from the rivt file folder.

.. topic:: | MARKUP |

    .. code-block:: text

        Syntax:
            | MARKUP | relative path | type
        Example:
            | MARKUP | rvsrc/script.rst | rest

=========== =====================================
API Scope     rv.I, rv.V
File Types    txt, .py, .cmd, .bat, .sh, .rst 
Doc Types     text, PDF, HTML
=========== =====================================

.. _Table file:

**[4]** Table file
------------------------------------------

 

The TABLE command reads csv, xls, and rst files and outputs formatted tables.
The title may be ommited by inserting a hyphen "-". The width parameter
specifies the maximum character width of a column. The align parameter
specifies the cell justification - left, center, right. The number parameter
specifies whether the table is numbered. For csv files, the head parameter
specifies whether the first row is a column header.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/data/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
single doc the file is read from the rivt file folder.

.. topic:: | TABLE |   

    .. code-block:: text

        Syntax:
            | TABLE | rel path | title, max width, rows, l;c;r, head;nohead, num;nonum 

        Example:
            | TABLE | file1.csv | Forces, 30, 0:0, c, nohead, num 

=========== ==========================
API Scope     rv.I, rv.V
File Types    csv, xls, rst
Doc Types     text, PDF, HTML
=========== ==========================

.. _Image file:

**[5]** Image file
-------------------------------------------

 

The IMAGE command reads a PNG or JPEG file and centers it in the *doc*. The
scale parameter is a decimal fraction of the page width. The caption may be
ommited by using a single hyphen. The *num;nonum* parameter specifies whether
to assign a figure number. The image path is inserted in the text *doc* instead
of the image.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/img/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a single doc 
the file is read from the rivt file folder.

.. code-block:: text

    Syntax:
        | IMAGE | relative path | caption, scale, num;nonum

    Example:
        | IMAGE | file1.png | Map, 0.5, num

=========== ==========================
API Scope     rv.V, rv.I
File Types    PNG, JPG 
Doc Types     PDF, HTML
=========== ==========================

.. _Adjacent images:

**[6]** Adjacent images
--------------------------------------------------

 

The IMAGE2 command reads two PNG or JPEG file and places them side by side in
the *doc*. The scale parameters are a decimal fraction of the page width. The
captions may be ommited by using a single hyphen for either or both images. The
*fig;nofig* parameters specify whether to assign a figure number to either or
both images. The image path is inserted in the text *doc* instead
of the image.

If a *doc* is part of a report and no path is specified, the file is assumed to
be in the default folder */src/img/* . Otherwise the path needs to be specified
relative to the report root (rivt file folder). If the doc is a 
single doc the file is read from the rivt file folder.

.. code-block:: text

    Syntax:
        | IMAGE2 | relative path | cap1, cap2, scale1, scale2, num;nonum, num;nonum

    Example:
        | IMAGE2 | file1.png, file2.png | Map, Photo, .5,.5, num, num

=========== ==========================
API Scope     rv.I, rv.V
File Types    PNG, JPG jenn
Doc Types     PDF, HTML
=========== ==========================

.. _Values file:

**[7]**  Valtable file
------------------------------------------------

 

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
folder. If the doc is a single doc the file is read from the rivt file
folder.

.. code-block:: text

    Syntax:
        | VALTABLE | relative path | title, rows, *num;nonum*

    Example:
        If read from the default folder:
        | VALTABLE | newvals.csv | Beam Properties, 1:10, num
        If read from the stored folder:
        | VALTABLE | /stored/vals/vA01-2.csv | Beam Properties, 1-10, num

=========== ==========================
API Scope     rv.V
File Types    .csv, .xls, 
Doc Types     text, PDF, HTML
=========== ==========================

.. _Define value:

**[8]** Define value
-------------------------------------------

 

Defines a value and writes it to the file *vdocnum-s.csv* where *num* is the 
*docnumber* and *s* is the section number. The file is written to the folder
*stored/vals* unless *singledocB* is set to *True* in the comment variable.

The stored values can read and defined in other rivt files using the VALUES
command.

.. code-block:: text

    Syntax:
        c =: 5*unit | unit1, unit2, decimals | label, *num,nonum*

    Example:
        D_1 =: 10*IN | IN, M, 3 | beam depth, num
  
=========== ==========================
API Scope     rv.V
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================

.. _Assign value:

**[9]** Assign value
-------------------------------------------

 

Assigns a value to an equation and writes the values to a file *vdocnum-s.csv*
where *num* is the *doc number* and *s* is the section number. The file is
written to the folder *stored/vals* unless *rv single doc* is set to *True* 
in which case values are stored in the rivt file folder (root).

The label is a reference printed with the equation. The units specify the
result expressed in two different units. The integer specifies the number of
places after the decimals.

.. code-block:: text

    Syntax:
        b <=: a * 10*FT | unit1, unit2, decimals | label, num;nonum

    Example:
        b_1 <=: E_1 * 12.1*IN^2 | KIP, KN, 2 | Std. 123, num


=========== ==========================
API Scope     rv.V
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================


.. _Inline function:

**[10]** Inline function
-------------------------------------------

 

Assigns a value to an equation and writes the values to a file *vdocnum-s.csv*
where *num* is the *doc number* and *s* is the section number. The file is
written to the folder *stored/vals* unless *rv single doc* is set to *True* 
in which case values are stored in the rivt file folder (root).

The label is a reference printed with the equation. The units specify the
result expressed in two different units. The integer specifies the number of
places after the decimals.

.. code-block:: text

    Syntax:
        c :=: function name() | unit1, unit2, decimals | label, num;nonum

    Example:

        c_1 :=: func1(a,b) | KIP, KN, 2 | ACI 318-19 Table 22.5.5.1, num 


=========== ==========================
API Scope     rv.V
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================



.. _Compare value:

**[11]** Compare values
-----------------------------------------

Inserts a text with alignment and color on the following line if the expression
evaluates to true. text1 and text2 are printed if true or false repectively.
Colors are assigned accordingly as *red;blue;yellow;green;black;gray* defined
in the *style files*.  The text is right aligned.

Comparison operators:


.. code-block:: text

    ==	  Equal	x == y	
    !=	  Not equal	x != y	
    >	  Greater than	x > y	
    <	  Less than	x < y	
    >=	  Greater than or equal to x >= y	
    <=	  Less than or equal to x <= y

.. topic:: <> 

    .. code-block:: text

        Syntax:  
            a < b | text1, text2, color1, color2
        
        Example:
           a < b |OK, NOT OK, blue, red
  
=========== ==========================
API Scope     rv.V
Doc Types     text, PDF, HTML
=========== ==========================


.. _Python file:

**[12]** Python file
-------------------------------------------

 

Executes Python code in the *rivt namespace* or user specified namespace. File
paths used in the script are relative to the root *rivt* folder.

.. code-block:: text

    Syntax:
        | PYTHON | relative path | *rvspace*; user space

    Example:
        | PYTHON | script1.py | rv-space

=========== ==========================
API Scope     rv.V, rv.T
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================


.. _Function value:

**[13]** Function
-------------------------------------------

Executes Python functions imported by the PYTHON command. 
Function args are defined and named by the [[ARG]] block. 

.. code-block:: text

    Syntax:
        | FUNCTION | func name, args, return var, type | label

    Example:
        | FUNCTION | bending1, beamprops, result1, str | beam design

=========== ==========================
API Scope     rv.V
File Types    .py
Doc Types     text, PDF, HTML
=========== ==========================


.. _Copy file:

**[14]** Copy Files
-------------------------------------------

Copy files using absolute paths. -rvsrc- is an alias for the rvsrc folder.
OS alias may also be used e.g. %USERPROFILE% on Windows.

.. code-block:: text

    Syntax:
        | COPY | abs src path | abs dest path | file name and wildcards
    Example:
        | COPY | -rvsrc-/scripts | %USERPROFILE%/venv1

=========== ==========================
API Scope     Tools
File Types    *.*
Doc Types     text, PDF, HTML
=========== ==========================


.. _Attach PDF:

**[15]** Attach PDF
-------------------------------------------

 

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
API Scope     rv.D
File Types    tex, html, text, pdf
Doc Types     text, PDF, HTML
=========== ==========================

.. _Publish doc:

**[16]** Publish doc
-------------------------------------------

 

Publishes a *doc*. 

.. code-block:: text

    Syntax:
        | PUBLISH | ini relative path | rst2pdf, texpdf, tex, hmtl

    Example:
        | PUBLISH | ini relative path | rst2pdf

=========== ==========================
API Scope     rv.D
File Types    tex, html, text, pdf
Doc Types     text, PDF, HTML
=========== ==========================

