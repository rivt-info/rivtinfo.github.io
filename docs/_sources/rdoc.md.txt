---
myst:
    substitutions:
        "key3": |
            ```{image} _static/img/riv-doc02.png
            :alt: rivt-doc logo
            :target: https://github.com/rivt-doc.html
            :width: 50px
            ```
---

#  {{ key3 }} **rivt-doc**

- VS Code
- Texlive 

<hr>

## installation
<hr>

- VSCode + extensions 
- LaTeX 
- Github account

rivt-doc is available for every OS platform and installs either into a single
portable folder via a zip file, or as a collection of system programs. It also
runs in the cloud at **rivt-online** and may be installed on GitHub CodeSpaces
or other cloud service providers.

<hr>

## folders
<hr>

<pre style="background:#cfdde2;color:#000000">
[rivt]-Report-Label/               
    ├── .git
    ├── units.py                        (inputs: unit over-ride)
    ├── README.md                       (outputs: toc and summary) 
    ├── rivt01.ini                      (inputs: config file)
    ├── [doc0101]-div-label/            (division label)
        ├── [data0101]/                     (inputs: data files)
            ├── data1.csv                   
            ├── paper1.pdf
            └── functions1.py                   
        ├── [rivt]-doc-label1.py            (input: rivt file)
        └── README.md                       (output: GFM doc)
    ├── [doc0102]/                      (division file)
        ├── data[0102]/                     (inputs: data files)
            ├── data1.csv
            ├── fig1.png
            └── fig2.png
        ├── [rivt]-doc-label2.py            (input: rivt file)
        └── README.md                       (output: GFM doc)
    ├── [doc0201]-div-label/            (division label)
        ├── [data0201]/                     (inputs: data files)
            ├── data1.csv
            ├── attachment.pdf
            ├── functions.py
            └── fig1.png
        └── README.md                       (outputs: GFM doc)
    └── [private]/                      (private files)
        ├── [temp]/                         (outputs: temp files)
        ├── [report]/                       (report files)
            ├── 0101-Doc Label1.pdf         (outputs: PDF docs)
            ├── 0102-Doc Label2.pdf
            ├── 0201-Doc Label3.pdf
            └── Report Label.pdf            
        ├── images/                         (inputs: optional data folders ...)
            ├── fig1.png
            └── fig2.png
        ├── text/    
            ├── text1.txt
            └── text2.txt
        ├── append/    
            ├── report1.pdf
            └── report2.pdf
        └── tables/
            ├── data1.csv
            └── data1.xls
</pre>

<hr>

## VSCode
<hr>

### profiles

The rivt VSCode profile includes extensions, snippets and shortcuts for common editing functions.

### shortcuts

<pre style="background:#cfdde2;color:#000000">
==============  ===========================================================
Keystroke                   Description
==============  ===========================================================


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
</pre>

### snippets


| **snippet**
| :---------:
|     ini    
|     app    
|     img    
|     tbl    
|     dec    
|     txt   


### command snippets




 



