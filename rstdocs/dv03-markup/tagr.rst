3.2 Tags in [R]un
===================

*line tags* format a line of text and are denoted with _[TAG], usually at the
end of the line. *Block tags* format a block of text that begin with _[[TAG]]
on the first line and end with _[[Q]] after the last line. 


**KEY**  
--------------------------------------------

_[TAG] : tag description
_[[TAG]] : tag description

.. raw:: html

    <hr>

.. topic::  syntax

    types of output


_[[WIN]] : batch commands
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[WIN]] *optional description*

   ::
    
     _[[WIN]]
     script
     script
     ...
     _[[Q]]

   text, pdf, html


_[[MACOS]] : shell commands
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[MACOS]] *optional description*

   ::
    
     _[[MACOS]]
     script
     script
     ...
     _[[Q]]

   text, pdf, html


_[[LINUX]] : shell commands
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[LINUX]] *optional description*

   ::
        
     _[[B]]
     script
     script
     ...
     _[[Q]]
 
   text, pdf, html
