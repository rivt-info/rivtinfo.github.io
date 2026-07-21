**E.3 | Cloud Storage**
===================================

**[1]** General Considerations
----------------------------------------

A typical *rivt report folder* is about 50 to 100 MB in size, depending on the
formats used and resources stored. Folders can be stored locally or in the
cloud. The preferred storage location depends on the purpose.
The simplest location is local storage. It does not require and internet
connection.Other options include remote repositories and file based cloud
storage.

-------------------------------  


**[2]** Remote Repositories
----------------------------------------

A remote repository stores a version of the rivt project files and version
history hosted on a server or online network (like GitHub, GitLab, or
Bitbucket) rather than on your local computer. It acts as a central hub for
team collaboration and an off-site backup.

GitHub is the repository for rivtlib and related code. See 
`rivtlib.dev <https://github.com/rivtlib-dev>`__ and
`rivtlib.info <https://github.com/rivtlib-info>`.

Repositories usually include local files managed by a tool like which are synced to a cloud based
host. The local files should not be stored on folders that are also synced to
other file based cloud storage services. This leads to potential conflicts
between the syncing services.

One approach to avoid this conflict is to independently synchronize the local
files to a file based cloud storage folder using a synchronization utility. File
management tools like *git* only sync when invoked, not as a background process.

*GitHub* is a popular and widely used cloud and version control system 
based on the :term:`Git` program that may be downloaded
`here <https://git-scm.com/>`__. `Git <https://git-scm.com/>` is part of
*rivt-code*. It is a free, open-source, distributed version control
system designed to manage and track changes in files. It allows multiple people
to work on the same project simultaneously without overwriting each other's
work. *GitHub* is a web-based platform for hosting, managing, and collaborating
on code built around Git. It allows teams to work together efficiently on
software projects and provides features like pull requests, issue tracking, and
project management.

Each *rivt folder* is typically stored in its own repository. Every user of
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

-------------------------------   


**[3]** File Based Cloud Storage
--------------------------------

File base cloud storage is convenient for storing and sharing *rivt folders*.
Public *rivt files* may be downloaded from 
`Google Drive. <https://www.openmodels.info>`__


**Summary of File Based Cloud Storage**

- Microsoft OneDrive: Best for Windows and Microsoft 365 users, featuring
  strong collaborative editing and deep OS integration.

- Google Drive: The go-to for Google Workspace users, offering seamless sharing
  and heavy-duty data workloads.

- iCloud: The standard choice for Apple device owners, syncing photos,
  documents, and backups across all iOS and macOS devices.

- Dropbox: Ideal for remote teams and general file synchronization across
  multiple platforms.

- pCloud: Highly rated for media storage and video streaming, offering unique
  lifetime payment plans.

- Proton Drive: Based in Switzerland, this is the top pick for a
  privacy-focused ecosystem with end-to-end encryption.

- IDrive: Comprehensive online backup that supports external hard drives and
  disaster recovery.

- Box: Geared toward enterprise businesses with advanced security, compliance
  tracking, and administrative controls.

- MEGA: A great option if you need a generous free tier or highly affordable
  massive storage capacities.