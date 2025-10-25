**C.7 Doc - rv.D**
===========================

The *Doc API function* writes formatted document files from rivt strings. Tags
are not used in this function. 

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** KEY  
-------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | path | parameters

    example 

output types


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** | APPEND  | - append PDF file
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | APPEND | relative path | *before;after*


    | APPEND | src/appendix1.pdf | after

Appends PDF file to PDF *doc*. The *before* parameter may be used for cover
pages.

outputs:  PDF
 
.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[3]** | PUBLISH |  - write doc file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | DOCS | relative path |  *txt;html;pdf;tpdf*


    | PUBLISH | /reports | pdf

The     *rivt* exits after writing the *doc* file.


outputs: PDF, HTML, text
  

