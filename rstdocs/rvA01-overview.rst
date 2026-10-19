**A.1 |** Overview
==============================================

.. _rivt-overview:

**[1]** Start
-------------------------------------------------------------------------------- 

*rivt* is an open source project for writing, sharing and reusing engineering
calculation documents [1]_. This user manual is written in *rivt*. 
It runs on the desktop and in the cloud. The project includes *rivtlib* - 
a `Python package <https://pypi.org/project/rivtlib/>`_ that formats and compiles 
*rivt files*, *rivtStudio* - an integrated desktop editor that manages and 
publishes *rivt docs*, and *rivtRemote* - a containerized version of *rivtStudio*
that runs on a server in the cloud. Python knowledge is not required to use 
*rivt*, but adding custom Python scripts increases its capabilities. 

A rivt file (.py) uses *rivt markup* to organize text, calculations, images,
code and external programs that may be published as a *rivt doc* (a formatted
text, HTML and PDF document).The *rivt* folder structure provides a replicable
format for organizing a wide variety of file types. Groups of *docs* can form a
complete, structured *rivt report*.

This :ref:`tutorial <rivt-tutor>` provides examples of a 
:ref:`rivt file <example-file>` and its :ref:`text <text-doc>`, 
:ref:`PDF <pdf-doc>`, and :ref:`HTML <html-doc>` *docs*. 
 
To get started running examples see :ref:`install <rivt-overview>`. For *rivt
with AI* see :ref:`here <rivt-context>`.

*rivt files and reports* may be shared and distributed through any cloud
storage service. *rivt reports* and *rivt handbooks* are organized in top level
:ref:`project folders <rivt-folders>` that may be zipped for convenient
distribution. Examples are available on *Google Drive* at 
`openmodels.info <https://www.openmodels.info>`_. and on GitHub.A
convenient interface for searching public *rivt* READMEs GitHub 
is :ref:`here <search-interface>`.

.. [1] rivt includes provisions for selectively exporting *rivt file*
    sections to a *public rivt report folder* for open-source distribution.

------------------------------------------------------

.. _rvmotivation:
 
**[2]** Motivation
-------------------------------------------------------------------------------- 

Broadly sharing engineering documents has been a challenge because they are
complex and because commercial software objectives do not align with this goal.
They may include text, images, tables, calculations, active models and computer
code. They are also dynamic and are frequently updated and recalculated as
project designs evolve and change.

The need for reuse of engineering documents is a matter of improving efficiency
and making time for independent and creative thought. Most engineering
calculations are not fundamentally unique. The basic equations and methods are
shared across many projects. However they are always organized in a unique way
for the specific project requirements. The commercial market response to this
need has been to develop a number of siloed programs with barriers to sharing
and reuse including:

- incompatible documents across different programs
- costly software updates that are backward incompatible
- software limited to specific platforms
- limited version control
- limited report generation
- limited collaboration

*rivt* produces organized, formatted engineering documents from active
calculation files that can be shared anywhere. The primary use cases for *rivt*
are:

    A. producing reusable engineering documents that are easier to write, edit and 
    maintian compared to LaTeX, Excel, or Word.

    B. producing documents that need to be partitioned into public
    and private parts prior to sharing.

    C. using Python and AI tools to write engineering documents

    D. functioning as a front and back end for external software.

Engineering document types include:

    #. internal communications
    #. research documentation
    #. government permits
    #. technical reports
    #. funding applications
    #. teaching and presentation materials
    #. homework

`Quarto <https://quarto.org/>`_ is likely a better fit for documents with
highly specific format requirements including journal articles and books and
that do not need live recalculation . For interactive calculation documents
that do not need organized reports or partitioning into private and public
sections `Jupyter Notebooks <https://jupyter.org/>`_ is likely a better tool.
Finally, the table below summarizes and compares limitations between specific
programs that *rivt* is designed to complement or replace.


.. rst-class:: center

**Software Comparison (commercial programs in italics)**

============= ============ ========= ======== ========== =========== ========== ========= ============= ===========
Program       Reprt [2]_   Ver [3]_  Txt [4]_  Priv [5]_  Unts [6]_  Comp [7]_  C-P [8]_   Coll [9]_     Pub [10]_
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

.. [2] Report generation.
.. [3] Native Git version control.
.. [4] Plain text input and output files.
.. [5] Integrated syntax control of private/public files.
.. [6] Calculation with dual units.
.. [7] Forward and backward compatibility.
.. [8] Cross-platform support.
.. [9] Collaboration support.
.. [10] Text, PDF, and HTML documents from the same input file.



.. toctree::
    :maxdepth: 1
    :hidden:

    rvA02-run.rst 
    rvA03-tutor.rst
    rvA04-exfile.rst
    rvA05-txtdoc.rst
    rvA06-htmldoc.rst
    rvA07-pdfdoc.rst
