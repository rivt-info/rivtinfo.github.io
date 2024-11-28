
.. image::  _static/img/rivt54d.png
    :class: dark-light
    :scale: 95%
    :align: center
    :alt: rivt logo


.. raw:: html

    <embed>
        <h1 style="font-size:2em; text-align:center"> rivt.info </h1>
        <hr width="100%" size="6" color="LightGrey" noshade>
    </embed>


Manual / API
------------

**rivt** is a markup language and framework for writing and publishing
engineering documents, with an emphasis on template reuse.

Software for engineering documents is already widely available but they come
with barriers to modifying and resuing source files. These include high initial
software and update costs, incompatibility between various programs and their
software updates, and limited operating system support. This leads to similar
engineering documents being repeatedly written from scratch for different
programs. The table below summarizes the features addressed by **rivt** that
address this wasted effort.


**Comparison - Engineering Document Programs**

========= ======== ======= ======== ======== ======= ======= ======= ====== =========
Program   Subscrip Open    Compat.  Version  Text    Local   Local   Online  Collated  
--------- -------- ------- -------- -------- ------- ------  ------- ------  --------
Features  Fee      Source  Versions Control  Input   All-OS  Mobile  Collab  Reports
========= ======== ======= ======== ======== ======= ======= ======= ======= ======== 
**rivt**  **no**   **yes**  **yes** **yes**  **yes** **yes** **yes** **yes** **yes** 
Matlab    yes      no        no       no      no       no     no      no     no 
Mathcad   yes      no        no       no      no       no     no      no     no 
Mathemat. yes      no        no       no      no       no     no      no     no 
Online    yes      no        no       no      no       no     no      yes    no 
Jupyter   no       yes       yes      no      no       yes    yes     yes    no
========= ======== ====== ======== ======= ===== ====== ====== ====== ======== 



.. toctree::
    :maxdepth: 1
    :caption: Introduction
    
    introduction.rst
    install.rst
    
.. toctree::
    :maxdepth: 1
    :caption: Write
    :hidden:

    organize.rst
    edit.md

.. toctree::
    :maxdepth: 1
    :caption: Publish
    :hidden:

    github.md
    find.md

.. toctree::
    :maxdepth: 1
    :caption: FAQ - Examples
    :hidden:
    
    faq.md
    terms.md
    example1.md
    example2.md
    changes.md