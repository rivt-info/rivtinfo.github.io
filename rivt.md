
```{image} _static/img/riv02.png
:alt: rivt logo
:target: https://www.rivt-doc.net/index.html
:width: 125px
:align: left
```
<style>
a {
    color: blue;
    text-decoration: underline;
}

</style>

# **rivt**

**rivt** is a markdown language that prioritizes clarity, efficiency and access
when writing, organizing and sharing engineering documents. **rivtlib** is an
open source Python library for processing **rivt**. The minimum software needed
to write rivt documents is Python 3.8 and libraries.

<a href="rivt-doc.html">rivt-doc</a> is an installable, open source editing and
publishing framework that requires additional open source programs.

## rivt files

A rivt file is a utf-8 Python file that includes the import statement:

*import rivtlib.rivtapi as rv*
 
which exposes the single-letter API functions referred to as: repo, insert,
values and tools. Each function takes a triple quoted string as argument.

<pre style="background:  #cfdde2">
rv.R(str) - repository and report information 
rv.I(str) - static text, images, tables and math
rv.V(str) - equations
rv.T(str) - Python functions and scripts
</pre>

When running in an IDE (e.g. VSCode), functions may be run individually
with the standard cell decorator (# %%). Interactive output is formatted as
utf-8 text for speed and general compatiblility.

Document and report files are generated using the rv.writemd() and rv.writepdf()
functions which generate files in GitHub Flavored Markdown (GFM) and PDF
formats respectively.

rivt works with documents of all sizes; from single files to extensive reports
including hundreds of files. Multi-file reports are structured through a
tri-level folder structure explained here <a href="rivt-doc.html">here</a>.

## API functions

<pre style="background:  #cfdde2">
========= ========================================================
 name                       function
========= ========================================================

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
</pre>

## rivt syntax

rivt syntax includes arbitrary unicode text including rivt commands and tags. A
rivt command reads or writes external files and is denoted by || at the
beginning of a line. Command parameters are separated by |. In the summary
below parameter options are desginated with semi-colons and list parameters
with commas.

Tags format a line or block of text and are denoted with _[tag] at the end of a
line. Block tags start a block of text with _[[tag]] and end with _[[q]]. The
"=" and ":=" tags used in the Value method are exceptions.

### commands
<pre style="background: #dce8ef">
==================================================== ==============
    command syntax                                          API 
==================================================== ==============

|| init | rel file path                                      R

|| append | rel file path                                    R

|| image  | rel file path, .. | .50, ..                      I

|| table  | rel file path | 60,r; l; c                       I

|| declare | rel file path |  print; noprint                 V

|| text | rel file path | rivt; plain                      R I V
</pre>

### tags

<pre style="background: #dce8ef">
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

============================ ================================= ==========
   block tags                        description                   API
============================ ================================ ===========
_[[b]]                          bold                            R I V
_[[c]]                          center                          R I V
_[[i]]                          italic                          R I V
_[[p]]                          plain                           R I V
_[[q]]                          quit block                      R I V
_[[l]]                          LaTeX                             I V
</pre>


The first line of a rivt file is *import rivt.rivtapi as rv* followed by the
Repo function rv.R(). rv.R is followed by any of the other three methods in any
number or order. The first line of each function is a label followed by section
parameters. Each function defines a new section with the label as the title.
The labels may be converted into editing references that do not start a new
section by prepending a double hyphen.

File format conventions follow the Python formatter pep8, and linter ruff.
Method names start in column one. All other lines must be indented 4 spaces to
facilitate section folding, bookmarks and legibility. The first line of each
rivt function defines the section title and parameters.

