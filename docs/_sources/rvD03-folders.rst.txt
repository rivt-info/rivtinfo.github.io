**D.3 Folders**
============================


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** File Names
-------------------------------

.. raw:: html

    <hr>

A *rivt report* is assembled from a set of *docs*. *Reports* are organized
using *doc numbers*. If the *rivt file* names are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

the *report numbers* used in the report would be: 

.. code-block:: bash

    A.1
    1.5
    2.12

where leading zeroes are dropped and *docs* are sorted alpha-numerically into
divisions and subdivisions in the *report*.



.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]**  Report Folders
-------------------------------

.. raw:: html

    <hr>

An example *report* folder structure is shown below.

**Folder Key**

- Explicit folder and file names and prefixes are shown in brackets [ ]. 
- Files provided by the report author are marked with a single vertical bar ( | ).  
- Files written by rivtlib are marked with double vertical bars ( || ).


*Source files* provided by a report author are stored in the *src* folder.
*Docs* are written to the *publish* folder. *rivt files* marked for open source
sharing are written to the *public* folder. Process files generated during *doc*
formatting are written to the *log* folder.

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


.. _report-folders:

**Expanded Folders**

.. code-block:: bash


    [rivt]-Report-Label/                 Report Folder Name                
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

