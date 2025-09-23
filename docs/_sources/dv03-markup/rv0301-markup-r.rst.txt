3.1  **rv.R** - Run
======================

**TAG KEY**  
----------------------------------

_[[TAG]] : block tag description
        
.. raw:: html

    <hr>

.. topic::  syntax : description

  example

file types


**COMMAND KEY**  
------------------

.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

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
-----------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *optional description*
  shell command
  shell command
  ...
   _[[Q]]

  text, pdf, html



**[04]** | WIN | - command script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | WIN | path | filename

   reads .txt, .cmd, .bat  files

**[05]** | MACOS | - shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | path | filename  

   reads .sh files

**[06]** | LINUX | - shell script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LINUX | path | filename 

   reads .sh files

