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
Scope             Line Tags                    Description (doc scope)
============= ========================== =======================================
I              text _[#] text              endnote (all)
I              text _[L] doc link          doc link (all)
I              text _[R] report link       report link (all)
I              text _[U] url               url link (all)
I              text          _[B]          center bold text (pdf, html)
I              description   _[D]          endnote description (all)
I              text          _[C]          center text (all)
I, V           equation      _[S]          format sympy math (all) 
I, V           equation      _[M]          format LaTeX math (all) 
I, V           label         _[E]          equation label (all)
I, V           caption       _[F]          image label (all) [1]
I, V           title         _[T]          table label (all) [1]
I, V             _____   or  _[H]          horizontal line >4 underscores (all)
I, V                         _[P]          new page (all)
============= ========================== =======================================

[1] tag may be added to parameter in IMG and TABLE commands

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Block tags
----------------------

.. raw:: html

    <hr>

============ ============================= =====================================
Scope          Block Tags                    Description (doc scope)
============ ============================= =====================================
I             _[[B]]                          indent bold (pdf, html)
I             _[[I]]                          indent italic (pdf, html)
I             _[[O]]                          italic, oblique (pdf, html)
I             _[[L]]                          LaTeX (pdf, html)
I             _[[N]]                          indent (all)
I             _[[C]] *language*               code, literal (all)
M             _[[AUTH]] *description*         author data (all)
M             _[[FORK]] *description*         fork data (all)
R             _[[WIN]] *description*          Windows command script (all)
R             _[[MACOS]] *description*        Mac shell script (all)
R             _[[LINUX]] *description*        Linux shell script (all)
T             _[[PYTHON]] *description*       Python functions (all)
T             _[[RUBY]] *description*         Ruby script (all)
T             _[[QCAD]] *description*         QCAD script (pdf,html)
T             _[[OPENSEES]] *description*     OpenSeesscript (all)
T             _[[LATEX]] *description*        LaTeX commands (pdf,html)
T             _[[HTML]] *description*         HTML commands (all)
all           _[[T]] *topic*                  topic (all)
all           _[[Q]]                          quit (all)
============ ============================= =====================================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** Commands
-------------------

.. raw:: html

    <hr>

======= ==================================================== ===== ==================
Scope           | Command | path | parameters                 R/W     file types
======= ==================================================== ===== ==================
R         | LINUX | relative path | popen; run                R     sh
R         | MACOS | relative path | popen; run                R     sh
R         | WIN | relative path   | popen; run                R     bat, cmd
I, V      | TEXT | relative path | normal; literal            R     txt, tex, rst
I, V      | TABLE | relative path | title, width, l;c;r       R     csv, txt, xlsx
I, V      | IMG | relative path |  caption, scale             R     png, jpg
I, V      | IMG2 | relative path | c1, c2, s1, s2             R     png, jpg
V         | VALUES | relative path | title                    R     csv
V         a := 1*IN  | unit1, unit2, decimal | description    W     define value
V         b <= a + 3*FT | unit1, unit2, decimal | reference   W     assign value
T         | HTML | relative path | html; file                 R     html
T         | LATEX | relative path | pdftex, file              R     tex
T         | PYTHON | relative path | rivt; external           R     py
D         | APPEND | relative path | cover_page_title         W     pdf, html
D         | DOCS | relative path | pdf; pdftex; text; html    W     pdf, html, txt
======= ==================================================== ===== ==================


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Folders
-------------------


**Folder Key**

- Required folder and file prefixes names are shown in brackets [ ]. 
- Single vertical bar ( | ) identifies files provided by the report author. 
- Double vertical bar ( || ) identifies files written by rivtlib 
- Four vertical bars ( |||| ) mix of author and rivtlib written files


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
        └── README.txt                  | GitHub searchable text report 

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


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** Default Header Settings
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