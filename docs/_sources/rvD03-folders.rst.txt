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
are relative to the roo.  Resource files are stored in four primary subfolders:

*public* 
    Includes *rivt files* written by *rivtlib* intended for upload to 
    a public repository.

*publish*
    Includes formatted *docs* and *reports* written by *rivtlib*.

*src*
    Includes author provided content, style and generating files for *docs* 
    and *reports*.

*stored*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden*, and *metadata* and *reports*

An example *report* folder structure is shown below.

**Folder Key**

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    Required names or prefixes are shown in brackets [ ]. <br>
    <br>
    Folders (including subfolders) that contain author generated files 
    are marked with a single vertical bar ( | ).<br>  
    <br>ri
    Folders (including subfolders) that contain rivtlib generated files are 
    marked with double vertical bars ( || ).</p>

.. _single-doc-folders:

**[2t]**  Single Doc Folders
-------------------------------

.. raw:: html

    <hr>

.. code-block:: bash

    [rivt-]single-doc-label/                 Single doc Folder            
        ├── [rv101-]filename.py              |  rivt input file
        ├── multiple source files            |  data, image and function files
        ├── addunits.py                      |  define new units
        ├── rv-101-log.txt                   || log file                          
        ├── rv-101-docname.py                || public rivt file
        ├── README.txt                       || searchable text doc 
        ├── [.vscode]/                       |  optional VSCode settings            
        ├── [rstdocs]/                       |  rst style input
            ├── _downloads/                  |  external doc files 
            ├── _static/                     |  style files
            ├── _locale/                     |  style files
            ├── _templates/                  |  style files   
            ├── coverpage.rst                |  pdf cover page template
            ├── logoname.png                 |  cover page logo
            ├── conf.py                      |  style settings
            └── rv101-filename.rst           || intermediate rst file      
        ├── [pdfdocs]/                       || pdf output
            ├── process folders/             
            └── rv101-filename.pdf           
        ├── [htmldocs]/                      || html output 
            ├── process folders/                html process folders
            ├── site folders/                   html site folders and files                            
            └── rv101-filename.html             html doc
        ├── [latexdocs]/                     || latex output
            ├── latexstyle.sty               |  pdf style file
            ├── process files/                  latex process files                   
            └── rv101-filename.pdf              pdf doc from LaTeX 
        ├── [textdocs]/                      || text output 
            └── rv101-filename.txt              text doc   
  


.. _report-folders:

**[3t]**  Report Folders
-------------------------------

.. raw:: html

    <hr>

**Reports - Top Level Folders**

.. code-block:: bash

    [rivt-]Report-Label/                Report Folder
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 
        ...
        ├── [.vscode]/                  |  optional VSCode settings   
        ├── [Files]/                    |  source and style files from author
        ├── [publish]/                  || doc and report files
        ├── [stored]/                   || rivt stored files
        └── README.txt                  || searchable text report 


**Reports - Expanded Folders**

.. code-block:: bash

   [rivt-]Report-Label/                         Report Folder Name                
        ├── [rv101-]filename1.py                 |  rivt file
        ├── [rv102-]filename2.py                 |  rivt file       
        ├── [rv201-]filename3.py                 |  rivt file          
        ├── [rv202-]filename4.py                 |  rivt file            
        ├── [.vscode]/                           |  optional VSCode settings   
        ├── [Files]/                             |  files from authors               
            ├── [Rstdocs]/                       |  intermediate rst files
                ├── _downloads/                  |  external doc files 
                ├── _static/                     |  style files
                ├── _locale/                     |  style files
                ├── _templates/                  |  style files 
                ├── rv101-filename1.rst          || intermediate rst file 
                ├── rv102-filename2.rst                          
                ├── rv201-filename3.rst          
                ├── rv202-filename4.rst          
                ├── coverpage.rst                |  pdf cover page template
                ├── logoname.png                 |  cover page logo
                └── conf.py                      |  style paths and settings              
            ├── [Data]/                          |  data files
                ├── data1.csv  
                └── conc-vals.csv                        
            ├── [Image]/                         | image files                                             
                ├── fig1.png
                └── fig2.jpg
            ├── [Scripts]/                       | script and shell files     
                ├── shell1.cmd   
                ├── shell1.csv  
                ├── plot.py                               
                ├── addunits.py                                    
                └── opensees1.cmd   
            └── [Attach]/                        | pdf attachments
                ├── attach1.pdf
                └── attach2.pdf 
        ├── [publish]/                           || published docs and reports
            ├── [htmldocs]/                      || html output 
                ├── process folders/                html process folders
                ├── site folders/                   html site folders and files                            
                ├── rv101-filename1.html      
                ├── rv102-filename2.html                      
                ├── rv201-filename3.html                        
                ├── rv202-filename4.html         
            ├── [latexdocs]/                     || latex output
                ├── process folders/             || latex process folders
                ├── latexstyle.sty               |  pdf style file
                ├── rv101-filename.rst           || intermediate rst file
                ├── rv101-filename1.rst          
                ├── rv102-filename2.rst          
                ├── rv201-filename3.rst          
                ├── rv202-filename4.rst          
                ├── rv-101-filename1.pdf         || latex pdf doc output    
                ├── rv-102-filename1.pdf             
                ├── rv-201-filename3.pdf 
                └── rv-202-filename4.pdf 
            ├── [pdfdocs]/                       || pdf doc output
                ├── process folders/                pdf working files
                ├── rv-101-filename1.pdf             
                ├── rv-102-filename1.pdf             
                ├── rv-201-filename3.pdf 
                └── rv-202-filename4.pdf  
            ├── [publicfiles]/                   || public rivt files                      
                ├── rv-101-filename1.py              
                ├── rv-102-filename1.py              
                ├── rv-201-filename3.py  
                └── rv-202-filename4.py    
            └── [textdocs]/                      || text output 
                ├── rv-101-filename1.txt              
                ├── rv-102-filename1.txt             
                ├── rv-201-filename3.txt 
                └── rv-202-filename4.txt        
        ├── [stored]/                            || stored files from processing
            ├── [logs]/                          ||log files
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [sect]/                          || excluded sections                  
                ├── rv202-5d.txt   
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            └── [data]/                          || rivt generated data
                ├── table1.csv                      stored script output                                  
                ├── image1.png                      stored images
                └── v102-3.csv                      rivt value table output
        └── README.txt                           || searchable text report 

