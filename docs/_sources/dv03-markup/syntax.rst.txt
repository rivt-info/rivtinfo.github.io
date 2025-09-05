3.1 Syntax
================

[01] Header 
--------------

The first line of a *rivt-string* is a header containing a *section label* and
two control *parameters*. The *section label* is the title for a new section. When
preceeded by two dashes (--) the section is merged with the prior section.
  
.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content
        ...
        
        """)

The *parameters* specifiy whether the *section content* is output to *docs*,
and whether the section is written to a *public file*. The paramters only
need to be specified when different from the defaults.

============= ============================
API function    default header parameters       
============= ============================
rv.R             noprint, private
rv.I             print, private
rv.V             print, private
rv.T             noprint, private
rv.D             noprint, private
rv.S             noprint, private
rv.Q             noprint, private
============= ============================


[02] Section Content
----------------------

Section content is indented four spaces (for legibility and code folding) and
includes *commands* for file operations and *tags* for text formatting. Any
text not defined by *commands* or *tags* is passed through unchanged to
intermediate files for further PDF and HTML processing, or formatted to a utf-8
*doc*.


.. code-block:: python

    rv._("""Section Label | print; noprint, public; private

        section content
        ...
        
        """)

*rivt markup* wraps and extends *restructuredText* and adds the additional
markup elements - *tags* and *commands*. They simplify use and improve
legiblity. For example, the same rivt file can generate  text, PDF or HTML docs.

**Tags**

:doc:`Line tags <tagsl>` format a line of text and are denoted
with _[**TAG**], typically added at the end of the line.

:doc:`Block tags <tagsb>` evaluate a multi-line text block that starts
with _[[**TAG**]] and ends with _[[**Q**]].

**Commands**

:doc:`Commands <commands>` read and write files and assign values to variables. They start in the
first column with double vertical bars, followed by the command name, the
relative file path and parameters. The exceptions are the assign (=) and define
(:=) commands, related to equations.

*RestructuredText*

Text in a *rivt string* not defined by *commands* or *tags* is passed through
to a *restructuredText (reST)* file used to write PDF and HTML *docs*. In
addition, *commands* and *tags* are often converted to *reST* when processing a
*rivt file*. Most *restructuredText* syntax is stripped out
when writting a *text doc*.


Common *restructuredText* useful in a *rivt string* include surrounding test
with * for italics and ** for bold.




