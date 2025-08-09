**API**
========


A **rivt** file is a text file (.py) that imports the **rivtlib** api:: 

    import rivtlib.api as rv

which exposes 6 API functions ::

    rv.R(rS) - (Run) Run shell scripts 
    rv.I(rS) - (Insert) Insert text, images, tables and math equations 
    rv.V(rS) - (Values) Evaluate tables and equations 
    rv.T(rS) - (Tools) Execute Python functions 
    rv.D(rS) - (Write) Write formatted rivt documents 
    rv.X(rS) - (eXclude) Skip rivt-string processing (interactive editing) 
    rv.Q()   - (Quit) Stop file processing (interactive editing)    




- A **rivt file** is a text file (.py) that imports the **rivtlib** package.

- A **rivt doc** (document) is a text, HTML or PDF file output of a **rivt** file. 

- A **rivt report** is a collated collection of **rivt docs**.

- **rivtlib** is a `Python library <https://rivtlib.net>`_ that generates **rivt docs** and **reports** from a **rivt** file.

- **rivtedit** is a an open source editing and publishing framework built around `VScode <https://vscode.com>`_.

- **rivtzip** is a portable, single folder version of **rivtedit**.