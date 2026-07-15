**B.3 | Frameworks**
=================================  

.. _rivt framework:

**[1]** rivt frameworks
-----------------------------------------------------------------------------

*rivt* interoperates with a large number of external programs that improve its
user interface and capabilities. The documented frameworks include
*rivt-code* and *rivt-framework*.

----------------------------------


**[2]** rivt-code and CodeSpaces
------------------------------------------------------------------------------

The *rivt-code* and *rivt-CodeSpaces* framework includes *VSCode* for editing 
and *git* for remote storage and version control. *rivt-code* is a local 
portable zip  :ref:`installation  <rivt-code>`. *rivt-CodeSpaces* is a cloud
based installation that may be forked into a personal GitHub repository.

======================= =====================================================
Purpose                    Link
======================= =====================================================
Editing                     `VSCode <https://code.visualstudio.com/>`_  
rivt Extensions             :ref:`vscode-settings`
Version Control             `Git <https://git-scm.com>`_
======================= =====================================================

---------------------------------


**[2]** VSCode and CodeSpaces
-----------------------------------------------------------------------------

`VSCode <https://code.visualstudio.com/>`_ is an open source IDE with a large
set of extensions, including collaboration support. Collaboration is 
facilitated by the `Visual Studio Live Share
<https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_. 
You can start a *Live Share* session either within *CodeSpaces* in 
your browser, or within the *VS Code* desktop application. *CodeSpaces* 
is a cloud based GitHub implementation of VSCode that shares many of the 
same features.

*GitHub Codespaces* is a VSCode cloud-based development environment connected
to GitHub files. It can be set up with *rivt extensions* that provide a complete
rivt editing and collaboration environment in the cloud.

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

---------------------------


**[3]** git
----------------------------------------------------------------------------

Git is a free, open-source distributed version control system designed to track
changes in source code during software development. It allows multiple
programmers to collaborate on the same project simultaneously without
overwriting each other's work. 

**Key Functions**

- Track changes: Records every modification made to a project's files over time.
- Revert history: Restores previous file versions easily if errors or bugs are 
  introduced.
- Enable collaboration: Merges independent updates from multiple team members 
  into a single codebase.
- Work offline: Provides each developer with a complete local copy of the full 
  project history.

**Essential Concepts**

- Repository (Repo): The tracking folder where your project files and their
  revision histories live.
- Commit: A permanent saved snapshot of your staged files at a specific point in
  time.Branch: An isolated environment used to develop new features without
  altering the stable main code.
- Merge: The automated process of combining changes from one branch back into
  another.

**Core Workflow**

The core workflow in a local or remote Git project transitions through four
distinct environments before saving:

- Working Directory: The actual files you are modifying on your computer.
- Staging Area: A temporary holding zone where you select and prepare changes
  for the next snapshot.
- Local Database: The final destination where commits are permanently saved to 
  your project history.
- Push: Copy local database to remote repository e.g. GitHub


---------------------------



**[4]** Extended framework
-----------------------------------------------------------------------------

The *rivt extended framework* includes the *rivt-code* and additional 
programs and libraries for formatting, drawing, diagramming and calculating.

======================= ==========================================================================
Purpose                  Link
======================= ==========================================================================
Additional Formatting     `LaTeX <https://www.tug.org/texlive/>`_
2D Drawing                `QCAD <https://qcad.org/en/85-new-community-edition-open-source>`_
3D Modeling               `FreeCad <https://www.freecad.org/>`_
Diagrams                  `Mermaid <https://mermaid.ai/open-source/intro/syntax-reference.html>`_
Program environment       `uv <https://docs.astral.sh/uv/>`_
======================= ==========================================================================
