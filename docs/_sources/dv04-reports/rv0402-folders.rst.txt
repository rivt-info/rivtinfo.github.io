4.2 - Files and Folders
============================

**[01]** rivt files
--------------------

A *rivt file* is the basic unit of a rivt report. Its output is a *rivt doc* - a
subdivision in a *report heirarchy*. Each *rivt* and *doc* file is identified
with a *doc number* of the form:

.. code-block:: bash

    [rvddss]-file-name.py 


**[02]** Project Folders 
-------------------------------


.. topic:: Note: 

    - Fixed prefixes are shown in brackets ([]). 
    - A single vertical bar (|) identifies files provided by the author. 
    - A double bar (||) identifies a file or folder written by rivt 


The top level folder structure is:

.. code-block:: bash

    [rivt]-Report-Label/          Report Folder 
        ├── [dv01-]divlabel/          division folder
        ├── [dv02-]divlabel/          division folder                   
        ├── [public]/                 public rivt files
        ├── [reports]/                reports and docs
        ├── [source]/                 source files      
        └── README.txt                text report 


*rivt files* are organized into numbered division folders of the form:

.. code-block:: bash

    [dvdd-]division-name

where dd is a two digit division number. 

An expanded folder structure looks like this:

.. code-block:: bash


    [rivt]-Report-Label/                 # Report Folder
        ├── [dv01-]divlabel/                  # div 01 folder
            ├── [rv0101-]doclabel1.py               | rivt file
            └── [rv0102-]doclabel2.py               | rivt file
        ├── [dv02-]divlabel/                  # div 02 folder
            ├── [rv0101-]doclabel3.py               | rivt file
            └── [rv0102-]doclabel4.py               | rivt file         
        ├── [public]/                         # rivt files - public sections
            ├── dv01-divlabel1/                   || div 01 files - public
                ├── rv0101-doclabel1.py        
                └── rv0102-doclabel2.py  
            ├── dv02-divlabel2/                   || div 02 files - public
                ├── rv0101-doclabel3.py      
                └── rv0102-doclabel4.py
            └── README.txt                        || GitHub searchable report              
        ├── [reports]/                        # Reports and Docs
            ├── [html]/                       # HTML sites and docs
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
                        ├── _locale                | settings
                        ├── _static                | settings
                        └── _templates             | settings
                        ├── dv01-divlabel1\
                            ├── rv0101-doclabel1.rst
                            └── rv0102-doclabel2.rst
                        ├── dv02-divlabel2\                            
                            ├── rv0201-doclabel3.rst                        
                            └── rv0202-doclabel4.rst 
                        ├── conf.py                 
                        ├── index.rst              
                        └── README.txt 
                ├── conf.py                         | config file
                ├── index.rst                       | index file
                └── genhtml.cmd                     | build commands
            ├── [rpdf]/                           # rPDF report and docs             
                ├── [srcdocs]                      || rPDF reST files
                    ├── fonts\                      | fonts
                    └── style\                      | settings 
                    ├── dv01-divlabel1\
                        ├── rv0101-doclabel1.rst
                        └── rv0102-doclabel2.rst
                    ├── dv02-divlabel2\                            
                        ├── rv0201-doclabel3.rst                        
                        └── rv0202-doclabel4.rst
                ├── dv01-divlabel1\                  || rPDF docs   
                    ├── rv0101-doclabel1.pdf
                    └── rv0102-doclabel2.pdf
                ├── dv02-divlabel2\                            
                    ├── rv0201-doclabel3.pdf                       
                    └── rv0202-doclabel4.pdf
                ├── README.txt                       || GitHub searchable report 
                ├── Report-Label.pdf                 || rPDF report
                └── genrpdf.cmd                      | build commands
            ├── [tpdf]/                           # tPDF report and docs
                ├── [srcdocs]                        || tPDF reST files
                    ├── texpdf-style\
                    ├── dv01-divlabel1\
                        ├── rv0101-doclabel1.rst
                        └── rv0102-doclabel2.rst
                    ├── dv02-divlabel2\                            
                        ├── rv0201-doclabel3.rst                        
                        └── rv0202-doclabel4.rst
                ├── dv01-divlabel1\               # tPDF docs
                    ├── rv0101-doclabel1.pdf
                    └── rv0102-doclabel2.pdf
                ├── dv02-divlabel2\                            
                    ├── rv0201-doclabel3.pdf                       
                    └── rv0202-doclabel4.pdf
                ├── [temp]/
                    └── d0201-label3.tex  
                ├── README.txt                   || GitHub searchable report 
                ├── Report-Label.pdf             || tPDF report
                └── gentpdf.cmd                  | build commands
            ├── [text]/                          || text report and docs
                ├── dv01-divlabel1\
                    ├── rv0101-label1.txt      
                    └── rv0102-label2.txt
                ├── dv02-divlabel1\
                    ├── rv0201-label3.txt
                    └── rv0202-label4.txt
                └── rivt-Report-Label.txt                                    
        ├── [source]                          # Sources for rivt files 
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
            ├── [v01]/                          | div 01 Value files 
                ├── val0101-2.csv                 
                └── val0102-3.csv
            ├── [v02]/                          | div 02 Value files 
                └── othervals.csv
        └── README.txt                       # GitHub searchable report 


