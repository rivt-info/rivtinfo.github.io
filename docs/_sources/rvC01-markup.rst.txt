**C.1 Markup**
==================

**[1t]** rivt String
----------------------------------

.. raw:: html

    <hr>

Each :doc:`API function <rvA01-intro>` takes a triple quoted string argument
:term:`rivt string` composed of two parts - a :term:`header` followed by
:term:`content text`. 

The first line is the *header*, followed by *text content** indented 4
spaces for improved readability and section folding. Content may include
:term:`rivt markup`, a readable, plain text language that generates formatted
text, PDF or HTML :term:`docs` and other arbitrary text.


.. code-block:: python

    rv._("""Section Label | include;store, private;public, section;merge

         Content text indented 4 spaces (utf-8 text)
        
        ...
        
        """)


**[2t]** Headers 
-------------------------

.. raw:: html

    <hr>

The :term:`header` starts with a *section label* followed by comma separated
*section parameters* that may override default behavior. The *section label* is
the section title and is separated from the *section header* paramaters by a
vertical bar. Parameters include the following:

- private/public : determines whether the API section text is copied to the
    the */public* folder *rivt file* for sharing. 

- print/store : determines whether the *rivt string* is formatted and printed 
    in the doc or just annotated and written to a file for optional inclusion 
    as an appendix. eps

- section/merge : determines whether the API starts a new *doc* section
    or is merged into the previous section.   


Default settings do not need to be specified in the *header*. In the table
below, the default setting for each API is listed first (in bold).
 
========== ===================== ==================== =====================
API          private;public         include;store        section;merge         
========== ===================== ==================== ===================== 
rv.R        **private**;public     **store**;include     **merge**;section
rv.I        **private**;public     **include**;store     **section**;merge   
rv.V        **private**;public     **include**;store     **section**;merge    
rv.T        **private**;public     **store**;include     **merge**;section
rv.D        **private**;public     **store**             **merge**
rv.S        **private**;public     **store**;include     **merge**;section
rv.X        **private**            **store**             **merge**
========== ===================== ==================== ===================== 


Examples of *header* settings are shown below.

**An example with explicit defaults that do not have to be declared**

.. code-block:: python

    rv.I("""A New Section | private, include, section

        Content text
        ...
        
        """)
    
    # Equivalent to:

    rv.I("""A New Section | 

        Content text
  
        ...
        
        """)


**An example that merges a section to the previous section**

.. code-block:: python

    rv.I("""A Merged Section | merge

        Content text

        ...
        
        """)

**[3t]** Content string
--------------------------

.. raw:: html

    <hr>

:term:`Content text` is indented four spaces for legibility and code folding.
It has arbitrary text along with :doc:`line tags<rvC02-linetags>`, 
:doc:`block tags<rvC03-blocktags>` and 
:doc:`commands<rvC04-commands>`.

.. code-block:: python

    rv._("""Section Label | 

        Content text indented 4 spaces (utf-8).
        ...
        
        """)


Content text is converted line by line into formatted text and `RestructuredText
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_, and then
further processed to an HTML or PDF file. If a line does not contain a
*command* or *tag* it is passed through as is, which allows for including some
*restructured text* directly. For example surrounding words with * for italics
or ** for bold. 

In addition the *Tools API function* (rv.T) supports processing raw Python,
HTML, LaTex and reStructuredText. 

**[5t]** Tags and Commands
----------------------------

:doc:`Line Tags <rvC02-linetags>`

A :term:`line tag` formats a line of text and is denoted with **_[LETTER]**,
generally placed at the end of the line for readability.

:doc:`Block Tags <rvC03-blocktags>`

A :term:`block tag` formats a block of text and begins with **_[[TAGNAME]]**
and terminates with **_[[END]]**. 

:doc:`Commands <rvC04-commands>`

*rivt commands* read and write external files. They typically start in the
first column with a vertical bar ( | ) followed by the file path, name and
parameters. The exceptions to this pattern are the assignment (**<=** ) and
definition (**:=**) commands, which are used to assign values to equation
results and define variables.

.. code-block:: bash  
    
    | COMMAND | relative path | parameters

File paths are specified relative to the *report* and *rivt file* folder.  
The *rivt report* folder structure is described :doc:`here. <rvD03-folders>`.

If the path is ommitted the default path for each command is applied. 

**[4t]** Markup Key
----------------------------------

.. raw:: html

    <hr>

Tag and Command syntax for each API type is defined and described using the
following format.


_[TAG] : description of :term:`line tag` 


.. topic::  syntax : description

   example

outputs: types of output


.. raw:: html

    <hr>


_[[TAG]] :  description of :term:`block tag`
        

.. topic::  syntax : description

  example

file types

.. raw:: html

    <hr>

| COMMAND |  description of :term:`command`

.. topic:: | COMMAND | relative path | parameters

  example

file types

**[5t]** Folders
-----------------------

.. raw:: html

    <hr>

Folders organize files in standard locations to simplify *docs* and *report*
generation.

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Key</b><br>

    - Required names or prefixes are shown in brackets [ ]. <br>
    - Folders (including subfolders) that contain author generated files 
    are marked with a single vertical bar ( | ).<br>  
    - Folders (including subfolders) that contain *rivtlib* generated files are 
    marked with double vertical bars ( || ).</p>

**Folders**

.. code-block:: bash

    [rivt]-Report-Label/                Report Folder Name
        ├── [rv101-]filename1.py        | rivt file
        ├── [rv102-]filename2.py        | rivt file
        ├── [rv201-]filename3.py        | rivt file
        ├── [rv202-]filename4.py        | rivt file 

        ...

        ├── [public]/                   || public rivt files 
        ├── [publish]/                  || doc and report files
        ├── [src]/                      |  source files from author
        ├── [stored]/                   || rivt stored files
        └── README.txt                  || searchable text report 

**Expanded Folders**

.. code-block:: bash

    [rivt]-Report-Label/                       Report Folder Name                
        ├── [rv101-]filename1.py               | rivt input files
        ├── [rv102-]filename2.py               
        ├── [rv201-]filename3.py               
        ├── [rv202-]filename4.py                 
        ├── [public]/                          || public rivt files                      
            ├── rv-101-filename1.py              
            ├── rv-201-filename3.py  
            └── rv-202-filename4.py      
        ├── [publish]/                         || reports and docs
            ├── [html]/                              HTML site  
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
            ├── [pdf]/                               PDF from rst2pdf 
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
            ├── [pdftex]/                            PDF from LaTeX  
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
            ├── [text]/                              text report
                ├── rv101-filename1.txt              text docs
                ├── rv102-filename2.txt       
                ├── rv201-filename3.txt       
                ├── rv202-filename4.txt       
                └── README.txt                       searchable text report                     
        ├── [src]                              | source files from author               
            ├── data/                               author created subfolder
                ├── data1.csv   
                └── conc-vals.csv  
            ├── image/                              author created subfolder                          
                ├── fig1.png
                └── fig2.jpg
            ├── output/                             author created subfolder
                ├── table1.csv                                               
                ├── image1.png                            
                └── opensees1.txt    
            ├── [gendoc]/
                ├── gen-html.cmd                     html generating script
                ├── gen-pdf.cmd                      pdf generating script
                ├── gen-pdftex.cmd                   LaTeX generating script
                ├── rivt-report.py                   report generating script
                ├── new-units.py                     define new units
                └── [style]/                         doc style files 
                    ├── [html]/                      html style files
                        ├── _locale/                 
                        ├── _static/                        
                        ├── _templates/                     
                        ├── conf.py                         
                        ├── genhtml.cmd                     
                        └── index.rst
                    ├── [pdf]/                       rst2pdf style files
                        ├── fonts/              
                        ├── style/                 
                        ├── Report-Cover.pdf           
                        └── genrst2pdf.cmd
                    ├── [pdftex]/                    pdftex style files
                        ├── gentexpdf.cmd             
                        ├── Report-cover.pdf                     
                        └── rivt.sty              
                    ├── [text]/                      text ini file
                        └── rv-text.ini
            ├── [py]/                                Python scripts and functions
                    ├── plot.py                               
                    └── loads.py
            └── [vals]/                              value files
                ├── steel-vals.csv     
                └── plastic-vals.csv
        ├── [stored]/                          || stored files from rivt            
            ├── [logs]/                              log files
                ├── rv101-api.txt   
                ├── rv101-log.txt
                └── rv102-log.txt
            ├── [sect]/                              stored sections                    
                ├── rv202-5d.txt   
                ├── rv103-4t.txt                         
                └── rv301-2r.txt               
            ├── [temp]/                              temp files
                └── rv101-label3.tex
            └── [vals]/                              stored value files
                ├── v101-2.csv
                └── v102-3.csv        
        └── README.txt                         || searchable text report 


.. toctree::
    :maxdepth: 1
    :hidden:

    rvC02-linetags.rst
    rvC03-blocktags.rst
    rvC04-commands.rst    
    rvC05-markup-r.rst
    rvC06-markup-i.rst
    rvC07-markup-v.rst
    rvC08-markup-t.rst
    rvC09-markup-d.rst
