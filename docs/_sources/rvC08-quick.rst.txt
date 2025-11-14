**C.8 Quick Lookup**
=======================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** API Headers
--------------------

.. raw:: html

    <hr>

:term:`API header` paramaters include the following:

- private/public : determines whether the API markup is copied to the
    *rivt file* in the */public* folder intended for sharing. 

- show/hide : determines whether the API markup is shown in the output doc.

- section/merge : determines whether the API markup starts a new doc section 
    or merges it with the previous section.   

Default settings do not need to be specified in the *header*. In the table
below, the default setting for each API is listed first in bold.
 
========== ===================== ================= =====================
API          private/public        show/hide           section/merge         
========== ===================== ================= ===================== 
rv.M        **private**; public   **hide**; show     **merge**; section
rv.R        **private**; public   **hide**; show     **merge**; section
rv.I        **private**; public   **show**; hide     **section**; merge   
rv.V        **private**; public   **show**; hide     **section**; merge    
rv.T        **private**; public   **hide**; show     **merge**; section
rv.D        **private**; public   **hide**; show     **merge**; section
rv.S        **private**; public   **hide**; show     **merge**; section
rv.Q        **private**; public   **hide**; show     **merge**; section
========== ===================== ================= ===================== 

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Line tags
----------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

============= ============================= =======================================
API Scope             Line Tags              Description (doc scope)
============= ============================= =======================================
rv.I, V           text _[#]                  endnote number (all)
rv.I, V           text _[C]                  center text (all)
rv.I, V           text _[R]                  right justify text (all)
rv.I, V           math _[L]                  format LaTeX math (all) 
rv.I, V           math _[A]                  format ASCII math (all) 
rv.I, V          label _[E]                  equation number and label (all)
rv.I, V        caption _[I]                  image number and caption (all) [1]
rv.I, V          title _[T]                  table number and title (all) [1]
rv.I, V           text _[P]                  new page (all)
rv.I, V           text _[S] section link     link section within doc (all)
rv.I, V           text _[D] report link      link doc within report (all)
rv.I, V           text _[U] external url     external url link (all)
rv.I, V           _____                      line >4 underscores (all)
============= ============================= =======================================

[1] tag may be added to the label parameter in the IMAGE and TABLE commands

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** Block tags
----------------------

.. raw:: html

    <hr>

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
rv.T        _[[RST]] label                          reStructuredText (pdf,html)
all         _[[END]]                                End block (all)
========== ======================================= ==============================

[1] LaTeX processing requires the installation of *Texlive*

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Commands
-------------------

.. raw:: html

    <hr>

========== ======================================================== ===== ==================
API Scope           | Command | path | parameters                    R/W   input types
========== ======================================================== ===== ==================
rv.R        \| LINUX | relative path | *wait;nowait*                 R     *sh*
rv.R        \| MACOS | relative path | *wait;nowait*                 R     *sh*
rv.R        \| WIN | relative path   | *wait;nowait*                 R     *bat, cmd*
rv.I, V     \| IMAGE | relative path |  scale, caption (_[I])        R     *png, jpg*
rv.I, V     \| IMAGE2 | relative path | s1, s2, c1, c2 (_[I])        R     *png, jpg*
rv.I, V     \| TABLE | relative path | width, l;c;r, title           R     *csv, txt, xlsx*
rv.I, V     \| TEXT | relative path |  *normal;literal* ;code        R     *txt, code*
rv.V        \| VALUES | relative path | *visible;hide* (_[T])        R     *csv*
rv.V       a := 1*IN  | unit1, unit2, decimal | description          W     define value
rv.V       b <= a + 3*FT | unit1, unit2, decimal | ref (_[E])        W     assign value
rv.V       c <= func1(a,b) | unit1, unit2, decimal | ref (_[E])      W     assign value
rv.T        \| PYTHON | relative path | *rv-namespace*; userspace    R     *py*
rv.T        \| HTML | relative path | *html*                         R     *html*
rv.T        \| LATEX | relative path | *pdf*                         R     *tex*
rv.T        \| RST | relative path | *pdf;html;both*                 R     *rst*
rv.D        \| APPEND | relative path | cover_page_title             W     *pdf*
rv.D        \| PUBLISH | relative path | *pdf;pdftex;text;html*      W     *pdf, html, txt*
========== ======================================================== ===== ==================


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** Folders
-------------------

.. raw:: html

    <hr>

**Folder Key**

- Explicit names and prefixes are shown in brackets [ ]. 
- Author provided files are marked with a single vertical bar ( | ).  
- Files written by rivtlib are marked with double vertical bars ( || ).


**Top Level Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 

        ...

        ├── [out]/                      || output folder
        ├── [public]/                   || public rivt file folder
        ├── [publish]/                  || reports folder
        ├── [src]/                      |  doc source folder
        └── README.txt                  || searchable text report 


**Expanded Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name                
        ├── [rv101-]filename1.py               | rivt files
        ├── [rv102-]filename2.py               
        ├── [rv201-]filename3.py               
        ├── [rv202-]filename4.py               
        ├── [out]/                             || output files
            ├── [logs]/                             || log files
                ├── rv101-api.txt   
                ├── rv101-log.txt   
                └── rv102-log.txt   
            ├── [temp]/                             || temp files
                └── rv101-label3.tex
            ├── t103-4.py                      || doc processing outputs
            ├── t202-5.htm   
            ├── m201-1.txt
            ├── table1.csv                               
            ├── image1.png          
            ├── v101-2.csv
            └── v102-3.csv                
        ├── [public]/                          || public rivt files                      
            ├── rv-101-filename1.py              
            ├── rv-201-filename3.py  
            └── rv-202-filename4.py      
        ├── [publish]/                         || Reports and Docs
            ├── [html]/                        || HTML site  
                ├── [docs]/                           
                    ├── _images/                
                    ├── _sources/              
                    ├── _static/                  
                    ├── rv101-filename1.html        || HTML files
                    ├── rv102-filename2.html                              
                    ├── rv201-filename3.html                        
                    ├── rv201-filename4.html   
                    └── index.html                  || HTML site entry point          
                ├── rv101-filename1.rst             || intermediate rst files 
                ├── rv102-filename2.rst  
                ├── rv201-filename3.rst  
                └── rv202-filename4.rst  
            ├── [pdf]/                         || PDF from rst2pdf 
                ├── [src]/                          || intermediate rst files  
                    ├── rv101-filename1.rst          
                    ├── rv102-filename2.rst                           
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst              
                ├── rv101-filename1.pdf             || PDF docs from rst2pdf 
                ├── rv102-filename2.pdf                          
                ├── rv201-filename3.pdf                        
                ├── rv202-filename4.pdf         
                └── Report-Label.pdf                || PDF report from rst2pdf 
            ├── [pdftex]/                      || PDF from LaTeX  
                ├── [src]/                         || intermediate rst files   
                    ├── rv101-filename1.rst         
                    ├── rv102-filename2.rst                        
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst               
                ├── rv101-filename1.pdf             || PDF docs from LaTeX 
                ├── rv102-filename2.pdf                          
                ├── rv201-filename3.pdf                       
                ├── rv202-filename4.pdf
                └── Report-Label.pdf                || PDF report from LaTeX 
            ├── [text]/                        || text report
                ├── rv101-filename1.txt             || text docs
                ├── rv102-filename2.txt       
                ├── rv201-filename3.txt       
                ├── rv202-filename4.txt       
                └── README.txt                      || searchable text report                     
        ├── [src]                              | doc source files               
            ├── data/                               | author created folder
                ├── data1.csv
                ├── newvals.csv        
                └── download1.csv  
            ├── image/                              | author created folder                
                ├── fig1.png
                └── fig2.jpg
            [publish]/
                ├── gen-html.cmd                    | html generating script
                ├── gen-pdf.cmd                     | pdf generating script
                ├── gen-pdftex.cmd                  | LaTeX generating script
                ├── rivt-report.py                  | report generating script
                └── [style]/                        | doc style files 
                    ├── [html]/                     | html style files
                        ├── _locale/                 
                        ├── _static/                        
                        ├── _templates/                     
                        ├── conf.py                         
                        ├── genhtml.cmd                     
                        └── index.rst
                    ├── [pdf]/                      | rst2pdf style files
                        ├── fonts/              
                        ├── style/                 
                        ├── Report-Cover.pdf           
                        └── genrst2pdf.cmd
                    ├── [pdftex]/                   | pdftex style files
                        ├── gentexpdf.cmd             
                        ├── Report-cover.pdf                     
                        └── rivt.sty              
                    ├── [text]/                     | text ini file
                        └── rv-text.ini        
            ├── [tools]/                            | scripts and markup
                ├── plot.py                               
                └── loads.py
            ├── [values]/                           | stored values
                ├── new-units.py       
                └── add-values-v.csv       
        └── README.txt                         || searchable text report 

