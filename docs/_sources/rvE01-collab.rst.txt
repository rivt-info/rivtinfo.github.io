**E.1 Collaboration**
=======================

**[1t]** Overview
--------------------

.. raw:: html

    <hr>

A primary motivation for *rivt* is to facilitate cooperative improvement of
files and docs, and a reduction of reptitive work. As a Python open source
project a number of tools are available to faciliate these goals. Cooperative
work and community improvements can happen in a number of ways including:


Contribute to rivtlib at `rivtlib-dev <https://github.com/rivtlib-dev/rivtlib>`_ 
and documentation at `rivt-info <https://github.com/rivt-in>`_

- report issues and bugs
- issue pull requests to propose changes
- contribute to documentation

Share and collaborate with others on rivt files of interest. Relevant projects
can be found using the search interface :doc:`here <rvE03-ghsearch>`.

- upload the *Public* rivt folder to public repositories such as *GitHub*
- fork rivt files to create new versions
- issue pull requests to propose changes
- report issues and bugs
- use an :term:`IDE` to edit code with others in real time

:doc:`Public rivt files</rvE02-publicrivt>` are written to the */Public*
folder which may be uploaded to a remote repository. *Public rivt
files* are re-identified with the naming convention rv-A01-filename.py, in
contrast with rvA01-filename for private files. After downloading a public rivt
file, use *Batch Rename* to delete the hyphen after *rv* and convert it to a
private rivt file.

The development platform *GitHub* and the IDE *VSCode* are external tools that
are part of the *rivt framework* and have collaboration features that work well
with *rivt files*.

**[2t]** Git and GitHub
------------------------

.. raw:: html

    <hr>

`Git <https://git-scm.com/>`_ is part of the *rivt framework*. It is a free,
open-source, distributed version control system designed to manage and track
changes in files. It allows multiple people to work on the same project
simultaneously without overwriting each other's work.

`GitHub <https://github.com/>`_ is also part of the *rivt framework*. It is a
web-based platform for hosting, managing, and collaborating on code built
around Git. It allows teams to work together efficiently on software projects
and provides features like pull requests, issue tracking, and project
management.

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

`VSCode <https://code.visualstudio.com/>`_ is an open source IDE with a 
large set of extensions, including collaboration support. 
CodeSpaces is a cloud based GitHub implementation of VSCode that shares 
many of the same features.

Collaboration in VS Code is primarily facilitated by the Visual Studio Live
Share extension. This extension enables:

- Real-time Co-editing: Multiple participants can work on the same file
  simultaneously, seeing each other's cursors, selections, and edits instantly,
  much like in Google Docs.

- Collaborative Debugging: Teams can debug together, inspecting variables,
  setting breakpoints, and stepping through code execution simultaneously, all
  within their own personalized environments.

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

    rvE02-publicrivt.rst
    rvE03-ghsearch.rst