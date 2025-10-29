**D.3 Folders**
============================


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Folder Names
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


**[2]**  Report Folders
-------------------------------

An example *report* folder structure is shown below.

**Folder Key**

- Required folder and file prefix names are shown in brackets [ ]. 
- A single vertical bar ( | ) identifies files provided by the report author. 
- Double vertical bars ( || ) identifies files written by rivtlib 
- Four vertical bars ( |||| ) are a mix of author and rivtlib written files


*Source files* provided by a report author are stored in the *src* folder.
*Docs* are written to the *publish* folder. *rivt files* marked for open source
sharing are written to the *public* folder. Process files generated during *doc*
formatting are written to the *log* folder.

**Collapsed Folders**

.. code-block:: bash


    [rivt-]Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file  
        ├── [logs]/                     || log folder
        ├── [public]/                   || public rivt folder
        ├── [publish]/                  || reports folder
        ├── [src]/                      |||| source folder
        └── README.txt                  || Searchable text report 



.. _full-report-folder:

**Expanded Folders**

.. code-block:: bash

    [rivt]-Report-Label/                       Report Folder Name                
        ├── [rv101-]filename1.py                | rivt file
        ├── [rv102-]filename2.py                | rivt file
        ├── [rv201-]filename3.py                | rivt file
        ├── [rv202-]filename4.py                | rivt file        
        ├── [logs]/                              || log files
            ├── rv101-api.rst                   ||
            ├── rv101-log.txt                   ||
            └── rv102-log.txt                   ||
        ├── [public]/                           || Public rivt files                      
            ├── rv-101-filename1.py             ||  
            ├── rv-201-filename3.py             ||
            └── rv-202-filename4.py             || 
        ├── [publish]/                          || Reports and Docs
            ├── [html]/                         || HTML Docs    
                ├── [docs]/                     ||  
                    ├── _images/                || HTML source
                    ├── _sources/               ||
                    ├── _static/                ||   
                    ├── rv101-filename1.html    || HTML file
                    ├── rv102-filename2.html    ||                           
                    ├── rv201-filename3.html    ||                     
                    ├── rv201-filename4.html    ||
                    └── index.html              || HTML site           
                ├── rv101-filename1.rst         || reStructuredText file
                ├── rv102-filename2.rst         || 
                ├── rv201-filename3.rst         || 
                └── rv202-filename4.rst         || 
            ├── [pdf]/                          || PDF report  
                ├── [docs]/                     ||     
                    ├── rv101-filename1.pdf     || PDF file
                    ├── rv102-filename2.pdf     ||                           
                    ├── rv201-filename3.pdf     ||                     
                    ├── rv201-filename4.pdf     ||
                    └── Report-Label.pdf        || PDF from rst2pdf report       
                ├── rv101-filename1.rst         || reStructuredText file
                ├── rv102-filename2.rst         || 
                ├── rv201-filename3.rst         || 
                └── rv202-filename4.rst         || 
            ├── [pdftex]/                       || PDFtex report
                ├── [docs]/                     ||     
                    ├── rv101-filename1.pdf     || PDF file
                    ├── rv102-filename2.pdf     ||                           
                    ├── rv201-filename3.pdf     ||                     
                    ├── rv201-filename4.pdf     ||
                    └── Report-Label.pdf        || PDF from LaTeX report       
                ├── rv101-filename1.rst         || reStructuredText file
                ├── rv102-filename2.rst         || 
                ├── rv201-filename3.rst         || 
                └── rv202-filename4.rst         || 
            ├── [text]/                         || text report
                ├── rv101-filename1.txt         ||
                ├── rv102-filename2.txt         || 
                ├── rv201-filename3.txt         ||
                ├── rv202-filename4.txt         ||
                └── README.txt                  || Searchable text report
            ├── [temp]/                         || temp files
                └── rv01-label3.tex             ||        
            └── rivt-report.py                  | report generating script
        ├── [src]                               |||| doc source files               
            ├── data/                           | author created folder
                ├── data1.csv                   |
                ├── newvals.csv                 |
                └── download1.csv               |
            ├── image/                          | author created folder                
                ├── fig1.png                    |
                └── fig2.jpg                    |
            ├── [Styles]/                       | doc style files 
                ├── [html]/                     | html style files
                    ├── _locale/                | 
                    ├── _locale/                |
                    ├── _static/                |        
                    ├── _templates/             |        
                    ├── conf.py                 |        
                    ├── genhtml.cmd             |        
                    └── index.rst               |
                ├── [pdf]/                      | rst2pdf style files
                    ├── fonts/                  |        
                    ├── style/                  |        
                    ├── Report-Cover.pdf        |            
                    └── genrst2pdf.cmd          |        
                ├── [pdftex]/                   | pdftex style files
                    ├── gentexpdf.cmd           |  
                    ├── Report-cover.pdf        |             
                    └── rivt.sty                |
                ├── [text]/                     | text ini file
                    └── rv-text.ini             | 
            ├── [Tools]/                        |||| scripts, input, output
                ├── plot.py                     | Python script or function                         
                ├── tablepy.csv                 | input read by Python                 
                └── imagepy.png                 || Python output
            ├── [Values]/                       |||| values files
                ├── [new-units.py]              | new units from author
                ├── added-values-v.csv          | new values from author
                ├── v101-2.csv                  || written by rivt
                └── v102-3.csv                  || written by rivt
        └── README.txt                          || Searchable text report 