1. Introduction
=======================

*rivt* is a software project that faciliates reuse and community improvement of
engineering documents. Writing engineering documents typically involves text,
tables, diagrams, equations and calculations from a variety of sources.
Although software combining these elements is available, reusing an arbitrary
document is generally difficult because of the following limitations:

- documents are divided among many incompatible programs
- newer documents are inaccessible without frequently updating software
- update costs are high
- software is limited to specific platforms
- collaboration and version control is limited
- report generation features are limited
  
As an open source project, **rivt** addresses these limitations. The table
below compares it with other representative software:

.. rst-class:: center


Table 1 - **Reuseable Features Comparison**

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

    api.rst
    terms.rst
    faq.rst
    smallex.rst