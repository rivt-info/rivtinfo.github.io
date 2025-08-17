**1 - Introduction**
=======================

.. toctree::
    :maxdepth: 2
    :hidden:

    api.rst
    terms.rst
    faq.rst


**rivt** was motivated by an interest in software that could efficiently reuse
engineering design calculations and documents. Engineering documents typically
include text, tables, diagrams, equations and calculations from a variety of
sources. Although document software that combines these elements is available,
implementation issues reduce their usefulness with regard to reuse. The
deficiencies can be summarized as:

- each program has a relatively small market share
- they generally ignore forward compatibility 
- version update costs are high
- they are not cross-platform
- they are not designed for collaboration and version control
- they do not produce organized reports
  
**rivt** addresses these limitations.

**Table - Software Comparison**
--------------------------------

============ ========= ======== ======== ========= ======= ============ 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_ OS [5]_ Collab [6]_  
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
.. [6] Supports collaboration




