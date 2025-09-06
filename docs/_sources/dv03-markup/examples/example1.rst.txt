Example 1
==========


.. code-block:: python

    import rivtlib.rivtapi as rv

    rv.R("""Run function | pass; redact | nocolor; color code

        The Run function processes shell commands.

        Each API function defines a new document section. The first line is a
        heading line which includes the section heading, a parameter for redacting
        sections in a mirror file intended for public sharing, and a parameter for
        the background color for the section. If the section heading is preceded by
        two dashes (--) the section is continued from the prior section without
        introducting a new number.
        
        File formatting follows pep8 and ruff. API functions start in column one.
        All other lines are indented 4 spaces to facilitate section folding,
        bookmarks and legibility.

        """)

    rv.I("""Insert function | pass; redact | nocolor 

        The Insert function formats static objects including images, tables,
        equations and text.

        ||text | data01/describe.txt | rivt     

        The table command inserts and formats tabular data from csv or xls files.
        The _[t] tag formats and autonumbers table titles.

        A table title  _[t]
        || table | data/file.csv | 60,r

        The image command inserts and formats image data from png or jpg files. The
        _[f] tag formats and autonumbers figures.
            
        A figure caption _[f]
        || image | data/f1.png | 50

        Two images may be placed side by side as follows:

        The first figure caption  _[f]
        The second figure caption  _[f]
        || image | private/image/f2.png, private/image/f3.png | 45,35
        
        The tags _[x] and _[s] format LaTeX and sympy equations:

        \gamma = \frac{5}{x+y} + 3  _[x] 

        x = 32 + (y/2)  _[s]

        """)

    rv.V("""Values function |  pass; redact | nocolor 

        The Values fucntion evaluates variables and equations. 
        
        The equal tag declares a value. A sequence of declared values terminated
        with a blank line is formatted as a table.
        
        Example of assignment list _[t]
        f1 = 10.1 * LBF |LBF, N| a force value
        d1 = 12.1 * IN  |IN, CM| a length value

        An equation tag provides an equation description and number. A colon-equal
        tag assigns a value and specifies the result units and the output decimal
        places printed in the result and equation.

        Example equation - Area of circle  _[e]
        a1 := 3.14(d1/2)^2 | IN^2, CM^2 | 1,2

        || declare | data01/values02.csv
        
        The declare command imports values from the csv file written by rivt when
        processing values in other documents. 

        """)

    rv.T("""Tools function | pass; redact | nocolor

        The Tools function processes Python code.
            
        """)


    rv.X("""Any text 

        Changing a function to X skips evaluation of that function. Its purposes
        include review commenting and debugging.

        """) 

    rv.D("""Doc function | pass; redact | nocolor

        The Write function generates docs and reports.

        | docs |
        
        | report |

        """)
