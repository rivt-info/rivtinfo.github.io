**C.8 Tool - rv.T**
=======================

**[1t]** rv.T Markup
------------------------------------------------

.. raw:: html

    <hr>

Files processed by the *Tools API function* are usually read and written to the
*src/* folder unless the *rv_localB* variable is set to *True* in the *Meta API
function*. In that case files are read and written to the *rivt file* folder.

**Format blocks of text**

========== ========================================= ==============================
API Scope         Block Tags                           Description 
========== ========================================= ==============================
rv.T        _[[PYTHON]] namespace                      :ref:`pythontag`
rv.T        _[[SCRIPT]] type                           :ref:`scripttag` [1]
all         _[[END]]                                   :ref:`endblk`
========== ========================================= ==============================

::

    [1] LaTeX processing requires the installation of *Texlive*


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
