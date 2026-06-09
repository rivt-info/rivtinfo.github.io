**B.1 | Motivations**
=====================================================================

.. _motivation: 

**[1]** Background
--------------------------------------------------------------------- 

*rivt* is an open source software project that simplifies sharing and reuse of
engineering documents. This has always been a challenge because engineering
documents are complex. They may include text, images, tables, calculations,
models and computer code. They are also dynamic and are freqeuently updated
as projects evolve and progress. 

The desire to reuse engineering documents is a matter of simple efficiency. Most
engineering projects are not fundamentally unique. They follow familiar patterns
and differ in ddegree and detials, not kind. The commercial market response to
engineering document software has been to develop incompatible, siloed programs
with barrriers to sharing and reuse that include:

- incompatible documents across programs
- costly software updates that are backward incompatible
- software limited to specific platforms
- limited version control
- limited report generation
- limited collaboration

Open source solutions have begun to change that. *rivt* is designed to address
these barriers as a compliment and replacement to existing software. The table
below summarizes and compares limitations between different programs
(commercial programs in italics).

.. rst-class:: center

**Software Comparison**

============= ============ ========= ======== ========== ========= ========= ============= ===========
Program        Report [1]_  Ver [2]_ Txt [3]_  Pub [4]_  Comp [5]_  CP [6]_   Collab [7]_   Priv [8]_
============= ============ ========= ======== ========== ========= ========= ============= ===========
*Matlab*         no           no         no     yes         no          no      no            no
*Mathcad*        no           no         no     no          no          no      no            no
*Mathematica*    no           no         no     yes         no          no      no            no
*Cloud SaaS*    limited       no         no    limited      no          yes     limited       no
*Excel*         limited       no         no     yes         yes         no      yes           no
Jupyter          no           no         no     yes         yes         yes     yes           no
Quarto           yes          yes        no     yes         no          yes     yes           no
**rivt**        **yes**     **yes**   **yes**  **yes**    **yes**   **yes**    **yes**      **yes**
============= ============ ========= ======== ========== ========= ========= ============= ===========

.. rst-class:: left

    .. [1] Report generation
    .. [2] Native version control
    .. [3] Plain text formatted input and published files
    .. [4] PDF and HTML publication from same input file  
    .. [5] Forward and backward compatibility
    .. [6] Cross-platform
    .. [7] Collaboration support
    .. [8] Syntax control of private vs public input file content


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
