---
myst:
    substitutions:
        "key2": |
            ```{image} _static/img/riv02.png
            :alt: rivt logo
            :target: "toy example"
            :width: 50px
            ```
---

#  {{ key2 }} rivt examples

<hr>

## **Simple**
<hr>

<pre style="background:#e6ecdf;color:#000000">
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

rv.I("""The Insert method | default 

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
    # the code and result of any print statement in the doc. New functions 
    # may be written explicitly or imported from other files. Line comments 
    # are printed. Triple quotes cannot be used. Use raw strings instead.
    
    # Four Python libraries, if installed, are imported by rivt and available as: 
    # pyplot -> plt
    # numpy -> np
    # pandas -> pd
    # sympy -> sy
    
    # Python code:
    
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

    Changing a function to X skips evaluation of that function and may be used
    for review comments and debugging.

    """) 
</pre>


### text output

<pre style="background: #e6ecdf;color:#000000">

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

rv.I("""The Insert method | default 

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
    # the code and result of any print statement in the doc. New functions 
    # may be written explicitly or imported from other files. Line comments 
    # are printed. Triple quotes cannot be used. Use raw strings instead.
    
    # Four Python libraries, if installed, are imported by rivt and available as: 
    # pyplot -> plt
    # numpy -> np
    # pandas -> pd
    # sympy -> sy
    
    # Python code:
    
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

    Changing a function to X skips evaluation of that function and may be used
    for review comments and debugging.

    """) 
</pre>


### markdown output

some markdown


### PDF output

[PDF output from example](./_static/attach/rivt-toy-example.pdf)

<hr>

## **Solar canopy**
<hr>
xyz

### text output

ccc

<hr>

## **Seismic Strengthening**
<hr>

xyz

### text output

ccc
