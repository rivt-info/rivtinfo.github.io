**C.2 Metadata - rv.M**
===========================

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[1]** **Summary**
------------------------------------

.. raw:: html

    <hr>

The *Metadata* API function is the first *API function* if used. The function
provides *doc* metadata and overrides defaults. Metadata is specified using
Python dictionaries, lists and strings. It uses the convention (used in
rivtlib code) of a suffix indicating the data type.
    
============================= ===============================================
    Variable                        Description (doc scope)
============================= ===============================================
:term:`rv_authD`                specifies author information
:term:`rv_fork1D`               specifies author fork information
:term:`rv_localB`               true; false - specifies if a single doc
:term:`rv_docnameS`             overrides *doc* name taken from file name
:term:`rv_headerL`              ordered list of header content
============================= ===============================================

.. raw:: html

    <p id="api">&lt;m&gt;</p>


**[2]** Dictionaries
------------------------------------------------

*rv_authD* specifies the author, version, email, repository and license
information and lists the forks. *rv_forknD* specifies data for the forked
file. The *rv_authD* is always included.

.. raw:: html

    <hr>

..  code-block:: python

    # default - author dictionary
    rv_authD = {
            "authors": "",
            "version": "0.0.0",
            "email": "",
            "repo": "",
            "license": "https://opensource.org/license/mit/",
            "forks": ["", "", "", ""],
            }

    # example - author dicitionary
    rv_authD = {
            "authors": "rholland",
            "version": "0.6.1",
            "email": "rod.h.holland@gmail.com",
            "repo": "https://github.com/rivt-info/rivt-simple-doc",
            "license": "https://opensource.org/license/mit/",
            "forks": ["rv_fork1D", "", "", ""],
            }
    
    #example - fork dictionary
    rv_fork1D = {
            "authors": "",
            "version": "0.1.0",
            "email": "",
            "repo": "",
            }

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[3]** Lists
------------------------------------------------

.. raw:: html

    <hr>

*rv_headerL* specfies the contents and order of the doc per page heading.

..  code-block:: python

    # default - header list
    rv_headerL = ["date", "time", "file", "version"]
    
    # example - header list
    rv_headerL = ["date", "file", "authors", "version"]

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[4]** Variables
------------------------------------------------

.. raw:: html

    <hr>

*rv_localB* overrides the default report structure and specifies that the *values*
and *logs* files are written to the local rivt folder.

..  code-block:: python

     # default - folder setting
     rv_localB = false
     
     # example - folder setting override
     rv_localB = true

*rv_docnameS* overrides the default doc title derived from the rivt file name.

..  code-block:: python

    # default - doc name override
     rv_docnameS = "" # does not override default name
     
     # example - folder setting override
     rv_docnameS = "My Document Title"
