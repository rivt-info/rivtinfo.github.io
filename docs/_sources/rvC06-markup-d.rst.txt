**C.7 Doc - rv.D**
===========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Summary
-------------------------------------------

.. raw:: html

    <hr>

The *Doc API* publishes formatted document files from rivt API strings.

**Block Tags**

======================================= ==============================
       Block Tags                        Description (doc scope)
======================================= ==============================
 _[[LAYOUT]] label                       Doc format settings (all)
 _[[END]]                                End block (all)
======================================= ==============================

**Commands**

============================================================== ================= 
        | Command | relative path | parameters                   doc types
============================================================== ================= 
\| APPEND | relative path | *none*;title;separatorfile          pdf, html, text
\| PUBLISH | *pdf;pdftex;html;text* | *none*;title;coverfile    pdf, html, text
============================================================== ================= 

**[2]** _[[INDENT]] : indent text
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[LAYOUT]] label

    ::

        _[[LAYOUT]] 4
        head_template: 
        foot_template:
        ...
        _[[QUIT]]

    The LAYOUT block overrides default style settings.

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** | APPEND  | - append PDF file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | APPEND | relative path | *none*;title;cover file 

    | APPEND | src/appendix1.pdf | none

Appends file to *doc* with optional separator page.

outputs:  PDF, HTML, text
 
.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** | PUBLISH |  - write doc file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PUBLISH | *pdf;pdftex;text;html* | *none*;title;coverfile 

    | PUBLISH | doc1.pdf | none

*rivt* exits after writing the *publish* file.

outputs: PDF, HTML, text
  

