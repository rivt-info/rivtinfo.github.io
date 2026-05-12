**E.1 Collaboration**
=======================

**[1]** Overview
--------------------

 

There are several ways to collaborate on *rivt files* by using
tools available in the Python, GitHub and VSCode ecosystem.

#. :doc:`Public rivt files <rvE02-publicrivt>` 
   may be shared by uploading them to repositories e.g. *GitHub*.  
   Public *rivt files* can be found and downloaded using the 
   :doc:`search interface <rvE04-ghsearch>`.  *Public rivt files* are 
   identified with the naming convention
  
   .. code-block:: bash

      rv-DocNumber-filename.py

   where the doc name and number are the doc number of the corresponding *doc* e.g.
   with an added hypen prefix. The file is writtnen to the *_shared* folder. 
   This is in contrast with the form: 
  
   .. code-block:: bash

      rvDocNumber-filename.py 
  
   for active, private files stored in the report root directory. After
   downloading shared rivt files, use a *batch rename* extension or utility
   to delete the hyphen and convert it to an active rivt file form. *Public rivt
   files* may be collaboratively improved by:
    
   - forking to create different versions.
   - providing pull requests.
   - submitting issues and bugs.

#. Contributions to rivtlib at `rivtlib-dev <https://github.com/rivtlib-dev/rivtlib>`_ 
   and documentation at `rivt-info <https://github.com/rivt-in>`_ in the from of;
    
   - report issues and bugs
   - issue pull requests to propose changes
   - improved documentation

#. Contributioons to extensions and scripts that improve the interaction of 
   *rivt* with other components in the *rivt framework*.

#.  Collaborative editing in *VSCode* using `Visual Studio Live Share
    <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_.    

**[2]** Open Models
---------------------------

 

The web site `OpenModels.info <https://www.openmodels.info/>`__ is a
*Google Drive* repository of open source engineernig model files, including
*rivt files* and *reports*.

**[3]** Git and GitHub
---------------------------

 

`Git <https://git-scm.com/>`_ and `GitHub <https://github.com/>`_ are part of
the *rivt framework*. *Git* is a free, open-source, distributed version control
system designed to manage and track changes in files. It allows multiple people
to work on the same project simultaneously without overwriting each other's
work. *GitHub* is a web-based platform for hosting, managing, and collaborating
on code built around Git. It allows teams to work together efficiently on
software projects and provides features like pull requests, issue tracking, and
project management.

Each *rivt project* is typically stored in its own repository. Every user of
GitHub has a personal account with essentially unlimited repositories.Free
accounts provide for:

- Unlimited Repositories: You can create as many public and private
  repositories as you need.

- Unlimited Collaborators: There is no limit to the number of people you can
  work with on your repositories.

- Community Support: You have access to the GitHub Community Discussions for help.

- Core Services with Usage Limits: The free plan includes a certain amount of
  monthly usage for services:

  + GitHub Actions: 2,000 minutes per month for private repositories 
      (unlimited for public repositories). 
  
  + GitHub Codespaces: 120 core hours and 15 GB of storage per month.

*GitHub Codespaces* is a VSCode cloud-based development environment connected
to GitHub files. It can be set up with *rivt extensions* that provide a complete
rivt editing and collaboration environment in the cloud.

**[4]** VSCode
------------------

 

`VSCode <https://code.visualstudio.com/>`_ is an open source IDE with a large
set of extensions, including collaboration support. Collaboration is 
facilitated by the `Visual Studio Live Share
<https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_. 
You can start a *Live Share* session either within *CodeSpaces* in 
your browser, or within the *VS Code* desktop application. *CodeSpaces* 
is a cloud based GitHub implementation of VSCode that shares many of the 
same features.

The *Live Share* extension enables:

- Real-time Co-editing: Multiple participants can work on the same file
  simultaneously, seeing each other's cursors, selections, and edits instantly,
  much like in Google Docs..

- Shared Terminals and Servers: The host can share their terminal and localhost
  servers with guests, eliminating the need for guests to set up their own
  environments or dependencies.

- Navigation and Following: Participants can independently navigate the project
  or choose to "follow" another collaborator, keeping their editor synchronized
  with the leader's actions.

- File Access Control: Hosts can use a .vsls.json file to control which files and
  folders are visible or editable by guests, ensuring security and focus

.. toctree::
    :maxdepth: 1
    :hidden:

    rvE02-publicrivt.rst
    rvE03-git.rst
    rvE04-ghsearch.rst
