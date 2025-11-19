**C.8 Quick Lookup**
=======================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** API 
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

The API defines *doc* content and properties.

=============== =============== ========================================
API Function        Name             Purpose
=============== =============== ========================================
rv.M(rS)           Meta              Meta data 
rv.R(rS)           Run               Run shell commands
rv.I(rS)           Insert            Insert static resources 
rv.V(rS)           Value             Calculate values
rv.T(rS)           Tool              Import Python and Markup functions
rv.D(rS)           Doc               Publish docs 
rv.S(rS)           Skip              Skip section
rv.X(rS)           Quit              Exit rivt 
=============== =============== ========================================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[2]** API Headers
----------------------- 

.. raw:: html

    <hr>

:term:`API headers` determine overall section processing.

========== ===================== ==================== =====================
API          private/public        print/noprint           section/merge         
========== ===================== ==================== ===================== 
rv.M        **private**; public   **noprint**; print   **merge**; section
rv.R        **private**; public   **noprint**; print   **merge**; section
rv.I        **private**; public   **print**; noprint   **section**; merge   
rv.V        **private**; public   **print**; noprint   **section**; merge    
rv.T        **private**; public   **noprint**; print   **merge**; section
rv.D        **private**; public   **noprint**; print   **merge**; section
rv.S        **private**; public   **noprint**; print   **merge**; section
rv.Q        **private**; public   **noprint**; print   **merge**; section
========== ===================== ==================== ===================== 


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Tags
----------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>


Tags format lines and blocks of text.

**Line Tags**

============= ============================= =======================================
API Scope             Line Tags              Description (doc scope)
============= ============================= =======================================
rv.I, V           text _[#]                  endnote number (all)
rv.I, V           text _[C]                  center text (all)
rv.I, V           text _[R]                  right justify text (all)
rv.I, V           math _[L]                  format LaTeX math (all) 
rv.I, V           math _[A]                  format ASCII math (all) 
rv.I, V          label _[E]                  equation number and label (all)
rv.I, V        caption _[I]                  image number and caption (all)[1]
rv.I, V          title _[T]                  table number and title (all)[1]
rv.I, V           text _[S] section link     link section within doc (all)
rv.I, V           text _[D] report link      link doc within report (all)
rv.I, V           text _[U] external url     external url link (all)
rv.I, V           \-\-\-\-\-                 >4 dashes inserts line (all)[2]
rv.I, V           \=\=\=\=\=                 >4 underscores inserts page (all)[2]
============= ============================= =======================================

[1] tag may be added to the label parameter in the IMAGE and TABLE commands

[2] must start in first indented column (absolute column 4)


**Block Tags**

========== ======================================= ==============================
API Scope         Block Tags                        Description (doc scope)
========== ======================================= ==============================
rv.M        _[[AUTH]] label                         author data (all)
rv.R        _[[WIN]] label, *wait;nowait*           Windows command script (all)
rv.R        _[[MACOS]] label, *wait;nowait*         Mac shell script (all)
rv.R        _[[LINUX]] label, *wait;nowait*         Linux shell script (all)
rv.I, V     _[[INDENT]] spaces (4 default)          Indent (all)
rv.I, V     _[[ITALIC]] spaces (4 default)          Italic indent - (all)
rv.I, V     _[[NOTES]] optional label               Endnote descriptions (all)
rv.I, V     _[[TEXT]] optional language             *literal*, code (all)
rv.I, V     _[[TOPIC]] topic                        Topic (all)
rv.V        _[[VALUES]] table title (_[T])          Define values(all)
rv.T        _[[PYTHON]] label, *rv-space*;newspace  Python script (all)
rv.T        _[[LATEX]] label                        LaTeX markup (pdf)[1]
rv.T        _[[HTML]] label                         HTML markup (html)
all         _[[END]]                                End block (all)
========== ======================================= ==============================

[1] LaTeX processing requires the installation of *Texlive*

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** Commands
-------------------

.. raw:: html

    <hr>

Commands read, write and format files.

========== ======================================================== ===== ==================
API Scope           | Command | path | parameters                    R/W   input types
========== ======================================================== ===== ==================
rv.R        \| LINUX | relative path | *wait;nowait*                 R     *.sh*
rv.R        \| MACOS | relative path | *wait;nowait*                 R     *.sh*
rv.R        \| WIN | relative path   | *wait;nowait*                 R     *.bat, .cmd*
rv.I, V     \| IMAGE | relative path |  scale, caption (_[I])        R     *.png, .jpg*
rv.I, V     \| IMAGE2 | relative path | s1, s2, c1, c2 (_[I])        R     *.png, jpg*
rv.I, V     \| TABLE | relative path | width, l;c;r, title           R     *csv, txt, xlsx*
rv.I, V     \| TEXT | relative path |  *normal;literal* ;code        R     *txt, code*
rv.V        \| VALUES | relative path | *visible;hide* (_[T])        R     *csv*
rv.V       a := 1*IN  | unit1, unit2, decimal | descrip (_[E])[1]    W     define a value
rv.V       b <= a + 3*FT | unit1, unit2, decimal | descrip (_[E])    W     assign a value
rv.V       c <= func1(x,y) | unit1, unit2, decimal | descrip (_[E])  W     assign a value
rv.T        \| PYTHON | relative path | *rv-namespace*; userspace    R     *py*
rv.T        \| HTML | relative path | *html*                         R     *html*
rv.T        \| LATEX | relative path | *pdf*                         R     *tex*
rv.T        \| RST | relative path | *pdf;html;both*                 R     *rst*
rv.D        \| APPEND | relative path | cover_page_title             W     *pdf*
rv.D        \| PUBLISH | relative path | *pdf;pdftex;text;html*      W     *pdf, html, txt*
========== ======================================================== ===== ==================

[1] Values are usually defined in a block where the equation tag (_[E]) 
would not apply and will be disregarded.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** Folders
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
    Folders (including subfolders) that contain rivtlib generated files are 
    marked with double vertical bars ( || ).</p>


**Top Level Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 

        ...

        ├── [out]/                      || other output files
        ├── [public]/                   || public rivt files 
        ├── [publish]/                  || report and doc files
        ├── [src]/                      |  source files 
        └── README.txt                  || searchable text report 


**Expanded Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name                
        ├── [rv101-]filename1.py               | rivt input files
        ├── [rv102-]filename2.py               
        ├── [rv201-]filename3.py               
        ├── [rv202-]filename4.py               
        ├── [out]/                             || other output files from rivt
            ├── data/                              output files from programs
                ├── data1.txt   
                └── data2.txt                
            ├── [logs]/                              log files
                ├── rv101-api.txt   
                ├── rv101-log.txt
                └── rv102-log.txt    
            ├── [noprint]/                           noprint sections
                ├── m103-1.txt                      
                ├── t202-5.txt   
                ├── t103-4.py                         
                └── opensees1.txt           
            ├── [temp]/                              temp files
                └── rv101-label3.tex
            └── [vals]/                              value output files
                ├── v101-2.csv
                └── v102-3.csv          
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
            ├── data/                               author created subfolders
                ├── data1.csv   
                └── conc-vals.csv  
            ├── image/                                             
                ├── fig1.png
                └── fig2.jpg
            ├── scripts/                            
                ├── plot.py                               
                └── loads.py
            ├── output/                              script and shell output
                ├── table1.csv                                               
                ├── image1.png                            
                └── opensees1.txt    
            ├── [gen]/
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
            └── [vals]/                              value files
                ├── steel-vals.csv     
                └── plastic-vals.csv             
        └── README.txt                         || searchable text report 

