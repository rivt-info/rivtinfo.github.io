
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

**rivt** is a markup language and framework for writing and publishing documents
with an emphasis on template reuse.

Software for engineering documents is widely available but always presents
barriers to resuing and sharing the source files. They include high initial and
upgrade costs, incompatibility between versions, programs, and operating
systems, and limited version control. This leads to similar engineering
documents being repeatedly written from scratch for different programs. The
table below summarizes the features addressed by **rivt** that address this wasted
effort.

**Engineering Document Programs - Compared**

========= ======== ====== ======== ======= ===== ====== ====== ====== ========
Program   Subscrip Open   Compat.  Version Text  Local  Local  Online Collated  
--------- -------- ------ -------- ------- ----- ------ ------ ------ --------
Features  Fee      Source Versions Control Input All-OS Mobile Collab Reports
========= ======== ====== ======== ======= ===== ====== ====== ====== ======== 
rivt      no       yes    yes      yes     yes   yes    yes    yes    yes 
Matlab    yes      no     no       no      no    no     no     no     no 
Mathcad   yes      no     no       no      no    no     no     no     no 
Mathemat. yes      no     no       no      no    no     no     no     no 
Online    yes      no     no       no      no    no     no     yes    no 
Jupyter   no       yes    yes      no      no    yes    yes    yes    no
========= ======== ====== ======== ======= ===== ====== ====== ====== ======== 



.. toctree::
    :maxdepth: 1
    :hidden:
    
    setup.rst
    system.md
    organize.rst
    edit.md
    find.md

.. toctree::
    :maxdepth: 1
    :caption: Publish
    :hidden:
    
    docs.md
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