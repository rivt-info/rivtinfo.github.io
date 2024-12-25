
Intro
=====

**rivt** is a markup language for writing and publishing engineering documents
with an emphasis on template sharing and reuse. Software for engineering
documents is already widely available but there are barriers to sharing and
modifying source files. These include high initial software and update costs,
incompatibility between various programs and upgrades, and limited operating
system support. This results in a need to repeatedly rewrite similar
engineering documents to accomodate different software programs. It also
restricts the sharing of ideas and calculations methods. 

In addition, many engineering documents are assembled from a variety of
modeling, calculation, standards and other published and programatic sources.
**rivt** is designed to organize inputs from various sources into a single
document. The table below summarizes **rivt** features intended to address these
lonigstnding and frustrating limitations.

**Comparison of Engineering Document Programs**

=========  ======== =========== =========== ======== ======== ======= ======= ======= 
Features   O-Source  Compat.[1]  Vers. Ctrl  Text[2]  All-OS  Remote  Local   Reports  
=========  ======== =========== =========== ======== ======== ======= ======= ======= 
Matlab     no        no          no          no      no       no      yes      no 
Mathcad    no        no          no          no      no       no      yes      no 
Mathemat.  no        no          no          no      no       no      yes      no 
Online     no        no          no          no      no       yes     no       no 
Jupyter    yes       yes         no          no      yes      yes     yes      no
**rivt**   **yes**  **yes**     **yes**     **yes**  **yes**  **yes** **yes** **yes** 
=========  ======== =========== =========== ======== ======== ======= ======= =======  

[1] Backward and forward file compatiblilty

[2] Readable text input files


A **rivt** file is a Python file (.py) that imports the **rivtlib** library:: 

    import rivtlib.rivtapi as rv


and exposes 6 API functions ::

    rv.R(rS) - (Run) Run shell scripts 
    rv.I(rS) - (Insert) Insert text, images, tables and math equations 
    rv.V(rS) - (Values) Evaluate tables, values and equations 
    rv.T(rS) - (Tools) Execute Python functions 
    rv.X(rS) - (eXclude) Skip rivt-string processing 
    rv.W(rS) - (Write) Write formatted rivt documents 

    
where **rS** is a triple quoted string that follows rivt markup syntax.

**rivtlib** is a Python library that generates **rivt docs** and **reports**. A
**rivt doc** (document) is a text, HTML or PDF file output from a rivt file. A
**rivt report** is a collated collection of rivt docs.

**rivtlib** is distributed under the MIT license and is part of an open source
editing and publishing framework, **rivtzip** - The framework can be downloaded
as portable Windows zip files, or installed through OS specific shell scripts
(https://rivt.zip). The framework includes five established technologies:

- **VSCode and extensions** - document editing and processing

- **Python and libraries** - analysis and formatting
    
- **Latex** - typesetting
    
- **Git, GitHub** - version control

- **QCAD** - diagramming





