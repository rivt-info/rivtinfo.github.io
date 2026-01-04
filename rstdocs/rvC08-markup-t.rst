**C.8 Tool - rv.T**
=======================

**[1t]** rv.T Markup
------------------------------------------------

.. raw:: html

    <hr>

The *Tools* API function executes markup and scripts. 

**Format blocks of text**

========================================= ==============================
       Block Tags                           Description 
========================================= ==============================
 _[[PYTHON]] namespace                      :ref:`pythontag`
 _[[SCRIPT]] type                           :ref:`scripttag` [1]
 _[[END]]                                   :ref:`endblk`
========================================= ==============================

.. highlight:: none

::

    [1] LaTeX processing requires the installation of Texlive


**Read, write and format files**

============================================================== =====================
         | Command | path | parameters                          Description
============================================================== =====================
\| PDFAPPEND | relative path | place, cover                     :ref:`appcmd`   
\| PUBLISH | ini rel. path | type                               :ref:`pubcmd` 
============================================================== =====================

.. highlight:: none

::

    [1] optional tags number the equation or table
