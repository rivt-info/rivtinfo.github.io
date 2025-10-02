
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
:doc:`rivt markup <dv03-markup/rv0300-markup>` within a Python file (.py).

A *rivt file* is a Python file that imports the package *rivtlib*. The
*rivtlib* API outputs a formatted *rivt doc* as text, HTML or PDF from the same
*rivt file*. The API also organizes *docs* into a *rivt report*. This site is
an example of an HTML report.

*rivt* also integrates well with other open source programs in a *rivt
framework*. The framework is described 
:doc:`here. <dv02-install/rv0200-install>`

:doc:`This <dv01-intro/rv0105-smallex1>` is a small single *doc* example.
:doc:`This <dv01-intro/rv0106-smallex2>` is a small *report* example. A
search interface for discovering *rivt files* on 
:doc:`GitHub is here <dv05-collab/rv0502-ghsearch>`.


.. raw:: html

    <hr>
    <br>

rivt User Manual
==================

.. toctree::
    :maxdepth: 1

    dv01-intro/rv0100-intro.rst
    dv02-install/rv0200-install.rst
    dv03-markup/rv0300-markup.rst
    dv04-reports/rv0400-reports.rst
    dv05-collab/rv0500-collab.rst
