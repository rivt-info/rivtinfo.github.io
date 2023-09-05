
```{image} _static/img/riv02.png
:alt: rivt logo
:target: index.html
:width: 125px
:align: left
```

**<p style="text-align: left;"><a href="index.html"> HOME </a></p>**

**rivt**

rivt is both an open source engineering document markdown language and the
Python library that processes it. The language and library are designed to
write, assemble and share engineering documents and prioritize legibility,
flexibility, efficiency and universal access. They run on any platform that
supports Python 3.8 or and have not dependencies. However rivt-doc (see below)
has a number of dependencies.

A rivt file is a Python file that begins with the import statement:

*import rivt.rivtapi as rv*
 
which in turn provides four API functions (referred to as Repo, Insert, Values
and Tools). Each function takes a single, triple quoted string as an
argument.

rv.R(rmS) - repository and report information 
rv.I(rmS) - static text, images, tables and math
rv.V(rmS) - equations
rv.T(rmS) - Python functions and scripts

A rivt file begins with rv.R followed by an arbitrary sequence of the
three later string methods.

When running in an IDE (e.g. VSCode), each method may be run interactively
using the standard cell decorator (# %%). Interactive output is formatted as
utf-8 text. The rv.writemd() and rv.writepdf() functions generate documents and
compilations in GitHub Markdown (ghmd) and PDF formats. 

rivt works with both simple, single file documents as well as extensive reports
with hundreds of files. Multi-file reports can be structured in an efficient
folder based framework.


rivt syntax
===========

rivt syntax includes arbitrary unicode text including rivt commands and tags. A
rivt command reads or writes external files and is denoted by || at the
beginning of a line. Command parameters are separated by |. In the summary
below parameter options are desginated with semi-colons and list parameters
with commas.

Tags format a line or block of text and are denoted with _[tag] at the end of a
line. Block tags start a block of text with _[[tag]] and end with _[[q]]. The
"=" and ":=" tags used in the Value method are exceptions.

======= ===================================================================
 name    Commands per API function (VSCode snippet prefix)
======= ===================================================================

Repo    rv.R("""label | toc; notoc | page
(re)
                ||init (ini)
                ||text (tex)
                ||append (app)

                """)

Insert  rv.I("""label | color  
(in)
                ||image (img)
                ||text (tex)
                ||table (tab)

                """)

Values  rv.V("""label | sub; nosub 
(va)
                ||declare (dec)

                """)

Tools  rv.T("""label | color | print; noprint 
(to)
                Python code

                """)

exclude rv.X("""any method

                Any method changed to X is not evaluated. It may be used for
                comments and debugging.

                """)

write   rv.writemd()
(wm)

write   rv.writepdf()
(wp)


=============================================================== ============
    command syntax and description (snippet)                         API 
=============================================================== ============

|| init | rel file path                                               R
    (ini)   config file path

|| append | rel file path                                             R
    (app)   pdf path

|| text | rel file path | text type                                 R I V
    (tex)   .txt | plain; tags

|| image  | rel file path | .50, ..                                 R I V
    (img)   .png; .jpg |  page width 

|| table  | rel file path | 60,r;l;c                                R I V
    (tab)   .csv; xls  | max col width, align

|| declare | rel file path | print,;noprint                           V
    (dec)    .csv; .xls  | print or hide

============================ ============================================
 tags                                  description 
============================ ============================================
lines in R,I,V:
text _[b]                       bold 
text _[c]                       center
text _[i]                       italic
text _[bc]                      bold center 
text _[bi]                      bold italic
text _[r]                       right justify
text _[u]                       underline   
text _[l]                       LaTeX math
text _[s]                       sympy math
text _[bs]                      bold sympy math
text _[e]                       equation label and autonumber
text _[f]                       figure caption and autonumber
text _[t]                       table title and autonumber
text _[#]                       footnote and autonumber
text _[d]                       footnote description 
_[page]                         new page
_[address, label]               url or internal reference

lines in V: 
a = n | unit, alt | descrip    declare = 
a := b + c | unit, alt | n,n   assign := 

blocks in R,I,V:          
_[[b]]                          bold
_[[c]]                          center
_[[i]]                          italic
_[[p]]                          plain  
_[[l]]                          LaTeX
_[[q]]                          quit block


The first line of a rivt file is *import rivt.rivtapi as rv* followed by the
Repo method rv.R(). rv.R is followed by any of the other three methods in any
number or order. The first line of each method is a section label followed by
section parameters. Section labels may be converted into editing references by
prepending a double hyphen --.

File format conventions follow the Python formatter pep8, and linter ruff.
Method names start in column one. All other lines must be indented 4 spaces to
facilitate section folding, bookmarks and legibility. The first line of each
rivt function defines the section title and parameters.

============================================================================
rivt example
============================================================================

import rivt.rivtapi as rv

rv.R("""Introduction | notoc, 1

    The Repo method (short for repository and report) is the first method of a
    rivt file which specifies document configuration settings.

    The first line of any method is the heading line, which starts a new
    document section. If the section heading is preceded by two dashes (--) it
    becomes a section reference and a new section is not started. The toc
    parameter specifies whether a document table of contents is generated (not
    to be confused with a report table of contents). The page number is the
    starting page number for the doc when processed as a stand alone document.

    The init command specifies the name of the configuration file which is read
    from the rivt-doc folder. Report formatting can be easily modified by
    specifying a different init file.

    ||init | rivt01.ini

    The text command inserts text from an external file. Text files may be
    plain text or include rivt tags.

    ||text | private/text/proj.txt | plain
    
    The append command attaches PDF files to the end of the doc.

    || append | append/report1.pdf
    || append | append/report2.pdf

    
    """)

rv.I("""The Insert method | color 

    The Insert method formats static information e.g. images and text. The
    color command specifies a background color for the section.

    The text command inserts and formats text from external files into the
    rivt file. Text files may be plain text or text with rivt tags.

    ||text | data0101/describe.txt | rivt     

    The table command inserts and formats tabular data from csv or xls files.
    
    The _[t] tag formats and autonumbers table titles.

    A table title  _[t]
    || table | data0101/file.csv | 60,r

    The image command inserts and formats image data from png or jpg files.
`
    The _[f] tag formats and autonumbers figures.
        
    A figure caption _[f]
    || image | data0101/f1.png | 50

    Two images may be placed side by side as follows:

    The first figure caption  _[f]
    The second figure caption  _[f]
    || image | private/image/f2.png, private/image/f3.png | 45,35
    
    The tags _[x] and _[s] format LaTeX and sympy equations:

    \gamma = \frac{5}{x+y} + 3  _[x] 

    x = 32 + (y/2)  _[s]

    """)

rv.V("""The Values method |  sub; nosub 

    The Values method assigns values to variables and evaluates equations. The
    sub; nosub setting specifies whether the equations are printed a second
    time with substituted numerical values.

    A table tag provides a table title and number.  
    
    The equal tag declares a value. A sequence of declared values terminated
    with a blank line are formatted as a table.
    
    Example of assignment list _[t]
    f1 = 10.1 * LBF | N | a force
    d1 = 12.1 * IN | CM | a length

    An equation tag provides an equation description and number. A colon-equal
    tag assigns a value and specifies the result units and printed output
    decimal places in the result and equation.

    Example equation - Area of circle  _[e]
    a1 := 3.14(d1/2)^2 | IN^2, CM^2 | 1,2

    || declare | data0102/values0102.csv
    
    The declare command imports values from a csv file written by rivt when
    processing assigned and declared values from another doc in the same
    project.

""")

rv.T("""The Tools method | color 

    # The Tools method processes Python code in the rivt namespace and prints
    # the code and the result of any print statement in the doc. 
    # Functions may be written explicitly or imported from other
    # files. Line comments (#) are printed. Triple quotes cannot be used. Use
    # raw strings instead.
    
    # Four Python libraries are imported by rivt and available as: 
    # pyplot -> plt
    # numpy -> np
    # pandas -> pd
    # sympy -> sy
    
    # Python code example:
    
    def f1(x,y): z = x + y
        print(z)
        return Z

    with open('file.csv', 'r') as f: 
        input = f.readlines()
    
    var = range(10)
    with open('fileout.csv', 'w') as f: 
        f.write(var)
        
    """)

rv.X("""any text

    Changing a function to X skips evaluation of that function. Its uses
    include review comments and debugging.

    """) 