**A.2 Motivations**
=====================================================================


**[1]** Background
--------------------------------------------------------------------- 

*rivt* is an open source software project that simplifies sharing and reuse of
engineering documents. This has always been a challenge because engineering
documents are complex. They may include text, images, tables, calculations,
models and computer code. The market response to engineering document software
has been to develop incompatible, siloed programs with barrriers to 
sharing and reuse that include:

- incompatible documents across programs
- costly software updates that are backward incompatible
- software limited to specific platforms
- limited version control
- limited report generation
- limited collaboration

*rivt* is designed to address these barriers as both a compliment and
replacement to existing software. The table below summarizes and compares
limitations between different programs.

.. rst-class:: center

**Software Comparison**

============ ============ ========= ======== ========= ========= ============= 
Program      Report [1]_   Ver [2]_ Txt [3]_ Comp [4]_  CP [5]_   Collab [6]_  
============ ============ ========= ======== ========= ========= ============= 
Matlab         no           no         no      no          no       no   
Mathcad        no           no         no      no          no       no   
Mathematica    no           no         no      no          no       no   
Cloud SaaS    limited       no         no      no          yes      limited  
Excel         limited       no         no      yes         no       yes 
Jupyter        no           no         no      yes         yes      yes  
**rivt**      **yes**     **yes**   **yes**  **yes**   **yes**    **yes**
============ ============ ========= ======== ========= ========= ============= 

.. rst-class:: left

    .. [1] Report generation
    .. [2] Native version control
    .. [3] Plain text, readable input files
    .. [4] Forward and backward compatibility
    .. [5] Cross-platform
    .. [6] Collaboration support


---------------------------------------------------


**[2]** Use Cases
--------------------------------------------------------------------- 

The primary use case for *rivt* is writing and sharing document source files,
and publishing engineering documents in text, PDF or HTML formats. A second use
case is as a front or back end for pre- and post-processing data from other
software. A third use case is real-time collaboration using interfaces like
VSCode, Codespaces, Firebase, Gitpod or replit.

A. Engineering documents for:

#. internal communication
#. research documentation
#. government permits
#. technical reports
#. funding applications
#. homework

B. Front and back ends for:

#. software pre- and post-processing
#. visualization
#. instrumentation


C. Collaboration for:

#. teaching
#. presentations
#. document preparation
