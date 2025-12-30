**C.8 Tool - rv.T**
=======================

**[1t]** Summary
------------------------------------------------

.. raw:: html

    <hr>

Files processed by the *Tools API function* are usually read and written to the
*src/* folder unless the *rv_localB* variable is set to *True* in the *Meta API
function*. In that case files are read and written to the *rivt file* folder.

======================================== ==============================
       Block Tags                         Description (doc scope)
======================================== ==============================
 _[[HTML]] label                          HTML markup (html)
 _[[LATEX]] label                         LaTeX markup (pdf)[1]
 _[[RST]] label                           reStructuredText markup (all)
 _[[PYTHON]] label, *rv-space*;newspace   Python script (all)
 _[[END]]                                 End block (all)
======================================== ==============================

[1] LaTeX requires an installation of LaTeX.

=================================================== ===== =================
        | Command | path | parameters                R/W     input types
=================================================== ===== =================
 \| HTML | src/path | label                           R     *html*
 \| LATEX | src/path | label                          R     *tex*
 \| RST | src/path | label                            R     *rst*
 \| PYTHON | src/path | *rv-namespace*; userspace     R     *py*
=================================================== ===== =================

