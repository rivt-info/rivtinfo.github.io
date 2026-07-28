**B.2 |** Motivations
=====================================================================

.. _motivation: 

**[1]** Background
--------------------------------------------------------------------- 

*rivt* is an open source software program that for writing, assembling
and reusing engineering calculation documents. Reuse of engineering documents has
always been a challenge because engineering documents are complex and apparently
commercial software goals do not align with this goal.

Widely used text and image oriented software is generally not sufficient
because of the additional complexity of engineering documents. They may include
text, images, tables, calculations, active models and computer code. They are
also dynamic, and are frequently updated and recalculated by others as
project designs evolve and progress.

The desire to reuse engineering documents is a matter of simple efficiency. Most
engineering calculations are not unique. They may be organized in different ways
with different inputs, but the basic equations and methods are shared across
many projects and evolve slowly. The commercial market 
response has been to develop incompatible, 
siloed programs with a number of barriers to sharing and reuse that include:

- incompatible documents across programs
- costly software updates that are backward incompatible
- software limited to specific platforms
- limited version control
- limited report generation
- limited collaboration

The table below summarizes and compares limitations between specific programs
that *rivt* is designed to complement or replace.

.. rst-class:: center

**Software Comparison (commercial programs in italics)**

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
