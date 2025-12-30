**C.9 Doc - rv.D**
===========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1t]** Summary
-------------------------------------------

.. raw:: html

    <hr>

The *Doc API* publishes formatted *docs* from the rivt API strings.

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
\| APPEND | relative path | *none*;title                        pdf, html, text
\| PREPEND | relative path | *none*;title                       pdf, html, text
\| PUBLISH | *rivt*; rel path | *rst2pdf;pdftex;html;text*       pdf, html, text
============================================================== ================= 




**[2t]** _[[LAYOUT]] :  format settings
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[LAYOUT]] optional label

    ::

        _[[LAYOUT]] 
        pdfheaderL = []
        foot_template:
        ...
        _[[QUIT]]

    The LAYOUT block overrides default style settings.

**[3t]** | APPEND  | - append PDF file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | APPEND | relative path | *none*;title

    | APPEND | src/appendix1.pdf | none

Appends file to *doc* with optional separator page.

outputs:  PDF, HTML, text

**[4t]** | PREPEND  | - prepend PDF file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | APPEND | relative path | *none*;title

    | APPEND | src/appendix1.pdf | none

Appends file to *doc* with optional separator page.

outputs:  PDF, HTML, text

**[5t]** | PUBLISH |  - write doc file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PUBLISH | *rst2pdf;texpd;text;html* | *none*;title

    | PUBLISH | doc1.pdf | none

*rivt* exits after writing the *publish* file.

outputs: PDF, HTML, text
  

