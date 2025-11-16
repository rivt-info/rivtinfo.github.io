**C.3 Run API - rv.R**
==========================

**Summary**

======================================= ==============================
       Block Tags                        Description (doc scope)
======================================= ==============================
 _[[AUTH]] label                         author data (all)
 _[[WIN]] label, *wait;nowait*           Windows command script (all)
 _[[MACOS]] label, *wait;nowait*         Mac shell script (all)
 _[[LINUX]] label, *wait;nowait*         Linux shell script (all)
======================================= ==============================

======================================================== ===== ==================
         | Command | path | parameters                    R/W   input types
======================================================== ===== ==================
 \| LINUX | relative path | *wait;nowait*                 R     *.sh*
 \| MACOS | relative path | *wait;nowait*                 R     *.sh*
 \| WIN   | relative path | *wait;nowait*                 R     *.bat, .cmd*
======================================================== ===== ==================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** **Block Tags**
------------------------------------

.. raw:: html

    <hr>

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[2]** _[[WIN]] : batch commands
------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[WIN]] *nowait;waiting*
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
    
  _[[MACOS]] *nowait;waiting*
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
    
  _[[LINUX]] *nowait;waiting*
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

