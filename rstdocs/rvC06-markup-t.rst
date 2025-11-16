**C.6 Tool - rv.T**
=======================

Files processed by the *Tools API function* are read and written to the
*src/tools* folder unless the *rvsource* variable is set to *True* in the *Meta
API function*. In that case files are read and written to the *rivt file* folder.

**Summary**

======================================= ==============================
       Block Tags                        Description (doc scope)
======================================= ==============================
 _[[PYTHON]] label, *rv-space*;newspace  Python script (all)
 _[[LATEX]] label                        LaTeX markup (pdf)[1]
 _[[HTML]] label                         HTML markup (html)
 _[[END]]                                End block (all)
======================================= ==============================


======================================================== ===== =================
         | Command | path | parameters                    R/W   input types
======================================================== ===== =================
 \| PYTHON | relative path | *rv-namespace*; userspace    R     *py*
 \| HTML | relative path | *html*                         R     *html*
 \| LATEX | relative path | *pdf*                         R     *tex*
 \| RST | relative path | *pdf;html;both*                 R     *rst*
======================================================== ===== =================

[1] Values are usually defined in a block where the equation tag (_[E]) 
would not apply and will be disregarded.


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** _[[HTML]] : HTML code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[HTML]] pdf;nopdf
     code
     code
     ...
     _[[QUIT]]

If the parameter is pdf a PDF file is output. It may be added as a
source of the HTML *doc*. The file name is derived from the rivt doc and section
number.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** _[[LATEX]] : LaTeX code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LATEX]] description
    code
    code
    ...
    _[[QUIT]]

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** _[[PYTHON]] : Python code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
     
      _[[PYTHON]] *rv-namespace*; user namespace
      code
      code
      ...
      _[[QUIT]]

Executes Python script in the *rivt namespace* or a user specified namespace.
File paths are constucted relative to the *rivt file* folder.


outputs: text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** | RST | reStructuredText markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | RST | relative path | description

    | RST | src/tools/page1.rst | a sidebar

Reads *.rst* files and outputs PDF or HTML markup. The description is for author
reference only.

outputs: pdf, html


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** | HTML | HTML markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | HTML | relative path | *pdf;nopdf*

    | HTML | src/tools/page1.html | pdf

Reads .html and .htm files and outputs HTML markup. If the parameter is *pdf* a
separate PDF file is output from the formatted HTML and may be appended to a
PDF report. The file name is derived from the rivt doc and section number.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[6]** | LATEX | LaTeX markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | relative path | *pdf;nopdf*

    | LATEX | src/tools/page1.tex | nopdf

Reads .tex files. If the parameter is *pdf* a separate PDF file is output from
the formatted LaTeX and may be appended to an HTML report. The file name is
derived from the rivt doc and section number.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>



**[7]** | PYTHON | Python script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | SCRIPT | rel path | 
   
    | PYTHON | src/tools/script1.py | *rv-namespace*; user namespace

Executes Python code in the *rivt namespace* or user specified namespace. File
paths are constucted relative to the *rivt file* folder.

outputs: text, pdf, html