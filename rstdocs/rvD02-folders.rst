**D.2 Files and Folders**
============================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** rivt Files
--------------------

.. raw:: html

    <hr>

A *rivt file* name has the form:

.. code-block:: bash

    rvDss-file-label.py 

where the prefix is the :term:`doc number`. *D* is a capital alphanumeric 
division label and *ss* is a two digit subdivision number. The output 
of a *rivt file* is a :term:`doc` file with the same file name. 

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Report Folders 
-------------------------------

.. raw:: html

    <hr>

A *rivt report* is assembled from a set of *docs*. *Reports* are organized
using *doc numbers*. If the *rivt file* names are:

.. code-block:: bash

    rvA01-rivtfile.py
    rv105-rivtfile.py
    rv212-rivtfile.py  

the *report numbers* used in the report would be: 

.. code-block:: bash

    A.1
    1.5
    2.12

where leading zeroes are dropped and *docs* are sorted alpha-numerically in a
*report*.


**[3]**  Folder Structure
-------------------------------

*Source files* provided by a report author are stored in the *source* folder.
*Docs* are written to the *report* folder. *rivt files* flagged for open source
sharing are written to the *public* folder. 

Example *report* folder structures are shown below.

**Key**::

    - Required folder and file prefixes names are shown in brackets []. 
    - Single vertical bar (|) identifies files provided by the *report* author. 
    - Double vertical bar (||)| identifies files written by *rivtlib* 
    - Four vertical bars (||||) mix of author and *rivtlib* written files


.. code-block:: bash

    Collapsed folders

    [rivt]-Report-Label/                Report Folder Name
        ├── [log]/                      || log files
        ├── [public]/                   || public rivt files
        ├── [report]/                   || reports and docs
        ├── [src]/                      |||| doc source files
        ├── [style]/                    |||| doc style files
        ├── [rv101-]doclabel1.py        | rivt file
        ├── [rv102-]doclabel2.py        | rivt file
        ├── [rv201-]doclabel3.py        | rivt file
        ├── [rv202-]doclabel4.py        | rivt file  
        └── README.txt                  | GitHub searchable text report 

    Expanded folders

    [rivt]-Report-Label/                Report Folder Name                
        ├── [rv101-]doclabel1.py        | rivt file
        ├── [rv102-]doclabel2.py        | rivt file
        ├── [rv201-]doclabel3.py        | rivt file
        ├── [rv202-]doclabel4.py        | rivt file        
        ├── [log]/                      || log files
            ├── rv101-log.txt   
            └── rv102-log.txt   
        ├── [public]/                   || public rivt files                      
            ├── rv-101-doclabel1.py     
            ├── rv-201-doclabel3.py   
            └── rv-202-doclabel4.py   
        ├── [report]/                   || Reports and Docs
            ├── [html]/    
                ├── [docs]/             || HTML site        
                    ├── _images/
                    ├── _sources/
                    ├── _static/           
                    ├── rv-101-doclabel1.html
                    ├── rv-102-doclabel2.html                           
                    ├── rv-201-doclabel3.html                       
                    ├── rv-201-doclabel4.html
                    └── index.html                       
                ├── rv-101-doclabel1.rst
                ├── rv-102-doclabel2.rst                          
                ├── rv-201-doclabel3.rst                        
                └── rv-202-doclabel4.rst                             
            ├── [rst2pdf]/                  || rst2pdf    
                ├── [src]/                          
                    ├── rv-101-doclabel1.rst
                    ├── rv-102-doclabel2.rst                           
                    ├── rv-201-doclabel3.rst                        
                    └── rv-202-doclabel4.rst              
                ├── rv-101-doclabel1.pdf    || PDF files
                ├── rv-102-doclabel2.pdf                         
                ├── rv-201-doclabel3.pdf                       
                ├── rv-202-doclabel4.pdf
                └── Report-Label.pdf        || PDF report
            ├── [texpdf]/                   || texpdf
                ├── [src]/                          
                    ├── rv-101-doclabel1.rst
                    ├── rv-102-doclabel2.rst                        
                    ├── rv-201-doclabel3.rst                        
                    └── rv-202-doclabel4.rst               
                ├── rv-101-doclabel1.pdf    || PDF files
                ├── rv-102-doclabel2.pdf                          
                ├── rv-201-doclabel3.pdf                       
                ├── rv-202-doclabel4.pdf
                └── Report-Label.pdf        || PDF report  
            ├── [text]/                     || text
                ├── rv-101-label1.txt      
                ├── rv-102-label2.txt
                ├── rv-201-label3.txt
                ├── rv-202-label4.txt
                └── README.txt              || GitHub searchable text report                     
            └── rivt-report.py              | report generating script
        ├── [src]                           | doc source files               
            ├── image/                        
                ├── fig1.png
                └── fig2.jpg
            ├── pdf/                  
                ├── cover-page.pdf                       
                └── attach1.pdf
            ├──  run/                       
                ├── opensees.cmd                
                └── opensees.sh   
            ├── text/            
                ├── boiler.txt
                └── paragraph.rst
            ├── tools/            
                ├── plot.py                               
                └── loads.py
            ├── values/            
                ├── v101-2.csv       
                ├── v102-3.csv         
                └── newvals.csv        
            ├── [temp]/
                └── rv01-label3.tex
        ├── [style]                         | doc style files 
            ├── [html]/               
                ├── _locale/                 
                ├── _static/                        
                ├── _templates/                     
                ├── conf.py                         
                ├── genhtml.cmd                     
                └── index.rst
            ├── [rst2pdf]/            
                ├── fonts/              
                ├── style/                 
                ├── Report-Cover.pdf           
                └── genrst2pdf.cmd
            ├── [texpdf]/             
                ├── gentexpdf.cmd             
                ├── Report-cover.pdf                     
                └── rivt.sty              
            └── [text]/               
                └── rv-text.ini                  
        └── README.txt                 || GitHub searchable text report 