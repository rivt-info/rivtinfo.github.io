6. Search
==========

This section provides a convenient search interface for **rivt** files
distributed across GitHub. It searches the full text of the **rivt** root
README file which contains the rivt report in text form. For advanced searching
the GitHub interface is `here <https://github.com/search>`_.

[S] Search GitHub (Ctrl+Enter)   [C] Clear input (Ctrl+R)

Example: **solar+steel+frame** is passed to GitHub as **rivt+solar+steel+frame**

.. raw:: html

    <head>
    
    <style>
    .button {
    background-color: #6f6968; border: 3 px solid white; color: white; padding: 4px 10px; 
    text-align: center; text-decoration: none; display: inline-block; font-size: 16px; 
    margin: 4px 2px; cursor: pointer;} </style>

    <script> 
    function searchRivt(){var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;
    window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});</script>

    <script> function searchOrg(){var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;
    window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});</script>

    <script> function clearRivt(){document.getElementById("terms").value="";
    document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 82) && e.ctrlKey){document.getElementById("clearBtn").click();}})};</script>
    
    </head>

    <button class="button" id="searchBtn" onclick="searchRivt()">S</button><button class="button" id="clearBtn" onclick="clearRivt()">C</button><input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal"><br>

    <hr>

Search within GitHub organizations (comma separated)

.. raw:: html    
    
    <input type="text" id="terms" name="terms" size=30 style="height:40px;font-size:14pt; font-weight: normal">

    <hr>

    Search Terms<br>
    <button class="button" id="searchBtn" onclick="searchOrg()">S</button> <button class="button" id="clearBtn" onclick="clearRivt()">C</button><input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal">



Definitions
===========

doc
---
the output file (document) after processing a rivt file

division
--------
open source markdown language for writing, organizing and sharing engineering documents

report
------
open source markdown language for writing, organizing and sharing engineering documents asdfasf sdflkjsadf sd fsaedlfk fsadlf sa

section 
-------
open source markdown language for writing, organizing and sharing engineering documents

open source editing and publishing framework for rivtlib Python library for processing 

rivtpub-*
---------
project folder containing private files not uploaded when sharing templates

rivt
----
open source markdown language for organizing, modifying and publishing
engineering documents

rivtlib
-------
Python library for processing **rivt** files. It outputs formatted documents in
a serveral different formats. 

rivtzip
-------
an editing and publishing framework for rivt using additional open source
programs. **rivt** works with both single file documents and extensive reports
with hundreds of files.

namespace
---------
a `name <https://en.wikipedia.org/wiki/Namespace>`_ that provides a scope for
functions, variables, etc. Namespaces are used to organize code into logical
groups and to prevent name collisions that can occur especially when your code
base includes multiple libraries. In Python, namespaces are defined by the
individual modules.
  
GitHub
------
version control

repo
----
short for repository


FAQ
===


Questions
---------

1.0 - aslkfas fdasdf asdflk sdfljk asdflk jasdlf sadf asdflk sdflkj sdflkj saf `A1.0`_  


2.0 - aslkfas fdasdf asdflk sdfljk asdflk jasdlf sadf asdflk sdflkj sdflkj saf `A2.0`_  


Answers
-------

.. _A1.0: 

the answer to question 1.0 


.. _A2.0: 

the answer to question 2.0 


