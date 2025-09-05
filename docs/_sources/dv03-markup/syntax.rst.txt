3.1 Syntax
================

[01] Overview
--------------

The basic syntax of a *rivt string* is utf-8 characters preceded by a header.
Character strings that are not tags or commands are passed, unchanged, to an
intermediate .rst file. This allows for restructuredText commands to be
embedded in a *rivt string* for formatting PDF and HTML docs. Most
restructuredText syntax is stripped out when a *text doc* is written.


[02] Header 
--------------

The first line of a *rivt-string* is a header that specifies a section label
and two formatting parameters. If the section label is preceeded by two
dashes (--) a new section is not created and the section content is merged with the
prior section.
  
.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content
        ...
        
        """)

The parameters specifiy whether the section contents are formatted and output
to docs and whether the section is written to a public rivt file.


New sections may be labeled as separate or
integrated with preceding sections. The section body can contain any utf-8
text. Commands and tags applicable to each function are defined
[here](#commands) and [here](#tags).

.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content
        ...
        
        """)


[03] Section Content
----------------------

**rivt** syntax includes **COMMANDS** for file operations and **TAGS** for text
formatting. Any text not defined by commands or tags is passed through as
`restructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`

**rivt markup**  wraps and extends restructured text markup. It adds two
additional markup elements - tags and commands - and provide simplified
backend and default settings for writing the same rivt file as different
document types (text, PDF and HTML).

API functions start in column one. rivt-strings are indented four spaces (for
legibility and code folding).A rivt doc is assembled by each function in order
of the input order. Each function also, optionally, defines a doc section.


**rivt markup**  wraps and extends restructured text markup. It adds two
additional markup elements - tags and commands - and provide simplified
backend and default settings for writing the same rivt file as different
document types (text, PDF and HTML).

**rivt** syntax includes **COMMANDS** for file operations and **TAGS** for text
formatting. Any text not defined by commands or tags is passed through as
`restructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_. 

Tags
-----------


**Line** tags format a line of text,are added at the end of the line and
are denoted with _[**TAG**]. **Block** tags are denoted with _[[**TAG**]] on
the first line. They evaluate a multi-line text block and end with _[[**Q**]]
on the last line of the block (note: some tags only format pdf and html output).

Commands
-----------

Commands read and write files and assign values to variables. They typically
start in the first column with double vertical bars. The command bar is
followed by the command name, the relative file path and any applicable
parameters.There are two exceptions to this pattern - the assignment (=) and
definiition (:=) commands.

In the syntax description below parameter options are separated with
semi-colons and elements by commas. File locations are specified using paths
relative to the rivt file location. Using the standard folder structure is
strongly recommended. Folder organization is described `here <5-folders.html>`_.

Commands read and write external files. They start in the first column with a
vertical bars. A double bar is used for write commands (||) and a single bar
(|) for read commands. The command bar is followed by the command name,
the relative file path and parameters, each separated by a single bar:

In the syntax description below parameter options are separated with
semi-colons and elements by commas. File locations are specified using paths
relative to the rivt file location. Using the standard folder structure is
strongly recommended. Folder organization is described `here <5-folders.html>`_.


