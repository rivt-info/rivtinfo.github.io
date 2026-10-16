**C.3 |** Folders
===============================================================================

.. _rivt-folders:

**[1]**  Report Folders
------------------------------------------------------------------------------

A typical :term:`report folder` structure is shown below. The top level 
folder is the *rivt project folder*. The required 
*rivt file* names and prefixes are shown in brackets.  For the
:term:`rivtbook folder` structure see :ref:`see <rivt-books>`.

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Naming</b><br>
    <br>

    A report project folder can contain any file or folder but the following structure
    is required for <i>doc</i> processing. <i>report folders</i> include at least
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
    Top level project folder containing rivt report and public files.

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
*reports* and *doc folders* for *rivtbooks*. They have the form:

| COMMAND | filename | parameters

For example, to read and insert an image file the command would be:

| IMAGE | image1.png | parameters 

If a different file path is needed it needs to be specified relative to
the *rivt-report* folder for *reports* and the *doc folder* for
*rivtbooks*. A unique path is triggered by including at least one folder 
separator "/" in the path specification. 

See :ref:`command summary <command-summary>` for further details.

**Default Paths for Commands**

================= ========================= =============================
    Command        Default Report Paths     Default rivtbook Paths  
================= ========================= =============================
\| SHELL |          **rvsrc/script**         **script/**     
\| IMAGE |          **rvsrc/image**          **image/** 
\| IMAGE2 |         **rvsrc/image**          **image/**   
\| PYTHON |         **rvsrc/script**         **script/**  
\| TABLE |          **rvsrc/data**           **data/**  
\| TEXT |           **rvsrc/script**         **script/**  
\| VALTABLE |       **rvsrc/data**           **data/**   
\| VALDATA |        **_rvstor/data**         **_rvstor/** 
\| ATTACHPDF |      **rvsrc/image**          **image/**  
\| PUBLISH | [1]    **/_published/**         **rivtbook/_published/**  
================= ========================= =============================

[1] *docs* are written to subdirectories of *_published*


.. _report-folders2:

**[4]**  Report Folder Structure
------------------------------------------------------------------------------

.. code-block:: bash

    [rivt-]Report-Label/             report project folder              
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


.. _rivt-reports:

**[1]**  Report Folders
-------------------------------------------------------

A typical :term:`report folder` structure is shown below. The required 
*rivt file* names and prefixes are shown in brackets.  For the
:term:`rivtbook folder` structure see :ref:`here <rivt-books>`.

A report folder can contain any file or folder but the following structure is
required for doc processing. *report folders* include at least the folders and
files with prefixesshown in brackets[] below. Folders with an underscore
contain rivt generated files. Files and folders are organized under a rivt root
folder with the prefix *rivt-* followed by the report label, e.g.
rivt-Report-Label.

A new report folder is typically started by copying and editing a
similar folder. rivt-folder examples can be downloaded at 
`Google Drive <https://drive.google.com/drive/folders/1hwVOs0CVJqdZlTieV_Lt5bICbd3ywzWj?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto>`__.

**[2]**  Folder Names
------------------------------------------------------------------------------

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

*_rvstor*
   Includes output files written by *rivtlib* including *logs*, *values*, 
   *hidden sections* and *metadata* that may be read by other *rivt files*.

*_published*
    Formatted *docs* and *reports* written by *rivtlib* for publication. 
    Subfolders include *docs* (HTML), *pdfdocs* (PDF) and *txtdocs* (text).

*_rstdocs*
    Intermediate restructured text files written by *rivtlib*.


.. _report-folders:

**[3]**  Report Folder Structure
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
                ├── [image]/                          page layout images              
                    ├── favicon.png    
                    ├── covlogo1.png    
                    └── runlogo1.png                   
                ├── [data]/                         tables    
                    └── steel-vals.csv                                                 
                ├── [scripts]/                      scripts and shell coammands
                    ├── bending.py    
                    └── opensees.sh                                 
            ├── [_rvstor]/                    rivt-generated files
                ├── [logs]/                          log and temp files
                    ├── rv101-log.txt
                    └── rv102-log.txt
                ├── [sect]/                          sections not printed                    
                    ├── rv202-5d.txt  
                    ├── rv103-4t.txt                         
                    └── rv301-2r.txt               
                ├── [data]/
                    ├── output.dat                   output files
                    ├── v101-2.csv
                    └── v102-3.csv         
            ├── [_published]/                  docs and reports
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
            └── [_rstdocs]/                     rst files
                ├── _downloads/                    
                ├── _static/                                                       
                ├── rv101-filename1.rst            
                ├── rv102-filename2.rst                          
                ├── rv201-filename3.rst          
                    ...


.. _rivt-report:

**[2]** rivt-report.py
----------------------------------------------------------

The Python *report script* includes settings that specify assembly parameters
and override defaults. These include:

- *Docs* to be included in the report
- Division names
- recompiling *docs*
- report cover page and title

provides the option to either regenerate all *docs* or to
assemble the report from previously generated *docs*.  Most aspects of
the *report* appearance are determined at when generating *docs*.

An example rivt-report.py script is shown below.

.. code-block:: python

    #! python
    """generate rivt report

    Run this Python script in the rivt-report folder to write reports to the
    _published folder. Copy and rename this file to save custom report settings
    (e.g. rivt-folder-new.py).

    The script does not regenerate individual PDF docs unless specified in the
    settings. Regenerating individual PDF docs adds execution time. HTML and text
    docs are always regenerated. See https://www.rivt.info for more details.
    """

    # ========= Modify report settings between the double lines ==============
    iniS = """
    [settings]
    ;----- file name for report including extension (pdf, html, txt)
    rept_filename = rivt-treehouse-report.txt
    ;----- comma separated list of excluded doc numbers eg. rv102, rv204
    exclude = -- 
    ;-----  update settings and configuration files from rivt 
    rivt_cfg = true
    ;----- regenerate pdf doc files 
    regen_pdf = false

    [format]
    title = Treehouse Design 
    subtitle =rivt report
    client = Example
    project_ref = Proj. 0001
    authors = R Holland 
    copyright = StL
    version = 1.0.0a12
    ;----- logo files are stored in rvsrc/page folder, size is % page width
    coverlogo = tree1.png
    coverlogo_size = 50
    ;----- header and footer logos and labels
    running_logo = rivt02.png 
    running_label = rivt
    ;----- underline links in PDF - true or false
    pdf_link = true 
    ;----- page size letter, legal, A4 - margins top, right, bottom and left
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    """
    # ============================================================================
    # the following line is required after settings
    import rivtlib.rvreport

    
.. _rivt-books:

**[1]** rivtbooks
----------------------------------------------------------

A :term:`rivtbook` collects *rivt files* sharing a common theme under a folder
structure that allows direct copy and paste into *rivt docs* and *reports*. 
Its primary purpose is as an organized collection of files that can be
directly selected and copied/merged as shown in the diagram below.

.. figure::  _static/img/rvbk-rivt.jpg
    :class: dark-light
    :scale: 40%
    :align: center
    :alt: copy rivtbook


A *rivtbook* may be printed as a PDF, txt and README.txt file for review and
exploration by using the *rivtbook-report.py* script.


**[2]** rivtbook Folder
----------------------------------------------------------
 
 
A typical :term:`rivtbook folder` structure is shown below. The required 
*rivt file* names and prefixes are shown in brackets. For the 
:term:`report folder` structure see :ref:`see <rivt-report>`.

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Naming</b><br>
    <br>

    A rivtbook folder can contain any file or folder but the following structure is
    required for <i>rivtbook</i> processing. <i>rivtbook folders</i> include at 
    least the folders and files shown in brackets[] below. Folders with an 
    underscore contain rivt generated files. Files and folders are organized under
    a <i>rivtbk</i> root folder with the prefix <i>rivtbk-</i> followed by the 
    rivtbook label, e.g. <i>rivtbk-Book-Label</i>. <br> <br>

    A new <i>rivtbook folder</i> is typically started by copying and editing a
    similar folder. Several <i>rivt-folder</i> examples can be downloaded at 
    <a href="https://drive.google.com/drive/folders/1hwVOs0CVJqdZlTieV_Lt5bICbd3ywzWj?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto">openmodels.info</a>.
    <br> <br>

**rivtbook Folders**

.. code-block:: bash

    [rivtbk-]Book-Label/             rivtbook report folder              
        ├── .help/                        help files
        ├── .vscode/                      optional VSCode settings   
        ├── README.txt                    rivtbook as text
        ├── [rivtbook-report]-1.py        rivtbook generating script                  
        ├── [_pdfdocs]/                   rivtbook pdf report
            ├── pdf auxiliary folders     
            ├── report-title.pdf
            ├── rv101-filename1.pdf             
            ├── rv102-filename1.pdf             
            ├── rv201-filename3.pdf
        ├── [_rstdocs]/                   rst files
            ├── _downloads/                    
            ├── _static/                                                       
            ├── rv101-filename1.rst            
            ├── rv102-filename2.rst                          
            ├── rv201-filename3.rst          
                ...
        └── [_rvstor]/                    rivt-generated source files
            ├── [logs]/                          log and temp files
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [sect]/                          sections stored and not printed                    
                ├── rv202-5d.txt  
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [data]/                          rivt and script output files
                ├── v101-2.csv
                └── v102-3.csv         
        ├── [bk1-]folder name              rivtbook chapter folder
            ├── [rv001-]filename1.py          rivt file       
            ├── [downloads]/                  files to download      
                └── conc-vals.txt 
            ├── [images]/                     page layout images              
                ├── favicon.png    
                ├── covlogo1.png    
                ├── runlogo1.png
                └── fig1.png
            ├── [data]/                        tables 
                ├── v101-2.csv                     
                └── steel-vals.csv                                                 
            ├── [scripts]/                     scripts and shell commands
                ├── opensees.sh                     
                └── calc1.py                              
        ├── [bk2-]folder name             rivtbook chapter folder
                ...        
        └── [bk3-]folder name             rivtbook chapter folder
                ...


**[3]** rivtbook Application
----------------------------------------------------------
 
*rivtbooks* are organized to simplify selection of *rivt files* for 
inclusion in *rivt docs* and *reports*. Typical use involves the following
steps. To insert a *rivtbook subdivision* into a *rivt doc or report*: 

#. Copy the *rivt file* within a *rivtbook subdivision folder* to the 
   *rivt-report* folder of the target report or doc and edit the 
   *rivt doc number*.

#. Within the same *subdivision folder* copy all resource files and folders and 
   paste (merge) them into the *rvsrc* folder of the target report or doc. A 
   single copy and paste command will merge all of the required files.

#. The *subdivision* from the book is now inserted as a *subdivision* in the 
   report, where further edits can be made.
   