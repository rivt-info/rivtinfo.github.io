
Introduction
------------

**rivt** is a markup language and framework for writing and publishing
engineering documents, with an emphasis on template reuse.

Software for engineering documents is already widely available but they come
with barriers to modifying, sharing and resuing source files. These include high
initial software and update costs, incompatibility between various programs and
upgrades, and limited operating system support. Therefore, similar engineering
documents need to be repeatedly written from scratch to accomodate different
software programs. The table below summarizes the features addressed by **rivt**
to address this wasted effort.


**Comparison - Engineering Document Programs**

========= ======== ======= ======== ======== ======= ======= ======= ======= ========
Features  Subscrip Open    Compat.  Version  Text    Local   Local   Online  Collated  
Programs  Fee      Source  Versions Control  Input   All-OS  Mobile  Collab  Reports
========= ======== ======= ======== ======== ======= ======= ======= ======= ======== 
Matlab    yes      no        no       no      no       no     no      no     no 
Mathcad   yes      no        no       no      no       no     no      no     no 
Mathemat. yes      no        no       no      no       no     no      no     no 
Online    yes      no        no       no      no       no     no      yes    no 
Jupyter   no       yes       yes      no      no       yes    yes     yes    no
**rivt**  **no**   **yes** **yes**  **yes**  **yes** **yes** **yes** **yes** **yes** 
========= ======== ======= ======== ======== ======= ======= ======= ======= ======== 


.. toctree::
    :maxdepth: 1
    :caption: Introduction
    :hidden:
    
    introduction.rst
    install.rst

.. toctree::
    :maxdepth: 1
    :caption: Write
    :hidden:

    organize.rst
    edit.md
    find.md


.. toctree::
    :maxdepth: 1
    :caption: Publish
    :hidden:
    
    github.md

.. toctree::
    :maxdepth: 1
    :caption: FAQ - Examples
    :hidden:
    
    faq.md
    terms.md
    example1.md
    example2.md
    changes.md