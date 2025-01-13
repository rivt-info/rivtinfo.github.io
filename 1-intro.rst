
Intro
=====

**rivt** is a markup language for writing and publishing engineering documents
with an emphasis on template sharing and reuse. Software for engineering
documents is already widely available but there are barriers to sharing and
modifying source files between programs and versions. These include high
software and update costs, and incompatibility between programs, upgrades and
operating systems. The current situation requires repeated unproductive
rewrites of similar engineering documents to accomodate different software
programs. Sharing calculation details for new or improved technologies is also
restricted by these barriers.

In addition, existing programs are generally not designed to produce collated
reports. Engineering documents are assembled from a variety of modeling,
calculation, standards and other published and programatic sources. **rivt** is
designed to organize inputs from various sources into a single document. The
table below summarizes **rivt** features intended to address these lonigstnding
and frustrating limitations.

**Comparison of Programs**

=========  ======== =========== =========== ======== ======== ======= ======= ======= 
Features    Opn Src  Compat.[1]  Vers. Ctrl  Text[2]  All-OS  Remote  Local   Reports  
=========  ======== =========== =========== ======== ======== ======= ======= ======= 
Matlab     no        no          no          no      no       no      yes      no 
Mathcad    no        no          no          no      no       no      yes      no 
Mathemat.  no        no          no          no      no       no      yes      no 
Online     no        no          no          no      no       yes     no       no 
Jupyter    yes       yes         no          no      yes      yes     yes      no
**rivt**   **yes**  **yes**     **yes**     **yes**  **yes**  **yes** **yes** **yes** 
=========  ======== =========== =========== ======== ======== ======= ======= =======  

[1] Forward, backward file compatiblilty

[2] Readable text input files


A **rivt** file is a Python file (.py) that imports the **rivtlib** library:: 

    import rivtlib.rivtapi as rv


and exposes 6 API functions ::

    rv.R(rS) - (Run) Run shell scripts 
    rv.I(rS) - (Insert) Insert text, images, tables and math equations 
    rv.V(rS) - (Values) Evaluate tables and equations 
    rv.T(rS) - (Tools) Execute Python functions 
    rv.X(rS) - (eXclude) Skip rivt-string processing 
    rv.W(rS) - (Write) Write formatted rivt documents 

    
where **rS** is a triple quoted string that follows rivt markup syntax.

**rivtlib** is a Python library that generates **rivt docs** and **reports**.

A **rivt doc** (document) is a text, HTML or PDF file output from a rivt file. 

A **rivt report** is a collated collection of rivt docs.

**rivtzip** is a portable, free and open source editing and publishing framework.

**rivtlib** is distributed under the MIT license and is included in **rivtzip**
which can be downloaded as portable Windows zip files, or installed through OS
specific shell scripts (https://rivt.zip). The rivtzip framework includes five
established technologies:

- **VSCode and extensions** - editing and processing

- **Python and libraries** - analysis and formatting
    
- **Latex** - typesetting
    
- **Git, GitHub** - version control

- **QCAD** - diagramming





