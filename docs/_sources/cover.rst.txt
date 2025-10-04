
.. figure::  _static/img/rivdark55c.png
    :class: dark-light
    :scale: 20 %
    :align: center
    :alt: rivt logo
    
.. raw:: html

    <p style="text-align: center; font-size: 1.5rem;">rivt</p>


.. raw:: html

    <br>
    <hr>


*rivt* is an open source Python project for writing and distributing
engineering documents. Documents are written in 
:doc:`rivt markup <dvC0-markup/rv01-markup>` within a Python file (.py).

A *rivt file* is a Python file that imports the package *rivtlib*. The
*rivtlib* API outputs a formatted *rivt doc* as text, HTML or PDF from the same
*rivt file*. The API also organizes *docs* into a *rivt report*. This site is
an example of an HTML report.

*rivt* also integrates well with other open source programs in a *rivt
framework*. The framework is described  :doc:`here. <dvA0-install/rv01-install>`

:doc:`This <dvA0-intro/rv05-smallex1>` is a small single *doc* example.
:doc:`This <dvA0-intro/rv06-smallex2>` is a small *report* example. A
search interface for discovering *rivt files* on is
:doc:`GitHub here <dvA0-collab/rv02-ghsearch>`.


.. raw:: html

    <hr>
    <br>

rivt User Manual
==================

.. toctree::
    :maxdepth: 1

    dvA0-intro/rv01-intro.rst
    dvB0-install/rv01-install.rst
    dvC0-markup/rv01-markup.rst
    dvD0-reports/rv01-reports.rst
    dvE0-collab/rv01-collab.rst
