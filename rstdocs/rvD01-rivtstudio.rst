**D.1 |** rivtStudio
========================


.. _rivtstudio:

**[2]** rivtstudio
------------------------------------------------------------------------------

*rivtstudio* includes *VSCode* `VSCode <https://code.visualstudio.com/>`
for editing and managing *rivt-docs*. *rivtstudio* is a local
:ref:`portable installation <rivtstudio>`.

rivt folders include markdown help files that can be accessed from VSCode and
other IDE's

======================= =====================================================
Purpose                    Link
======================= =====================================================
Editing                     `VSCode <https://code.visualstudio.com/>`_  
rivt Extensions             :ref:`rivtstudio-settings`
======================= =====================================================

---------------------------------


**[2]** VSCode and rivtstudiospaces
-----------------------------------------------------------------------------

*CodeSpaces* is a cloud based GitHub implementation of VSCode with a large
set of extensions, including collaboration and versioning support. 

======================= =====================================================
Purpose                    Link
======================= =====================================================
Editing                     `VSCode <https://code.visualstudio.com/>`_  
rivt Extensions             :ref:`rivtstudio-settings`
Version Control             `Git <https://git-scm.com>`_
======================= =====================================================

*GitHub Codespaces* is a VSCode cloud-based development environment connected
to GitHub files. It can be set up with *rivt extensions* that provide a complete
rivt editing and collaboration environment in the cloud.

*rivtstudiospace* is a cloud based rivt installation that may be 
:ref:`forked<rivt-remote>` into a personal GitHub repository.


.. _rivtstudio-settings:

**[11]** VSCode Profile
---------------------------------------------------------------------------

Workspace extension and other settings are stored in the *.vscode* folder and
should be included as part of a *report folder*. Settings that affect the
*rivt* editing and execution environment incldue:

- rivt.code-snippets
- settings.json (extension settings)
- tasks.json
- launch.json

Global settings can be exported and imported using VSCode Profiles. VSCode
*rivt* extensions and settings may be installed from this link.


**Snippets and extensions**

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

================= ==============================================================
Keystrokes                   Description
================= ==============================================================
api                 insert import statement for API
rvr                 API Run  
rvi                 API Insert    
rvv                 API Values 
rvt                 API Tools 
rvd                 API Docs
| at                 attach command 
| im                 image command
| i2                 side by side image command
| pu                 publish command
| ta                 table command
| va                 value command
| vs                 value table command
_ce                 center bold line of text
_ma                 utf-8 text math
_la                 LaTeX math
_ta                 number table
_ur                 URL link
_gl                 glossary term link
_se                 section link
_en                 endnote link
_do                 download link
_[m                 markup block
_[p                 python block
_[e                 end block 
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

   rvD02-rivtremote.rst
   rvD03-collab.rst
  
