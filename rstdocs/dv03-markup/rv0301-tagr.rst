3.1 Tags in [R]un
===================

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 


**KEY**  
--------------------------------------------

_[TAG] : line tag description

_[[TAG]] : block tag description

.. raw:: html

    <hr>

.. topic::  syntax

    types of output


**[01]** _[[WIN]] : batch
------------------------------------------------

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
------------------------------------------------

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
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *optional description*
  shell command
  shell command
  ...
   _[[Q]]

  text, pdf, html
