**1. Intro**
=============

**rivt** is a markup language for writing and formatting engineering documents,
with an emphasis on rivt file sharing and integration of existing engineering
software tools.

Engineering documents typically include text, tables, diagrams, equations and
calculations. Even though software exists for this use, there are implementation
issues that reduce their usefulness. 

These include high initial and update costs combined with incompatibilities
between programs, program updates and operating systems. Given these
constraints, a typical document source will generally have limited distribution.
Also, sharing details and insights around new and developing technologies is
restricted because of the program acqusition and rewrite costs. Finally,
existing programs are not designed to easily produce organized reports.

Engineering reports are typically assembled from a variety of model outputs,
calculations, and design codes. **rivt** is designed to integrate many output
types and automate report assembly. The table below compares **rivt** features
with other programs.

**Table: Comparison of Program Features**

=========== ========= ========== ========== ======== ======== ======= ======== ======== 
Program     Open Src  Compat.[1]  Vers.[2]  Text[3]  All-OS   Remote   Local   Reports  
=========== ========= ========== ========== ======== ======== ======= ======== ======== 
Matlab      no        no          no          no      no       no      yes      no 
Mathcad     no        no          no          no      no       no      yes      no 
Mathemat.   no        no          no          no      no       no      yes      no 
Cloud Prg.  no        no          no          no      yes      yes     no       no 
Jupyter     yes       yes         no          no      yes      yes     yes      no
**rivt**    **yes**   **yes**    **yes**    **yes**  **yes**  **yes** **yes**  **yes** 
=========== ========= ========== ========== ======== ======== ======= ======== ========  

[1] Forward, backward file compatiblilty

[2] Extensive versioning for document files

[3] Readable and editable text input files


**Definitions**
----------------

A **rivt** file is a text file (.py) that imports the **rivtlib** api:: 

    import rivtlib.api as rv

which exposes 6 API functions ::

    rv.R(rS) - (Run) Run shell scripts 
    rv.I(rS) - (Insert) Insert text, images, tables and math equations 
    rv.V(rS) - (Values) Evaluate tables and equations 
    rv.T(rS) - (Tools) Execute Python functions 
    rv.W(rS) - (Write) Write formatted rivt documents 
    rv.X(rS) - (eXclude) Skip rivt-string processing (interactive editing) 
    rv.Q()   - (Quit) Stop file processing (interactive editing)    



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

    - A **rivt file** is a text file (.py) that imports the **rivtlib** package.

    - A **rivt doc** (document) is a text, HTML or PDF file output of a **rivt** file. 

    - A **rivt report** is a collated collection of **rivt docs**.

    - **rivtlib** is a `Python library <https://rivtlib.net>`_ that generates **rivt docs** and **reports** from a **rivt** file.

    - **rivtedit** is a an open source editing and publishing framework built around `VScode <https://vscode.com>`_.

    - **rivtzip** is a portable, single folder version of **rivtedit**.


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


