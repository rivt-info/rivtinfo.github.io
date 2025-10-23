**C.6 Tools - rv.T**
=======================

Files processed by the *Tools API function* are read and written to the
*src/tools* folder unless the *rvsource* variable is set to *True* in the *Meta
API function*.

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** TAG KEY
--------------------------------------------

.. raw:: html

    <hr>

_[[TAG]] : block tag description

.. raw:: html

    <hr>

.. topic::  syntax

    example

output types


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** _[[PYTHON]] : Python code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
     
      _[[PYTHON]] wait;nowait
      code
      code
      ...
      _[[Q]]

Executes Python script in the *rivt namespace*. If the parameter is *wait* the
*rivt file* waits for the script to complete. If the parameter is *nowait*
execution continues without waiting.

outputs: text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** _[[RST]] : reStructuredText code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text 
        
     _[[RST]] description
     code
     code
     ...
     _[[Q]]
   
outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** _[[HTML]] : HTML code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[HTML]] pdf;nopdf
     code
     code
     ...
     _[[Q]]

If the parameter is "pdf" a PDF formatted file is output. The file name is
derived from the rivt doc and section number. It may then be appended to a PDF
*doc*.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[5]** _[[LATEX]] : LaTeX code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LATEX]] description
    code
    code
    ...
    _[[Q]]

pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[6]** COMMAND KEY
----------------------

.. raw:: html

    <hr>

.. topic:: | COMMAND | parameters

    example

output file types


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[7]** | HTML | markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | HTML | relative path | pdf;nopdf

    | HTML | src/tools/page1.html | pdf

Reads .html and .htm files. If the parameter is "pdf" a PDF formatted file is
output. The file name is derived from the rivt doc and section number. It may
then be appended to a PDF *doc*. The page parameter specifies whether a new
page is started.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[8]** | RST | reStructuredText
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | RST | relative path | newpage;samepage

    | RST | src/tools/page1.rst | samepage

Reads .rst files. The file name is derived from the rivt doc and section
number.  The page parameter specifies whether a new page is started.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[9]** | LATEX | markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | relative path | newpage;samepage

    | LATEX | src/tools/page1.tex | newpage

Reads .tex files. The file name is derived from the rivt doc and section
number.  The page parameter specifies whether a new page is started.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[10]** | QCAD | script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | QCAD | relative path | newpage;samepage

    | QCAD | relative path | newpage

reads .js file

outputs: pdf, html