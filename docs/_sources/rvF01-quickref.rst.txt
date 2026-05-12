
**F.1 Quick Ref**
================== 

.. _API Summary:

**[1]** API
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

**API functions**

=============== =============== ===========================================
Function           Name             Purpose
=============== =============== ===========================================
**rv.R** (rS)         Run            Run scripts and markup
**rv.I** (rS)         Insert         Insert static sources 
**rv.V** (rS)         Values         Calculate values
**rv.T** (rS)         Tools          Execute shell commands and programs
**rv.D** (rS)         Doc            Publish docs 
**rv.S** (rS)         Skip           Skip section (comments and debugging)
**rv.X** (rS)         Exit           Exit rivt (debugging)
=============== =============== ===========================================

where **rS** is a *rivt string*. The first line of a *rivt string* (rS)
is the :term:`header substring`.

**Header substrings**

.. code-block:: python

    rv.I("""A New Section | private, doc, section

        Content text
        ...
        
        """)

Default settings in the *header substring* do not need to be specified. The
default setting for each API is listed first (in bold) in the table below.
The default privacy settings for all sections in a rivt file may be reversed by
including the *setpublic setting* set to true immediately following the 
*rivlib import statement*. Individual sections may still be set as private 
in the *header substring*.

.. code:: python

    import rivtlib.rvapi as rv

    # rv setpublic = true
 
**Header substring defaults**

========== ===================== ===================== =====================
API          private; public         doc; stored           section; merge         
========== ===================== ===================== ===================== 
rv.R        **private**; public     **stored**; doc      **merge**; section
rv.I        **private**; public     **doc**; stored      **section**; merge   
rv.V        **private**; public     **doc**; stored      **section**; merge    
rv.T        **private**; public     **stored**; doc      **merge**; section
rv.S        **private**; public     **stored**           **merge**
rv.D        **public**             **stored**            **merge**
rv.X         -                      -                    -
========== ===================== ===================== =====================

.. _Line Tags:

**[2]** Line Tags
-------------------------------------

  
**Format a line of text**
   
========== ==================================================== ================================
API Scope             Line Tag                                      Description 
========== ==================================================== ================================
rv.I                   text **_[#]** text                         :ref:`Endnote number`  
rv.I                   text **_[D] label, filename]** text        :ref:`Download link`
rv.I                   text **_[G] glossary term]** text          :ref:`Term link`
rv.I                   text **_[S] label, section]** text         :ref:`Section link`
rv.I                   text **_[U] label, url]** text             :ref:`URL link`   
rv.I                  **title _[T]**                              :ref:`Number table`
rv.I,V              **caption _[F]**                              :ref:`Number figure`
rv.I,V                 text **_[C]**                              :ref:`Bold center text` 
rv.I,V            **text math _[M]** description                  :ref:`Text math` 
rv.I,V           **LaTeX math _[L]** description                  :ref:`LaTeX math` 
rv.I,V                 text **_[V] var_name]** text               :ref:`Variable value`
all                     **##** text                               nonprinting comment
========== ==================================================== ================================

.. _Block Tags:

**[3]** Block Tags
-------------------------------------

**Format or run blocks of text or code**

========== ========================================= ===============================
API Scope         Block Tag                                Description 
========== ========================================= ===============================
rv.R        **_[[MARKUP]]** type                      :ref:`Markup file`
rv.R        **_[[PYTHON]]** namespace                 :ref:`Python block`
rv.I        **_[[BOX]]** label                        :ref:`Box block`
rv.I        **_[[TOPIC]]** topic                      :ref:`Topic block`
rv.I        **_[[TABLE]]** label                      :ref:`Table block`
rv.T        **_[[SHELL]]** os, wait;nowait            :ref:`Shell script`
rv.D        **_[[METADATA]]** label                   :ref:`Meta block` 
all         **_[[END]]**                              :ref:`End block`
========== ========================================= ===============================

.. _Commmands:

**[4]** Commands
-------------------------------------

**Read, write and format files**

========== ================================================================ ========================
API Scope           Command                                                  Description
========== ================================================================ ========================
rv.R        | **MARKUP** | rel path | type                                  :ref:`Markup file`
rv.I, V     | **TABLE** | rel path | title,width,rows,                      :ref:`Table file`     
rv.I, V     | **IMAGE** | rel path | caption, scale, num;non                :ref:`Image file`
rv.I, V     | **IMAGE2** | rel pth1, rel pth2 | cap1,cap2,sc1,sc2,num,num   :ref:`Adjacent images`
rv.V        | **VALTABLE** | rel path | title, rows                         :ref:`Values file`     
rv.V        | **PYTHON** | rel path | description                           :ref:`Python file`
rv.V        a **==:** 1*IN  | unit1, unit2, decimal | description           :ref:`Define value`
rv.V        c **<=:** expression | unit1, unit2, decimal | description      :ref:`Assign value`
rv.V        c **:=:** function(x,y) | unit1, unit2, decimal | description   :ref:`Function value`
rv.V        a **<** c | unit, decimal, text1, text2 | description           :ref:`Compare value`
rv.T        | **SHELL** | rel path | os, wait;nowait                        :ref:`Shell file`
rv.D        | **ATTACHPDF** | rel path | place, title                       :ref:`Attach PDF`   
rv.D        | **PUBLISH** | doc title | type                                :ref:`Publish doc` 
========== ================================================================ ========================


**Relative file paths for commands**

See :ref:`here <report-folders>` for the full folder structure. File paths are
relative to the *rivt-report* folder. Use *_stored/filename* to read values
or files defined and written by the *rivt file*.

================ ==========================
   Command          Standard Path
================ ==========================
\| ATTACHPDF |      **src/filename**   
\| IMAGE |          **src/filename**
\| IMAGE2 |         **src/filename**
\| MARKUP |         **src/filename**
\| PYTHON |         **src/filename**
\| SHELL |          **src/filename**  
\| TABLE |          **src/filename**
\| VALTABLE |       **src/filename**  
\| PUBLISH |      docs written to _publish
================ ==========================


.. _Folders:

**[5]** Folders
-------------------------------------

.. code-block:: bash

    [rivt-]Report-Label/             rivt Folder                
        ├── .vscode/                      optional VSCode settings   
        ├── README.txt                    rivt-generated report                  
        ├── [_rivt-public]/               rivt-generated public files
            ├── src/                          source files            
            ├── rv-101-filename1.py           public rivt file
            ├── rv-102-filename2.py           public rivt file       
            ├── rv-201-filename3.py           public rivt file          
            ├── rv-202-filename4.py           public rivt file
            ...
        └── [rivt-report]/                 report folder               
                ├── [rv101-]filename1.py        rivt file
                ├── [rv102-]filename2.py        rivt file       
                ├── [rv201-]filename3.py        rivt file          
                ├── [rv202-]filename4.py        rivt file
                ...
                ├── [src]                  author source files        
                    ├── data/                        user folder (tables, etc.)    
                        ├── opensees1.txt   
                        └── conc-vals.csv  
                    ├── image/                                                 
                        ├── fig1.png
                        └── fig2.jpg   
                    ├── tool/                        OS shellcommands
                        ├── run1_win.cmd                    
                        └── run1_linux.sh                   
                    ├── run/                         markup and functions
                        ├── coverpage.rst                   
                        ├── logoname.png                    
                        ├── plot.py                         
                        └── loads.py                        
                    ├── steel-vals.csv     
                    └── plastic-vals.csv               
                ├── [_published]/               published docs and reports
                    ├── [docs]/                      html docs
                        ├── _images/                
                        ├── _sources/              
                        ├── _static/            
                        ├── site folders/
                        ├── process folders/                                         
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
                ├── [_rstdocs_]/                         restructured text files
                    ├── _downloads/                    
                    ├── _static/                       
                    ├── _locale/                       
                    ├── _templates/                    
                    ├── rv101-filename1.rst            
                    ├── rv102-filename2.rst                          
                    ├── rv201-filename3.rst          
                    ├── rv202-filename4.rst
                    ...
                ├── [_stored]/                      rivt generated files
                    ├── [logs]/                         log files
                        ├── rv101-log.txt
                        └── rv102-log.txt
                    ├── [sect]/                          sections (not printed)                    
                        ├── rv202-5d.txt  
                        ├── rv103-4t.txt                         
                        └── rv301-2r.txt               
                    ├── [temp]/                          temp files
                        └── rv101-label3.tex
                    ├── output.dat
                    ├── v101-2.csv
                    └── v102-3.csv      


.. _Project requirements:

**[6]** Python Requirements
-------------------------------------

.. raw:: html

    <hr>

The minimum Python version is *3.14*. *rivt* project packages include the
following categories:

- formatting
- numerical analysis
- symbolic processing
- visualization
- IDE

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

.. _VSCode settings:

**[7]** VSCode Settings
------------------------------------

.. raw:: html

    <hr>

Workspace extension and other settings are stored in the *.vscode* folder and
should be included as part of a *rivt folder*. Settings that affect the
*rivt* editing and execution environment incldue:

- rivt.code-snippets
- settings.json (extension settings)
- tasks.json
- launch.json

Global settings can be exported and imported using VSCode Profiles. VSCode
*rivt* extensions and settings may be installed from this link.

============================================== ===============================
Extension                                        description
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

**Snippets and extensions**

================= ==============================================================
Keystrokes                   Description
================= ==============================================================
rvr                 API Run 
rvi                 API Insert    
rvv                 API Values 
rvt                 API Tools 
rvd                 API Docs
alt+ctrl+c          insert cell marker with label above API function
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
================= ==============================================================

**Modified Keyboard Shortcuts**

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


.. toctree::
    :maxdepth: 1
    :hidden:

    rvF02-terms.rst




