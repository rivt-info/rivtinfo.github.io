**C.2 Folders**
============================

 

.. _rivt-folders:

**[1]**  rivt Folder
-------------------------------

.. _report-folders:

**Folder Names**

 .. raw:: html

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

    [rivt-]Report-Label/             rivt Folder
        ├── .vscode/                    optional VSCode settings   
        ├── README.txt                  rivt-generated report                  
        ├── [_rivt-public]/                 public subset of rivt files
            ├── rv_stor/                    
            ├── rvsrc/                        
            ├── README.txt                              
            ├── rv-101-filename1.py         
            ├── rv-102-filename2.py                
            ├── rv-201-filename3.py                   
            ├── rv-202-filename4.py         
            ...
        └── [rivt-report]/              report folder              
            ├── [_published]/               published docs and reports
            ├── [_rstdocs]/                 restructured text files               
            ├── [rv_stor]/                  rivt generated source files
            ├── [rvsrc]/                    author provided source files
            ├── [rv101-]filename1.py        rivt file
            ├── [rv102-]filename2.py        rivt file       
            ├── [rv201-]filename3.py        rivt file          
            ├── [rv202-]filename4.py        rivt file
            ...    

**Expanded Folders**

A typical :term:`rivt folder` structure is shown below. The required *rivt file* 
names and prefixes are shown in brackets. 

.. code-block:: bash

    [rivt-]Report-Label/             rivt Folder              
        ├── .vscode/                      optional VSCode settings   
        ├── README.txt                    rivt-generated report                  
        ├── [_rivt-public]/               rivt-generated public files
            ├── rv_stor/                    rivt source files
            ├── rvsrc/                        author source files          
            ├── rv-101-filename1.py             public rivt file
            ├── rv-102-filename2.py             public rivt file       
            ├── rv-201-filename3.py             public rivt file          
            ├── rv-202-filename4.py             public rivt file
             ...
        └── [rivt-report]/                 report folder               
                ├── [rv101-]filename1.py          rivt file
                ├── [rv102-]filename2.py          rivt file       
                ├── [rv201-]filename3.py          rivt file          
                ├── [rv202-]filename4.py          rivt file
                 ...
                ├── [rvsrc]                     author source files and folders        
                    ├── down/                      files to download      
                        └── conc-vals.txt 
                    ├── data/                       tables    
                        └── steel-vals.csv                                                 
                    ├── run/                        scripts and functions              
                        └── plot.py                   
                    ├── tools/                       OS shell commands               
                        └── opensees.sh                        
                    ├── fig1.png
                    └── fig2.jpg                  
                ├── [rv_stor]/                     rivt-generated source files
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
                ├── [_published]/                   published docs and reports
                    ├── [docs]/                       html docs
                        ├── html auxiliary files
                         ...                
                        ├── index.html
                        ├── rv101-filename1.html      
                        ├── rv102-filename2.html                      
                        ├── rv201-filename3.html                        
                        ├── rv202-filename4.html
                         ...     
                    ├── [pdfdocs]/                      pdf docs
                        ├── pdf auxiliary files
                         ...             
                        ├── report-title.pdf
                        ├── rv101-filename1.pdf             
                        ├── rv102-filename1.pdf             
                        ├── rv201-filename3.pdf 
                        ├── rv202-filename4.pdf
                        ...  
                    └── [txtdocs]/                      text docs
                        ├── report-title.txt
                        ├── rv101-filename1.txt              
                        ├── rv102-filename1.txt             
                        ├── rv201-filename3.txt 
                        ├── rv202-filename4.txt
                        ...
                ├── [_rstdocs]/                       restructured text files
                    ├── _downloads/                    
                    ├── _static/                       
                    ├── _locale/                                         
                    ├── rv101-filename1.rst            
                    ├── rv102-filename2.rst                          
                    ├── rv201-filename3.rst          
                    ├── rv202-filename4.rst
                    ...

**[2]**  Folder Names
-------------------------------

Reports are organized using the folllowing folders and naming conventions,
with the required names and prefixes shown in italics:

*rivt-* report-label 
    Top level rivt folder containing rivt report and public files.

*_rivt-public* 
    Includes *public rivt files* written by *rivtlib* for public sharing.
    The prefix *rvAnn-* is changed to *rv-Ann-* to avoid confusion with 
    private files.

*rivt-report* 
    Includes folders for source and published files and *docs*. 

*rvsrc* 
    Includes source files used by *rivt files* including data, images, run
    commands, tools and value files.

*_published*
    Includes formatted *docs* and *reports* .

*rv_stor*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden sections* and *metadata*.

*_rstdocs*
    Includes intermediate restructured text files written by *rivtlib*.

