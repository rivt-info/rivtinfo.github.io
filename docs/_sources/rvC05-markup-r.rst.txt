**C.5 Run - rv.R**
==========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** Summary
------------------------------------

.. raw:: html

    <hr>


The *Run* API function executes shell commands.

======================================= ==============================
       Block Tags                        Description (doc scope)
======================================= ==============================
 _[[WIN]] label, *wait;nowait*           Windows command script (all)
 _[[MACOS]] label, *wait;nowait*         Mac shell script (all)
 _[[LINUX]] label, *wait;nowait*         Linux shell script (all)
======================================= ==============================

============================================= ===== ==================
        | COMMAND | path | parameters          R/W     input types
============================================= ===== ==================
 \| LINUX | path | *wait;nowait*                 R     *.sh*
 \| MACOS | path | *wait;nowait*                 R     *.sh*
 \| WIN   | path | *wait;nowait*                 R     *.bat, .cmd*
============================================= ===== ==================




