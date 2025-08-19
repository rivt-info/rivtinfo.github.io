**1.1 - Motivation**
=======================

.. toctree::
    :maxdepth: 2
    :hidden:

    api.rst
    terms.rst
    faq.rst


rivt development is motivated by an interest in software that can efficiently reuse
engineering design calculations and documents. Engineering documents typically
include text, tables, diagrams, equations and calculations from a variety of
sources. Although document software combining these elements is available,
document reused is limited. *rivt is designed to address these limitations.* 

The deficiencies can be summarized as:

- each program has a relatively small market share
- forward incompatibility - newer documents cannot be reused without upgrading
- high version update costs
- limited cross-platform
- limited collaboration and version control
- limited report generation
  
The table below provides comparisons with several available software programs.


.. rst-class:: center
    
Software Comparison


============ ========= ======== ======== ========= ======= ============ 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_ CP [5]_ Collab [6]_  
============ ========= ======== ======== ========= ======= ============ 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS     some     some       no      no          yes      some  
Jupyter        no       no         no      yes         yes      yes  
**rivt**      **yes**  **yes**   **yes**  **yes**  **yes**  **yes**
============ ========= ======== ======== ========= ======= ============ 


.. [1] Report generation
.. [2] Version control
.. [3] Plain text input files
.. [4] Forward and backward compatibility
.. [5] Cross-platform
.. [6] Collaboration support




