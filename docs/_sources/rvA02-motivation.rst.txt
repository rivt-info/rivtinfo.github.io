**A.2 Motivations**
=====================================================================


**[1]** Background
--------------------------------------------------------------------- 

*rivt* is an open source software project that simplifies sharing and reuse of
engineering documents. This has always been a challenge because engineering
documents are complex. They may include text, images, tables, calculations,
models and computer code. The market response to these documents has been to
develop incompatible, siloed software that precludes document input sharing. The
barriers to resuse include:

- incompatible documents from different programs.
- frequent software updates required to maintain document access.
- high update costs.
- platform limited software.
- limited version control
- limited report generation
- limited collaboration

*rivt* is designed to address these barriers as both a compliment and
replacement to existing software. The table below summarizes and compares
limitations between different programs.

.. rst-class:: center

**Software Comparison**

============ ========= ======== ======== ========= ========= ============= 
Program      Rep [1]_  Ver [2]_ Txt [3]_ Comp [4]_  CP [5]_   Collab [6]_  
============ ========= ======== ======== ========= ========= ============= 
Matlab         no       no         no      no          no       no   
Mathcad        no       no         no      no          no       no   
Mathematica    no       no         no      no          no       no   
Cloud SaaS    limited   no         no      no          yes      limited  
Excel         limited   no         no      yes         no       yes 
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

**[2]** Use Cases
--------------------------------------------------------------------- 

The primary use case for *rivt* is sharing and publishing engineering documents
that are clear, formatted and organized but do not need to meet the standards
of formal journal publications. It also provides the option to publish in a
variety of formats including text, PDF or HTML.

A second use case is as a front or back end for pre- and post-processing data
from other software.

A third use case is document collaboration when used with interfaces like
VSCode, Codespaces, Firebase, Gitpod or replit.

1. Engineering documents for:

#. internal communication
#. research documentation
#. government permits
#. technical reports
#. funding applications
#. homework

2. Front and back ends for:

#. software pre- and post-processing
#. visualization
#. instrumentation


3. Collaboration in:

#. teaching
#. presentations
#. document preparation
