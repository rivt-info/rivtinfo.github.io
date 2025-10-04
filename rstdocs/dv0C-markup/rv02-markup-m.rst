**C.2 rv.M - Meta Data**
===========================


**[1]** TAG KEY  
--------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

*Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 

_[[TAG]] : block tag description

.. raw:: html

    <hr>

.. topic::  tag

   syntax

types of output


**[2]** _[[AUTH]] : Author 
------------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

.. code-block:: text
     
    _[[AUTH]] Authors
    authors: Sarah, Jon
    version: 0.3.1
    email: sarah@email.com, jon@email.com
    repo: github.com/jonstuff/rivt-example
    license: https://opensource.org/license/mit/ 
    _[[Q]]

text, pdf, html

**[3]** _[[FORK]] : Contributor 
------------------------------------------------

.. raw:: html

    <hr>
    <p style="text-align: right;"> &lt;i&gt; </p>

.. code-block:: text

    _[[FORK]] Contributor 1
    contribs: Lisa
    version: 0.0.4
    email: lisa@email.com
    repo: github.com/lisastuff/rivt-files
    license: https://opensource.org/license/mit/ 
    _[[Q]]

text, pdf, html

