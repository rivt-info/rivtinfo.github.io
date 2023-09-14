---
myst:
    substitutions:
        "key1": |
            ```{image} _static/img/riv02.png
            :alt: rivt logo
            :target: /rivt.html#rivt-syntax
            :width: 50px
            ```
---

# {{ key1 }}  **rivt** 

**rivt** is a markdown language for writing, organizing and sharing engineering
documents. It emphasizes clarity, efficiency and access.
[rivtlib](https://rivt-code.net) is a Python library for processing **rivt**.
The minimum software needed to write **rivt** documents is Python 3.8, and
other Python libraries including **rivtlib**. 

[rivt-doc](/rivt-doc.md) is an open source editing and publishing framework
using additional programs. All of the programs are open source. **rivt** works
with single files and extensive reports with hundreds of files. Multi-file
reports are organized in a tri-level folder structure explained
[here](/rivt-doc.md#folder-structure).

<hr>

## rivt Files
<hr>

A **rivt** file is a utf-8 Python file that includes the import statement: 

<pre style="background:#e6ecdf;color:#000000">import rivtlib.rivtapi as rv</pre> 

which exposes four API functions. Each function takes a triple quoted string as
argument, which may include arbitrary text.

<pre style="background: #cfdde2;color:#000000">
============= ========== =================================
API function   name           purpose
============= ========== =================================
rv.R(str)      rivtinit    repository and report settings
rv.I(str)      insert      static text, images and tables
rv.V(str)      values      equations
rv.T(str)      tools       Python functions and scripts
</pre>

When running in an IDE (e.g. VSCode) the file may be executed interactively.
Interactive output is formatted as utf-8 text for speed and compatiblility. API
functions may be grouped and executed step-wise using the standard cell decorator:

<pre style="background:#e6ecdf;color:#000000"># %%</pre>

Complete document and report files are generated using the functions

<pre style="background:#e6ecdf;color:#000000">rv.writemd() 
rv.writepdf() </pre>

which write output files in GitHub Flavored Markdown
(GFM) and PDF formats respectively.

<hr>

## API Functions
<hr>

Each API function defines a document section. The first line of each function
includes a section label that converts to a section title, followed by section
formatting parameters. The titles and section breaks may be suppressed by
prepending a double hyphen.

The section body can contain any utf-8 text. Commands and tags applicable to
each function are defined [here](/rivt-syntax.md#commands) and
[here](/rivt-syntax.md#tags)


<pre style="background: #cfdde2; color: #000000">
========== ========================================================
  name                   API  function definition
========== ========================================================

rivtinit    rv.R("""label | toc; notoc, start page

                rivt file settings and text

                """)

insert      rv.I("""label | background color  

                Static tables, images and text

                """)

values      rv.V("""label | sub; nosub 

                Equations and text
                
                """)

tools       rv.T("""label | lines; nolines

                Python code

                """)

exclude     rv.X("""any text

                    Any function changed to X is not evaluated. Used for
                    comments and debugging.

                """)

write-md    rv.writemd()
        
            writes markdown document file (default is a GitHub README.md)

write-pdf   rv.writepdf()
    
            writes markdown and PDF document files
</pre>

File format conventions follow the Python formatter pep8 and linter ruff. API
function names start in column one. All other content is indented 4 spaces
to facilitate section folding, bookmarking and legibility. API functions can
be written in any order and frequency except for *rivtinit*, which occurs only once
as the initial function in the file.

<hr>




