**C.8 Quick Lookup**
=======================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[01]** Line tags
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
I, V           equation      _[S]          format symbol math (all) 
I, V           label         _[E]          equation label (all)
I, V           caption       _[F]          image label (all) [1]
I, V           title         _[T]          table label (all) [1]
I, V             _____   or  _[H]          horizontal line >4 underscores (all)
I, V                         _[P]          new page (all)
============= ========================== =======================================

[1] tag may be added to parameter in IMG and TABLE commands

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[02]** Block tags
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
T             _[[LATEX]] *description*        LaTeX commands (all)
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

======= ================================================= ===== ==================
Scope           | Command | parameters                     R/W     file types
======= ================================================= ===== ==================
R         | LINUX | relative path                           R     sh
R         | MACOS | relative path                           R     sh
R         | WIN | relative path                             R     bat, cmd
I, V      | TEXT | relative path | normal; literal          R     txt, tex, rst
I, V      | TABLE | relative path | title, width, l;c;r     R     csv, txt, xlsx
I, V      | IMG | relative path |  caption, scale           R     png, jpg
I, V      | IMG2 | relative path | c1, c2, s1, s2           R     png, jpg
V         | VALUES | relative path | title, [rows]          R     csv
V         a := 1*IN  | unit1, unit2, decimal | descrip      W     define value
V         b <= a + 3 | unit1, unit2, decimal | ref          W     assign value
T         | HTML | relative path                            R     html
T         | LATEX | relative path                           R     tex
T         | PYTHON | relative path                          R     py
T         | QCAD   | relative path                          R     js
D         | APPEND | relative path | page;nopage            W     pdf, html
D         | DOCS | relative path | rpdf; tpdf; txt; html    W     pdf, txt, htm
======= ================================================= ===== ==================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Folders
-------------------

.. raw:: html

    <hr>

**Collapsed Folders**

.. code-block:: bash


    [rivt]-Report-Label/              Report Name
        ├── [dv01-]divlabel/          | division folder
        ├── [dv02-]divlabel/          | division folder                   
        ├── [public]/                 || public rivt files
        ├── [report]/                 || reports and docs
        ├── [source]/                 | source files
        ├── rivt-report.py            | report generator
        └── README.txt                | GitHub searchable report 


**Expanded Folders**


.. code-block:: bash

    [rivt]-Report-Label/                          # Report Folder Name
        ├── [dv01-]divlabel/                      # div 01 folder
            ├── [rv01-]doclabel1.py               | rivt file
            └── [rv02-]doclabel2.py               | rivt file
        ├── [dv02-]divlabel/                      # div 02 folder
            ├── [rv01-]doclabel3.py               | rivt file
            └── [rv02-]doclabel4.py               | rivt file         
        ├── [public]/                             || public rivt files
            ├── dv01-divlabel1/                   
                ├── rv01-doclabel1.py        
                └── rv02-doclabel2.py  
            ├── dv02-divlabel2/                   
                ├── rv01-doclabel3.py      
                └── rv02-doclabel4.py             
        ├── [report]/                              || Reports and Docs
            ├── [html]/                            || HTML site
                ├── [docs]/                       
                    ├── _images/
                    ├── _sources/
                    └── _static/
                    ├── dv01-divlabel1/           
                        ├── rv01-doclabel1.html
                        └── rv02-doclabel2.html
                    ├── dv02-divlabel2/                            
                        ├── rv01-doclabel3.html                       
                        └── rv02-doclabel4.html
                    ├── index.html 
                    └── README.txt                 || GitHub searchable report                      
                ├── [src]/                         
                    ├── dv01-divlabel1/
                        ├── rv01-doclabel1.rst
                        └── rv02-doclabel2.rst
                    ├── dv02-divlabel2/                            
                        ├── rv01-doclabel3.rst                        
                        └── rv02-doclabel4.rst                             
            ├── [rst2pdf]/                         || rst2pdf report and docs             
                ├── [src]/                          
                    ├── dv01-divlabel1/
                        ├── rv01-doclabel1.rst
                        └── rv02-doclabel2.rst
                    ├── dv02-divlabel2/                            
                        ├── rv01-doclabel3.rst                        
                        └── rv02-doclabel4.rst
                ├── dv01-divlabel1/                
                    ├── rv01-doclabel1.pdf
                    └── rv02-doclabel2.pdf
                ├── dv02-divlabel2/                            
                    ├── rv01-doclabel3.pdf                       
                    └── rv02-doclabel4.pdf
                ├── README.txt                     || GitHub searchable report
                └── Report-Label.pdf               || PDF report
            ├── [texpdf]/                          || texpdf report and docs
                ├── [src]/                          
                    ├── dv01-divlabel1/
                        ├── rv01-doclabel1.rst
                        └── rv02-doclabel2.rst
                    ├── dv02-divlabel2/                            
                        ├── rv01-doclabel3.rst                        
                        └── rv02-doclabel4.rst
                ├── dv01-divlabel1/                 
                    ├── rv01-doclabel1.pdf
                    └── rv02-doclabel2.pdf
                ├── dv02-divlabel2/                            
                    ├── rv01-doclabel3.pdf                       
                    └── rv02-doclabel4.pdf
                ├── [temp]/
                    └── rv01-label3.tex
                ├── README.txt                     || GitHub searchable report
                └── Report-Label.pdf               || PDF report  
            ├── [text]/                            || text report and docs
                ├── dv01-divlabel1/
                    ├── rv01-label1.txt      
                    └── rv02-label2.txt
                ├── dv02-divlabel1/
                    ├── rv01-label3.txt
                    └── rv02-label4.txt
                └── README.txt                      || GitHub searchable report                     
        ├── [source]                                | source files 
            ├── [html]\
                ├── _locale/                        | settings
                ├── _static/                        | settings
                ├── _templates/                     | settings                              # html config
                ├── conf.py                         | config file
                └── genhtml.cmd                     | build commands
                └── index.rst                       | intro page
            ├── [rst2pdf]/
                ├── fonts/                          | fonts
                ├── style/                          | settings 
                ├── Report-Cover.pdf                | report cover 
                └── genrst2pdf.cmd                  | build commands                        
            ├── [texpdf]/
                ├── gentexpdf.cmd                   | build commands
                ├── Report-cover.pdf                | report cover               
                └── rivt.sty                        | settings
            ├── [text]/                   
                └── rv-text.ini                    
            ├── [i01]/                              | div 01 Insert files 
                ├── data1.csv
                ├── cover-page.pdf                       
                └── standards.txt
            ├── [i02]/                              | div 02 Insert files 
                ├── data1.csv                   
                └── standards.txt
            ├── [rt01]/                             | div 01 Run and Tool files 
                ├── data1.csv                
                └── standards.txt
            ├── [rt02]/                             | div 02 Run and Tool files 
                ├── data1.csv                   
                └── standards.txt
            ├── [v01]/                              | div 01 Value files 
                ├── val0101-2.csv                 
                └── val0102-3.csv
            ├── [v02]/                              | div 02 Value files 
                └── othervals.csv
        └── README.txt                              # GitHub searchable report 



