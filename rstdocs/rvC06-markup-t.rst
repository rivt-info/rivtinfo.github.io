**C.6 Tools - rv.T**
=======================

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
     
      _[[PYTHON]] rvnamespace; user-namespace
      code
      code
      ...
      _[[Q]]

Executable code is run and functions are stored. If the parameter is
*rvnamespace* the module is imported into the rivt file namespace.
Alternatively the module is imported into a user specified namespace.

Functions are evaluated using the "=" command in the Value API function.

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
        
    _[[LATEX]]
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

**[7]** | PYTHON | script and functions 
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PYTHON | relative path |  user-namespace; rvnamespace
   
    | PYTHON | src/tools/module.py | tool1

Imports .py files. Executable code is run and functions are stored. If the
parameter is *rvnamespace* the module is imported into the rivt file namespace.
Alternatively the module is imported into a user specified namespace.

Functions are evaluated using the "=" command in the Value API function.

outputs: text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[8]** | HTML | markup
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | HTML | relative path | pdf;nopdf, newpage;samepage

    | HTML | src/tools/page1.html | pdf, newpage

Reads .html, .htm files. If the parameter is "pdf" a PDF formatted file is
output. The file name is derived from the rivt doc and section number. It may
then be appended to a PDF *doc*. The page parameter specifies whether a new
page is started.

outputs: pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[9]** | RST | reStructuredText
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

**[10]** | LATEX | markup
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

**[11]** | QCAD | script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | QCAD | relative path | newpage;samepage

    | QCAD | relative path | newpage

reads .js file

outputs: pdf, html