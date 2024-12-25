
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
        ├── d01-div-label/              (division 1 files)
            ├── r0101-label1.py         (rivt subdivsion file)
            └── r0102-label2.py         (rivt subdivsion file)
        ├── d02-div-label/              (division 2 files)
            └── r0201-label3.py         (rivt subdivision file)
        ├── rivt-docs/                       (document output)
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
        ├── r01/                        (source files)         
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
            ├── data.csv                   
            └── standard.txt
        ├── config.ini                   (report config file)
        ├── cover-page.pdf               (report cover page)
        └── README.txt                   (searchable report) 


rivtpub output
---------------

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
            ├── too
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
