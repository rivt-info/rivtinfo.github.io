
Intro
=====

**rivt** is a markup language for writing and publishing engineering documents
with an emphasis on template reuse. Software for engineering documents is
already widely available but it comes with barriers to sharing and modifying
source files. These include high initial and update costs, incompatibility
between various programs and upgrades, and limited operating system support.
Consequently, similar engineering documents need to be repeatedly written from
scratch to accomodate different software programs. 

The table below summarizes the features addressed by **rivt** to address this
wasteful and frustrating work.

**Comparison of Engineering Document Programs**

=========  ======== =========== =========== ======== ======== ======= ======= ======= 
Features   O-Source  Compat.[1]  Vers. Ctrl  Text[2]  All-OS  Online  Local  Reports  
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


Summary
-------

**rivt** is a lightweight, open source, markup language for writing engineering
documents based on restructured text Python libraries. It is designed to make it
easy to share and reuse engineering document templates.  

A rivt file is a Python file (*.py*) that imports the **rivtlib** library:: 

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
**rivt report** (report) is a collated collection of rivt docs.

rivtlib is part of the open source **rivtzip** framework and is distributed
under the MIT license. **rivtzip** is an open source framework for publishing
rivt documents. The framework can be downloaded as portable Windows zip files,
or installed through OS specific shell scripts (https://rivt.zip). It includes
five established technologies::

    VSCode and extensions - document editing and processing

    Python and libraries - analysis and formatting
        
    Latex - typesetting
        
    Git, GitHub - version control

    QCAD - diagramming





