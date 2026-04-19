**D.3 Folders**
============================

.. raw:: html

    <hr>

.. _rivt-folders:

**[1t]**  rivt Folders
-------------------------------

A *rivt report* is assembled from a set of *docs*. *Reports* are organized
using *doc numbers*. If the *rivt file* names are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py

The *report numbers* used in the published report would be: 

.. code-block:: bash

    A.1
    1.5
    2.12

where leading zeroes are dropped and *docs* are sorted alpha-numerically into
divisions and subdivisions in the *report*.

Reports are organized under a single root report folder with the prefix
*rivt-*. *rivt files* are stored in the root folder and *rivt markup* file paths
are relative to the roo.  Resource files are stored in five subfolders:

*_public* 
    Includes *rivt files* written by *rivtlib* intended for upload to a
    public repository. The prefix *rvAnn-* is changed to *rvAnn_* to 
    avoid confusion with private files.

*_publish*
    Includes formatted *docs* and *reports* written by *rivtlib*.

*_stored*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden sections*, *metadata* and *reports*

*_rstdocs*
    Includes restructured *docs* written by *rivtlib*.

*Src* Includes author provided content and formatting for *docs*, *reports*.


An example report folder structure is shown in the following section.


.. _report-folders:

**Folder Names**

.. raw:: html

    <hr>

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Names</b><br>
    <br>
    
    A rivt report folder can contain any set of files and folders but the
    following structure is required for doc processing. Files and folders are
    organized under a root folder with the prefix <i>rivt-</i> e.g.
    <i>rivt-Report-Label</i>. <br> <br>
    
    The root folder includes at least the rivt files and five required
    subfolders. Required folders and prefixes are shown in brackets. Folders
    preceded by an underscore contain rivt outputs. Capitalized folder names
    contain files requiring author input. <br> <br>


**Top Level Folders** 

.. code-block:: bash

    [rivt-]Report-Label/                Report Folder
        ├── [conf.py]                   configuration file
        ├── [rv101-]filename1.py        rivt file
        ├── [rv102-]filename2.py        rivt file
        ├── [rv201-]filename3.py        rivt file
        ├── [rv202-]filename4.py        rivt file 
        ...
        ├── .vscode/                    optional VSCode settings   
        ├── [_publish]/                 published docs and reports
        ├── [_rstdocs]/                 restructured text files               
        ├── [_shared]/                  public rivt files
        ├── [_stored]/                  stored files
        ├── [Src]/                      source files        
        └── README.txt                  searchable text report 


**Expanded Folders**

.. code-block:: bash

   [rivt-]Report-Label/                Report Folder Name
        ├── .vscode/                         optional VSCode settings                    
        ├── [conf.py]                        configuration file    
        ├── [rv101-]filename1.py             rivt file
        ├── [rv102-]filename2.py             rivt file       
        ├── [rv201-]filename3.py             rivt file          
        ├── [rv202-]filename4.py             rivt file                           
        ├── [_publish]/                      published docs and reports
            ├── [docs]/                         html docs
                ├── _images/                
                ├── _sources/              
                ├── _static/    
                ├── process folders/         
                ├── site folders/                                        
                ├── rv101-filename1.html      
                ├── rv102-filename2.html                      
                ├── rv201-filename3.html                        
                ├── rv202-filename4.html         
            ├── [pdfdocs]/                      pdf docs
                ├── process folders/             
                ├── rv101-filename1.pdf             
                ├── rv102-filename1.pdf             
                ├── rv201-filename3.pdf 
                └── rv202-filename4.pdf  
            └── [txtdocs]/                      text docs
                ├── rv101-filename1.txt              
                ├── rv102-filename1.txt             
                ├── rv201-filename3.txt 
                └── rv202-filename4.txt
        ├── [_rstdocs]/                      restructured text files
            ├── _downloads/                    
            ├── _static/                       
            ├── _locale/                       
            ├── _templates/                    
            ├── rv101-filename1.rst            
            ├── rv102-filename2.rst                          
            ├── rv201-filename3.rst          
            └── rv202-filename4.rst
        ├── [_shared]/                       public rivt files                      
            ├── rv-101-filename1.py              
            ├── rv-102-filename1.py              
            ├── rv-201-filename3.py  
            └── rv-202-filename4.py 
        ├── [_stored]/                       stored files genereatd by rivt            
            ├── [Logs]/                         log files
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [Sect]/                         sections                    
                ├── rv202-5d.txt  
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [Temp]/                         temp files
                └── rv101-label3.tex
            └── [Vals]/                         stored value files
                ├── v101-2.csv
                └── v102-3.csv                 
        ├── [Src]                            source files from author               
            ├── data/                            author created subfolder
                ├── data1.csv 
                ├── opensees1.txt   
                └── conc-vals.csv  
            ├── image/                           author created subfolder                          
                ├── fig1.png
                └── fig2.jpg   
            ├── [Run]/                       OS commands
                    ├── run1_win.cmd             windows command file                  
                    └── run1_linux.sh            linux command file
            ├── [Tools]/                     scripts and functions
                ├── rivt-report.py               report generating script
                ├── new-units.py                 define new units          
                ├── coverpage.rst                cover page template
                ├── logoname.png                 cover page logo
                ├── plot.py                      functions        
                └── loads.py                     functions
            └── [Vals]/                      value files
                ├── steel-vals.csv     
                └── plastic-vals.csv   
        └── README.txt                       searchable text report 

