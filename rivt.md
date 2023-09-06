
```{image} _static/img/riv02.png
:alt: rivt logo
:target: https://www.rivt-doc.net/index.html
:width: 125px
:align: left
```

**<p style="text-align: left;"><a href="index.html"> HOME </a></p>**

# **rivt**

**rivt** is an engineering document markdown language processed by **rivtlib**,
a Python library. They are both open source and run on any platform that
supports Python 3.8 or above. The language and library are designed to write,
assemble and share engineering documents in a way that prioritizes clarity,
efficiency, extension and universal access. **rivt-doc** is a complete open
source editing and publishing system with installers and requiring a number of
open source library and application dependencies.

The minimum software needed is:

- Python 3.8 or higher 
- **rivtlib** + Python dependencies

Full capabilities require the **rivt-doc** framework.

## rivt files

A rivt file is a utf-8 text (Python) file that includes the import statement:

*import rivtlib.rivtapi as rv*
 
which in turn provides four single-letter API functions referred to as repo,
insert, values and tools. Each function takes a single, triple quoted string
as argument.

rv.R(rmS) - repository and report information 
rv.I(rmS) - static text, images, tables and math
rv.V(rmS) - equations
rv.T(rmS) - Python functions and scripts

When running in an IDE (e.g. VSCode), each method may be run interactively
using the standard cell decorator (# %%). Interactive output is formatted as
utf-8 text. The rv.writemd() and rv.writepdf() functions generate document
files and report compilations in GitHub Flavored Markdown (GFM) and PDF formats.

rivt works with both single file documents, as well as extensive reports with
hundreds of files. Multi-file reports are structured through a two-level,
folder-based framework.

## API functions

```
name        function    
repo        rv.R("""label | toc; notoc page

                    Report, repository and introductory text

                    """)

insert      rv.I("""label | color  

                    Text, static tables and images

                    """)

values      rv.V("""label | sub; nosub 

                    Equations and text
                
                    """)

tools       rv.T("""label | lines; nolines

                    Python code

                    """)

exclude     rv.X("""any 

                    Any function changed to X is not evaluated and can be used for
                    comments and debugging.

                    """)

write-md    rv.writemd()
(wm)        writes markdown document

write-pdf   rv.writepdf()
(wp)        writes markdown and PDF document
```

## rivt syntax

rivt syntax includes arbitrary unicode text including rivt commands and tags. A
rivt command reads or writes external files and is denoted by || at the
beginning of a line. Command parameters are separated by |. In the summary
below parameter options are desginated with semi-colons and list parameters
with commas.

Tags format a line or block of text and are denoted with _[tag] at the end of a
line. Block tags start a block of text with _[[tag]] and end with _[[q]]. The
"=" and ":=" tags used in the Value method are exceptions.

### rivt commands

 |         **command**          | **API function** |
 | :--------------------------: | :--------------: |
 |  \|\|init \| rel file path   |        R         |
 | \|\|append \| rel file path  |        R         |
 |  \|\|image \| rel file path  |        I         |
 |  \|\|table \| rel file path  |        I         |
 | \|\|declare \| rel file path |        V         |
 |  \|\|text \| rel file path   |      R I V       |


### rivt tags

|          **line tags**           |      **description**      | **API** |
| :------------------------------: | :-----------------------: | :-----: |
|           text \_\[b\]           |           bold            |  R I V  |
|           text \_\[c\]           |          center           |  R I V  |
|           text \_\[i\]           |          italic           |  R I V  |
|          text \_\[bc\]           |        bold center        |  R I V  |
|          text \_\[bi\]           |        bold italic        |  R I V  |
|           text \_\[r\]           |       right justify       |  R I V  |
|           text \_\[u\]           |         underline         |  R I V  |
|           text \_\[l\]           |        LaTeX math         |  R I V  |
|           text \_\[s\]           |        sympy math         |  R I V  |
|          text \_\[bs\]           |      bold sympy math      |  R I V  |
|           text \_\[e\]           | equation label autonumber |  R I V  |
|           text \_\[f\]           | figure caption autonumber |  R I V  |
|           text \_\[t\]           |  table title autonumber   |  R I V  |
|          text \_\[\#\]           |    footnote autonumber    |  R I V  |
|           text \_\[d\]           |   footnote description    |  R I V  |
|            \_\[page\]            |         new page          |  R I V  |
|       \_\[address label\]        |           link            |  R I V  |
|  a = n \| unit, alt \| descrip   | = tag declares a variable |    V    |
| a := b \+ c \| unit, alt \| n, n |  := tag assigns a value   |    V    |



| **block tags** | **description** | **API function** |
| :------------: | :-------------: | :--------------: |
|  \_\[\[b\]\]   |      bold       |      R I V       |
|  \_\[\[c\]\]   |     center      |      R I V       |
|  \_\[\[i\]\]   |     italic      |      R I V       |
|  \_\[\[p\]\]   |      plain      |      R I V       |
|  \_\[\[q\]\]   |   quit block    |      R I V       |
|  \_\[\[l\]\]   |      LaTeX      |       I V        |



The first line of a rivt file is *import rivt.rivtapi as rv* followed by the
Repo function rv.R(). rv.R is followed by any of the other three methods in any
number or order. The first line of each function is a label followed by section
parameters. Each function defines a new section with the label as the title.
The labels may be converted into editing references that do not start a new
sectiojn by prepending a double hyphen --.

File format conventions follow the Python formatter pep8, and linter ruff.
Method names start in column one. All other lines must be indented 4 spaces to
facilitate section folding, bookmarks and legibility. The first line of each
rivt function defines the section title and parameters.

