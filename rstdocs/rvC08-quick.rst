**C.8 Quick Lookup**
=======================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Line tags
----------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

============= ========================== =======================================
API Scope             Line Tags                Description (doc type scope)
============= ========================== =======================================
I, V           text _[#]                   endnote number (all)
I, V           text _[S] section link      link section within doc (all)
I, V           text _[D] report link       link doc within report (all)
I, V           text _[U] url               external url link (all)
I, V           text          _[C]          center text (all)
I, V           text          _[R]          right justify text (all)
I, V           equation      _[L]          format LaTeX math (pdf, html) 
I, V           equation      _[A]          format ASCII math (all) 
I, V           label         _[E]          equation label (all)
I, V           caption       _[I]          image label (all) [1]
I, V           title         _[T]          table label (all) [1]
I, V             _____   or  _[H]          horizontal line >4 underscores (all)
I, V                         _[P]          new page (all)
============= ========================== =======================================

[1] tag may be added to the label parameter in IMG and TABLE commands

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Block tags
----------------------

.. raw:: html

    <hr>

============ ====================================== =============================
API Scope         Block Tags                        Description (doc type scope)
============ ====================================== =============================
M             _[[AUTH]] optional label              author data (all)
R             _[[WIN]] *wait;nowait*                Windows command script (all)
R             _[[MACOS]] *wait;nowait*              Mac shell script (all)
R             _[[LINUX]] *wait;nowait*              Linux shell script (all)
I             _[[BI]]                               bold indent (pdf, html)
I             _[[II]]                               italic indent (pdf, html)
I             _[[4]]                                indent spaces (all)
I, V          _[[NOTE]] optional label              endnote description (all)
I, V          _[[TEXT]] *language*                  standard, literal, code (all)
V             _[[FUNC]] userspace, *rvnamespace*    Python function (all)
V             _[[PYTHON]] *print;noprint*           Python script (all)
T             _[[HTML]] *pdf;nopdf*                 HTML commands (pdf,html)
T             _[[LATEX]] optional label             LaTeX commands (pdf,html)
T             _[[RST]] optional label               reStructuredText (pdf,html)
T             _[[OPENSEES]] *wait;nowait*           OpenSees script (all)
T             _[[QCAD]] *wait;nowait*               QCAD script (all)
T             _[[RUBY]] *wait;nowait*               Ruby script (all)
all           _[[TOPIC]] topic                      topic (all)
all           _[[QUIT]]                             quit (all)
============ ====================================== =============================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** Commands
-------------------

.. raw:: html

    <hr>

======= ==================================================== ===== ================
Scope           | Command | path | parameters                 R/W      types
======= ==================================================== ===== ================
R         | LINUX | relative path | *wait;nowait*             R     sh
R         | MACOS | relative path | *wait;nowait*             R     sh
R         | WIN | relative path   | *wait;nowait*             R     bat, cmd
I, V      | IMG | relative path |  caption, scale             R     png, jpg
I, V      | IMG2 | relative path | c1, c2, s1, s2             R     png, jpg
I, V      | TABLE | relative path | width, l;c;r, title       R     csv, txt, xlsx
I, V      | TEXT | relative path |  *literal, standard*       R     txt
V         | FUNC | relative path | *hide;visible*             R     csv
V         | VALUE | relative path | *hide;visible*            R     csv
V         | PYTHON | relative path | userspace;*rvnamespace*  R     py
V         a := 1*IN  | unit1, unit2, decimal | description    W     define value
V         b <= a + 3*FT | unit1, unit2, decimal | reference   W     assign value
V         c <= func1(a,b) | unit1, unit2, decimal | ref       W     assign value
T         | HTML | relative path | *pdf;nopdf*                R     html
T         | LATEX | relative path | *pdftex;tex*              R     tex
T         | RST | relative path | *pdf;html;both*             R     rst
T         | OPENSEES | relative path | *wait;nowait*          R     py
T         | QCAD | relative path | *wait;nowait*              R     js
T         | RUBY | relative path | *wait;nowait*              R     rb
D         | APPEND | relative path | cover_page_title         W     pdf
D         | PUBLISH | relative path | *pdf;pdftex;text;html*  W     pdf, html, txt
======= ==================================================== ===== ================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Default Header Settings
------------------------------------

.. raw:: html

    <hr>


====== ============= ================= ================ ============== 
API         print        public            merge          history       
====== ============= ================= ================ ============== 
rv.R   hide, print   private, public   section, merge    record, skip 
rv.I   print, hide   private, public   section, merge    record, skip 
rv.V   print, hide   private, public   section, merge    record, skip  
rv.T   hide, print   private, public   section, merge    record, skip  
rv.D   hide, print   private, public   section, merge    record, skip  
rv.M   hide, print   private, public   section, merge    record, skip  
rv.S   hide, print   private, public   section, merge    record, skip  
rv.Q   hide, print   private, public   section, merge    record, skip 
====== ============= ================= ================ ============== 

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** Folders
-------------------

.. raw:: html

    <hr>


**Folder Key**

- Required folder and file prefix names are shown in brackets [ ]. 
- Single vertical bar ( | ) identifies files provided by the report author. 
- Double vertical bar ( || ) identifies files written by rivtlib 
- Four vertical bars ( |||| ) are a mix of author and rivtlib written files

.. code-block:: bash

    Collapsed folders

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file  
        ├── [log]/                      || log folder
        ├── [public]/                   || public rivt folder
        ├── [publish]/                  || reports folder
        ├── [src]/                      |||| source folder
        └── README.txt                  || GitHub searchable text report 

    Expanded folders

    [rivt]-Report-Label/                       Report Folder Name                
        ├── [rv101-]filename1.py               | rivt file
        ├── [rv102-]filename2.py               | rivt file
        ├── [rv201-]filename3.py               | rivt file
        ├── [rv202-]filename4.py               | rivt file        
        ├── [log]/                             || log files
            ├── rv101-api.rst   
            ├── rv101-log.txt   
            └── rv102-log.txt   
        ├── [public]/                          || public rivt files                      
            ├── rv-101-filename1.py            ||  
            ├── rv-201-filename3.py            ||
            └── rv-202-filename4.py            || 
        ├── [publish]/                         || Reports and Docs
            ├── [html]/    
                ├── [docs]/                    || HTML     
                    ├── _images/               || 
                    ├── _sources/              ||
                    ├── _static/               ||   
                    ├── rv101-filename1.html   || HTML files
                    ├── rv102-filename2.html   ||                           
                    ├── rv201-filename3.html   ||                     
                    ├── rv201-filename4.html   ||
                    └── index.html             || HTML site           
                ├── rv101-filename1.rst  
                ├── rv102-filename2.rst  
                ├── rv201-filename3.rst  
                └── rv202-filename4.rst  
            ├── [pdf]/                         || pdf report  
                ├── [src]/                          
                    ├── rv101-filename1.rst
                    ├── rv102-filename2.rst                           
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst              
                ├── rv101-filename1.pdf         || PDF from rst2pdf files
                ├── rv102-filename2.pdf         ||                 
                ├── rv201-filename3.pdf         ||               
                ├── rv202-filename4.pdf         ||
                └── Report-Label.pdf            || PDF from rst2pdf report
            ├── [pdftex]/                       || pdftex report
                ├── [src]/                          
                    ├── rv101-filename1.rst
                    ├── rv102-filename2.rst                        
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst               
                ├── rv101-filename1.pdf         || PDF from LaTeX files
                ├── rv102-filename2.pdf                          
                ├── rv201-filename3.pdf                       
                ├── rv202-filename4.pdf
                └── Report-Label.pdf            || PDF from LaTeX report  
            ├── [text]/                         || text report
                ├── rv101-filename1.txt         ||
                ├── rv102-filename2.txt         || 
                ├── rv201-filename3.txt         ||
                ├── rv202-filename4.txt         ||
                └── README.txt                  || GitHub searchable text report                     
            └── rivt-report.py                  | report generating script
        ├── [src]                               |||| doc source files               
            ├── data/                           | author created folder
                ├── data1.csv
                ├── newvals.csv        
                └── download1.csv  
            ├── image/                          | author created folder                
                ├── fig1.png
                └── fig2.jpg
            ├── [style]/                        | doc style files 
                ├── [html]/                     | html style files
                    ├── _locale/                 
                    ├── _static/                        
                    ├── _templates/                     
                    ├── conf.py                         
                    ├── genhtml.cmd                     
                    └── index.rst
                ├── [pdf]/                       | rst2pdf style files
                    ├── fonts/              
                    ├── style/                 
                    ├── Report-Cover.pdf           
                    └── genrst2pdf.cmd
                ├── [pdftex]/                    | pdftex style files
                    ├── gentexpdf.cmd             
                    ├── Report-cover.pdf                     
                    └── rivt.sty              
                ├── [text]/                      | text ini file
                    └── rv-text.ini        
            ├── [temp]/                          || temp files
                └── rv01-label3.tex
            ├── [tools]/                         |||| functions and output
                ├── plot.py                               
                └── loads.py
                ├── tablepy.csv                               
                └── imagepy.png          
            ├── [values]/                        |||| stored values
                ├── new-units.py       
                ├── add-values-v.csv       
                ├── v101-2.csv
                └── v102-3.csv                
        └── README.txt                           || GitHub searchable text report 


