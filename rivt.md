---
myst:
  substitutions:
        "key1": |
            ```{image} _static/img/riv02.png
            :alt: rivt logo
            :target: /rivt.html#syntax
            :width: 60px
            ```
---

# {{ key1 }} rivt

**rivt** is a markdown language for writing, organizing and sharing engineering
documents. It emphasizes clarity, efficiency and access.
[rivtlib](https://rivt-code.net) is a Python library for processing **rivt**.
It reads **rivt** files and outputs formatted documents in a serveral different
formats. The minimum software needed to write **rivt** documents is Python 3.8,
and other Python libraries including **rivtlib**.

[rivt-doc](/rdoc.md) is an open source editing and publishing framework
using additional programs. All of the programs are open source. **rivt** works
with single files and extensive reports with hundreds of files. Multi-file
reports are organized in a tri-level folder structure explained
[here](/rdoc.md#folders).

<hr>

## **rivt files**
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

## **API functions**
<hr>

Each API function defines a document section. The first line of each function
includes a section label that converts to a section title, followed by section
formatting parameters. The titles and section breaks may be suppressed by
prepending a double hyphen.

The section body can contain any utf-8 text. Commands and tags applicable to
each function are defined [here](/syntax.md#commands) and
[here](/syntax.md#tags)


<pre style="background: #cfdde2; color: #000000">
============ ========================================================
  name                   API function definition
============ ========================================================

rivtinit      rv.R("""label | toc; notoc, start page

                  rivt settings, and text to be formatted and output to the
                  terminal.

                """)

insert        rv.I("""label | background color  

                  Static tables, images and text that are formmatted and output
                  to the terminal.

                """)

values        rv.V("""label | sub; nosub 

                  Equations and text that are evaluated, formatted and output to the terminal.
                
                """)

tools         rv.T("""label | line; noline | print; noprint

                  Python code evaluated in the rivt namespace.

                """)

exclude       rv.X("""any text

                  Any function changed to X is not processed. Used for
                  comments and debugging.

                """)

write-md      rv.writemd()
        
              Writes a markdown document file (default is a GitHub README.md)

write-pdf     rv.writepdf()
    
              Writes a markdown (default is a GitHub README.md) 
              and PDF document file (default uses rivt file name.)

all-readme    rv.readme()

              Collects, in order, all README.md document files in the project
              and writes them into a single README.md in the root project
              folder, making the project full-text searchable on GitHub. Note
              that file links in the document README will typically not resolve
              when compiled into the project README. This is by design. It
              makes the full-project README faster to search. For convenience
              links are inserted back to the original document README.
          
</pre>

The API function names start in column one. All other content is indented 4
spaces to facilitate section folding, bookmarking and legibility. API functions
can be written in any order and frequency except for *rivtinit*, which occurs
only once as the initial function in the file. A **rivt** file is a Python file
that follows pep8 and ruff conventions.






