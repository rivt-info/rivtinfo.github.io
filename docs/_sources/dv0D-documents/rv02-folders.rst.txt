**D.2 Files and Folders**
============================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** rivt files
--------------------

.. raw:: html

    <hr>

The output of a *rivt file* is a *rivt doc* formatted as a text, PDF or HTML
file. A *rivt report* is assembled from a set of *rivt docs*. *rivt* and
*doc* files are organized using *doc numbers* of the form:

.. code-block:: bash

    [rvss]-file-name.py 

where *ss* is a two digit subdivision number.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Report Folders 
-------------------------------

.. raw:: html

    <hr>


*rivt files* are stored in numbered division folders of the form,

.. code-block:: bash

    [dvdd-]division-name

where dd is a two digit alpha-numeric division label.

The division label and rivt number together make up the *doc number* used to
organize a report. If leading characters are 0 they are stripped. For example
if the *rivt file name* and *division folder* are: 

.. code-block:: bash

    dv0A-divisionfolder
    rv01-rivtfile.py 
   
    
then the *doc number* used in the report will be: 

.. code-block:: bash

    A.1

Resource files used for *rivt* are provided by the report author and are stored
in the *source* folder. *Docs* are wrtittne to the *report* folder. *rivt
files* marked for open source sharing are written to the *public* folder. The
full *report* folder structure (both collapsed and expanded) is shown below.

**Key**::

    - Required folder and file prefixes are shown in brackets ([]). 
    - Single vertical bar (|) identifies files provided by the *report* author. 
    - Double vertical bar (||) identifies files written by *rivtlib* 


.. code-block:: bash

    [rivt]-Report-Label/              Report Name
        ├── [dv01-]divlabel/          | division folder
        ├── [dv02-]divlabel/          | division folder                   
        ├── [public]/                 || public rivt files
        ├── [report]/                 || reports and docs
        ├── [source]/                 | source files
        ├── rivt-report.py            | report generator
        └── README.txt                | GitHub searchable report 



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


