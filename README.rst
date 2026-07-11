rivtlib
========

**rivtlib is alpha software. Some features are not complete and the program has
bugs.**


*rivt* is an extensible, open-source Python tool for writing engineering
documents with a focus on reuse [1]_. Python knowledge is not required but
*rivt* capabilities can be extended with Python scripts that access scientific
and engineering libraries.

There are four types of rivt document files:

.. code-block:: text

                    | A rivt file is the basic input file that
      rivt file     | compiles to a text, PDF or HTML document. 
                    | It is a Python file (.py) that imports the 
                    | rivtlib Python package.

                    | A rivt doc is the published output of a
      rivt doc      | rivt file. A doc is an output file in 
      rivt chapter  | formatted text, PDF or HTML. In the context
                    | of a report or book a doc is a chapter. All 
                    | formats are compiled from the same rivt file. 

                    | A rivt report is the published output 
                    | of multiple docs collated into a single 
      rivt report   | text, PDF or HTML file. Each doc is a
                    | chapter in the report. Chapters are
                    | grouped together in divisions.

                    | A rivtbook is a collection of rivt files
      rivtbook      | with a common subject matter and
                    | organized for efficient selection and 
                    | inclusion in docs and reports.
   

The primary use cases for *rivt* are: 

#. producing reusable engineering documents that are easier to write, edit and 
   format compared to LaTeX, Excel, or Word.

#. producing clear, organized documents that are simple to publish but not 
   necessarily formatted to standards of formal journal articles or books. 

#. producing documents with source files that need to be partitioned into public
   and private parts prior to sharing as open-source.

For futher details please refer to the `rivt user manual <https://rivt.info>`__.

Use Cases
-----------

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

The table below compares limitations between different software programs and
identifies the focus of *rivt*.

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




