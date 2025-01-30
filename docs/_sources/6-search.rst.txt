6. Search
==========

This page provides a convenient search interface for **rivt** files distributed
across GitHub.  The search covers the full text in the **rivt** root README
file, which typically contains the full rivt report. For advanced searching use
the GitHub search interface `here <https://github.com/search>`_.

[S] Search GitHub (Ctrl+Enter)

[C] Clear input (Ctrl+R)

Search GitHub
-------------

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



Search GitHub Organizations
---------------------------

Organizations (comma separated)

.. raw:: html    
    
    <input type="text" id="terms" name="terms" size=30 style="height:40px;font-size:14pt; font-weight: normal">

    <hr>

    Search Terms<br>
    <button class="button" id="searchBtn" onclick="searchOrg()">S</button> <button class="button" id="clearBtn" onclick="clearRivt()">C</button><input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal">



GitHub
======

The primary purpose of GitHub is to facilitate the version control and issue
tracking aspects of software development. Labels, milestones, responsibility
assignment, and a search engine are available for issue tracking. For version
control, Git (and, by extension, GitHub) allows pull requests to propose changes
to the source code. Users who can review the proposed changes can see a diff
between the requested changes and approve them. In Git terminology, this action
is called "committing" and one instance of it is a "commit." A history of all
commits is kept and can be viewed at a later time.


Features
--------

GitHub supports the following formats and features:

- Documentation,including automatically rendered README files in a variety of
  Markdown-like file formats (see README § On GitHub)

- Pages, a static web hosting service for blogs, project documentation,
  and books.

- Wikis, with some repositories consisting solely of wiki content. These
  include curated lists of recommended software which have become known as
  awesome lists.

- GitHub Actions, which allows building continuous integration and
  continuous deployment pipelines for testing, releasing and deploying software
  without the use of third-party websites/platforms

- GitHub Codespaces, an online IDE providing users with a virtual machine
  intended to be a work environment to build and test code

- Graphs: pulse, contributors, commits, code frequency, punch card, network,
  members

- Email notifications

- Discussions

- Nested task-lists within files

- Visualization of geospatial data

- image preview in many formats

- Security Alerts of known Common Vulnerabilities and Exposures in different
  packages

- GitHub's Terms of Service do not require public software projects hosted on
  GitHub to meet the Open Source Definition. The terms of service state, "By
  setting your repositories to be viewed publicly, you agree to allow others to
  view and fork your repositories."


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


