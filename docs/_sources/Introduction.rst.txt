**Introduction**
==================

.. toctree::
    :maxdepth: 2
    :hidden:

    ./filesintro/terms.rst
    ./filesintro/API.rst
    ./filesintro/FAQ.rst


**rivt** was developed out of personal frustration with the lack of software
that would efficiently leverage prior work when assembling engineering reports and
calculations. Engineering documents typically include text, tables, diagrams, equations and
calculations. Although software exists that combine these elements, there
are serious implementation issues that blunt their usefulness as tools for
reuse of existing designs and reports.

The issues with current software can be summarized as follows: 

- each has a relatively small market share
- it frequently breaks forward compatibility with new versions
- update costs are high
- it is not designed for file version control 
- it is not designed to produce organized reports
- it is not designed for collaborative work
  

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
.. [3] Text input files
.. [4] Compatibility with future versions
.. [5] Operating system independent
.. [6] Collaborative work




