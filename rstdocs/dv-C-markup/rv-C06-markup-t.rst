**C.6 Tools - rv.T**
=======================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** TAG KEY
--------------------------------------------

.. raw:: html

    <hr>

*Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 

_[[TAG]] : block tag description

.. raw:: html

    <hr>

.. topic::  syntax

    types of output


**[2]** _[[PYTHON]] : Python code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
     
      _[[PYTHON]] description
      code
      code
      ...
      _[[Q]]

text, pdf, html


**[3]** _[[RUBY]] : Ruby code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text 
        
     _[[RUBY]] description
     code
     code
     ...
     _[[Q]]
   
text, pdf, html



**[4]** _[[HTML]] : HTML code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
     _[[HTML]]
     code
     code
     ...
     _[[Q]]
   
    pdf, html


**[05]** _[[LATEX]] : LaTeX code
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
        
    _[[LATEX]]
    code
    code
    ...
    _[[Q]]

    pdf, html


**[06]** COMMAND KEY
----------------------

.. raw:: html

    <hr>

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

The *rivt report* folders are described :doc:`here. </dv-D-documents/rv-D02-folders>`


.. raw:: html

    <hr>


.. topic:: | COMMAND | parameters

  example

file types



**[07]** | PYTHON | functions 
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | PYTHON | path | filename

   reads .py files


**[08]** | HTML | markup
-------------------------------------------

.. raw:: html

    <hr>


.. topic:: | HTML | path | filename  

   reads .html files


**[09]** | LATEX | code
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | LATEX | path | filename 

   reads .tex file


**[10]** | QCAD | script
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: | QCAD | path | filename 

   reads .js file