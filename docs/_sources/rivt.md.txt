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

The minimum software needed to write **rivt** documents is Python 3.8,
**rivtlib** and several other Python libraries. 
[rivt-doc](/rivt-doc.md) is an open source editing and publishing framework
using additional programs. All of the programs are open source.

**rivt** works with single files and extensive reports with hundreds of files.
Multi-file reports are organized in a tri-level folder structure explained
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

When running in an IDE (e.g. VSCode), API functions may be grouped in cells and
run interactively using the standard cell decorator:

<pre style="background:#e6ecdf;color:#000000"># %%</pre>

Interactive output is formatted as utf-8 text for speed and compatiblility.
Document and report files are generated using the the two functions

<pre style="background:#e6ecdf;color:#000000">rv.writemd() 
rv.writepdf() </pre>

which generate output files in GitHub Flavored Markdown
(GFM) and PDF formats respectively.

<hr>

## API Functions
<hr>

The first line of each function is a label followed by parameters. Each
function typically defines a new section using the label as the title. The
labels may be converted to references, with no section break, by prepending a
double hyphen.


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

File format conventions follow the Python formatter pep8, and linter ruff.
Method names start in column one. All other content must be indented 4 spaces
which facilitates section folding, bookmarks and legibility. API functions can
occur with any order or frequency except for *rivtinit* which occurs only once
as the initial function.

<hr>




