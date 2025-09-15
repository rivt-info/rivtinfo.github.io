3.5 Tags in [T]ools
=====================

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


_[[PYTHON]] : Python code
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


_[[RUBY]] : Ruby code
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



_[[HTML]] : HTML code
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


_[[LATEX]] : LaTeX code
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