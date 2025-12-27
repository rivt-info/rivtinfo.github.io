**C.5 Tool - rv.T**
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

**[2t]** _[[HTML]] : HTML markup
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[HTML]] label
     markup
     markup
     ...
     _[[QUIT]]

Inserts HTML into *doc*. 

outputs: text, pdf, html

**[3t]** _[[LATEX]] : LaTeX markup
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LATEX]] label
    markup
    markup
    ...
    _[[END]]


Inserts TeX into *doc*.  May require installation of LaTeX.

outputs: text, pdf, html

**[4t]** _[[RST]] : reStructuredText code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[RST]] label
    markup
    markup
    ...
    _[[END]]


Inserts TeX into *doc*.  May require installation of LaTeX.

outputs: text, pdf, html

**[5t]** _[[PYTHON]] : Python code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
     
      _[[PYTHON]] *rv-namespace*; user namespace
      code
      code
      ...
      _[[END]]

Executes Python script in the *rivt namespace* or a user specified namespace.
File paths in the script are relative to the *rivt file* folder.

outputs: text, pdf, html

**[6t]** | HTML | HTML markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | HTML | src/path | label

    | HTML | src/tools/page1.html | code excerpt

Reads and inserts .html and .htm files into *doc*. 

outputs: text, pdf, html

**[7t]** | LATEX | LaTeX markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | src/path | label

    | LATEX | src/tools/page1.tex | frame analysis

Reads and inserts .tex files into *doc*. May require installation of LaTeX.

outputs: text, pdf, html

**[8t]** | RST | reStructuredText markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | src/path | label

    | LATEX | src/tools/page1.tex | frame analysis

Reads and inserts .tex files into *doc*. May require installation of LaTeX.

outputs: text, pdf, html


**[9t]** | PYTHON | Python script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PYTHON | src/path | *rv-space*; user space
   
    | PYTHON | src/tools/script1.py | rv-space

Executes Python code in the *rivt namespace* or user specified namespace. File
paths used in the script are relative to the *rivt file* folder.

outputs: text, pdf, html