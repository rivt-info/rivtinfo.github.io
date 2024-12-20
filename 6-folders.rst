
Folders
=======

The rivt folder structure organizes documents for reports and sharing. A starter
report folder structure can be taken from an existing project or generated
with::

    python -m rivtlib.folder-template

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

Each rivt file is idenfifed by a prefix with the form rivddss-filename where dd
is a two digit division number and ss is a two digit subdivision number e.g.,
riv0203-loads.py is the third subdivision of division two. Editing the rivt
number will change the report organization. 


rivt folders
------------

::

    rivt_Report-Label/               
        ├── div01_div-label/            (division 1 inputs)
            ├── r0101_label1.py         (rivt file)
            └── r0102_label2.py   
        ├── [div02_div-label/           (division 2 inputs)
            └── r0201_label3.py         (rivt file)
        ├── docs/                       (document output)
            ├── pdf_/                      
                ├── d0101_label1.pdf      
                ├── d0102_label2.pdf
                ├── d0201_label3.pdf
                └── Report-Label.pdf 
            ├── text_/                    
                ├── d0101_label1.txt      
                ├── d0102_label2.txt
                └── d0201_label3.txt       
            ├── md_/                    
                ├── d0101_label1.md      
                ├── d0102_label2.md
                └── d0201_label3.md       
            ├── html_/                    
                ├── d0101_label1.html
                ├── d0102_label2.html
                └── d0201_label3.html        
            ├── temp_/
                └── d0201_label3.tex
        ├── riv01/                        (input source files)         
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
        ├── config.ini                   (report config file)
        ├── cover-page.pdf               (report cover page)
        └── README.txt                   (searchable collated doc) 


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
        ├── cover-page.pdf
        └── README.txt    
