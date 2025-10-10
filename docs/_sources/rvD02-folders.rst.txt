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

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

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

An example *report* folder structure is shown below.

**Key**

- Required folder and file prefixes names are shown in brackets []. 
- Single vertical bar (|) identifies files provided by the report author. 
- Double vertical bar (||) identifies files written by rivtlib 
- Four vertical bars (||||) mix of author and rivtlib written files


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