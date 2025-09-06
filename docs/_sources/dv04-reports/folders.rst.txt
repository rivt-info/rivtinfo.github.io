4.1 - Files and Folders
============================

**[01]** rivt files
---------------------

A *rivt file* is the basic unit of a rivt report. Its output is a *rivt doc*
which is a subdivision in the report heirarchy. Each *rivt file* is
identified with a *doc* prefix number of the form: 

    rvddss-file-name.py 
    
where dd is a two digit division number and ss is a two digit subdivision
number e.g., rv0203-loads.py. Editing the doc number changes the report
organization.

Resource files used in *rivt files* are organized in the *source* folder.

**[02]** rivt folders
----------------------

An example *rivt folder structure* for reports is shown below. *rivt files* are
organized into numbered division folders of the form:

    dvdd-division-name

where dd is the two digit division number.

*Docs* are written to the *reports* folder. A *report* is an organized assembly
of *docs*.

Report and document titles are taken from folder and file names unless
over-rides are specified in the rivt-config.ini file.


**[03]** Report folder structure
---------------------------------

An example folder structure is shown below. 


.. topic:: Annotation notes:

    - Prefixes are shown in brackets ([]). 
    - A single vertical bar (|) identifies a file or folder produced by the user. 
    - A double bar (||) identifies a file or folder written by rivt

:: 


    [rivt]-Report-Label/           ======== Project Folder =========
        ├── [dv01-]divlabel/                   div 01 folder
            ├── [rv0101-]doclabel1.py               | rivt file
            └── [rv0102-]doclabel2.py               | rivt file
        ├── [dv02-]divlabel/                   div 02 folder
            ├── [rv0101-]doclabel3.py               | rivt file
            └── [rv0102-]doclabel4.py               | rivt file         
        ├── [public]/                     ==== rivt files - public sections ====
            ├── dv01-divlabel1/                 || div 01 files
                ├── rv0101-doclabel1.py        
                └── rv0102-doclabel2.py  
            ├── dv02-divlabel2/                 || div 02 files
                ├── rv0101-doclabel3.py      
                └── rv0102-doclabel4.py
            └── README.txt                      || GitHub searchable report              
        ├── [reports]/                     ==== Reports and Docs ====
            ├── [html]/                           || HTML reports and docs
                ├── [docs]/                       || HTML site
                        ├── _images
                        ├── _sources
                        └── _static
                        ├── dv01-divlabel1\       || HTML docs
                            ├── rv0101-doclabel1.html
                            └── rv0102-doclabel2.html
                        ├── dv02-divlabel2\                            
                            ├── rv0201-doclabel3.html                       
                            └── rv0202-doclabel4.html
                        ├── index.html 
                        └── README.txt            || GitHub searchable report                      
                ├── [srcdocs]                     || HTML reST files
                        ├── _locale
                        ├── _static
                        └── _templates
                        ├── dv01-divlabel1\
                            ├── rv0101-doclabel1.rst
                            └── rv0102-doclabel2.rst
                        ├── dv02-divlabel2\                            
                            ├── rv0201-doclabel3.rst                        
                            └── rv0202-doclabel4.rst 
                        ├── conf.py 
                        ├── index.rst 
                        └── README.txt            || GitHub searchable report 
                ├── conf.py 
                ├── index.rst 
                └── genhtml.cmd               
            ├── [rpdf]/                           || rPDF report and docs             
                ├── [srcdocs]                     || rPDF reST files
                    ├── fonts\
                    └── rstpdf-style\
                    ├── dv01-divlabel1\
                        ├── rv0101-doclabel1.rst
                        └── rv0102-doclabel2.rst
                    ├── dv02-divlabel2\                            
                        ├── rv0201-doclabel3.rst                        
                        └── rv0202-doclabel4.rst
                ├── dv01-divlabel1\               || rPDF docs   
                    ├── rv0101-doclabel1.pdf
                    └── rv0102-doclabel2.pdf
                ├── dv02-divlabel2\                            
                    ├── rv0201-doclabel3.pdf                       
                    └── rv0202-doclabel4.pdf
                ├── README.txt                    || GitHub searchable report 
                └── Report-Label.pdf              || rPDF report
            ├── [tpdf]/                           || tPDF report and docs
                ├── [srcdocs]                     || tPDF reST files
                    ├── texpdf-style\
                    ├── dv01-divlabel1\
                        ├── rv0101-doclabel1.rst
                        └── rv0102-doclabel2.rst
                    ├── dv02-divlabel2\                            
                        ├── rv0201-doclabel3.rst                        
                        └── rv0202-doclabel4.rst
                ├── dv01-divlabel1\               || tPDF docs
                    ├── rv0101-doclabel1.pdf
                    └── rv0102-doclabel2.pdf
                ├── dv02-divlabel2\                            
                    ├── rv0201-doclabel3.pdf                       
                    └── rv0202-doclabel4.pdf
                ├── [temp]/
                    └── d0201-label3.tex  
                ├── README.txt                    || GitHub searchable report 
                └── Report-Label.pdf              || tPDF report
            ├── [text]/                           || text report and docs
                ├── dv01-divlabel1\
                    ├── rv0101-label1.txt      
                    └── rv0102-label2.txt
                ├── dv02-divlabel1\
                    ├── rv0201-label3.txt
                    └── rv0202-label4.txt
                └── rivt-Report-Label.txt                                    
        ├── [source]                      ==== Source files for rivt files ====      
            ├── [rt01]/                         | div 01 Run and Tool files 
                ├── data1.csv                
                └── standards.txt
            ├── [rt02]/                         | div 02 Run and Tool files 
                ├── data1.csv                   
                └── standards.txt
            ├── [i01]/                          | div 01 Insert files 
                ├── data1.csv
                ├── cover-page.pdf                       
                └── standards.txt
            ├── [i02]/                          | div 02 Insert files 
                ├── data1.csv                   
                └── standards.txt
            ├── [v01]/                        ||| div 01 Value files 
                ├── val0101-2.csv                 
                └── val0102-3.csv
            ├── [v02]/                        ||| div 02 Value files 
                └── othervals.csv
        └── README.txt                      || GitHub searchable report 
