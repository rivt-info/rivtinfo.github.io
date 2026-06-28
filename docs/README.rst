rivtlib
========

**rivtlib is alpha software. Some features are not complete and the program has
bugs.**

*rivt* is an extensible, open source tool for writing and sharing reproducible
engineering documents. Engineering documents may need to include text, images,
tables, calculations, models and computer code. The primary use case for *rivt*
is producing reproducible engineering documents:

#. that are easier to write and format than LaTeX, Excel, or Word when
   equations, code and external programs are needed.

#. that need to be clear and complete but not formatted to the 
   standards of formal journal publications.

#. that need to be published as text, PDF or HTML documents.

For futher details please refer to the `rivt user manual <https://rivt.info>`__.

Use Cases
-----------

Publishing engineering documents for:

#. internal communication
#. research documentation
#. government permits
#. technical reports
#. funding applications
#. teaching
#. presentations
#. homework

Other uses include:

#. Functioning as a front and back end for external software. 
#. Collaboration through sharing or real time interaction. 

The table below compares limitations between different software programs.
*rivt* is designed to address these limitations and serve as a complement or
replacement to existing software.

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



