**C.9 Doc - rv.D**
===========================

**[1t]** rv.D Markup
-------------------------------------------

.. raw:: html

    <hr>

The *Doc API* publishes formatted *docs* from the rivt API strings.

**Format blocks of text**

======================================= ==============================
       Block Tags                        Description 
======================================= ==============================
 _[[META]] label                            :ref:`Meta block`
 _[[LAYOUT]] label                          :ref:`Layout block` 
======================================= ==============================

**Read, write and format files**

========================================================= ==================== 
        | Command | relative path | parameters                Description
========================================================= ==================== 
\| PDFATTACH | relative path | place, cover                :ref:`Attach PDF`   
\| PUBLISH | ini rel. path | type                          :ref:`Publish Doc`
========================================================= ==================== 
