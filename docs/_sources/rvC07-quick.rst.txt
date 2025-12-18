**C.7 Quick Lookup**
=======================


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** API and Headers
------------------------

.. raw:: html

    <hr>

The rivt API formats *doc* conteent.

=============== =============== =========================================
API Function        Name             Purpose
=============== =============== =========================================
rv.R(rS)           Run               Run shell commands
rv.I(rS)           Insert            Insert static resources 
rv.V(rS)           Values            Calculate values
rv.T(rS)           Tools             Python and Markup scripts
rv.D(rS)           Docs              Publish docs 
rv.S(rS)           Skip              Skip section
rv.X(rS)           Quit              Exit rivt 
=============== =============== =========================================


The :term:`API headers` determine overall processing of the section.

========== ===================== ==================== =====================
API          private;public         include;store        section;merge         
========== ===================== ==================== ===================== 
rv.R        **private**;public     **store**;include     **merge**;section
rv.I        **private**;public     **include**;store     **section**;merge   
rv.V        **private**;public     **include**;store     **section**;merge    
rv.T        **private**;public     **store**;include     **merge**;section
rv.D        **private**;public     **store**             **merge**
rv.S        **private**;public     **store**;include     **merge**;section
rv.X        **private**;public     **store**;include     **merge**;section
========== ===================== ==================== ===================== 


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Tags
----------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>


Tags format lines and blocks of text.

**Line Tags**

============= ============================= ======================================
API Scope             Line Tags              Description (doc scope)
============= ============================= ======================================
rv.I, V           text _[#]  text            endnote number (all)
rv.I, V           text _[C]                  center text (all)
rv.I, V           text _[R]                  right justify text (all)
rv.I, V          label _[E]                  equation number and label (all)
rv.I, V          title _[T]                  table number and title (all)[1]
rv.I, V           text _[D] term link        link to defined term in report (all)
rv.I, V           text _[S] section link     link to section in doc (all)
rv.I, V           text _[R] report link      link to doc in report (all)
rv.I, V           text _[U] external url     external url link (all)
rv.I, V           \-\-\-\-\-                 >4 dashes inserts line (all)[2]
rv.I, V           \=\=\=\=\=                 >4 underscores inserts page (all)[2]
rv.I              math _[L]                  format LaTeX math (all) 
rv.I              math _[A]                  format ASCII math (all) 
============= ============================= ======================================

[1] label tag may be added to TABLE command

[2] must start in first indented column (absolute column 4)


**Block Tags**

========== ======================================= ==============================
API Scope         Block Tags                        Description (doc scope)
========== ======================================= ==============================
rv.R        _[[WIN]] label, *wait;nowait*           Windows command script (all)
rv.R        _[[MACOS]] label, *wait;nowait*         Mac shell script (all)
rv.R        _[[LINUX]] label, *wait;nowait*         Linux shell script (all)
rv.I, V     _[[INDENT]] spaces (4 default)          Indent (all)
rv.I, V     _[[ITALIC]] spaces (4 default)          Italic indent - (all)
rv.I, V     _[[ENDNOTES]] optional label            Endnote descriptions (all)
rv.I, V     _[[TEXT]] optional language             *literal*, code (all)
rv.I, V     _[[TOPIC]] topic                        Topic (all)
rv.V        _[[VALUES]] table title, rows (_[T])    Define values(all)
rv.T        _[[PYTHON]] label, *rvspace*;newspace   Python script (all)
rv.T        _[[LATEX]] label                        LaTeX markup (pdf)[1]
rv.T        _[[HTML]] label                         HTML markup (html)
rv.D        _[[LAYOUT]] label                       Doc format settings (all)
all         _[[END]]                                End block (all)
========== ======================================= ==============================

[1] LaTeX processing requires the installation of *Texlive*

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** Commands
-------------------

.. raw:: html

    <hr>

Commands read, write and format files.

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
rv.V       \| VALUES | relative path | title, rows (_[T])[1]         R     *csv*
rv.V       a := 1*IN  | unit1, unit2, decimal | label   (_[E])       W     define a value
rv.V       b <= a + 3*FT | unit1, unit2, decimal | label  (_[E])     W     assign a value
rv.V       c <= func1(x,y) | unit1, unit2, decimal | label (_[E])    W     assign a value
rv.V,T     \| PYTHON | relative path | *rvspace*; userspace          R     *py*
rv.T       \| HTML | relative path | label                           R     *html*
rv.T       \| LATEX | relative path | label                          R     *tex*
rv.D       \| APPEND | relative path | cover_page_title              W     *pdf*
rv.D       \| PUBLISH | ini rel. path | *rst2pdf;pdftex;text;html*   W     *pdf, html, txt*
========== ======================================================== ===== ==================

[1] Values are typically defined in a block that formats to a table

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Folders
-------------------

.. raw:: html

    <hr>

Folders organize files in standard locations to generate *docs* and *reports*

**Folder Key**

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    Required names or prefixes are shown in brackets [ ]. <br>
    <br>
    Folders (including subfolders) that contain author generated files 
    are marked with a single vertical bar ( | ).<br>  
    <br>
    Folders (including subfolders) that contain *rivtlib* generated files are 
    marked with double vertical bars ( || ).</p>


**Top Level Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 

        ...

        ├── [public]/                   || public rivt files 
        ├── [publish]/                  || doc and report files
        ├── [src]/                      |  source files from author
        ├── [stored]/                   || rivt stored files
        └── README.txt                  || searchable text report 


**Expanded Folders**

.. code-block:: bash

    [rivt]-Report-Label/                       Report Folder Name                
        ├── [rv101-]filename1.py               | rivt input files
        ├── [rv102-]filename2.py               
        ├── [rv201-]filename3.py               
        ├── [rv202-]filename4.py                 
        ├── [public]/                          || public rivt files                      
            ├── rv-101-filename1.py              
            ├── rv-201-filename3.py  
            └── rv-202-filename4.py      
        ├── [publish]/                         || reports and docs
            ├── [html]/                              HTML site  
                ├── [docs]/                           
                    ├── _images/                
                    ├── _sources/              
                    ├── _static/                  
                    ├── rv101-filename1.html         
                    ├── rv102-filename2.html                              
                    ├── rv201-filename3.html                        
                    ├── rv201-filename4.html   
                    └── index.html                   HTML site entry point          
                ├── rv101-filename1.rst              intermediate rst files 
                ├── rv102-filename2.rst  
                ├── rv201-filename3.rst  
                └── rv202-filename4.rst  
            ├── [pdf]/                               PDF from rst2pdf 
                ├── [src]/                           intermediate rst files  
                    ├── rv101-filename1.rst          
                    ├── rv102-filename2.rst                           
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst              
                ├── rv101-filename1.pdf              PDF docs from rst2pdf 
                ├── rv102-filename2.pdf                          
                ├── rv201-filename3.pdf                        
                ├── rv202-filename4.pdf         
                └── Report-Label.pdf                 PDF report from rst2pdf 
            ├── [pdftex]/                            PDF from LaTeX  
                ├── [src]/                           intermediate rst files   
                    ├── rv101-filename1.rst         
                    ├── rv102-filename2.rst                        
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst               
                ├── rv101-filename1.pdf              PDF docs from LaTeX 
                ├── rv102-filename2.pdf                          
                ├── rv201-filename3.pdf                       
                ├── rv202-filename4.pdf
                └── Report-Label.pdf                 PDF report from LaTeX 
            ├── [text]/                              text report
                ├── rv101-filename1.txt              text docs
                ├── rv102-filename2.txt       
                ├── rv201-filename3.txt       
                ├── rv202-filename4.txt       
                └── README.txt                       searchable text report                     
        ├── [src]                              | source files from author               
            ├── data/                               author created subfolder
                ├── data1.csv   
                └── conc-vals.csv  
            ├── image/                              author created subfolder                          
                ├── fig1.png
                └── fig2.jpg
            ├── output/                             author created subfolder
                ├── table1.csv                                               
                ├── image1.png                            
                └── opensees1.txt    
            ├── [gendoc]/
                ├── gen-html.cmd                     html generating script
                ├── gen-pdf.cmd                      pdf generating script
                ├── gen-pdftex.cmd                   LaTeX generating script
                ├── rivt-report.py                   report generating script
                ├── new-units.py                     define new units
                └── [style]/                         style files for docs 
                    ├── [html]/                      html style files
                        ├── _locale/                 
                        ├── _static/                        
                        ├── _templates/                     
                        ├── conf.py                         
                        ├── genhtml.cmd                     
                        └── index.rst
                    ├── [pdf]/                       rst2pdf style files
                        ├── fonts/              
                        ├── style/                 
                        ├── Report-Cover.pdf           
                        └── genrst2pdf.cmd
                    ├── [pdftex]/                    pdftex style files
                        ├── gentexpdf.cmd             
                        ├── Report-cover.pdf                     
                        └── rivt.sty              
                    ├── [text]/                      text ini file
                        └── rv-text.ini
            ├── [py]/                                Python scripts and functions
                    ├── plot.py                               
                    └── loads.py
            └── [vals]/                              value files
                ├── steel-vals.csv     
                └── plastic-vals.csv
        ├── [stored]/                          || stored files from rivt            
            ├── [logs]/                              log files
                ├── rv101-api.txt   
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [sect]/                              stored sections                    
                ├── rv202-5d.txt   
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [temp]/                              temp files
                └── rv101-label3.tex
            └── [vals]/                              stored value files
                ├── v101-2.csv
                └── v102-3.csv        
        └── README.txt                         || searchable text report 


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** Metadata
-------------------

.. raw:: html

    <hr>

*Metadata* is stored in the file *rivtmeta.py*. If used, it is imported prior
to *rivtlib* and provides author information and specifies whether the *rivt
file* is a single doc or part of report. Metadata is specified using standard
Python data types. See :doc:`here <rvC01-markup>` for further details.
    
=================== ==========================================================
    Variable                        Description
=================== ==========================================================
:term:`rv_authD`     specifies author information
:term:`rv_localB`    True; False [default] if True resource files are local
=================== ==========================================================

*rv_authD* is a dictionary that pecifies the author, version, email, repository
and license information and forks. 

..  code-block:: python

    # default - author dictionary
    rv_authD = {
            "authors": "",
            "version": "0.0.0",
            "email": "",
            "repo": "",
            "license": "https://opensource.org/license/mit/",
            "fork1": ["author", "version", "email", "repo"],
            "fork2": ["author", "version", "email", "repo"],
            }

    # example - author dicitionary
    rv_authD = {
            "authors": "rholland",
            "version": "0.6.1",
            "email": "rod.h.holland@gmail.com",
            "repo": "https://github.com/rivt-info/rivt-simple-doc",
            "license": "https://opensource.org/license/mit/",
            }

*rv_localB* overrides the default report structure and specifies that all
resource files are read from and written to the *rivt file* folder instead of
*rivt folders*. It is intended for simple, *single docs* with more limited
formatting options.

..  code-block:: python

     # default setting uses report folders
     rv_localB = false
     
     # resource files are read from and written to the rivt file folder
     rv_localB = true
