**Introduction**
==================

.. toctree::
    :maxdepth: 2
    :hidden:

    ./filesintro/terms.rst
    ./filesintro/API.rst
    ./filesintro/FAQ.rst


**rivt** was motivated by a need for document software that could efficiently
reuse prior engineering work. Engineering documents typically include text,
tables, diagrams, equations and calculations from a variety of sources.
Although document software is available that effectively combines these
elements, implementation issues reduce their usefulness. The deficiencies can
be summarized as follows:

- each program has a relatively small market share
- they generally ignore forward compatibility 
- version update costs are high
- they are not cross-platform
- they are not designed for collaboration and version control
- they do not produce organized reports
  
**rivt** addresses these limitations.

_______________________________________

**Table: Engineering Document Software Comparison**

============ ========= ======== ======== ========= ======= =========== 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_ OS [5]_ Col [6]_  
============ ========= ======== ======== ========= ======= =========== 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS     some     some       no      no          yes      some  
Jupyter        no       no         no      yes         yes      yes  
**rivt**      **yes**  **yes**   **yes**  **yes**  **yes**  **yes**
============ ========= ======== ======== ========= ======= =========== 

.. [1] Report generation
.. [2] Version control
.. [3] Plain text input files
.. [4] Forward and backward compatibility
.. [5] Cross-platform
.. [6] Supports collaboration




