**C.3 |** Folders
===============================================================================

.. _rivt-folders:

**[1]**  Report Folders
------------------------------------------------------------------------------

A typical :term:`report folder` structure is shown below. The required 
*rivt file* names and prefixes are shown in brackets.  For the
:term:`rivtbook folder` structure see :ref:`see <rivt-books>`.

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Naming</b><br>
    <br>

    A report folder can contain any file or folder but the following structure is
    required for <i>doc</i> processing. <i>report folders</i> include at least
    the folders and files shown in brackets[] below. Folders with an underscore
    contain rivt generated files. Files and folders are organized under
    a rivt root folder with the prefix <i>rivt-</i> followed by the report
    label, e.g. <i>rivt-Report-Label</i>. <br> <br>

    A new <i>report folder</i> is typically started by copying and editing a
    similar folder. Several <i>rivt-folders</i> can be downloaded at 
    <a href="https://drive.google.com/drive/folders/1hwVOs0CVJqdZlTieV_Lt5bICbd3ywzWj?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto">openmodels.info</a>.
    <br> <br>


Reports are organized using the folllowing folders and subfolders. 

*rivt-* report-label 
    Top level report folder containing rivt report and public files.

*_rivt-public* 
    Includes *public rivt files* designated byt the author written by 
    *rivtlib* for public sharing. The prefix *rvAnn-* is changed to 
    *rv-Ann-* to avoid confusion with non-public files.

*rivt-report* 
    Includes files and folders for publishing docs and reports. 


*required subfolders of rivt-report*

*rvsrc* 
    Includes author provided source files used by *rivt files* including 
    data, images, run commands, tools and value files.

*rv_stor*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden sections* and *metadata* that may be read by other *rivt files*.

*_published*
    Formatted *docs* and *reports* written by *rivtlib* for publication. 
    Subfolders include *docs* (HTML), *pdfdocs* (PDF) and *txtdocs* (text).

*_rstdocs*
    Intermediate restructured text files written by *rivtlib*.

.. _default-folders:

**[3]**  Default Folders
------------------------------------------------------------------------------

Files are opened using default paths relative to the *rivt-report* folder for
*reports* and the *specific chapter folder* for *rivtbooks*. They have the form:

| COMMAND | filename | parameters

For example, to read and insert an image file the command would be:

| IMAGE | filename.png | parameters 

If a user specified file path is needed it needs to be specified relative to
the *rivt-report* folder for *reports* and the *specific chapter folder* for
*rivtbooks*. It needs to include at least one folder separator "/" in the path
specification. See :ref:`command summary <command-summary>` for further
details.

**Default Paths for Commands**

================ ========================= =============================
    Command        Default Report Paths     Default rivtbook Paths  
================ ========================= =============================
\| SHELL |          **rvsrc/script**         **script/**     
\| IMAGE |          **rvsrc/image**          **image/** 
\| IMAGE2 |         **rvsrc/image**          **image/**   
\| PYTHON |         **rvsrc/script**         **script/**  
\| TABLE |          **rvsrc/data**           **data/**  
\| TEXT |           **rvsrc/script**         **script/**  
\| VALTABLE |       **rvsrc/data**           **data/**   
\| VALDATA |        **_rvstor/data**         **_rvstor/** 
\| ATTACHPDF |      **rvsrc/image**          **image/**  
\| PUBLISH |        **/_published/**         **rivtbook/_published/**  
================ ========================= =============================

[1] file paths begin with rvsrc/ and may include subdirectories 
[2] values are read from *rvsrc/* and its subdirectories
[3] values written by *rivt* are read from *rv_stor/vals*  
[4] *docs* are written to subdirectories of *_published*


.. _report-folders2:

**[4]**  Report Folder Structure
------------------------------------------------------------------------------

.. code-block:: bash

    [rivt-]Report-Label/             report folder              
        ├── .help/                        help files
        ├── .vscode/                      optional VSCode settings   
        ├── README.txt                    rivt-generated text report                  
        ├── [_rivt-public]/               rivt-generated public files
            ├── rvsrc/                        author source files          
            ├── rv-101-filename1.py           public rivt file
            ├── rv-102-filename2.py           public rivt file       
            ├── rv-201-filename3.py           public rivt file          
             ...
        ├── [rivt-report]/                 report folder               
            ├── [rivt-report]-1.py            report generating script
            ├── [rv101-]filename1.py          rivt file
            ├── [rv102-]filename2.py          rivt file       
            ├── [rv201-]filename3.py          rivt file          
                ...
            ├── [rvsrc]/                      author provided files and folders        
                ├── [downloads]/                    files to download      
                    └── conc-vals.txt 
                ├── [img]/                          page layout images              
                    ├── favicon.png    
                    ├── covlogo1.png    
                    └── runlogo1.png                   
                ├── [vals]/                         tables    
                    └── steel-vals.csv                                                 
                ├── [scripts]/                      scripts
                    └── bending.py    
                ├── tools/                          OS shell commands               
                    └── opensees.sh                        
                ├── fig1.png
                └── fig2.jpg                  
            ├── [rv_stor]/                    rivt-generated source files
                ├── [logs]/                          log files
                    ├── rv101-log.txt
                    └── rv102-log.txt
                ├── [sect]/                          sections not printed                    
                    ├── rv202-5d.txt  
                    ├── rv103-4t.txt                         
                    └── rv301-2r.txt               
                ├── [temp]/                          temp files
                    └── rv101-label3.tex
                ├── [vals]/                          values files
                    ├── v101-2.csv
                    └── v102-3.csv         
                ├── output.dat
            ├── [_published]/                 rivt-published docs and reports
                ├── [docs]/                          html docs
                    ├── html auxiliary folders    
                    ├── index.html
                    ├── rv101-filename1.html      
                    ├── rv102-filename2.html                      
                    ├── rv201-filename3.html                        
                        ...     
                ├── [pdfdocs]/                       pdf docs
                    ├── pdf auxiliary folders     
                    ├── report-title.pdf
                    ├── rv101-filename1.pdf             
                    ├── rv102-filename1.pdf             
                    ├── rv201-filename3.pdf 
                        ...  
                └── [txtdocs]/                       text docs
                    ├── report-title.txt
                    ├── rv101-filename1.txt              
                    ├── rv102-filename1.txt             
                    ├── rv201-filename3.txt 
                        ...
            └── [_rstdocs]/                     rivt-generated rst files
                ├── _downloads/                    
                ├── _static/                                                       
                ├── rv101-filename1.rst            
                ├── rv102-filename2.rst                          
                ├── rv201-filename3.rst          
                    ...


.. _rivtbook-folders:       

**[3]**  rivtbook Folders
------------------------------------------------------------------------------

.. code-block:: bash

    [rivtbk-]Book-Label/             rivtbook report folder              
        ├── .help/                        help files
        ├── .vscode/                      optional VSCode settings   
        ├── README.txt                    rivt-generated book as text
        ├── [rivtbook-report]-1.py        rivtbook generating script                  
        ├── [_rstdocs]/                   rivt-generated rst files
            ├── _downloads/                    
            ├── _static/                                                       
            ├── rv101-filename1.rst            
            ├── rv102-filename2.rst                          
            ├── rv201-filename3.rst          
                ...
        ├── [_pdfdocs]/                   pdf docs and rivtbook report
            ├── pdf auxiliary folders     
            ├── report-title.pdf
            ├── rv101-filename1.pdf             
            ├── rv102-filename1.pdf             
            ├── rv201-filename3.pdf
        └── [_rv_stor]/                    rivt-generated source files
            ├── [logs]/                          log files
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [sect]/                          sections not printed                    
                ├── rv202-5d.txt  
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [temp]/                          temp files
                └── rv101-label3.tex
            ├── [vals]/                          values files
                ├── v101-2.csv
                └── v102-3.csv         
            └── output.dat 
        ├── [bk1-]folder name              rivtbook chapter folder
            ├── [rv001-]filename1.py          rivt file       
            ├── [downloads]/                    files to download      
                └── conc-vals.txt 
            ├── [img]/                          page layout images              
                ├── favicon.png    
                ├── covlogo1.png    
                ├── runlogo1.png
                └── fig1.png
            ├── [data]/                          tables    
                └── steel-vals.csv                                                 
            ├── [vals]/                          values files
                ├── v101-2.csv
                └── v102-3.csv         
            └── tools/                           OS shell commands               
                └── opensees.sh                           
        ├── [bk2-]folder name             rivtbook chapter folder
                ...        
        └── [bk3-]folder name             rivtbook chapter folder
                ...
