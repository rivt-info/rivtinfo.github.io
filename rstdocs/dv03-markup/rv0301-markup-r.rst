3.1  rv. **R** - Run
======================

**[01]** TAG KEY
----------------------------------

_[[TAG]] : block tag description
        
.. raw:: html

    <hr>

.. topic::  syntax : description

  example

file types



**[01]** _[[WIN]] : batch
------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[WIN]] *optional description*
  batch command
  batch command
  ...
   _[[Q]]

text, pdf, html


**[02]** _[[MACOS]] : shell
--------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[MACOS]] *optional description*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html


**[03]** _[[LINUX]] : shell 
---------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *optional description*
  shell command
  shell command
  ...
   _[[Q]]

text, pdf, html



**[04]** COMMAND KEY
----------------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

  example

file types



**[05]** | WIN | - command script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | WIN | path | filename

  | WIN | rvsource | file.cmd

reads .txt, .cmd, .bat  files


**[06]** | MACOS | - shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | path | filename  


  | MACOS | rvsource | file.sh

reads .sh files


**[07]** | LINUX | - shell script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LINUX | path | filename 

  | LINUX | rvsource | file.sh   

reads .sh files

