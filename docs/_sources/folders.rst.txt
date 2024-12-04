Folders
=======

Folders are needed for organizing reports. A starter report folder structure can
be generated in the folder where the following command is executed:

*python -m rivtlib.folder-template*

This constructions 

**rivtlib** can process single rivt files, but typically it is used to generate
reports. rivt documents are organized into divisions (folders) and documents
(files). Reprort section names are taken from the the file and folder names but
may be overridden by a configuration file.



Document inputs and outputs may be stored in or directed to publically
shareable or private foldrers. Reports is formatted with divisions,
subdivisions and sections.


Fixed folder and file prefixes are shown in [ ]. Report and document headings
are taken from the folder and file labels. 


Folder structure
----------------

::

    [rivt]_Report-Label/               
        ├── [div01]-div-label/            (division folder)
            ├── [data01]/                 (resource data)
                ├── data.csv                   
                ├── attachment1.pdf
                ├── fig.png            
                └── functions.py                   
            ├── [riv01]-label1.py         (rivt file)
            └── [riv02]-label2.py         (rivt file)   
        ├── [div02]-div-label/            (division folder)
            ├── [data02]/                 (resource data)
                ├── data.csv
                └── fig.png
            └── [riv01]_label3.py         (rivt file)
        ├── [data-private]/                 
            ├── [data]/                   (private data)                   
                ├── data.csv
                ├── attachment.pdf
                └── fig.png        
            ├── [functions]/              (private functions)                   
                ├── [data]/
                ├── [output]/
                └── function.py                
            ├── [rivt-docs]/              (private output documents)
                ├── [pdf]/                      
                    ├── doc0101-label1.pdf      
                    ├── doc0102-label2.pdf
                    ├── doc0201-label3.pdf
                    └── Report-Label.pdf 
                ├── [text]/                    
                    ├── doc0101-label1.txt      
                    └── doc0201-label3.txt       
                ├── doc0101-label1.md            
                └── doc0201-label3.md
            ├── [temp]/
                └── doc0201-label3.tex 
        ├── [functions]/                  (public functions)                   
            ├── [data]/
            ├── [output]/
            ├── function1.py
            └── function2.py                
        ├── [rivt-docs]/                  (public output documents)
            ├── [pdf]/                      
                ├── doc0101-label1.pdf      
                ├── doc0102-label2.pdf
                ├── doc0201-label3.pdf
                └── Report-Label.pdf 
            ├── [text]/                    
                ├── doc0101-label1.txt      
                ├── doc0102-label2.txt
                └── doc0201-label3.txt           
        ├── .gitignore
        ├── config.ini                    (config file)
        ├── doc0101-label1.md             (public output documents) 
        ├── doc0102-label2.md
        ├── doc0201-label3.md
        └── README.txt                    (cumulative documents - searchable) 



::
        
    [rivt]-Report-Label/               
        ├── .git
        ├── units.py                        (input: unit over-ride)
        ├── README.md                       (output: toc and summary) 
        ├── rivt01.ini                      (input: config file)
        ├── [doc0101]-div-label/            (first division - first file)
            ├── [data0101]/                     (inputs: data files)
                ├── data1.csv                   
                ├── paper1.pdf
                └── functions1.py                   
            ├── [rivt]-doc-label1.py            (input: rivt file)
            └── README.md                       (output: GFM doc)
        ├── [doc0102]/                      (first division - second file)
            ├── data[0102]/                     (inputs: data files)
                ├── data1.csv
                ├── fig1.png
                └── fig2.png
            ├── [rivt]-doc-label2.py            (input: rivt file)
            └── README.md                       (output: GFM doc)
        ├── [doc0201]-div-label/            (second division - first file)
            ├── [data0201]/                     (inputs: data files)
                ├── data1.csv
                ├── attachment.pdf
                ├── functions.py
                └── fig1.png
            ├── [rivt]-doc-label3.py            (input: rivt file)
            └── README.md                       (outputs: GFM doc)
        └── [private]/                      (private files)
            ├── [temp]/                         (outputs: temp files)
            ├── [report]/                       (report files)
                ├── 0101-Doc Label1.pdf         (outputs: PDF docs)
                ├── 0102-Doc Label2.pdf
                ├── 0201-Doc Label3.pdf
                └── Report Label.pdf            
            ├── images/                         (inputs: optional private data)
                ├── fig1.png
                └── fig2.png
            ├── text/    
                ├── text1.txt
                └── text2.txt
            ├── append/    
                ├── report1.pdf
                └── report2.pdf
            └── tables/
                ├── data1.csv
                └── data1.xls


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
    