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



<pre>
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
</pre>

