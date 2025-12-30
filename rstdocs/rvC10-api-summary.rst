**C.10 API Summary**
=======================

**[1t]** API Import
------------------------

The API is imported using the import statement:

..  code-block:: python

    import rivt.rivtlib as rv

Following the import statement, optional variables may be set.

..  code-block:: python

     # rv singledocB=True

*singledocB* overrides the default report structure and specifies that
resource files are read from and written to the *rivt file* folder instead of
*rivt folders*. It is intended for simple, *single docs* with more limited
formatting options. The default is *False*.

..  code-block:: python

     # rv docNameS=new doc name

*docNameS* overrides the default doc name taken from the rivt file name.


**[2t]** API Functions
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


**[3t]** API Headers
------------------------

The :term:`API headers` inlcude processing settings for 11111111the section.

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

**[4t]** Folders
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


**Folders**

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
                └── [style]/                         doc style files 
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


