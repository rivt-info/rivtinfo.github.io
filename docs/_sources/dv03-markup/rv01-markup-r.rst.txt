3.1  rv. **R** - Run
======================


**[01]** TAG KEY
----------------------------------

*Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 


_[[TAG]] : block tag description
        
.. raw:: html

    <hr>

.. topic::  syntax : description

  example

file types

.. raw:: html

    <hr>


**[02]** _[[WIN]] : batch
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


**[03]** _[[MACOS]] : shell
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


**[04]** _[[LINUX]] : shell 
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



**[05]** COMMAND KEY
----------------------

*Command* parameter options are separated with commas and parameter elements by
semicolons. Path names can be directly specified relative to the project
*source folder* or specified with an alias:

    *rvsource* : this alias directs *rivtlib* to look for the file in the
    default *source* folder. For example if the *rivt file* is in Division 1 and
    the API function is *Insert* the *i01* subfolder in the *source* folder is
    searched.

    *rvlocal* : this alias directs *rivtlib* to look for the file in the *rivt
    file* directory. It is used when a *single doc*, rather than a *report
    doc* is processed.

The *rivt report* folders are described 
:doc:`here. </dv04-reports/rv02-folders>`


.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

  example

file types



**[06]** | WIN | - command script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | WIN | relative path | filename

  | WIN | rvsource | file.cmd

reads .txt, .cmd, .bat  files


**[07]** | MACOS | - shell script
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | MACOS | relative path | filename  


  | MACOS | rvsource | file.sh

reads .sh files


**[08]** | LINUX | - shell script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LINUX | relative path | filename 

  | LINUX | rvsource | file.sh   

reads .sh files

