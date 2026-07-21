**F.2 |** Conversion
=================================  

**[1]** Docs
-------------------------------------------------------------------------------


.. image:: _static/img/process2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: rivt flow chart 

.. rst-class:: center

    **rivt Doc Processing**

Each :term:`rivt file` outputs a corresponding :term:`doc` of the format
specified in PUBLISH command of the *rv.D()* API. A rivt file number has the
form:

.. code-block:: text

    rvAnn-filename.py

where rvAnn is a required file number prefix with A an alphanumeric character and nn a two
digit non-negative integer. Corresponding rivt docs are output as:

.. code-block:: text

    rvAnn-filename.txt, pdf or html

A *rivt report* is organized using the *file numbers*. The file numbers are
used to organize reports into divisions and subdivisions. Each *rivt file* or
*doc* is a report subdivision. If the *rivt filenames* are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

the corresponding *doc numbers* in a report would be: 

- A.1 (division A, subdivision 1)
- 1.5 (division 1, subdivision 5)
- 2.12 (division 2, subdivision 12)

