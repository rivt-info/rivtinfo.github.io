**C.1 Markup**
==================

.. _rivt string:

**[1t]** rivt string
----------------------------------

.. raw:: html

    <hr>

Each :doc:`API function <rvA01-intro>` takes a triple quoted :term:`rivt
string` argument composed of two parts - a :term:`header substring` followed 
by a :term:`content substring`.

The *header substring* is the first line of a *rivt string* that defines
section processing and formatting. It is followed by a *content substring* that
includes :term:`rivt markup` and other text. It is indented 4 spaces for
improved readability and section folding.

.. _Header substring:

**[2t]** Header substring 
----------------------------

.. raw:: html

    <hr>

The :term:`header substring` starts with a *section label* followed by vertical
bar that deliniates three comma separated *section parameters* that can
override default behavior. The *section label* is the section title. 

.. code-block:: python

    rv._("""Section Label | doc;stored, private;public, section;merge

         Content text indented 4 spaces (utf-8 text)
        
        ...
        
        """)

The parameters include the following, in any order:

*private/public* 
    Determines whether the API section text is copied to the
    the */public* folder *rivt file* for sharing. For public files 
    the file is renamed from:

    .. code-block:: text

        rvAnn-filename.py

    to a filename with an additional hyphen.
    
    .. code-block:: text

        rv-Ann-filename.py


*doc/stored*
    Determines whether the *rivt string* is formatted and printed in the doc, 
    or just annotated in the doc and written to a file in the *Stored* folder 
    for optional inclusion as an appendix.

*section/merge* 
    Determines whether the API starts a new *doc* section
    or is merged into the previous section.   

Default settings in the *header substring* do not need to be specified. The
default setting for each API is listed first (in bold) in the table below.
 
========== ===================== ===================== =====================
API          private;public         doc;stored         section;merge         
========== ===================== ===================== ===================== 
rv.R        **private**;public     **stored**;doc       **merge**;section
rv.I        **private**;public     **doc**;stored       **section**;merge   
rv.V        **private**;public     **doc**;stored       **section**;merge    
rv.T        **private**;public     **stored**;doc       **merge**;section
rv.S        **private**;public     **stored**;doc       **merge**;section
rv.D        **public**             **stored**           **merge**
rv.X        **private**            **stored**           **merge**
========== ===================== ===================== ===================== 

Examples of *header substring* settings are shown below.

**An example with explicit defaults that do not have to be declared:**

.. code-block:: python

    # This
    
    rv.I("""A New Section | private, doc, section

        Content text
        ...
        
        """)
    
    # is equivalent to:

    rv.I("""A New Section  

        Content text
  
        ...
        
        """)


**An example that merges a section into the previous section. It does not 
create a new section and merges the section content into the prior one.**

.. code-block:: python

    rv.I("""A Merged Section | merge

        Content text

        ...
        
        """)

.. _Content substring:

**[3t]** Content substring
------------------------------

.. raw:: html

    <hr>

The :term:`content substring` is indented four spaces for legibility and 
code folding. It includes :doc:`line tags<rvC02-linetags>`, 
:doc:`block tags<rvC03-blocktags>` and  :doc:`commands<rvC04-commands>` 
along with  text.

.. code-block:: python

    rv._("""Section Label  

        Content text indented 4 spaces.
        ...
        
        """)

Content is converted line by line into formatted text and `RestructuredText
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_, and then
further processed into HTML or PDF. If a line does not contain a *command* or
*tag* it is passed through as is, which allows for including some *restructured
text* directly in the *Insert* function content (rv.I). For example 
surrounding words with * or ** formats a word as italic or bold respectively.

In addition the *Tools function* (rv.T) directly supports processing HTML,
LaTex and reStructuredText scripts with block tags.

**[5t]** Tags and Commands
----------------------------

Markup tags and commands are described in detail :doc:`here <rvC01-markup>`. 

:doc:`Line Tags <rvC02-linetags>`

A :term:`line tag` formats a line of text and is denoted with a single
**_[LETTER]**, placed at or near the end of the line, depending on the tag.

:doc:`Block Tags <rvC03-blocktags>`

A :term:`block tag` formats a block of text and begins with **_[[TAGNAME]]**
and terminates with **_[[END]]**.

:doc:`Commands <rvC04-commands>`

*rivt commands* read and write external files. They typically start in the
first column with a vertical bar ( | ) followed by the command name, file path,
and parameters. 

The exceptions are, the definition (**=:**), the assignment (**<=:**) 
and the compare (**<>**) commands, which are used to define, 
assign and compare values.

.. code-block:: bash  
    
    | COMMAND | relative path | parameters

File paths are specified relative to the *rivt root folder*.  
The *rivt report* folder structure is described :doc:`here. <rvD03-folders>`.

If the path is ommitted the default path for each command is applied. 
If the *singledoc* parameter is set, the *resource files* and *docs* are stored
in the *rivt root folder*.

Tag and Command syntax for each API type is defined and described 
using the following format:

.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Markup Key<br>
    <br>
    _[TAG] or | COMMAND |</b><br>
    <br>
    Description<br>
    <br>
    <pre>
        Syntax:
            _[TAG] or | COMMAND | syntax

        Example:
            This is a sentence. _[C]
    </pre> 
    </p>


**[6t]** Folders
---------------------------

.. raw:: html

    <hr>

Folders organize files in standard locations to simplify *doc* and *report*
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
