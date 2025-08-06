**2. Install**
===============

* `VSCode and extensions <https://code.visualstudio.com>`_  for editing and processing.

* `Python and libraries <https://www.python.org/>`_  for analysis and formatting, including 
  `rivtlib <https://rivtlib.net>`_  - the Python library that provides a **rivt** API and markup processing.


**rivtzip** is a collection of three zip files that installs the rivt framework
in a portable folder or usb drive. It is available for every OS platform. rivt
also runs in the cloud and on mobile devices using GitHub CodeSpaces or other
cloud service providers.


**Examples**
=============

**Ex. 1**
-----------

API functions start in column one. rivt-strings are indented four spaces (for
legibility and code folding).A rivt doc is assembled by each function in order
of the input order. Each function also, optionally, defines a doc section.

::

    import rivtlib.rivtapi as rv
    
    rv.R("""Run function | pass; redact | nocolor; color code
    
        The Run function processes shell commands.
    
        Each API function defines a new document section. The first line is a
        heading line which includes the section heading, a parameter for redacting
        sections in a mirror file intended for public sharing, and a parameter for
        the background color for the section. If the section heading is preceded by
        two dashes (--) the section is continued from the prior section without
        introducting a new number.
        
        File formatting follows pep8 and ruff. API functions start in column one.
        All other lines are indented 4 spaces to facilitate section folding,
        bookmarks and legibility.
    
        """)
    
    rv.I("""Insert function | pass; redact | nocolor 
    
        The Insert function formats static objects including images, tables,
        equations and text.
    
        ||text | data01/describe.txt | rivt     
    
        The table command inserts and formats tabular data from csv or xls files.
        The _[t] tag formats and autonumbers table titles.
    
        A table title  _[t]
        || table | data/file.csv | 60,r
    
        The image command inserts and formats image data from png or jpg files. The
        _[f] tag formats and autonumbers figures.
            
        A figure caption _[f]
        || image | data/f1.png | 50
    
        Two images may be placed side by side as follows:
    
        The first figure caption  _[f]
        The second figure caption  _[f]
        || image | private/image/f2.png, private/image/f3.png | 45,35
        
        The tags _[x] and _[s] format LaTeX and sympy equations:
    
        \gamma = \frac{5}{x+y} + 3  _[x] 
    
        x = 32 + (y/2)  _[s]
    
        """)
    
    rv.V("""Values function |  pass; redact | nocolor 
    
        The Values fucntion evaluates variables and equations. 
        
        The equal tag declares a value. A sequence of declared values terminated
        with a blank line is formatted as a table.
        
        Example of assignment list _[t]
        f1 = 10.1 * LBF |LBF, N| a force value
        d1 = 12.1 * IN  |IN, CM| a length value
    
        An equation tag provides an equation description and number. A colon-equal
        tag assigns a value and specifies the result units and the output decimal
        places printed in the result and equation.
    
        Example equation - Area of circle  _[e]
        a1 := 3.14(d1/2)^2 | IN^2, CM^2 | 1,2
    
        || declare | data01/values02.csv
        
        The declare command imports values from the csv file written by rivt when
        processing values in other documents. 
    
        """)
    
    rv.T("""Tools function | pass; redact | nocolor
    
        The Tools function processes Python code.
            
        """)
    
    
    rv.X("""Any text 
    
        Changing a function to X skips evaluation of that function. Its purposes
        include review commenting and debugging.
    
        """) 
    
    rv.W("""Write function | pass; redact | nocolor
    
        The Write function generates docs and reports.
    
        | docs |
     
        | report |
    
        """)

**Ex. 2**
------------

API functions start in column one. rivt-strings are indented four spaces (for
legibility and code folding).A rivt doc is assembled by each function in order
of the input order. Each function also, optionally, defines a doc section.

::

    import rivtlib.rivtapi as rv
    
    rv.R("""Run function | pass; redact | nocolor; color code
    
        The Run function processes shell commands.
    
        Each API function defines a new document section. The first line is a
        heading line which includes the section heading, a parameter for redacting
        sections in a mirror file intended for public sharing, and a parameter for
        the background color for the section. If the section heading is preceded by
        two dashes (--) the section is continued from the prior section without
        introducting a new number.
        
        File formatting follows pep8 and ruff. API functions start in column one.
        All other lines are indented 4 spaces to facilitate section folding,
        bookmarks and legibility.
    
        """)
    
    rv.I("""Insert function | pass; redact | nocolor 
    
        The Insert function formats static objects including images, tables,
        equations and text.
    
        ||text | data01/describe.txt | rivt     
    
        The table command inserts and formats tabular data from csv or xls files.
        The _[t] tag formats and autonumbers table titles.
    
        A table title  _[t]
        || table | data/file.csv | 60,r
    
        The image command inserts and formats image data from png or jpg files. The
        _[f] tag formats and autonumbers figures.
            
        A figure caption _[f]
        || image | data/f1.png | 50
    
        Two images may be placed side by side as follows:
    
        The first figure caption  _[f]
        The second figure caption  _[f]
        || image | private/image/f2.png, private/image/f3.png | 45,35
        
        The tags _[x] and _[s] format LaTeX and sympy equations:
    
        \gamma = \frac{5}{x+y} + 3  _[x] 
    
        x = 32 + (y/2)  _[s]
    
        """)
    
    rv.V("""Values function |  pass; redact | nocolor 
    
        The Values fucntion evaluates variables and equations. 
        
        The equal tag declares a value. A sequence of declared values terminated
        with a blank line is formatted as a table.
        
        Example of assignment list _[t]
        f1 = 10.1 * LBF |LBF, N| a force value
        d1 = 12.1 * IN  |IN, CM| a length value
    
        An equation tag provides an equation description and number. A colon-equal
        tag assigns a value and specifies the result units and the output decimal
        places printed in the result and equation.
    
        Example equation - Area of circle  _[e]
        a1 := 3.14(d1/2)^2 | IN^2, CM^2 | 1,2
    
        || declare | data01/values02.csv
        
        The declare command imports values from the csv file written by rivt when
        processing values in other documents. 
    
        """)
    
    rv.T("""Tools function | pass; redact | nocolor
    
        The Tools function processes Python code.
            
        """)
    
    
    rv.X("""Any text 
    
        Changing a function to X skips evaluation of that function. Its purposes
        include review commenting and debugging.
    
        """) 
    
    rv.W("""Write function | pass; redact | nocolor
    
        The Write function generates docs and reports.
    
        | docs |
     
        | report |
    
        """)



**VSCode Profiles**
--------------------

The rivt VSCode profile includes shortcuts for common editing functions and
snippets for API functions and commands.


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

---------------------------------------------------------------------------

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

------------------------------------------------------------------------

============== ===========================================================
Keystroke                   Description
-------------- -----------------------------------------------------------
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

-----------------------------------------------------------------------------

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



============================================== ===============================
Extensions                                       description
============================================== ===============================
BUTTONS                                             .
tombonnike.vscode-status-bar-format-toggle          format button
gsppvo.vscode-commandbar                            command buttons
AdamAnand.adamstool                                 command buttons
nanlei.save-all                                     save all button
Ho-Wan.setting-toggle                               toggle settings
yasukotelin.toggle-panel                            toggle panel
fabiospampinato.vscode-commands                     user command buttons
jerrygoyal.shortcut-menu-bar                        menu bar
EDITING                                             .
henryclayton.context-menu-toggle-comments           toggle comments
TroelsDamgaard.reflow-paragraph                     wrap paragraph
streetsidesoftware.code-spell-checker               spell check
jmviz.quote-list                                    quote elements in a list
njpwerner.autodocstring                             insert doc string
oijaz.unicode-latex                                 unicode symbols from latex
jsynowiec.vscode-insertdatestring                   insert date string
janisdd.vscode-edit-csv                             csv editor
VIEWS                                               .
GrapeCity.gc-excelviewer                            excel viewer
SimonSiefke.svg-preview                             svg viewer
tomoki1207.pdf                                      pdf viewer
RandomFractalsInc.vscode-data-preview               data viewing tools
Fr43nk.seito-openfile                               open file from path
vikyd.vscode-fold-level                             line folding tool
file-icons.file-icons                               icon library
tintinweb.vscode-inline-bookmarks                   inline bookmarks
MANAGEMENT                                          .
alefragnani.project-manager                         folder, project management
Anjali.clipboard-history                            clipboard history
dionmunk.vscode-notes                               notepad
hbenl.vscode-test-explorer                          test explorer
mightycoco.fsdeploy                                 save file to second location
lyzerk.linecounter                                  count lines in files
sandcastle.vscode-open                              open files in default app
zjffun.snippetsmanager                              snippet manager
spmeesseman.vscode-taskexplorer                     task explorer
GITHUB                                              .
GitHub.codespaces                                   run files in codespaces
GitHub.remotehub                                    run remote files
ettoreciprian.vscode-websearch                      search github within VSCode
donjayamanne.githistory                             git history
MichaelCurrin.auto-commit-msg                       git auto commit message     
github.vscode-github-actions                        github actions
GitHub.vscode-pull-request-github                   github pull request
k9982874.github-gist-explorer                       gist explorer
vsls-contrib.gistfs                                 gist tools
PYTHON                                              .
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
LANGUAGES                                           .
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

