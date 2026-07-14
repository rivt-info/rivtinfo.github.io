**C.3 | rivt Report**
============================================

.. _rivt-folders:

**[1]**  Report Folder
-------------------------------------------------------

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



.. _report-folders:

**rivt Report Top Level Folders** 

.. code-block:: bash

    [rivt-]Report-Label/             report folder
        ├── .help/                      help files
        ├── .vscode/                    optional VSCode settings   
        ├── README.txt                  rivt-generated report                  
        ├── [_rivt-public]/                 public subset of rivt files
            ├── rv_stor/                    
            ├── rvsrc/                        
            ├── README.txt                              
            ├── rv-101-filename1.py         
            ├── rv-102-filename2.py                
            ├── rv-201-filename3.py                          
             ...
        └── [rivt-report]/              report folder              
            ├── [_published]/               published docs and reports
            ├── [_rstdocs]/                 restructured text files               
            ├── [rv_stor]/                  rivt generated source files
            ├── [rvsrc]/                    author provided source files
            ├── [rv101-]filename1.py        rivt file
            ├── [rv102-]filename2.py        rivt file       
            ├── [rv201-]filename3.py        rivt file          
             ...    

**rivt Report Expanded Folders**

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
                ├── [data]/                         tables    
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