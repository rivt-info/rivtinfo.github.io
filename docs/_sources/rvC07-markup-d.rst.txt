**C.7 Doc - rv.D**
===========================


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Summary
-------------------------------------------

.. raw:: html

    <hr>

The *Doc API* publishes formatted document files from rivt strings.
*Tags* are not used in this function.

======================================================================== === 
                  | Command | relative path | parameters                 
======================================================================== === 
\| APPEND | relative path | *none*;title;separatorfile      
\| PUBLISH | *pdf;pdftex;text;html* | *none*;title;coverfile   
======================================================================== === 

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** | APPEND  | - append PDF file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | APPEND | relative path | *none*;title;cover file 

    | APPEND | src/appendix1.pdf | none

Appends file to *doc* with optional separator page.

outputs:  PDF, HTML, text
 
.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** | PUBLISH |  - write doc file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | PUBLISH | *pdf;pdftex;text;html* | *none*;title;coverfile 

    | PUBLISH | doc1.pdf | none

*rivt* exits after writing the *publish* file.

outputs: PDF, HTML, text
  

