# Folders

**rivtlib** can process single rivt files, but typically it is used to generate
reports. rivt documents are organized into divisions (folders) and documents
(files). Reprort section names are taken from the the file and folder names but
may be overridden by a configuration file.



Document inputs and outputs may be stored in or directed to publically
shareable or private foldrers. Reports is formatted with divisions,
subdivisions and sections.


Fixed folder and file prefixes are shown in [ ]. Report and document headings
are taken from the folder and file labels. 


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
