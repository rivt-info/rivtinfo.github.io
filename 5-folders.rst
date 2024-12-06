Folders
=======

Folders are needed for organizing reports. A starter report folder structure can
be generated in the folder where the following command is executed::

    python -m rivtlib.folder-template


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

Source files for rivt docs are stored in 6 folders:

- append
- images
- scripts
- tables
- text
- values

Output is written to the write folder with 4 sub-folders:

- html
- pdf
- text
- temp
- xrivt

Doc files are the text, PDF or HTML output of a rivt file that are stored in
the *write* folder. rivt reports are collections of docs specified in the
config.ini. Resource files are stored in user-defined sub-folders which
organize the data allow for separation of public and private data.

Fixed folder and file prefixes are shown in [ ]. Report and document headings
are taken from the folder and file labels. 

Folder structure
----------------

::

    [rivt]_Report-Label/               
        ├── [div01]-div-label/           (division folder)
            ├── [data01]/                (resource folder)
                ├── data.csv                   
                ├── attachment1.pdf
                ├── fig.png            
                └── functions.py                   
            ├── [riv01]-label1.py        (rivt file)
            └── [riv02]-label2.py   
        ├── [div02]-div-label/           (division folder)
            ├── [data02]/                (resource folder)
                ├── data.csv
                └── fig.png
            └── [riv01]_label3.py        (rivt file)
        ├── [rivt-docs]/                 (documents)
            ├── [pdf]/                      
                ├── doc0101-label1.pdf      
                ├── doc0102-label2.pdf
                ├── doc0201-label3.pdf
                └── Report-Label.pdf 
            ├── [text]/                    
                ├── doc0101-label1.txt      
                ├── doc0102-label2.txt
                └── doc0201-label3.txt       
            ├── [md]/                    
                ├── doc0101-label1.md      
                ├── doc0102-label2.txt
                └── doc0201-label3.md       
            ├── [html]/                    
                ├── doc0101-label1.html
                ├── doc0102-label2.html
                └── doc0201-label3.html        
            ├── [temp]/
                └── doc0201-label3.tex 
        ├── .gitignore
        ├── config.ini                   (config file)
        └── README.md                    (collated doc - searchable) 

