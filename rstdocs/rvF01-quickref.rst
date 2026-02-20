
**F.1 Quick Ref**
================== 


**[1t]** API functions
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

=============== =============== ===========================================
API Function         Name             Purpose
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
rv.S        **private**;public     **stored**           **merge**
rv.D        **public**             **stored**           **merge**
rv.X         -                      -                   -
========== ===================== ===================== =====================

**[2t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>
  
========== ==================================================== ===============================
API Scope             Line Tag                                      Description 
========== ==================================================== ===============================
rv.I                          text **_[C]**                      :ref:`Center text` 
rv.I                          text **_[R]**                      :ref:`Right justify text`
rv.I                     **text math _[M]**                      :ref:`Text math` 
rv.I                    **LaTeX math _[L]**                      :ref:`LaTeX math` 
rv.I                          text **_[#]** text                 :ref:`Endnote number`  
rv.I                          text **_[G] glossary term**        :ref:`Term reference`
rv.I                          text **_[S] text, section label**  :ref:`Section link`
rv.I                          text **_[D] text,rivt_file**       :ref:`Doc link`
rv.I                          text **_[U] text, url**            :ref:`URL link`   
rv.V, I                       text **_[V] var_name** text        :ref:`Variable value`
rv.V, I        assign var or **label _[E]**                      :ref:`Equation number`
rv.V, I                      **title _[T]**                      :ref:`Table number`
rv.V, I                    **caption _[F]**                      :ref:`Figure number`
rv.V, I                       text **_[P]**                      :ref:`New Page`
========== ==================================================== ===============================


**[3t]** Block Tag Summary
-------------------------------------

.. raw:: html

    <hr>

========== ========================================= ===============================
API Scope         Block Tag                                Description 
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
rv.V, I     **| IMAGE |** rel path | caption, scale, figure                 :ref:`Image file`
rv.V, I     **| IMAGE2 |** rel path1, rel path2 | c1, c2, s1, s2, f1, f2    :ref:`Adjacent images`
rv.V        **| VALTABLE |** rel path | title, rows, number                 :ref:`Values file`     
rv.V        a **:=:** 1*IN  | unit1, unit2, decimal | label                 :ref:`Define variable`
rv.V        c **<=:** expression | unit1, unit2, decimal | label            :ref:`Assign value`
rv.V        a **<** c  | decimal | text1, text2, color1, color2             :ref:`Compare values`
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
            ├── [Data]/                             
                ├── data1.csv
                ├── steel-vals.csv        
                └── conc-vals.csv  
            ├── [Shell]/                           
                ├── shell1.cmd   
                └── shell1.csv  
            ├── [Image]/                                                   
                ├── fig1.png
                └── fig2.jpg
            ├── [Scripts]/                         
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
            └── [Data]/
                ├── table1.csv                      stored script output                                  
                ├── image1.png                      stored value files
                ├── v101-2.csv
                └── v102-3.csv             
        └── README.txt                         || searchable text report 


.. _package requirements:

**[6t]** package requirements
-------------------------------------

.. raw:: html

    <hr>

The minimum Python version is *3.13*. A *rivt* installation includes Python
packages for:

- document formatting
- numerical analysis
- symbolic processing
- visualization

=============================================== ================================
      Dependency                                      description
=============================================== ================================
  "pyzo>=4.20.0"                                   lightweight IDE
  "pyside6>=6.10.1"                                QT bindings
  "fastcore>=1.8.16"                               code simplification                 
  "tabulate>=0.9.0"                                format tables                 
  "pillow>=11.2.1"                                 image processing
  "matplotlib>=3.10.1"                             data visualization
  "sympy>=1.13.3"                                  symbolic analysis
  "numpy>=2.2.5"                                   numerical analysis
  "scipy>=1.16.3"                                  numerical analysis
  "pandas>=2.2.3"                                  data analysis    
  "docutils>=0.21.2"                               reStructuredText processing  
  "ipython>=8.16.2"                                interactive Python shell
  "ipykernel>=6.28.1"                              Jupyter kernel for Python
  "reportlab>=4.4.0"                               PDF generation without LaTeX
  "rst2pdf>=0.103.1"                               PDF generation without LaTeX
  "pypdf>=1.0.3"                                   PDF manipulation
  "Sphinx>=8.2.3"                                  HTML generation  
  "pydata-sphinx-theme>=0.16.1"                    HTML generation  
  "sphinx-copybutton>=0.5.2"                       HTML generation  
  "sphinx_design>=0.6.1"                           HTML generation  
  "sphinx-favicon>=1.0.1"                          HTML generation  
  "sphinx-togglebutton>=0.3.2"                     HTML generation  
  "sphinxcontrib-applehelp>=2.0.0"                 HTML generation 
  "sphinxcontrib-devhelp>=2.0.0"                   HTML generation
  "sphinxcontrib-email>=0.3.6"                     HTML generation
  "sphinxcontrib-htmlhelp>=2.1.0"                  HTML generation
  "sphinxcontrib-jquery>=4.1"                      HTML generation
  "sphinxcontrib-jsmath>=1.0.1"                    HTML generation
  "sphinxcontrib-qthelp>=2.0.0"                    HTML generation
  "sphinxcontrib-serializinghtml>=2.0.0"           HTML generation
=============================================== ================================        



**[7t]** VSCode settings for rivt
------------------------------------

.. raw:: html

    <hr>

Workspace extension and other settings are stored in the *.vscode* folder and
can be included and moved as part of a *rivt report*. Settings that affect the
*rivt* environment incldue:

    - rivt.code-snippets
    - settings.json (extension settings)
    - tasks.json
    - launch.json

Global settings can be exported and imported using VSCode Profiles. VSCode
*rivt* extensions and settings may be installed from this link.

============================================== ===============================
Extensions                                       description
============================================== ===============================
**BUTTONS**                                         ---
tombonnike.vscode-status-bar-format-toggle          format button
gsppvo.vscode-commandbar                            command buttons
AdamAnand.adamstool                                 command buttons
nanlei.save-all                                     save all button
Ho-Wan.setting-toggle                               toggle settings
yasukotelin.toggle-panel                            toggle panel
fabiospampinato.vscode-commands                     user command buttons
jerrygoyal.shortcut-menu-bar                        menu bar
**EDITING**                                         ---
henryclayton.context-menu-toggle-comments           toggle comments
TroelsDamgaard.reflow-paragraph                     wrap paragraph
streetsidesoftware.code-spell-checker               spell check
jmviz.quote-list                                    quote elements in a list
njpwerner.autodocstring                             insert doc string
oijaz.unicode-latex                                 unicode symbols from latex
jsynowiec.vscode-insertdatestring                   insert date string
janisdd.vscode-edit-csv                             csv editor
**VIEWS**                                           ---
GrapeCity.gc-excelviewer                            excel viewer
SimonSiefke.svg-preview                             svg viewer
tomoki1207.pdf                                      pdf viewer
RandomFractalsInc.vscode-data-preview               data viewing tools
Fr43nk.seito-openfile                               open file from path
vikyd.vscode-fold-level                             line folding tool
file-icons.file-icons                               icon library
tintinweb.vscode-inline-bookmarks                   inline bookmarks
**MANAGEMENT**                                      ---
alefragnani.project-manager                         folder, project management
Anjali.clipboard-history                            clipboard history
dionmunk.vscode-notes                               notepad
hbenl.vscode-test-explorer                          test explorer
mightycoco.fsdeploy                                 save file to second location
lyzerk.linecounter                                  count lines in files
sandcastle.vscode-open                              open files in default app
zjffun.snippetsmanager                              snippet manager
spmeesseman.vscode-taskexplorer                     task explorer
**GITHUB**                                          ---
GitHub.codespaces                                   run files in codespaces
GitHub.remotehub                                    run remote files
ettoreciprian.vscode-websearch                      search github within VSCode
donjayamanne.githistory                             git history
MichaelCurrin.auto-commit-msg                       git auto commit message     
github.vscode-github-actions                        github actions
GitHub.vscode-pull-request-github                   github pull request
k9982874.github-gist-explorer                       gist explorer
vsls-contrib.gistfs                                 gist tools
**PYTHON**                                          ---
ms-python.autopep8                                  python pep8 formatting
ms-python.isort                                     python sort imports
donjayamanne.python-environment-manager             python library list
ms-python.python                                    python tools
ms-python.vscode-pylance                            python language server
ms-toolsai.jupyter                                  jupyter tools
ms-toolsai.jupyter-keymap                           jupyter tools
ms-toolsai.jupyter-renderers                        jupyter tools
ms-toolsai.vscode-jupyter-cell-tags                 jupyter tools
ms-toolsai.vscode-jupyter-slideshow                 jupyter tools
**LANGUAGES**                                       ---
qwtel.sqlite-viewer                                 sqlite tools
RDebugger.r-debugger                                R tools
REditorSupport.r                                    R tools
ms-vscode-remote.remote-wsl                         windows linux tools
James-Yu.latex-workshop                             latex tools
lextudio.restructuredtext                           restructured text tools
trond-snekvik.simple-rst                            restructured syntax
yzane.markdown-pdf                                  markdown to pdf
yzhang.markdown-all-in-one                          markdown tools
============================================== ===============================


============== ==============================================================
Snippets/Keys            description
============== ==============================================================
run                 API Run function
ins                 API Insert function   
val                 API Values function
too                 API Tools function
wri                 API Write function
alt+q               rewrap paragraph with hard line feeds (80 default)
alt+p               open file under cursor
alt+.               select correct spelling under cursor
alt+8               insert date
alt+9               insert time
ctl+1               focus on first editor
ctl+2               focus on next editor
ctl+3               focus on previous editor
ctl+8               focus on explorer pane
ctl+9               focus on github pane    
ctl+alt+x           reload window
ctl+alt+[           reload window
ctl+alt+]           unfold all code
ctl+alt+u           unfold all code
ctl+alt+f           fold code level 2 (rivt sections visible)
ctl+alt+a           fold code - all levels
ctl+alt+t           toggle local fold
ctl+alt+e           toggle explorer sort order
ctl+alt+s           toggle spell check
ctl+alt+g           next editor group
ctl+shift+u         open URL under cursor in browser
ctl+shift+s         open GitHub README search for rivt
ctl+shift+a         commit all 
ctl+shift+z         commit the current editor
ctl+shift+x         post to remote   
============== ==============================================================


============== ===========================================================
Keystroke                   Description
============== ===========================================================
alt+q                rewrap paragraph with hard line feeds (80 default)
alt+p                open file under cursor
alt+.                select correct spelling under cursor
alt+8                insert date
alt+9                insert time

ctl+1                focus on first editor
ctl+2                focus on next editor
ctl+3                focus on previous editor
ctl+8                focus on explorer pane
ctl+9                focus on github pane    

ctl+alt+x            reload window
ctl+alt+u            unfold all code
ctl+alt+f            fold code level 2 (rivt sections visible)
ctl+alt+a            fold code - all levels
ctl+alt+t            toggle local fold
ctl+alt+e            toggle explorer sort order
ctl+alt+s            toggle spell check
ctl+alt+g            next editor group

ctl+shift+u          open URL under cursor in browser
ctl+shift+s          open GitHub rivt README search
ctl+shift+a          commit all 
ctl+shift+z          commit current editor
ctl+shift+x          post to remote   
============== ===========================================================









