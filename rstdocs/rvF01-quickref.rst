
**F.1 Quick Ref**
================== 


**[1t]** API functions
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

=============== =============== ===========================================
API Functions        Name             Purpose
=============== =============== ===========================================
**rv.R** (rS)         Run            Run shell commands
**rv.I** (rS)         Insert         Insert static sources 
**rv.V** (rS)         Values         Calculate values
**rv.T** (rS)         Tools          Python and markup scripts
**rv.S** (rS)         Skip           Skip section (comments and debugging)
**rv.D** (rS)         Doc            Publish docs 
**rv.X** (rS)         Exit           Exit rivt (debugging)
=============== =============== ===========================================

The first line of a *rivt string* (rS) is a *header substring*.

.. code-block:: python

    rv.I("""A New Section | private, doc, section

        Content text
        ...
        
        """)

Default settings in the *header substring* do not need to be specified. The
default setting for each API is listed first (**in bold**) in the table below.
 
========== ===================== ===================== =====================
API          private;public         doc;stored           section;merge         
========== ===================== ===================== ===================== 
rv.R        **private**;public     **stored**;doc       **merge**;section
rv.I        **private**;public     **doc**;stored       **section**;merge   
rv.V        **private**;public     **doc**;stored       **section**;merge    
rv.T        **private**;public     **stored**;doc       **merge**;section
rv.S        **private**            **stored**           **merge**
rv.D        **public**             **stored**           **merge**
rv.X         -                      -                   -
========== ===================== ===================== =====================

**[2t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>
  
========== ================================================= ===============================
API Scope             Line Tags                                     Description 
========== ================================================= ===============================
rv.I                          text **_[C]**                     :ref:`Center text` 
rv.I                          text **_[R]**                     :ref:`Right justify text`
rv.I                    text  math **_[M]**                     :ref:`Text math` 
rv.I                    LaTeX math **_[L]**                     :ref:`LaTeX math` 
rv.I                   label, url  **_[U]**                     :ref:`URL link`   
rv.I                          text **_[G]** glossary term       :ref:`Term reference`
rv.I                          text **_[S]** section label       :ref:`Section link`
rv.I                          text **_[#]** more text           :ref:`Endnote number`  
rv.I                text rivt_file **_[D]** more text           :ref:`Doc link`
rv.V, I              text var_name **_[V]** more text           :ref:`Variable value`
rv.V, I            assign or label **_[E]**                     :ref:`Equation label`
rv.V, I          valtable or title **_[T]**                     :ref:`Table title`
========== ================================================= ===============================

**[3t]** Block Tag Summary
-------------------------------------

.. raw:: html

    <hr>

========== ========================================= ===============================
API Scope         Block Tags                               Description 
========== ========================================= ===============================
rv.R        **_[[SHELL]]** process parameters         :ref:`Shell script`
rv.I        **_[[INDENT]]** spaces (4 default)        :ref:`Indent text block`
rv.I        **_[[ITALIC]]** spaces (4 default)        :ref:`Indent italic block`
rv.I        **_[[ENDNOTES]]** optional label          :ref:`Endnotes block`
rv.I        **_[[TEXT]]** optional language           :ref:`Text block`
rv.I        **_[[TOPIC]]** topic                      :ref:`Topic block`
rv.I        **_[[BOX]]** label                        :ref:`Box block`
rv.V, T     **_[[PYTHON]]** namespace                 :ref:`Python block`
rv.D        **_[[METADATA]]** label                   :ref:`Meta block`
rv.D        **_[[LAYOUT]]** label                     :ref:`Layout block` 
all         **_[[END]]**                              :ref:`End block`
all         **_[[NEW PAGE]]**                         :ref:`Start new page`
========== ========================================= ===============================

**[4t]** Command Summary
-------------------------------------

.. raw:: html

    <hr>

See :ref:`here <report folders>` for the folder structure. If files
are in the default path only the file name needs to be provided.

**Read, write and format files**

========== ============================================================== ========================
API Scope           | Command | path | parameters                          Description
========== ============================================================== ========================
rv.R        **| SHELL |** rel path | os, wait                               :ref:`Shell file`
rv.I        **| TEXT |** rel path |  language                               :ref:`Text file`
rv.V, I     **| TABLE |** rel path | title, width, rows, align, head        :ref:`Table file`     
rv.V, I     **| IMAGE |** rel path | caption, scale, number                 :ref:`Image file`
rv.V, I     **| IMAGE2 |** rel path1, rel path2 | caption, scale number     :ref:`Adjacent images`
rv.V        **| VALTABLE |** rel path | title, rows, number                 :ref:`Values file`     
rv.V        a **=:** 1*IN  | unit1, unit2, decimal | label                  :ref:`Define variable`
rv.V        c **<=:** expression | unit1, unit2, decimal | label            :ref:`Assign value`
rv.V        a **<** c  | decimal | text, align, color                       :ref:`Compare values`
rv.T, V     **| PYTHON |** rel path | namespace                             :ref:`Python file`
rv.T        **| MARKUP |** rel path | type                                  :ref:`Markup file`
rv.D        **| ATTACHPDF |** rel path | place, title                       :ref:`Attach PDF`   
rv.D        **| PUBLISH |** rel path (ini) | type                           :ref:`Publish doc` 
========== ============================================================== ========================

**Default command paths**

================ =========================
   Command         Default Path
================ =========================
\| SHELL |          **/Src/Shell/**
\| TEXT |           **/Src/Data/**
\| TABLE |          **/Src/Data/**
\| IMAGE |          **/Src/Image/**
\| IMAGE2 |         **/Src/Image/**
\| VALTABLE |       **/Src/Data/**   [1]    
\| PYTHON |         **/Src/Scripts/**
\| MARKUP |         **/Src/Scripts/**
\| ATTACHPDF |      **/Src/Gendocs/**  
\| PUBLISH |        **/Src/Gendocs/**
================ =========================

[1]  use /stored/data/filename to read values previously defined and stored


**[5t]** Folders
-------------------------------------

.. raw:: html

    <hr>


.. code-block:: bash

    [rivt]-Report-Label/                     Report Folder Name                
        ├── [rv101-]filename1.py               | rivt input files
        ├── [rv102-]filename2.py               
        ├── [rv201-]filename3.py               
        ├── [rv202-]filename4.py                 
        ├── [Public]/                          || public rivt files                      
            ├── rv-101-filename1.py              
            ├── rv-102-filename1.py              
            ├── rv-201-filename3.py  
            └── rv-202-filename4.py    
        ├── [Publish]/                         || reports and docs
            ├── [Html]/                              HTML site  
                ├── [docs]/                           
                    ├── _images/                
                    ├── _sources/              
                    ├── _static/                  
                    ├── rv101-filename1.html         
                    ├── rv102-filename2.html                              
                    ├── rv201-filename3.html                        
                    ├── rv201-filename4.html   
                    └── index.html                   HTML site entry point          
                ├── rv101-filename1.rst              intermediate rst files 
                ├── rv102-filename2.rst  
                ├── rv201-filename3.rst  
                └── rv202-filename4.rst  
            ├── [Rstpdf]/                               PDF from rst2pdf 
                ├── [src]/                           intermediate rst files  
                    ├── rv101-filename1.rst          
                    ├── rv102-filename2.rst                           
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst              
                ├── rv101-filename1.pdf              PDF docs from rst2pdf 
                ├── rv102-filename2.pdf                          
                ├── rv201-filename3.pdf                        
                ├── rv202-filename4.pdf         
                └── Report-Label.pdf                 PDF report from rst2pdf 
            ├── [Texpdf]/                            PDF from LaTeX  
                ├── [src]/                           intermediate rst files   
                    ├── rv101-filename1.rst         
                    ├── rv102-filename2.rst                        
                    ├── rv201-filename3.rst                        
                    └── rv202-filename4.rst               
                ├── rv101-filename1.pdf              PDF docs from LaTeX 
                ├── rv102-filename2.pdf                          
                ├── rv201-filename3.pdf                       
                ├── rv202-filename4.pdf
                └── Report-Label.pdf                 PDF report from LaTeX 
            ├── [Text]/                              text report
                ├── rv101-filename1.txt              text docs
                ├── rv102-filename2.txt       
                ├── rv201-filename3.txt       
                ├── rv202-filename4.txt       
                └── README.txt                       searchable text report                     
        ├── [Src]                              | source files from authors               
            ├── [Data]/                             author created subfolder
                ├── data1.csv
                ├── steel-vals.csv        
                └── conc-vals.csv  
            ├── [Shell]/                            author created subfolder
                ├── shell1.cmd   
                └── shell1.csv  
            ├── [Image]/                            author created subfolder                          
                ├── fig1.png
                └── fig2.jpg
            ├── [Scripts]/                          author created subfolder
                ├── table1.csv                                               
                ├── image1.png
                ├── plot.py                               
                ├── new-units.py                     define new units                          
                └── opensees1.txt    
            ├── [Gendoc]/
                ├── genhtml.cmd                      html generating script
                ├── genpdf.cmd                       pdf generating script
                ├── gentexpdf.cmd                    LaTeX generating script
                ├── rivt-report.py                   report generating script
                ├── Report-Cover.pdf
                ├── attach1.pdf
                └── [Style]/                         style files for docs 
                    ├── [Html]/                      html style files
                        ├── _locale/                 
                        ├── _static/                        
                        ├── _templates/                     
                        ├── conf.py                         
                        ├── genhtml.cmd                     
                        └── index.rst
                    ├── [Rstpdf]/                    rst2pdf style files
                        ├── fonts/              
                        └── style/                 
                    ├── [Texpdf]/                    pdftex style files            
                        └── rivt.sty              
                    ├── [Text]/                      text ini file
                        └── rv-text.ini
        ├── [Stored]/                          || stored files from rivt            
            ├── [Logs]/                              log files
                ├── rv101-api.txt   
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [Sect]/                              stored sections                    
                ├── rv202-5d.txt   
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [Temp]/                              temp files
                └── rv101-label3.tex
            └── [Data]/                              stored value files
                ├── v101-2.csv
                └── v102-3.csv             
        └── README.txt                         || searchable text report 
