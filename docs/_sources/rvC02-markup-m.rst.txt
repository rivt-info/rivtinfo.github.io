**C.2 Metadata - rv.M**
===========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>


**[1]** Definitions
--------------------------------------------

.. raw:: html

    <hr>

If the *Metadata* function is used, it must be the first function in the rivt
file. The function provides *rivt metadata* for processing a *doc* and
overriding defaults. Metadata is specified in the form of pre-defined Python
dictionaries, lists and variables. Other text in this section is ignored.

.. raw:: html

    <p id="api">&lt;m&gt;</p>

**[2]** Dictionaries
------------------------------------------------

.. raw:: html

    <hr>

*rv_authD* provides information about the document itself.

..  code-block:: python

    # default
    rv_authD = {
            "authors": "",
            "version": "0.0.",
            "email": "",
            "repo": "",
            "license": "https://opensource.org/license/mit/",
            "fork1": ["", "", "", ""],
            }

    # example
    rv_authD = {
            "authors": "rholland",
            "version": "0.6.1",
            "email": "rod.h.holland@gmail.com",
            "repo": "https://github.com/rivt-info/rivt-simple-single-doc",
            "license": "https://opensource.org/license/mit/",
            "fork1": ["", "", "", ""],
            }


.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** Lists
------------------------------------------------

*r*v_headerL* specfies the contents and order of the doc header.

.. raw:: html

    <hr>

..  code-block:: python

    # default
    rv_headerL = ["date", "time", "file", "version"]
    
    #example
    rv_headerL = ["date", "time", "file", "version"]

**[3]** Variables
------------------------------------------------

*rv_localB* overrides the default report structure and specifies that *values*
and *logs* are written to the local rivt file.

.. raw:: html

    <hr>

..  code-block:: python

     # default
     rv_localB = true
     
     # example
     rv_localB = false


