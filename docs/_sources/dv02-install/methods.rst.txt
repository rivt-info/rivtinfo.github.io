2.1. Install Methods
======================

[ 1 ] - Framework Installation
--------------------------------

The basic rivt framweork includes:

- *VSCode* with extensions for document editing, processing and collaborating

- *Python* and libraries for analysis and formatting

- *Git* and GitHub for version control

The extended rivt framework includes:

- *Latex* for highly controlled typesetting

- *QCAD* for diagramming

The rivt framework may be installed in three ways: as a uv managed install, as
a portable zip file and as a system install. Each method has its advantages.

[ 2 ] - uv install 
--------------------

uv managed installation in a virtual, isolated environment. 


[ 3 ] - Zip install
----------------------

a portable (frozen) installation of the rivt framework from a single file 
that can be run from a USB drive or any folder on your computer. 


[ 4 ] - System install
-------------------------

a system-wide installation using open source installers for each 
component of the framework.


rivtlib is generally run in an IDE. If run from the command line the command
takes one of two forms depending on whether the file is part of a report. If
part of a report the form is:

    python -m rivtlib rddnn-filename.py

where *rvddnn-* is the doc number and *dd* and *nn* are integers identifying the
report division and subdivision respectively. Resource files need to be in the 
standard folders. If the file is a standalone document, and not part of a larger 
report, then resource files are assumed to be in the current folder or subfolder 
and the command is:

    python -m rivtlib filename.py

In this case output files will also be in the current file folder. See e **rivt
User Manual** at https://rivt.info for details.








