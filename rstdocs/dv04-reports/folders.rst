**4.2 - Folders**
==================

The rivt folder structure is designed to produce reports and open source
templates. A starting folder structure can be copied from an existing project,
or generated from the command line with::

    python -m rivtfolders

An example folder structure is shown below. **rivt** implements a file and
folder structure to simplify file sharing and control. Each rivt file (and doc)
is idenfiifed by a unique rivt file prefix with the form rivddss-filename where
dd is a two digit division number and ss is a two digit subdivision number
e.g., riv0203-loads.py is the third subdivision of division two. Editing the
rivt number also changes the report organization.

**rivt** input files are organized in numbered divisions. Output files (docs)
are written to the *docs* folder. rivt reports are collections of docs and are
also written to the *docs* folder. Doc files may be published as text, latex
pdf, text pdf or HTML documents. The privacy level of document inputs may be
set at the file or section level. A separate *osdocs* (open source docs) folder
is used to write the subset of file inputs intended for open sharing on GitHub
(or other version control systems).

**rivt files**
-----------------

Each **rivt** file is identified with a document prefix of the form
rddnn-filename where dd is a two digit division number and nn is a two digit
subdivision or file number e.g., riv0203-loads.py is the third subdivision (doc
file) of division two. rivt files are processed and published in document
order. Editing the rivt number will change the report organization. rivt
resource files (images, tables etc.) are stored in the sub-folders *insdd,
valdd* and *tools*. The folder names correspond to the associated function API.
**rivt** reports are collections of docs.

Report and document titles are taken from folder and file names unless
overridden in the rivt-config file. An example folder structure is shown below
where fixed file names or prefixes are shown in [ ].


**rivt folders**
----------------

::


    [rivt]-Report-Label/               
        ├── [d01]-div-label/                (division 1 files)
            ├── [ins01]/                    (insert files)
                ├── fig1.png            
                └── attach1.pdf
            └── [val01]/                    (values files)
                └── val0101.csv
            ├── r0101-label1.py             (rivt file)
            └── r0102-label2.py             (rivt file)
        ├── [d02]-div-label/                (division 2 files)
            ├── [ins01]/      
                ├── data1.csv                   
                └── standards.txt
            └── r0201-label3.py             (rivt file)
        ├── [docs]/                    (document output)
            ├── xpdf/                      
                ├── rivt0101-label1.pdf      
                ├── rivt0102-label2.pdf
                ├── rivt201-label3.pdf
                └── Report-Label.pdf 
            ├── lpdf/                      
                ├── rivt0101-label1.pdf      
                ├── rivt0102-label2.pdf
                ├── rivt201-label3.pdf
                └── Report-Label.pdf 
            ├── text/                    
                ├── rivt0101-label1.txt      
                ├── rivt0102-label2.txt
                └── rivt0201-label3.txt          
            ├── html/                    
                ├── rivt0101-label1.html
                ├── rivt0102-label2.html
                └── rivt0201-label3.html        
            ├── temp/
                └── d0201-label3.tex             
        ├── [tools]/                        (function and shell files)
            ├── func1.py                   
            └── sap.cmd
            └── func2.py                  
        ├── [rivt-config.ini]               (config file)
        ├── cover-page.pdf                  (report cover page)
        └── README.txt                      (text report - GitHub searchable) 

