
.. figure::  _static/img/riv-dark9e.png
    :class: dark-light
    :scale: 40 %
    :figwidth: image
    :align: center
    :alt: rivt logo


.. raw:: html

    <embed>
        <h1 style="font-size:2em; text-align:center"> rivt.info </h1>
        <hr width="100%" size="6" color="LightGrey" noshade>
    </embed>


rivt User Manual and API
------------------------

**rivtlib** is a Python `open source <https://opensource.org/license/mit/>`_
library for writing and publishing engineering documents using the **rivt**
markup language described here `rivt User Manual <https://rivt-doc.net>`_.
**rivt** is designed to simplify recombining and editing existing documents. The
following sections document the **rivtlib.py** code at `GitHub
<https://github.com/rivtlib/rivtlib.github.io/tree/main/src/rivtlib>`_

Engineering documents (e.g. calculations and drawings) are like road maps. Good
maps reduce the chance of getting lost or making wrong turns. Road maps only
need updates when new roads are built, not re-creation from scratch. Many
engineering technologies are changing slowly and assembling documents from
existing material saves time and reduces errors, compared to writing from
scratch.

**rivt** is designed for document sharing and reuse. In **rivt** it's easy to
edit and recombine arbitrary document components, including:

    - text
    - images
    - formulas
    - calculations
    - plots
    - data 

**rivt** allows engineers to explore more options, become familiar with
technologies, and find better solutions. The open source software model it
builds on encourages continuous, additive, improvements.

Engineering documents sometimes include confidential information. **rivt** can
designate specified inputs and outputs as private, and automatically generate
separate documents for private or "shared template" purposes.

Engineering document software is widely available but presents barriers to
sharing and reuse (see table). The barriers include high initial cost,
continuous upgrade costs, limited report formatting, limited version control,
and mutual incompatibility. Consequentially nearly identical engineering
documents are repeatedly written from scratch, simply because reusable
documents and templates are unavailable. **rivt** was developed to change this.

.. figure:: _static/img/table1.png
    :scale: 80 %
    :figwidth: image
    :align: left
    :alt: Comparative Table of Engineering Calculation Programs

**Comparative Table of Engineering Calculation Programs**


.. {toctree}::
    :maxdepth: 2
    :hidden:
    :caption: Write
    setup.md
    organize.md
    find.md

.. {toctree}::
    :maxdepth: 2
    :hidden:
    :caption: Publish
    docs
    github


.. {toctree}::
    :maxdepth: 2
    :hidden:
    :caption: Examples
    example1
    example2

.. {toctree}::
    :maxdepth: 2
    :hidden:
    :caption: FAQ
    faq
    terms
    changes



