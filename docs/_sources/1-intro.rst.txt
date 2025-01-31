**1. Intro**
=============

**rivt** is a markup language and framework for writing and publishing
engineering documents with an emphasis on template sharing and reuse. Software
for engineering documents is already widely available but there are barriers to
sharing and modifying source files between programs and versions. The barriers
include high software and update costs, and incompatibility between programs,
upgrades and operating systems. The current situation requires repeated
unproductive rewrites of similar engineering documents to accomodate different
software programs. Sharing calculation details for new and developing
technologies is also restricted by these barriers.

In addition, existing programs are generally not designed to produce collated
reports. Engineering reports are typically assembled from a variety of
modeling, calculations, standards and other published documents that need to be
organized and compiled. **rivt** is designed to compile inputs from various
sources into a single organized document.

The table below summarizes the **rivt** features that address these
longstanding and frustrating limitations to efficient collaboration and
publishing.

Table: Comparison of Program Features
-------------------------------------
========== ========= ========== ========== ======== ======== ======= ======== ======== 
Program    Open Src  Compat.[1]  Vers.[2]  Text[3]  All-OS   Remote   Local   Reports  
========== ========= ========== ========== ======== ======== ======= ======== ======== 
Matlab     no        no          no          no      no       no      yes      no 
Mathcad    no        no          no          no      no       no      yes      no 
Mathemat.  no        no          no          no      no       no      yes      no 
Online     no        no          no          no      no       yes     no       no 
Jupyter    yes       yes         no          no      yes      yes     yes      no
**rivt**   **yes**   **yes**    **yes**    **yes**  **yes**  **yes** **yes**  **yes** 
========== ========= ========== ========== ======== ======== ======= ======== ========  

[1] Forward, backward file compatiblilty

[2] Versioning for document files

[3] Readable text input files


**Definitions**
---------------


A **rivt file** is a Python file that imports the **rivtlib** package.

A **rivt doc** (document) is a text, HTML or PDF output file. 

A **rivt report** is a collated collection of rivt docs.

**rivtlib** is a `Python library <https://rivtlib.net>`_ that generates 
**rivt docs** and **reports**. 

The **rivtlib** source code is `here <https://github.com/rivtlib-net/rivtlib>`_

**rivtzip** is a portable, open source editing and publishing framework.

--------------------------------------------------------------------------------


A **rivt** file is a Python file (.py) that imports the **rivtlib** api:: 

    import rivtlib.api as rv


which exposes 6 API functions ::

    rv.R(rS) - (Run) Run shell scripts 
    rv.I(rS) - (Insert) Insert text, images, tables and math equations 
    rv.V(rS) - (Values) Evaluate tables and equations 
    rv.T(rS) - (Tools) Execute Python functions 
    rv.X(rS) - (eXclude) Skip rivt-string processing 
    rv.W(rS) - (Write) Write formatted rivt documents 



**FAQ**
-------

Questions
~~~~~~~~~~

1.0 - Which open source licenses apply to rivtzip? `A1.0`_  


2.0 - aslkfas fdasdf asdflk sdfljk asdflk jasdlf sadf asdflk sdflkj sdflkj saf `A2.0`_  


Answers
~~~~~~~~

.. _A1.0: 


**rivtlib** is distributed under the MIT license and can be installed through
PyPI or **rivtzip**, which is downloaded as portable, Windows
zip files. The rivtzip framework includes five open source projects:

- **VSCode and extensions** - for editing and processing

- **Python and libraries** - for analysis and formatting
    
- **Latex** - for typesetting
    
- **Git, GitHub** - for version control

- **QCAD** - for diagramming




.. _A2.0: 

the answer to question 2.0 


**Terms**
----------

doc
~~~
the output file (document) after processing a rivt file

division
~~~~~~~~
open source markdown language for writing, organizing and sharing engineering documents

report
~~~~~~~~
open source markdown language for writing, organizing and sharing engineering documents asdfasf sdflkjsadf sd fsaedlfk fsadlf sa

section 
~~~~~~~~
open source markdown language for writing, organizing and sharing engineering documents

open source editing and publishing framework for rivtlib Python library for processing 

rivtpub
~~~~~~~~
project folder containing private files not uploaded when sharing templates

rivt
~~~~~~~~
open source markdown language for organizing, modifying and publishing
engineering documents

rivtlib
~~~~~~~~
Python library for processing **rivt** files. It outputs formatted documents in
a serveral different formats. 

rivtzip
~~~~~~~~
an editing and publishing framework for rivt using additional open source
programs. **rivt** works with both single file documents and extensive reports
with hundreds of files.

namespace
~~~~~~~~~~
a `name <https://en.wikipedia.org/wiki/Namespace>`_ that provides a scope for
functions, variables, etc. Namespaces are used to organize code into logical
groups and to prevent name collisions that can occur especially when your code
base includes multiple libraries. In Python, namespaces are defined by the
individual modules.
  
GitHub
~~~~~~~~
version control

repo
~~~~~~~~
short for repository


