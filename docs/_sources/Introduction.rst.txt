**Introduction**
==================

.. toctree::
    :maxdepth: 2
    :hidden:

    ./filesintro/terms.rst
    ./filesintro/API.rst
    ./filesintro/FAQ.rst


**rivt** was developed out of personal frustration with existing software that
could not efficiently leverage prior work when writing and assembling
engineering reports. Engineering documents typically include text, tables,
diagrams, equations and calculations. Although software exists that combine
these elements, there are serious implementation issues that blunt their
usefulness as tools for reuse of pre-existing designs and reports.

The issues with current software can be summarized as follows: 

- each has a relatively small market share
- frequently breaks forward compatibility 
- update costs are high
- not designed for file version control 
- not designed to produce organized reports
- not designed for collaborative work
  

**Table: Comparison of Engineering Document Software Features**

============ ========= ======== ======== ========= ======= =========== 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_ OS [5]_ Col [6]_  
============ ========= ======== ======== ========= ======= =========== 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS     no       no         no      no          yes      yes  
Jupyter        no       no         no      yes         yes      yes  
**rivt**      **yes**  **yes**   **yes**  **yes**  **yes**  **yes**
============ ========= ======== ======== ========= ======= =========== 

.. [1] Report generation
.. [2] Version control
.. [3] Plain text input files
.. [4] Compatibility with future versions
.. [5] Operating system independent
.. [6] Collaborative work




