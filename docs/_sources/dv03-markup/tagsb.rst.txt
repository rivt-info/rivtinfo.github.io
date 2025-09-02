**3.3** Block Tags
===================

**Block** tags format a block of text and are denoted with _[[TAG]] on the
first line and end with _[[Q]] after the last line. Tags have a function
and output scope.


**KEY**  
--------------------------------------------

_[[TAG]] : description

.. raw:: html

    <hr>

.. topic:: first line - block syntax 

    block example

    - function scope
    - applicable output

_[[V]] :  evaluate values
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[V]] *title*

    ::
        _[[V]] title
        value1
        value2
        ...
        _[[Q]]

    - rv.I, rv.V
    - text, pdf, html

_[[N]] :  indent
----------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[N]]

    ::
        _[[N]] title
        value1
        value2
        ...
        _[[Q]]

    - rv.I, rv.V
    - text, pdf, html

_[[T]] : topic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[T]] *topic*

    _[[N]] topic
    text
    text
    ...
    _[[Q]]

    - rv.I, rv.V
    - text, pdf, html

_[[I]] : indent italic
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[I]] 

    _[[I]]
    text
    text
    ...
    _[[Q]]

    - rv.I, rv.V
    - text, pdf, html

_[[B]] : indent bold
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[B]] 

    _[[B]]
    text
    text
    ...
    _[[Q]]

    - rv.I, rv.V
    - text, pdf, html

_[[C]] : code or literal
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[C]] *language*

    _[[C]]
    text
    text
    ...
    _[[Q]]

    - rv.I, rv.V
    - text, pdf, html

_[[L]] : LaTeX
------------------------------------------------

.. raw:: html

    <hr>

.. topic::  _[[L]] 
    _[[L]]
    text
    text
    ...
    _[[Q]]

    - rv.I, rv.V
    - text, pdf, html


  
    