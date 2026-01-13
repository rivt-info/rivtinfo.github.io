**D.3 Folders**
============================

**[1t]** File Names
-------------------------------

.. raw:: html

    <hr>

A *rivt report* is assembled from a set of *docs*. *Reports* are organized
using *doc numbers*. If the *rivt file* names are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py

The *report numbers* used in the published report would be: 

.. code-block:: bash

    A.1
    1.5
    2.12

where leading zeroes are dropped and *docs* are sorted alpha-numerically into
divisions and subdivisions in the *report*.

**[2t]**  Report Folders
-------------------------------

.. raw:: html

    <hr>

Reports are organized under a single root report folder with the prefix
*rivt-*. *rivt files* are stored in the root folder and *rivt markup* file paths
are relative to the roo.  Resource files are stored in four primary subfolders:

*public* 
    Includes *rivt files* written by *rivtlib* intended for upload to 
    a public repository.

*publish*
    Includes formatted *docs* and *reports* written by *rivtlib*.

*src*
    Includes author provided content, style and generating files for *docs* 
    and *reports*.

*stored*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden*, and *metadata* and *reports*

An example *report* folder structure is shown below.

**Folder Key**

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    Required names or prefixes are shown in brackets [ ]. <br>
    <br>
    Folders (including subfolders) that contain author generated files 
    are marked with a single vertical bar ( | ).<br>  
    <br>ri
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

        ├── [Public]/                   || public rivt files 
        ├── [Publish]/                  || doc and report files
        ├── [Src]/                      |  source files from author
        ├── [Stored]/                   || rivt stored files
        └── README.txt                  || searchable text report 


.. _report folders:

**Expanded Folders**

.. code-block:: bash

    [rivt]-Report-Label/                     Report Folder Name                
        ├── [rv101-]filename1.py               | rivt input files
        ├── [rv102-]filename2.py               
        ├── [rv201-]filename3.py               
        ├── [rv202-]filename4.py                 
        ├── [Public]/                          || public rivt files                      
            ├── rv-101-filename1.py              
            ├── rv-102-filename1.py              
            ├── rv-201-filename3.py  
            └── rv-202-filename4.py    
        ├── [Publish]/                         || reports and docs
            ├── [Html]/                              HTML site  
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
            ├── [Rstpdf]/                               PDF from rst2pdf 
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
            ├── [Texpdf]/                            PDF from LaTeX  
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
            ├── [Text]/                              text report
                ├── rv101-filename1.txt              text docs
                ├── rv102-filename2.txt       
                ├── rv201-filename3.txt       
                ├── rv202-filename4.txt       
                └── README.txt                       searchable text report                     
        ├── [Src]                              | source files from authors               
            ├── [Data]/                             
                ├── data1.csv
                ├── steel-vals.csv        
                └── conc-vals.csv  
            ├── [Shell]/                           
                ├── shell1.cmd   
                └── shell1.csv  
            ├── [Image]/                                                   
                ├── fig1.png
                └── fig2.jpg
            ├── [Scripts]/                         
                ├── plot.py                               
                ├── new-units.py                     define new units                          
                └── opensees1.txt    
            ├── [Gendoc]/
                ├── genhtml.cmd                      html generating script
                ├── genpdf.cmd                       pdf generating script
                ├── gentexpdf.cmd                    LaTeX generating script
                ├── rivt-report.py                   report generating script
                ├── Report-Cover.pdf
                ├── attach1.pdf
                └── [Style]/                         style files for docs 
                    ├── [Html]/                      html style files
                        ├── _locale/                 
                        ├── _static/                        
                        ├── _templates/                     
                        ├── conf.py                         
                        ├── genhtml.cmd                     
                        └── index.rst
                    ├── [Rstpdf]/                    rst2pdf style files
                        ├── fonts/              
                        └── style/                 
                    ├── [Texpdf]/                    pdftex style files            
                        └── rivt.sty              
                    ├── [Text]/                      text ini file
                        └── rv-text.ini
        ├── [Stored]/                          || stored files from rivt            
            ├── [Logs]/                              log files
                ├── rv101-api.txt   
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [Sect]/                              stored sections                    
                ├── rv202-5d.txt   
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [Temp]/                              temp files
                └── rv101-label3.tex
            └── [Data]/
                ├── table1.csv                      stored script output                                  
                ├── image1.png                      stored value files
                ├── v101-2.csv
                └── v102-3.csv             
        └── README.txt                         || searchable text report 