3. Markup
==================

The general syntax of a *rivt string* is text enclosed in triple quotes, where
the first line is a section header and subsequent lines are indented 4 spaces.

  
.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content (utf-8 text)
        ...
        
        """)

A *rivt string* is the argument to each of the 7 API functions. Each function
starts in column one and may define a *doc section*.

=============== =============== ===================================
API              Name             Purpose
=============== =============== ===================================
**rv.R(rs)**       Run               Run shell commands
**rv.I(rs)**       Insert            Insert static resources 
**rv.V(rs)**       Values            Calculate values
**rv.T(rs)**       Tools             Run Python functions
rv.D(rs)           Docs              Write docs 
rv.S(rs)           Skip              Skip section
rv.Q(rs)           Quit              Exit rivt 
=============== =============== ===================================

Text that is not a *tag* or *command* is passed to an intermediate .rst file
that is subsequently formatted to a PDF or HTML doc. This facilitates extending
*rivt markup* by embedding `restructuredText
<https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ commands in a
*rivt string*.


.. toctree::
    :maxdepth: 1
    :hidden:

    syntax.rst
    tagsl.rst
    tagsb.rst
    commands.rst
    quick.rst
    examples/example1.rst