**D.3 Folders**
============================

.. raw:: html

    <hr>

.. _rivt-folders:

**[1t]**  rivt Folder
-------------------------------

.. _report-folders:

**Folder Names**

.. raw:: html

    <hr>

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Names</b><br>
    <br>
    
    A rivt folder can contain any set of files and folders but the following
    structure is required for <i>doc</i> processing. Files and folders are
    organized under a root folder with the prefix <i>rivt-</i> e.g.
    <i>rivt-Report-Label</i>. <br> <br>
    
    <i>rivt folders</i> (root folders) include at least the <i>rivt files</i>
    and the five required subfolders. Required folders and prefixes are shown
    in brackets[]. Folders preceded by an underscore contain rivt outputs.
    Folders and files requiring author input are capitalized. All files in the
    root folder except the README.txt file may require author input. <br> <br>

    A new <i>rivt folder</i> is typically copied from a similar folder or 
    template and then edited. Several <i>rivt folder templates</i> are at 
    <a href="https://drive.google.com/drive/folders/1hwVOs0CVJqdZlTieV_Lt5bICbd3ywzWj?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto">openmodels.info</a>.
     

**Top Level Folders** 

.. code-block:: bash

    [rivt-]Report-Label/             Report Folder                
        ├── .vscode/                    optional VSCode settings   
        ├── [_publish]/                 published docs and reports
        ├── [_rstdocs]/                 restructured text files               
        ├── [_shared]/                  public rivt files
        ├── [_stored]/                  stored files
        ├── [rv101-]filename1.py        rivt file
        ├── [rv102-]filename2.py        rivt file       
        ├── [rv201-]filename3.py        rivt file          
        ├── [rv202-]filename4.py        rivt file
        ...
        ├── [Src]/                      source files       
        ├── [Conf.py]                   configuration file
        ├── [Rivt-report.py]            report generating script
        ├── [New-units.py]              define new units (optional) 
        └──  README.txt                  text report written by rivt



**Expanded Folders**

A typical :term:`rivt folder` structure is shown below. The required *rivt file* 
names and prefixes are shown in brackets. 

.. code-block:: bash

   [rivt-]Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py             rivt file
        ├── [rv102-]filename2.py             rivt file       
        ├── [rv201-]filename3.py             rivt file          
        ├── [rv202-]filename4.py             rivt file
        ├── [Conf.py]                        configuration file
        ├── [Rivt-report.py]                 report generating script
        ├── [New-units.py]                   define new units (optional) 
        ├── README.txt                       text report written by rivt                        
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
                └── rv202-filename4.html         
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
        ├── [_rstdocs]/                     restructured text files
            ├── _downloads/                    
            ├── _static/                       
            ├── _locale/                       
            ├── _templates/                    
            ├── rv101-filename1.rst            
            ├── rv102-filename2.rst                          
            ├── rv201-filename3.rst          
            └── rv202-filename4.rst
        ├── [_shared]/                      public rivt files                      
            ├── rv-101-filename1.py              
            ├── rv-102-filename1.py              
            ├── rv-201-filename3.py  
            └── rv-202-filename4.py 
        ├── [_stored]/                      rivt generated stored files (not printed) 
            ├── [Logs]/                         log files
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [Sect]/                      rivt generated stored sections (not printed)                    
                ├── rv202-5d.txt  
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [Temp]/                         temp files
                └── rv101-label3.tex
            └── [Vals]/                         stored value files
                ├── v101-2.csv
                └── v102-3.csv                 
        ├── [Src]                            source files from author                       
            ├── data/                            author created subfolders
                ├── data1.csv 
                ├── opensees1.txt   
                └── conc-vals.csv  
            ├── image/                                                 
                ├── fig1.png
                └── fig2.jpg   
            ├── run/                              OS commands
                ├── run1_win.cmd                     windows command file                  
                └── run1_linux.sh                    linux command file
            ├── tools/                         scripts and functions
                ├── coverpage.rst                    cover page template
                ├── logoname.png                     cover page logo
                ├── plot.py                          functions        
                └── loads.py                         functions
            └── vals/                          value files
                ├── steel-vals.csv     
                └── plastic-vals.csv   


**[2t]**  Folder Names
-------------------------------

Reports are organized under a single root (rivt) folder with the prefix
*rivt-*. *rivt files* are stored in the root folder and *rivt markup* file paths
are relative to the roo.  Resource files are stored in five subfolders:

*_publish*
    Includes formatted *docs* and *reports* written by *rivtlib*.

*_share* 
    Includes *public rivt files* written by *rivtlib* intended for upload to a
    public repository. The prefix *rvAnn-* is changed to *rvAnn_* to 
    avoid confusion with private files.

*_stored*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden sections*, *metadata* and *reports*

*_rstdocs*
    Includes restructured *docs* written by *rivtlib*.

*Src* Includes author provided content and formatting for *docs*, *reports*.