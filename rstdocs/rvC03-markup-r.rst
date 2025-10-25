**C.3 Run - rv.R**
==========================

Only block tags are used in *rv.R*.

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** TAG KEY
----------------------------------

.. raw:: html

    <hr>


_[[TAG]] : :term:`block tag` description
        
.. raw:: html

    <hr>

.. topic::  syntax : description

  example

file types

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

**[5]** COMMAND KEY
----------------------

.. raw:: html

    <hr>

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[#]** | Command | : description


.. raw:: html

    <hr>


.. topic:: | COMMAND | relative path | parameters

  example

file types

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[6]** | WIN | - command script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | WIN | relative path | nowait;wait

  | WIN | src/run/file.cmd | nowait




reads .txt, .cmd, .bat  files

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[7]** | MACOS | - shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | relative path | nowait;wait

  | MACOS | src/run/file.cmd | nowait

reads .sh files

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[8]** | LINUX | - shell script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LINUX | relative path | nowait;wait

  | LINUX | src/run/file.cmd | nowait

reads .sh files

