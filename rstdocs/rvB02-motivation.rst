**B.2 |** Motivations
=====================================================================

.. _motivation: 

**[1]** Background
--------------------------------------------------------------------- 

*rivt* is an open source software program that simplifies publication and
general reuse of engineering documents. These software characteristics have
always been a challenge because engineering documents are complex and
commercial software purposes do not align with this goal.

Widely used document software is not sufficient because of the additional
complexity of engineering documents. They may include text, images, tables,
calculations, models and computer code. They are also dynamic and are
frequently updated by many people as projects evolve and progress.

The desire to reuse engineering documents is a matter of simple efficiency. Most
engineering projects are not fundamentally unique. They use similar patterns and
templates that differ in degree and details, not kind. The commercial market 
response to engineering document software has been to develop incompatible, 
siloed programs with barriers to sharing and reuse that include:

- incompatible documents across programs
- costly software updates that are backward incompatible
- software limited to specific platforms
- limited version control
- limited report generation
- limited collaboration

Open source solutions can alter that approach and *rivt* is designed to address
these barriers as both a compliment and replacement to existing software. The 
table below summarizes and compares limitations between different programs
(commercial programs in italics).

.. rst-class:: center

**Software Comparison**

============= ============ ========= ======== ========== =========== ========== ========= ============= ===========
Program       Reprt [1]_   Ver [2]_  Txt [3]_  Priv [4]_  Unts [5]_  Comp [6]_  C-P [7]_   Coll [8]_     Pub [9]_
============= ============ ========= ======== ========== =========== ========== ========= ============= ===========
*Matlab*         no           no         no     no        no           no         no        no            yes
*Mathcad*        no           no         no     no        no           no         no        no            no
*Mathematica*    no           no         no     no        no           no         no        no            yes
*Cloud SaaS*    limited       no         no     no        no           no         yes      limited       limited
*Excel*         limited       no         no     no        no           yes        no        yes           yes
Jupyter          no           no         no     no        no           yes        yes       yes           yes
Quarto           yes          yes        no     no        no           no         yes       yes           yes
**rivt**        **yes**     **yes**   **yes**  **yes**    **yes**     **yes**    **yes**   **yes**       **yes**  
============= ============ ========= ======== ========== =========== ========== ========= ============= ===========

.. rst-class:: left

    .. [1] Report generation
    .. [2] Native version control
    .. [3] Plain text input and output files
    .. [4] Syntax control of private/public sections
    .. [5] Dual units
    .. [6] Forward and backward compatibility
    .. [7] Cross-platform
    .. [8] Collaboration support
    .. [9] PDF and HTML documents from the same input file  


---------------------------------------------------

.. _use-case:

**[2]** Use Cases
--------------------------------------------------------------------- 


The primary use cases for *rivt* are: 

#. producing reusable calculation documents that are easier to write, edit and 
   format compared to LaTeX, Excel, Word or other general purpose document software.

#. producing clear, organized documents that are simple to publish but not 
   necessarily formatted to standards of formal journal articles or books. 

#. producing documents with source files that need to be partitioned into public
   and private parts prior to sharing as open-source

Specific examples include: internal communication, research documentation,
government permits, technical reports, funding applications, teaching, 
presentations, homework, and front or back ends for calculation software. 
