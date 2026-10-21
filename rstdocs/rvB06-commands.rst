**B.5 |** Commands
========================

.. _command-summary:

**[1]** Command Summary
-------------------------------------

**Command Syntax**

========== =============================================================== ========================
API Scope           Command                                                        Description
========== =============================================================== ========================
rv.R        **| SCRIPT |** file name | args, output file                     :ref:`Script file`
rv.R        **| ARGS |** file name | namespace                               :ref:`Args file`
rv.R        **| TEXT |** file name | type                                    :ref:`Text file`
rv.R        **| ABSTEXT |** file name | type                                 :ref:`Text file`
rv.R        **| ABSIMAGE |** file name | caption, scale, num;non, time;not   :ref:`Image file`
rv.I, V     **| IMAGE |** file name | caption, scale, num;non, time;not      :ref:`Image file`
rv.I, V     **| IMAGE2 |** file1, file2 | c1,c2,s1,s2,n1,n2                  :ref:`Adjacent images`
rv.I, V     **| TABLE |** file name | title,width,head;nohead,num;non        :ref:`Table file`    
rv.V        **| VALTABLE |** file name | title, width, num;non               :ref:`Valtable file`
rv.V        **| VALSTOR |** file name | title, width, num;non                :ref:`Valstor file`
rv.V        **| PYTHON |** file name | args, var, type, label                :ref:`Function value`  
rv.V        **| FUNCTION |** function name | args, var, type, label          :ref:`Function value`  
rv.T        **| COPY |** abs src path | abs dest path | file pattern         :ref:`Copy file`
rv.T        **| SHELL |** abs file path | os, wait                           :ref:`Shell file`
rv.D        **| PUBLISH |** doc title | type                                 :ref:`Publish doc` 
rv.D        **| ATTACHPDF |** file name | front;back, title                  :ref:`Attach PDF`   
========== =============================================================== ========================

**Command File Paths - Defaults**

================ ===================================== ======
   Command           Default Path [1]_                  R/W
================ ===================================== ======
\| SCRIPT |         **rvreport-.../scripts** [2]_       R/W
\| ARGS |           **rvreport-.../data**                R
\| TEXT |           **rvreport-.../data**                R 
\| IMAGE |          **rvreport-.../image**               R
\| IMAGE2 |         **rvreport-.../image**               R
\| TABLE |          **rvreport-.../data**                R
\| VALTABLE |       **rvreport-.../data**                R
\| VALSTOR |        **rv_stor/vals**                     R
\| ATTACHPDF |      **rvreport-.../data**                R
\| PUBLISH |        **rvreport-.../_published/** [3]_    W
\| COPY |               os root                          R
\| SHELL |              os root                          R
================ ===================================== ======

.. [1] Path overrides are relative to the **rvreport-...** folder and include an initial slash
.. [2] Output is written to **rvreport-.../data**   
.. [3] *docs* are written to subdirectories of **rvreport-../_published** for each type

See :ref:`here <report-folders>` for the folder layout. 


.. _Script file:

**[2]** Script
------------------------------------------

The SCRIPT block executes code and returns a file object (text, list, image
etc.) that is written to *rvreport-.../scripts*. The language parameter specifies
the processing and requires a compatible compiler installation.

Language types include:

    #. **python**
    #. **ruby**
    #. **mermaid** 
    #. **latex** 



.. topic:: | SCRIPT |

    .. code-block:: text

        Syntax:
            | TEXT | relative path | type
        Example:
            | TEXT | rvsrc/quote.txt | literal

=========== =====================================
API Scope     rv.R
File Types    see above 
Doc Types     text, PDF, HTML
=========== =====================================


.. _Args file:

**[3]** Args
------------------------------------------

The ARGS command reads a Python file with arguments defined as dictionaries. The
dictionary names are used as inputs to functions and scripts.

The namespace name *rivt* imports the values into the main *rivt file* namespace.

.. topic:: | ARGS |

    .. code-block:: text

        Syntax:
            | ARGS | relative path | namespace
        Example:
            | ARGS | bm1args.py | rivt

=========== =====================================
API Scope     rv.R
File Types    see above 
Doc Types     text, PDF, HTML
=========== =====================================


.. _Text file:

**[4]** Text
------------------------------------------

The TEXT and ABSTEXT commands read and format text and code files. They insert
text after framing and formatting, without actually running. 

Language types include:

    #. **text** - literal text
    #. **bold**
    #. **italic**
    #. **indent4**
    #. **python** - Python code
    #. **ruby** - Ruby code
    #. **sphinx** - Sphinx reStructuredText 
    #. **rst** - reStructuredText
    #. **html** - HTML markup


.. topic:: | TEXT |

    .. code-block:: text

        Syntax:
            | TEXT | relative path | type
        Example:
            | TEXT | quote.txt | literal


.. topic:: | ABSTEXT |

    .. code-block:: text

        Syntax:
            | TEXT | absolute path | type
        Example:
            | TEXT | c:/mydir/quote.txt | literal


=========== =====================================
API Scope     rv.R
File Types    see above 
Doc Types     text, PDF, HTML
=========== =====================================


.. _Image file:

**[5]** Image
-------------------------------------------

The IMAGE and ABSIMAGE commands read a PNG or JPEG file and centers it in the
*doc*. The scale parameter is a decimal fraction of the page width. The caption
may be ommited by using a single hyphen. The *num;nonum* parameter specifies
whether to assign a figure number. The image path is inserted in the text *doc*
instead of the image.

.. code-block:: text

    Syntax:
        | IMAGE | relative path | caption, scale, num;nonum

    Example:
        | IMAGE | file1.png | Map, 0.5, num

.. code-block:: text

    Syntax:
        | ABSIMAGE | absolute path | caption, scale, num;nonum

    Example:
        | ABSIMAGE | c:/mydir/file1.png | Map, 0.5, num



=========== ==========================
API Scope     rv.V, rv.I or rv.R
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

.. _Table file:

**[7]** Table
------------------------------------------

The TABLE command reads csv, xls, and rst files and outputs formatted tables.
The title may be ommited by inserting a hyphen "-". The width parameter
specifies the maximum character width of a column. The align parameter
specifies the cell justification - left, center, right. The number parameter
specifies whether the table is numbered. For csv files, the head parameter
specifies whether the first row is a column header.


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


.. _Valtable file:

**[8]**  Valtable
------------------------------------------------

The VALTABLE command imports and defines values from a *csv* or *xls* file. 
The file format is:: 

    var = value, unit1, unit2, decimal, label

The path variable is either from *src* or *stored* depending on if the values
were generated by rivtlib or provided by the author. The title parameter is the
table title. A hyphen omits the title. The *rows* parameter specifies the rows
to import. The *num; nonum* parameter specifies whether to assign a table
number to the values table.


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


.. _Valstor file:

**[9]**  Valstor
------------------------------------------------

The VALSTOR command imports and defines values from a *csv* or *xls* file. 
The file format is:: 

    var = value, unit1, unit2, decimal, label

The path variable is either from *src* or *stored* depending on if the values
were generated by rivtlib or provided by the author. The title parameter is the
table title. A hyphen omits the title. The *rows* parameter specifies the rows
to import. The *num; nonum* parameter specifies whether to assign a table
number to the values table.

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


.. _Python file:

**[10]** Python file
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

**[11]** Function
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

**[12]** Copy Files
-------------------------------------------

Copy files using absolute paths. -rvsrc- is an alias for the rvsrc folder.
OS alias may also be used e.g. %USERPROFILE% on Windows.

.. code-block:: text

    Syntax:
        | COPY | abs src path | abs dest path | file name and wildcards
    Example:
        | COPY | -rvsrc-/scripts | %USERPROFILE%/venv1

=========== ==========================
API Scope     rv.T
File Types    *.*
Doc Types     text, PDF, HTML
=========== ==========================
 
.. _Shell file:

**[13]** Shell file
-------------------------------------------

The SHELL command runs shell scripts including .cmd, .bat and .sh files. The
*os* parameter specifies the operating system: *win*, *mac* or *linux*. The
*wait; nowait* specifies whether rivt file processing waits for the script to
complete before continuing.

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
API Scope     rv.T
File Types    .cmd, .bat, .sh, .bsh 
Doc Types     text, PDF, HTML
=========== ==========================


.. _Publish doc:

**[14]** Publish doc
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

.. _Attach PDF:

**[15]** Attach PDF
-------------------------------------------

Appends or prepends a PDF file to the *doc*. The title parameter generates an
Appendix cover page with the specified title. A "-" omits the over page. For
HTML *docs* the file is inserted as a donwload link.

.. topic:: | ATTACHPDF |

    .. code-block:: text

        Syntax:``
            | ATTACHPDF | relative path | front;back, title
  
        Example:
            | ATTACHPDF | relative path | front;back, title


=========== ==========================
API Scope     rv.D
File Types    tex, html, text, pdf
Doc Types     text, PDF, HTML
=========== ==========================