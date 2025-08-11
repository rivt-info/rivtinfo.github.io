**Introduction**
==================

.. toctree::
    :maxdepth: 2
    :hidden:

    ./filesintro/terms.rst
    ./filesintro/API.rst
    ./filesintro/FAQ.rst


**rivt** was developed out of a need for document software that could
efficiently reuse prior engineering work. Engineering documents typically
include text, tables, diagrams, equations and calculations from a variety of
sources. Although document software exists that can combine these elements,
many implementation issues reduce their usefulness. They can be
summarized as follows:

- each has a relatively small market share
- they ignore forward compatibility 
- version update costs are high
- not cross-platform
- not designed for collaborative work and version control
- they do not produce organized reports
  
**rivt** is an open source solution that intends to address these limitations.

_______________________________________

**Table: Engineering Document Software - Comparison**

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
.. [6] Supports collaborative work




