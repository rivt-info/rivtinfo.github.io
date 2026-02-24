**A.2 Motivations**
=====================================================================


**[1t]** Background
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

*rivt* is an open source software project that simplifies sharing and reuse of
engineering documents. This has always been a challenge because engineering
documents are complex. They include text, images, tables, calculations, models
and computer code organized into reports. 

There are a number of engineering document programs, but sharing and reuse has
been restricted by their design and terms of use:

- documents written by different programs are incompatible
- frequent software updates are needed to maintain document access
- update costs are high
- newer document formats become inaccessible without upgrades
- software is limited to specific platforms
- document version control is limited
- report generation features are limited
- collaboration features are limited

The table below summarizes and compares limitations between different software
programs. *rivt* is designed to address these limitations.

.. rst-class:: center

**Software Comparison**

============ ========= ======== ======== ========= ========= ============= 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_  CP [5]_   Collab [6]_  
============ ========= ======== ======== ========= ========= ============= 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS    limited  limited     no      no          yes      limited  
Jupyter        no       no         no      yes         yes      yes  
**rivt**      **yes**  **yes**   **yes**  **yes**   **yes**    **yes**
============ ========= ======== ======== ========= ========= ============= 


.. rst-class:: left

    .. [1] Report generation
    .. [2] Native version control
    .. [3] Plain text, readable input files
    .. [4] Forward and backward compatibility
    .. [5] Cross-platform
    .. [6] Collaboration support


**[2t]** Use Cases
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

The primary use case for *rivt* is producing engineering documents that lie
somewhere between back of envelope notes and calculations, and formal journal
publications. In other words it produces formatted and organized documents that
are easily edited. The second use case is when format flexilibty is needed i.e.
text, PDF or HTML.

*rivt docs* can be used for:

#. internal communication
#. research documentation
#. government permits
#. funding applications

*rivt files* can function as a front and back end for:

#. software control
#. visualization
#. instrumentation

Because *rivt* is built with collaborative tools it may be used in:

#. teaching
#. demonstrations
#. real timecollaboration
