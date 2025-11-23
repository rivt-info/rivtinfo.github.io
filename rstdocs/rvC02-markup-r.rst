**C.2 Run API - rv.R**
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

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[2]** _[[WIN]] : batch commands
------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[WIN]] *nowait;wait*
  batch command
  batch command
  ...
   _[[Q]]

text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** _[[MACOS]] : shell commands
--------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[MACOS]] *nowait;wait*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** _[[LINUX]] : shell commands 
---------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *nowait;wait*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[5]** | WIN | - command script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | WIN | relative path | nowait;wait

  | WIN | src/run/file.cmd | nowait


reads .txt, .cmd, .bat  files

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[6]** | MACOS | - shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | relative path | nowait;wait

  | MACOS | src/run/file.cmd | nowait

reads .sh files

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[7]** | LINUX | - shell script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LINUX | relative path | nowait;wait

  | LINUX | src/run/file.cmd | nowait

reads .sh files

