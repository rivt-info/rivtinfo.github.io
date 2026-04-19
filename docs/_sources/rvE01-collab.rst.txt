**E.1 Collaboration**
=======================

**[1t]** Overview
--------------------

.. raw:: html

    <hr>

 There are several ways to collaborate on rivt and rivt files by building on
 the tools available in the Python and VSCode ecosystem.

#. :doc:`Public rivt files <rvE04-publicrivt>` may be shared by uploading them
    to repositories like *GitHub*.  Public *rivt files* can be found and 
    downloaded using the :doc:`search interface <rvE03-ghsearch>`. Public 
    rivt files may be improve by: 

    - forking to create different versions.
    - providing pull requests.
    - submitting issues and bugs.
  
    *Public rivt files* are identified with the naming convention
    rv-A01-filename.py, in contrast with rvA01-filename for an active, private
    files. After downloading a public rivt file, use the *Batch Rename*
    extension to delete the hyphen after *rv* and convert it to an active rivt
    file.

#.  Files may be collaboratively edited in real time using VSCode with the
    extension  `Visual Studio Live Share
    <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_.    


#. Contribute to rivtlib at `rivtlib-dev <https://github.com/rivtlib-dev/rivtlib>`_ 
   and documentation at `rivt-info <https://github.com/rivt-in>`_.
    
    - report issues and bugs
    - issue pull requests to propose changes
    - contribute to documentation

#. Contribute extensions and scripts that improve the interaction of 
   *rivt* with other components of the *rivt framework*.

**[2t]** Git and GitHub
---------------------------

.. raw:: html

    <hr>

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

**[3t]** VSCode
------------------

.. raw:: html

    <hr>

`VSCode <https://code.visualstudio.com/>`_ is an open source IDE with a large
set of extensions, including collaboration support. 
Collaboration is facilitated by the `Visual Studio Live Share
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
    :maxdepth: 3

    rvE02-git.rst
    rvE03-ghsearch.rst
    rvE04-publicrivt.rst