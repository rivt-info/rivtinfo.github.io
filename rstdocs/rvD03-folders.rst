**D.3 Folders**
============================

**[1t]** File Names
-------------------------------

.. raw:: html

    <hr>

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
   *hidden*, and *metadata* and *reports*

*Rst_docs*
    Includes formatted *docs* and *reports* written by *rivtlib*.

*Src*
    Includes author provided content, style and generating files for *docs* 
    and *reports*.


An example *report* folder structure is shown below.


.. _report-folders:

**[3t]**  Report Folders
-------------------------------

**Folder Names**

.. raw:: html

    <hr>

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Names</b><br>
    <br>
    A rivt report folder can contain any files and folders but the following
    structure is required for doc processing. Files and folders are organized
    under a root folder with the prefix *rivt-* e.g. *rivt-Report-Label*. The
    root folder includes the *rivt files* and five required subfolders.<br>
    <br>
    The folder structure for single docs is simplified by removing the 
    <i>Src</i> and <i>_stored</i> folders and storing their files in the 
    root folder. The report script is not used for single docs.<br>
    <br>
    Required folder prefixes are shown in brackets.Required folders are
    capitalized or preceded by an underscore. Folders preceded by an underscore
    are rivt outputs. Folder names that include both output and author input
    include an underscore.

**Top Level Folders** 

.. code-block:: bash

    [rivt-]Report-Label/                Report Folder
        ├── [rv101-]filename1.py        rivt file
        ├── [rv102-]filename2.py        rivt file
        ├── [rv201-]filename3.py        rivt file
        ├── [rv202-]filename4.py        rivt file 
        ...
        ├── [.vscode]/                  optional VSCode settings   
        ├── [_public]/                  public rivt files
        ├── [_publish]/                 published docs and reports
        ├── [_stored]/                  stored files
        ├── [Rst_docs]/                 restructured text files               
        ├── [Src]/                      source files        
        └── README.txt                  searchable text report 


**Expanded Folders**

.. code-block:: bash

   [rivt-]Report-Label/                  Report Folder Name
        ├── [.vscode]/                       optional VSCode settings                    
        ├── [rv101-]filename1.py             rivt file
        ├── [rv102-]filename2.py             rivt file       
        ├── [rv201-]filename3.py             rivt file          
        ├── [rv202-]filename4.py             rivt file                        
        ├── [_public]/                       public rivt files                      
            ├── rv_101-filename1.py              
            ├── rv_102-filename1.py              
            ├── rv_201-filename3.py  
            └── rv_202-filename4.py    
        ├── [_publish]/                      published docs and reports
            ├── [docs]/                      html output 
                ├── _images/                
                ├── _sources/              
                ├── _static/    
                ├── process folders/         
                ├── site folders/                                        
                ├── rv101-filename1.html      
                ├── rv102-filename2.html                      
                ├── rv201-filename3.html                        
                ├── rv202-filename4.html         
            ├── [pdfdocs]/                   pdf doc output
                ├── process folders/             
                ├── rv-101-filename1.pdf             
                ├── rv-102-filename1.pdf             
                ├── rv-201-filename3.pdf 
                └── rv-202-filename4.pdf  
            └── [txtdocs]/                   text output 
                ├── rv-101-filename1.txt              
                ├── rv-102-filename1.txt             
                ├── rv-201-filename3.txt 
                └── rv-202-filename4.txt        
        ├── [_stored]/                       stored files from rivt            
            ├── [Logs]/                      log files
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [Sect]/                      stored sections                    
                ├── rv202-5d.txt   
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [Temp]/                      temp files
                └── rv101-label3.tex
            └── [Vals]/                      stored value files
                ├── v101-2.csv
                └── v102-3.csv     
        ├── [Rst_docs]/                      restructured text files
            ├── _downloads/                    
            ├── _static/                       
            ├── _locale/                       
            ├── _templates/                    
            ├── rv101-filename1.rst            
            ├── rv102-filename2.rst                          
            ├── rv201-filename3.rst          
            ├── rv202-filename4.rst
            ├── gen-html.cmd                 html generating script
            ├── gen-pdf.cmd                  pdf generating script
            ├── gen-pdftex.cmd               LaTeX generating script
            ├── rivt-report.py               report generating script
            ├── new-units.py                 define new units          
            ├── coverpage.rst                cover page template
            ├── logoname.png                 cover page logo
            └── conf.py                      style paths and settings              
        ├── [Src]                            source files from author               
            ├── data/                        author created subfolder
                ├── data1.csv   
                └── conc-vals.csv  
            ├── image/                       author created subfolder                          
                ├── fig1.png
                └── fig2.jpg
            ├── output/                      author created subfolder
                ├── table1.csv                                               
                ├── image1.png                            
                └── opensees1.txt    
            ├── [Run]/                       OS commands
                    ├── run1_win.cmd                               
                    └── run1_linux.sh            
            ├── [Tools]/                     scripts and functions
                    ├── plot.py                               
                    └── loads.py
            └── [Vals]/                      value files
                ├── steel-vals.csv     
                └── plastic-vals.csv   
        └── README.txt                       searchable text report 

