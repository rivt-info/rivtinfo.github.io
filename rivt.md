---
myst:
    substitutions:
        "key1": |
            ```{image} _static/img/riv02.png
            :alt: rivt logo
            :target: ../rivt.md#rivt-syntax
            :width: 45px
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
[here](../rivt-doc.md#folders).

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

## rivt Syntax
<hr>

**rivt** markup includes arbitrary unicode text, rivt commands and rivt tags.
[restructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html) is used as a base for **rivt** and some of the reST markup language may also be used. 

### commands

A command reads or writes external files and is denoted by || at the beginning
of a line. Command parameters are separated by |. In the summary below,
parameter options are separated with semi-colons and parameter list elements
are separated with commas.

<pre style="background:#dce8ef; color: #000000">
==================================================== ==============
    command syntax                                         API 
==================================================== ==============

|| text | rel file path | rivt; plain                     R I V

|| init | rel file path                                     R

|| append | rel file path                                   R

|| image  | rel file path, .. | .50, ..                     I

|| table  | rel file path | 60,r;l;c                        I

|| declare | rel file path |  print; noprint                V
</pre>

### tags

Line tags format a line of text and are denoted with *_[tag]*, typically at the
end of a line. The *=* and *:=* tags used in the Value method are unique
exceptions. 

<pre style="background:#dce8ef; color: #000000">
============================ ================================= ==========
   line tags                        description                   API
============================ ================================ ===========
text _[b]                       bold                            R I V 
text _[c]                       center                          R I V  
text _[i]                       italic                          R I V  
text _[bc]                      bold center                     R I V  
text _[bi]                      bold italic                     R I V
text _[r]                       right justify                   R I V
text _[u]                       underline                       R I V   
text _[l]                       LaTeX math                        I V
text _[s]                       sympy math                        I V
text _[bs]                      bold sympy math                   I V
text _[e]                       equation label, autonumber        I V
text _[f]                       figure caption, autonumber        I V
text _[t]                       table title, autonumber           I V
text _[#]                       footnote, autonumber              I V
text _[d]                       footnote description              I V
_[page]                         new page                          I V
_[address, label]               url or internal reference         I V
a = 1.2 | unit, alt | descrip   declare =                           V
a := b + c | unit, alt | n,n    assign :=                           V
</pre>

Block tags format a text block and start a block with *_[[tag]]* and
end with *_[[q]]*.

<pre style="background:#dce8ef; color: #000000">
============================ ================================ ==========
   block tags                        description                 API
============================ ================================ ==========
_[[b]]                          bold                            R I V
_[[c]]                          center                          R I V
_[[i]]                          italic                          R I V
_[[p]]                          plain                           R I V
_[[q]]                          quit block                      R I V
_[[l]]                          LaTeX                             I V
</pre>




