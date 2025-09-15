3.2 Tags in [R]un
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


_[[WIN]] : batch commands
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[WIN]] *optional description*
  script
  script
  ...
   _[[Q]]

text, pdf, html


_[[MACOS]] : shell commands
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[MACOS]] *optional description*
  script
  script
  ...
   _[[Q]]

text, pdf, html


_[[LINUX]] : shell commands
------------------------------------------------

.. raw:: html

    <hr>

.. code-block:: text
    
  _[[LINUX]] *optional description*
  script
  script
  ...
   _[[Q]]

text, pdf, html
