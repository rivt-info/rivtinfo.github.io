**1.** Introduction
=========================

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

*rivt* is an open source software project that faciliates the reuse and
improvement of engineering documents. Writing engineering documents typically
involves combining text, tables, diagrams, equations and calculations from a
variety of sources. Although software combining these elements is available,
reusing a document is generally difficult because of the following limitations:

- documents are divided among many incompatible programs
- documents are inaccessible without frequently updating software
- update costs are high
- software is limited to specific platforms
- version controls are limited
- report generation features are limited
- collaboration features are limited

The table below compares *rivt* with other representative software and
summarizes how it addresses these limitations:

.. rst-class:: center


Table 1 - **Reuse Features Comparison**

============ ========= ======== ======== ========= ========= ============= 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_  CP [5]_   Collab [6]_  
============ ========= ======== ======== ========= ========= ============= 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS     some     some       no      no          yes      some  
Jupyter        no       no         no      yes         yes      yes  
**rivt**      **yes**  **yes**   **yes**  **yes**   **yes**    **yes**
============ ========= ======== ======== ========= ========= ============= 


.. rst-class:: left

    .. [1] Report generation
    .. [2] Version control
    .. [3] Plain text input files
    .. [4] Forward and backward compatibility
    .. [5] Cross-platform
    .. [6] Collaboration support


.. toctree::
    :maxdepth: 1
    :hidden:

    rv01-api.rst
    rv02-compile.rst
    rv03-terms.rst
    rv04-faq.rst
    rv05-smallex1.rst
    rv06-smallex2.rst