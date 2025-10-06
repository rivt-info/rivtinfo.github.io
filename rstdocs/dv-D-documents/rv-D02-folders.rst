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

    [rv-dss-]file-label.py 


where the file-label prefix in brackets is required. 

The *doc number* is *dss* where *d* is an alphanumeric division label
and *ss* is a two digit subdivision number. The output of a *rivt file* is
a text (.txt), PDF (.pdf) or HTML (html) file, with the same file name.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Report Folders 
-------------------------------

.. raw:: html

    <hr>

A *rivt report* is assembled from a set of *rivt docs*. *Reports* are organized
using *doc numbers*. *rivt files* may be grouped in division folders using a
folder name with the form:

.. code-block:: bash

    [dv-]division-label

Division grouping may help with file navigation - it does not affect report
formatting. If three example *doc numbers* are:


.. code-block:: bash

    rv-A01-rivtfile.py
    rv-105-rivtfile.py
    rv-212-rivtfile.py  


then the *report numbers* used in the report will be: 

.. code-block:: bash

    A.1
    1.5
    2.13

where leading zeroes are dropped and *docs* are sorted alpha-numerically in a
*report*.


**[3]**  Folder Structure
-------------------------------

*Resource files* provided by a report author are stored in the *source* folder.
*Docs* are written to the *report* folder. *rivt files* flagged for open source
sharing are written to the *public* folder. 

Example *report* folder structures are shown below.

**Key**::

    - Required folder and file [prefixes] are shown in brackets []. 
    - Single vertical bar (|) identifies files provided by the *report* author. 
    - Double vertical bar (||) identifies files written by *rivtlib* 
    - Three vertical bars (|||) mix of author and *rivtlib* files


.. code-block:: bash

    Collapsed folders without division folders

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv-101-]doclabel1.py       | rivt file
        ├── [rv-102-]doclabel2.py       | rivt file
        ├── [rv-201-]doclabel3.py       | rivt file
        ├── [rv-202-]doclabel4.py       | rivt file  
        ├── [public]/                   || public rivt files
        ├── [report]/                   || reports and docs
        ├── [source]/                   ||| source files
        └── README.txt                  | GitHub searchable text report 

    Collapsed folders with division folders

    [rivt]-Report-Label/                Report Folder Name
        ├── [dv-]1-divlabel/                          
            ├── [rv-101-]doclabel1.py   | rivt file
            └── [rv-102-]doclabel2.py   | rivt file
        ├── [dv-]2-divlabel/ 
            ├── [rv-201-]doclabel3.py   | rivt file
            └── [rv-202-]doclabel4.py   | rivt file  
        ├── [public]/                   || public rivt files
        ├── [report]/                   || reports and docs
        ├── [source]/                   ||| source files
        └── README.txt                  | GitHub searchable text report 


    Expanded report folder with division folders

    [rivt]-Report-Label/                Report Folder Name
        ├── [dv-]1-divlabel/                          
            ├── [rv-101-]doclabel1.py   | rivt file
            └── [rv-102-]doclabel2.py   | rivt file
        ├── [dv-]2-divlabel/ 
            ├── [rv-201-]doclabel3.py   | rivt file
            └── [rv-202-]doclabel4.py   | rivt file        
        ├── [public]/                   || public rivt files                      
            ├── rv-101-doclabel1.py   
            └── rv-102-doclabel2.py   
            ├── rv-201-doclabel3.py   
            └── rv-202-doclabel4.py   
        ├── [report]/                      || Reports and Docs
            ├── [html]/                    || ------ HTML 
                ├── [docs]/                || HTML site        
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
            ├── [rst2pdf]/                  || ------ rst2pdf    
                ├── [src]/                          
                    ├── rv-101-doclabel1.rst
                    ├── rv-102-doclabel2.rst                           
                    ├── rv-201-doclabel3.rst                        
                    └── rv-202-doclabel4.rst              
                ├── rv-101-doclabel1.pdf    || rst2pdf PDF files
                ├── rv-102-doclabel2.pdf                         
                ├── rv-201-doclabel3.pdf                       
                ├── rv-202-doclabel4.pdf
                └── Report-Label.pdf        || rst2pdf PDF report
            ├── [texpdf]/                   || ------ texpdf
                ├── [src]/                          
                    ├── rv-101-doclabel1.rst
                    ├── rv-102-doclabel2.rst                        
                    ├── rv-201-doclabel3.rst                        
                    └── rv-202-doclabel4.rst               
                ├── rv-101-doclabel1.pdf    || texpdf PDF files
                ├── rv-102-doclabel2.pdf                          
                ├── rv-201-doclabel3.pdf                       
                ├── rv-202-doclabel4.pdf
                └── Report-Label.pdf        || tex2pdf PDF report  
            ├── [text]/                     || ------- text
                ├── rv-101-label1.txt      
                ├── rv-102-label2.txt
                ├── rv-201-label3.txt
                ├── rv-202-label4.txt
                └── README.txt              || GitHub searchable text report                     
            └── rivt-report.py              | report generator
        ├── [source]                  | source files 
            ├── [html]/               | html settings
                ├── _locale/                 
                ├── _static/                        
                ├── _templates/                     
                ├── conf.py                         
                ├── genhtml.cmd                     
                └── index.rst              
            ├── [i-ins1]/             | Insert files 
                ├── data1.csv
                ├── cover-page.pdf                       
                ├── data1.csv                   
                └── standards.txt
            ├── [r-run1]/              | Run files
                ├── data1.csv                
                ├── standards.txt
                ├── data1.csv                   
                └── standards.txt
            ├── [rst2pdf]/            | rst2pdf settings
                ├── fonts/              
                ├── style/                 
                ├── Report-Cover.pdf           
                └── genrst2pdf.cmd      
            ├── [t-tool1]/             | Tool files
                ├── plot.py                               
                └── imh.txt
            ├── [v-val1]/              ||| Value files
                ├── v101-2.csv         || exported values 
                ├── v102-3.csv         || exported values
                └── newvals.csv        | values to import
            ├── [temp]/
                └── rv01-label3.tex
            ├── [texpdf]/             | tex2pdf settings  
                ├── gentexpdf.cmd             
                ├── Report-cover.pdf                     
                └── rivt.sty              
            ├── [text]/               | text settings
                └── rv-text.ini 
        └── README.txt                 || GitHub searchable text report 