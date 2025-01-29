4. Folders
==========

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


rivt folders
--------------

::


    rivt-Report-Label/               
        ├── d01-div-label/                  (division 1 files)
            ├── ins01/                      (insert files)
                ├── fig1.png            
                └── attach1.pdf
            └── val01/                      (values files)
                └── val0101.csv
            ├── r0101-label1.py             (rivt file)
            └── r0102-label2.py             (rivt file)
        ├── d02-div-label/                  (division 2 files)
            ├── ins01/      
                ├── data1.csv                   
                └── standards.txt
            └── r0201-label3.py             (rivt file)
        ├── rivt-docs/                      (document output)
            ├── rivt-pdf/                      
                ├── rivt0101-label1.pdf      
                ├── rivt0102-label2.pdf
                ├── rivt201-label3.pdf
                └── Report-Label.pdf 
            ├── rivt-xpdf/                      
                ├── rivt0101-label1.pdf      
                ├── rivt0102-label2.pdf
                ├── rivt201-label3.pdf
                └── Report-Label.pdf 
            ├── rivt-text/                    
                ├── rivt0101-label1.txt      
                ├── rivt0102-label2.txt
                └── rivt0201-label3.txt          
            ├── rivt-html/                    
                ├── rivt0101-label1.html
                ├── rivt0102-label2.html
                └── rivt0201-label3.html        
            ├── rivt-temp/
                └── d0201-label3.tex             
        ├── tools/                           (functions and shell files)
            ├── func1.py                   
            └── sap.cmd
            └── func2.py                  
        ├── rivt-config.ini                 (report config file)
        ├── cover-page.pdf                  (report cover page)
        └── README.txt                      (report - GitHub searchable) 

