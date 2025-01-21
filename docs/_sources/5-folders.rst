.. _5-folders:

Folders
=======

The rivt folder structure organizes documents for reports and sharing. An
initial folder structure can be taken from an existing project or generated
with::

    python -m rivtfolders

Report and document headings are taken from folder and file names unless
overridden in the config file. An example folder structure is shown below.
Folder and file prefixes up to the underscore are fixed. The rivt input and
resource files are organized in divisions. Output files are published to
subfolders under the *rivtdocs* folder. Output (doc) files can be text, PDF,
MarkDown or HTML. rivt reports are collections of docs specified in the
config.ini. 

A separate *rivtpub* output folder (see below) is generated for use as a
shareable template.  Components of a rivt project that are private (not
shared) are specified in the rivt file and are not included in *rivtpub*.

Each rivt file is idenfifed by a document prefix with the form rddnn-filename
where dd is a two digit division number and nn is a two digit subdivision number
e.g., riv0203-loads.py is the third subdivision of division two. rivt files are
processed and published in document order. Editing the rivt number will change
the report organization. 


rivt folders
------------

::

    rivt-Report-Label/               
        ├── d01-div-label/                  (division 1 files)
            ├── r0101-label1.py             (rivt subdivsion file)
            └── r0102-label2.py             (rivt subdivsion file)
        ├── d02-div-label/                  (division 2 files)
            └── r0201-label3.py             (rivt subdivision file)
        ├── rivt-docs/                      (document output)
            ├── rivt-pdf_/                      
                ├── rivt0101-label1.pdf      
                ├── rivt0102-label2.pdf
                ├── rivt201-label3.pdf
                └── Report-Label.pdf 
            ├── rivt-text_/                    
                ├── rivt0101-label1.txt      
                ├── rivt0102-label2.txt
                └── rivt0201-label3.txt          
            ├── rivt-html_/                    
                ├── rivt0101-label1.html
                ├── rivt0102-label2.html
                └── rivt0201-label3.html        
            ├── rivt-temp_/
                └── d0201-label3.tex
        ├── r01/                            (source files)         
            ├── ins
                ├── fig1.png            
                └── attach1.pdf
            ├── run
                └── sap.cmd
            ├── tool
                ├── func1.py                   
                └── func2.py
            └── val
                └── val0101.csv
        ├── r02/                    
            ├── data1.csv                   
            └── standards.txt
        ├── config.ini                   (report config file)
        ├── cover-page.pdf               (report cover page)
        └── README.txt                   (searchable report) 


rivtpub output folders
----------------------

::


    rivtpub_Report-Label/               
        ├── div01_div-label/           
            ├── r0101_label1.py         
            └── r0102_label2.py   
        ├── [div02_div-label/           
            └── r0201_label3.py         
         ├── riv01/                    
            ├── ins
                ├── fig1.png            
                └── attach1.pdf
            ├── run
                └── sap.cmd
            ├── tool
                ├── func1.py                   
                └── func2.py
            └── val
        ├── riv02/                    
            ├── ins
            └── val
                ├── data.csv                   
                └── standard.txt
        ├── config.ini    
        └── README.txt  






Folders: document organization 
------------------------------

**rivt** implements a file and folder structure to simplify file sharing and
control. The privacy level of document inputs and outputs may be may be set at
the file or API function level. Each rivt file (and doc) is idenfiifed by a
unique rivt file prefix with the form rivddss-filename where dd is a two digit
division number and ss is a two digit subdivision number e.g., riv0203-loads.py
is the third subdivision of division two. Editing the rivt number also changes
the report organization.

Report and document headings are taken from folder and file names unless
overridden in the config file. An example folder structure is shown below.
Required file names or prefixes are shown in [ ].

Source files for rivt docs are stored in 6 folders::

    - append
    - images
    - scripts
    - tables
    - text
    - values

Output is written to the write folder with 4 sub-folders::

    - html
    - pdf
    - text
    - temp
    - xrivt

Doc files are the text, PDF or HTML output of a rivt file that are stored in
the *write* folder. rivt reports are collections of docs specified in the
config.ini. Resource files are stored in user-defined sub-folders which
organize the data allow for separation of public and private data.

::

    [rivt]-Project-Name/               
        ├── [append]/            
            ├── app01/  
            └── app02/  
                ├── attach3.pdf                   
                └── attach4.pdf
        ├── [images]/            
            ├── img01/  
            └── img02/  
                ├── image3.jpg                   
                └── image4.jpg
        ├── [scripts]/
            ├── py01/                 
            └── py02/  
                ├── function3.py
                └── function4.py               
            ├── run01/  
            └── run02/  
                ├── script3.bat
                └── script4.sh  
        ├── [tables]/            
            ├── tbl01/  
            └── tbl02/  
                ├── table3.csv                   
                └── table4.csv
        ├── [text]/            
            ├── tex01/  
            ├── tex02/  
                ├── latex3.tex
                └── latex4.tex
            ├── txt01/  
            └── txt02/  
                ├── text3.txt                   
                └── text4.txt
        ├── [values]/                 
            ├── dat01/  
            ├── dat02/  
                ├── table3.csv                   
                └── table4.csv
            ├── equ01/                      
            ├── equ02/                    
                ├── equation1.txt      
                └── equation2.txt       
            ├── val01/                    
            └── val02/                    
                ├── values3.csv      
                └── values4.csv       
        ├── [write]/                        (output files)    
            ├── [html]/                     
                └── riv0101-codes.html      (html files)
                    riv0202-frames.html
                    Project-Name.html       (html report) 
            ├── [pdf]/                      
                └── riv0101-codes.pdf       (pdf files)        
                    riv0202-frames.pdf
                    Project-Name.pdf        (pdf report)        
            ├── [temp]/                     (temp files)     
                └── temp-files.tex
            └── [text]/                     
                └── riv0101-codes.txt       (text output)
                    riv0201-frames.txt
            └── [xrivt-redacted]/            
                └── README.txt              (redacted report)
                    xriv0101-codes.py       (redacted files)
                    xriv0102-loads.py
                    xriv0201-walls.py       
        └── config.ini                      (rivt config file)
            README.txt                      (searchable report in public repo)
            riv0000-report.py               (rivt input files)
            riv0101-codes.py
            riv0102-loads.py
            riv0201-walls.py
            riv0202-frames.py
    
    