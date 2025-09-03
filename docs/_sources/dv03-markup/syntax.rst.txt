**3.1** Syntax
================

The first line of each function includes a section label (that also may be a
section title) followed by formatting parameters. New sections may be labeled
as separate or integrated with preceding sections. The section body can contain
any utf-8 text. Commands and tags applicable to each function are defined
[here](#commands) and [here](#tags).

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


Syntax
--------

The first line of each function includes a section label (that also may be a
section title) followed by formatting parameters. New sections may be labeled
as separate or integrated with preceding sections. The section body can contain
any utf-8 text. Commands and tags applicable to each function are defined
[here](#commands) and [here](#tags).

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


Commands read and write external files. They start in the first column with a
vertical bars. A double bar is used for write commands (||) and a single bar
(|) for read commands. The command bar is followed by the command name,
the relative file path and parameters, each separated by a single bar:

In the syntax description below parameter options are separated with
semi-colons and elements by commas. File locations are specified using paths
relative to the rivt file location. Using the standard folder structure is
strongly recommended. Folder organization is described `here <5-folders.html>`_.
