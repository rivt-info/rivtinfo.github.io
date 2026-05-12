**C.2 Folders**
============================

.. raw:: html

    <hr>

.. _rivt-folders:

**[1]**  rivt Folder
-------------------------------

.. _report-folders:

**Folder Names**

.. raw:: html

    <hr>

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Names</b><br>
    <br>
    
    A rivt folder can contain any file or folder but the following
    structure is required for <i>doc</i> processing. Files and folders are
    organized under a rivt root folder with the prefix <i>rivt-</i> followed by
    the report label, e.g. <i>rivt-Report-Label</i>. <br> <br>
    
    A new <i>rivt folder</i> is typically started by editing a similar
    folder or template. Several <i>rivt folder templates</i> are at 
    <a href="https://drive.google.com/drive/folders/1hwVOs0CVJqdZlTieV_Lt5bICbd3ywzWj?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto">openmodels.info</a>.
     
    <i>rivt folders</i> include at least the folders and files shown in
    brackets[] below. Folders with an underscore prefix contain rivt input files.
    Folders with an underscore suffix contain output files written by *rivt*. 
    <br> <br>

    
**Top Level Folders** 

.. code-block:: bash

    [rivt-]Report-Label/               Report Folder
        ├── .vscode/                    optional VSCode settings   
        ├── README.txt                  rivt-generated report                  
        ├── [_rivt-public]/                 rivt-generated public files
            ├── _src/                       source files  
            ├── README.txt                  public report            
            ├── rv-101-filename1.py         public rivt file
            ├── rv-102-filename2.py         public rivt file       
            ├── rv-201-filename3.py         public rivt file          
            ├── rv-202-filename4.py         public rivt file
            ...
        └── [rivt-report]/              rivt files and docs               
            ├── [src_]/                     source files
            ├── [_published]/               published docs and reports
            ├── [_rstdocs]/                 restructured text files               
            ├── [_stored]/                  stored files
            ├── [config-report.py]          report generating script
            ├── [rv101-]filename1.py        rivt file
            ├── [rv102-]filename2.py        rivt file       
            ├── [rv201-]filename3.py        rivt file          
            ├── [rv202-]filename4.py        rivt file
            ...    

**Expanded Folders**

A typical :term:`rivt folder` structure is shown below. The required *rivt file* 
names and prefixes are shown in brackets. 

.. code-block:: bash

    [rivt-]Report-Label/             Report Folder                
        ├── .vscode/                      optional VSCode settings   
        ├── README.txt                    rivt-generated report                  
        ├── [_rivt-public]/               rivt-generated public files
            ├── _src/                           source files  
            ├── README.txt                      public report            
            ├── rv-101-filename1.py             public rivt file
            ├── rv-102-filename2.py             public rivt file       
            ├── rv-201-filename3.py             public rivt file          
            ├── rv-202-filename4.py             public rivt file
            ...
        └── [rivt-report]/                 rivt files and docs               
                ├── [rv101-]filename1.py          rivt file
                ├── [rv102-]filename2.py          rivt file       
                ├── [rv201-]filename3.py          rivt file          
                ├── [rv202-]filename4.py          rivt file
                ...
                ├── [src_]                  author source files        
                    ├── data/                       tables    
                        ├── opensees1.txt   
                        └── conc-vals.csv  
                    ├── image/                                                 
                        ├── fig1.png
                        └── fig2.jpg   
                    ├── run/                         OS commands
                        ├── run1_win.cmd                    
                        └── run1_linux.sh                   
                    ├── tools/                       scripts and functions
                        ├── coverpage.rst                   
                        ├── logoname.png                    
                        ├── plot.py                         
                        └── loads.py                        
                    └── vals/                         value files
                        ├── steel-vals.csv     
                        └── plastic-vals.csv               
                ├── [_published/               published docs and reports
                    ├── [docs]/                       html docs
                        ├── _downloads/                
                        ├── _images/              
                        ├── _locale/            
                        ├── _sources/                
                        ├── _sphinx_design_static/              
                        ├── _static/            
                        ├── _templates/            
                        ├── .doctrees/
                        ├── .buildinfo
                        ├── .buildinfo.bak
                        ├── .nojekyll
                        ├── genindex.html
                        ├── search.html
                        ├── objects.inv
                        ├── searchindex.js
                        ├── rv101-filename1.html      
                        ├── rv102-filename2.html                      
                        ├── rv201-filename3.html                        
                        ├── rv202-filename4.html
                        ...     
                    ├── [pdfdocs]/                      pdf docs
                        ├── process folders/             
                        ├── rv101-filename1.pdf             
                        ├── rv102-filename1.pdf             
                        ├── rv201-filename3.pdf 
                        ├── rv202-filename4.pdf
                        ...  
                    └── [txtdocs]/                      text docs
                        ├── rv101-filename1.txt              
                        ├── rv102-filename1.txt             
                        ├── rv201-filename3.txt 
                        ├── rv202-filename4.txt
                        ...
                ├── [_rstdocs]/                    restructured text files
                    ├── _downloads/                    
                    ├── _static/                       
                    ├── _locale/                       
                    ├── _templates/                    
                    ├── rv101-filename1.rst            
                    ├── rv102-filename2.rst                          
                    ├── rv201-filename3.rst          
                    ├── rv202-filename4.rst
                    ...
                ├── [_stored]/                     rivt generated files
                    ├── [logs]/                         log files
                        ├── rv101-log.txt
                        └── rv102-log.txt
                    ├── [sect]/                          sections not printed                    
                        ├── rv202-5d.txt  
                        ├── rv103-4t.txt                         
                        └── rv301-2r.txt               
                    ├── [temp]/                          temp files
                        └── rv101-label3.tex
                    ├── output.dat
                    ├── v101-2.csv
                    └── v102-3.csv         


**[2]**  Folder Names
-------------------------------

Reports are organized using the folllowing foldeers with the required names and prefixes
shown in italics:

*rivt-* report-label 
    Top level rivt folder containing rivt report and public files.

*rivt-public_* 
    Includes *public rivt files* written by *rivtlib* for public sharing.
    The prefix *rvAnn-* is changed to *rv-Ann-* to avoid confusion with 
    private files.

*rivt-report* 
    Includes folders for source and published files and *docs*. 

*_src* 
    Includes source files used by *rivt files* including data, images, run
    commands, tools and value files.

*published_*
    Includes formatted *docs* and *reports* .

*stored_*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden sections* and *metadata*.

*rstdocs_*
    Includes intermediate restructured text files written by *rivtlib*.

