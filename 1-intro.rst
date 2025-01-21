
Intro
=====

**rivt** is a markup language for writing and publishing engineering documents
with an emphasis on template sharing and reuse. Software for engineering
documents is already widely available but there are barriers to sharing and
modifying source files between programs and versions. These include high
software and update costs, and incompatibility between programs, upgrades and
operating systems. The current situation requires repeated unproductive
rewrites of similar engineering documents to accomodate different software
programs. Sharing calculation details for new and developing technologies is
also restricted by these barriers.

In addition, existing programs are generally not designed to produce collated
reports. Engineering reports are typically assembled from a variety of
modeling, calculation, standards and other published documents. **rivt** is
designed to organize inputs from various sources into a single organized
document. The table below summarizes the **rivt** features that address
these longstnding and frustrating limitations to collaboration and shared,
incremental improvements.

**Comparison of Programs**

=========  ======== =========== ========== ======== ======== ======= ======== ======= 
Features    Opn Src  Compat.[1]  Vers.[2]  Text[3]   All-OS  Remote   Local   Reports  
=========  ======== =========== ========== ======== ======== ======= ======== ======= 
Matlab     no        no          no          no      no       no      yes      no 
Mathcad    no        no          no          no      no       no      yes      no 
Mathemat.  no        no          no          no      no       no      yes      no 
Online     no        no          no          no      no       yes     no       no 
Jupyter    yes       yes         no          no      yes      yes     yes      no
**rivt**   **yes**  **yes**     **yes**     **yes**  **yes** **yes** **yes**  **yes** 
=========  ======== =========== ========== ======== ======== ======= ======== =======  

[1] Forward, backward file compatiblilty

[2] Versioning for document files

[3] Readable text input files


A **rivt** file is a Python file (.py) that imports the **rivtlib** api:: 

    import rivtlib.api as rv


which exposes 6 API functions ::

    rv.R(rS) - (Run) Run shell scripts 
    rv.I(rS) - (Insert) Insert text, images, tables and math equations 
    rv.V(rS) - (Values) Evaluate tables and equations 
    rv.T(rS) - (Tools) Execute Python functions 
    rv.X(rS) - (eXclude) Skip rivt-string processing 
    rv.W(rS) - (Write) Write formatted rivt documents 

    
where **rS** is a triple quoted string incorporationg rivt markup syntax.

Definitions
===========

**rivtlib** is a Python library that generates **rivt docs** and **reports**.

A **rivt file** (document) is a Python file that imports the **rivtlib** api.

A **rivt doc** (document) is a text, HTML or PDF file output of a rivt file. 

A **rivt report** is a collated collection of rivt docs.

**rivtzip** is a portable, free and open source editing and publishing framework.

Distribution
============

**rivtlib** is distributed under the MIT license and can be installed through
PyPI or by inclusion in **rivtzip**, which can be downloaded as portable, Windows
zip files. The rivtzip framework includes five established technologies:

- **VSCode and extensions** - editing and processing

- **Python and libraries** - analysis and formatting
    
- **Latex** - typesetting
    
- **Git, GitHub** - version control

- **QCAD** - diagramming





