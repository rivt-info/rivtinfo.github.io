**F.1 |** Quick Reference
=========================== 

.. _Quick Reference:

**[1]** Reference Summary
--------------------------------------------------------------------- 

- :ref:`API Summary <API Summary>` 
- :ref:`Line Tags <Line Tags Summary>` 
- :ref:`Block Tags <Block Tags Summary>` 
- :ref:`Assignment Summary <Assignment Summary>` 
- :ref:`Commands <commands list>` 
- :ref:`Folders <project-folders-summary>` 
- :ref:`Unit Definitions <unit-definitions>`


.. _API Summary:

**[2]** API Summary
--------------------------------------------------------------------- 

**API methods**

================= =============== =============================
API Function         Name             Purpose
================= =============== =============================
**rv.R** (rS)         Run          Run scripts and markup
**rv.I** (rS)         Insert       Insert static sources 
**rv.V** (rS)         Values       Calculate values
**rv.T** (rS)         Tools        Shell scripts and programs
**rv.D** (rS)         Doc          Publish docs 
**rv.S; X** (rS)     Skip; Exit    Skip section or exit 
================= =============== =============================

where **rS** is a *rivt string*. The first line of a *rivt string* (rS)
is the :term:`header substring`.

**Section Headers**

.. code-block:: python

    rv._("""Section Label 

        Default header for Insert and Values sections.
        Content text and rivt markup, indented four spaces.
        
        """)

    rv._("""Section Label | shmpn 

        Header with modifications for Insert and Values sections.
        Content text and rivt markup, indented four spaces.
        
        """)

**rv.D Header**

.. code-block:: python

    rv.D("""Section Label 

        Content text and rivt markup - indented four spaces.
         
        """)

The first parameter list in the *header substring* specifies handling of the
*content substring*. The second and third parameters, where applicable, specify 
a type and file that is processed by the API method before processing 
any *content*.

**Parameters**

Section parameters may be specified in any order or ommitted if defaults are
acceptable. 

- s | store - stores the section content in *_rvstored/sect* as a *.rvt file.*
- h | hide - processes the section but suppresses the *doc* output.
- m | merge - merges the section with the previous section.
- p | public - toggles the default public/private status of the section (see :ref:`comments <rivt-settings>`)
- n | new page - Starts a new pdf page.

The default parameters, when ommitted, are as follows:

- section is not stored
- section content is published
- section not merged
- private section
- continuous pages 
  
-------------------------------------

.. _Line Tags Summary:

**[3]** Line Tags Summary
---------------------------------------------------------------------------

  
**Format a line of text**

========== ==================================================== =============================
API Scope             Line Tag                                      Description 
========== ==================================================== =============================
rv.I                   text \*word word\* text                      italicize words  
rv.I                   text \*\*word word\*\* text                  bold words   
rv.I                   text **_[D] label, filename |** text       :ref:`Download link`
rv.I                   text **_[G] glossary term |** text         :ref:`Term link`
rv.I                   text **_[S] label, section |** text        :ref:`Section link`
rv.I                   text **_[U] label, url |** text            :ref:`URL link`
rv.I,V                 text **_[#]** text                         :ref:`Endnote number`    
rv.I,V                 text **_[R]**                              :ref:`Right justify` 
rv.I,V                 text **_[B]**                              :ref:`Bold text` 
rv.I,V                 text **_[C]**                              :ref:`Bold center text` 
rv.I,V                **title _[T]**                              :ref:`Number table`
rv.I,V      **ASCII text math _[M]** description                  :ref:`Text math` 
rv.I,V           **LaTeX math _[L]** description                  :ref:`LaTeX math` 
rv.I,V                 text **_[V] var_name |** text              :ref:`Substitute value`
all                     **##** text                               nonprinting comment
========== ==================================================== =============================

----------------------------------

.. _Block Tags Summary:

**[4]** Block Tags Summary
---------------------------------------------------------------------------

**Format or run blocks of text or scripts**


========== ========================================= ===============================
API Scope         Block Tag                                Description 
========== ========================================= ===============================
rv.R        **_[[WRITE]]** var name                   :ref:`Write block`
rv.R        **_[[SHELL]]** os, *wait;nowait*          :ref:`Shell script`
rv.I,V      **_[[TABLE]]** label                      :ref:`Table block`
rv.V        **_[[ARGS]]** arg dict name               :ref:`Arg block`
rv.D        **_[[METADATA]]** label                   :ref:`Meta block` 
all         **_[[END]]**                              :ref:`End block`
========== ========================================= ===============================


----------------------------------

.. _Assignment Summary:

**[5]** Assignment Summary
---------------------------------------------------------------------------

**Assign values to expressions**

========== =============================================================== ========================
API Scope           Command                                                        Description
========== =============================================================== ========================
rv.V         a **==:** 1*IN  | unit1, unit2, decimal | label                 :ref:`Define value`
rv.V         c **<=:** expression | unit1, unit2, decimal | label            :ref:`Assign value`
rv.V         c **:=:** func(x,y) | unit1, unit2, decimal | label             :ref:`Assign function`
rv.V         a **<=** c | unit, decimal, text1, text2 | label                :ref:`Compare value`
========== =============================================================== ========================


.. _commands list:

**[6]** Command Summary
---------------------------------------------------------------------------

**Read and format files**

========== =============================================================== ========================
API Scope           Command                                                        Description
========== =============================================================== ========================
rv.R        **| SCRIPT |** file name | args, output file                     :ref:`Script file`
rv.R        **| ARGS |** file name | namespace                               :ref:`Args file`
rv.R        **| TEXT |** file name | type                                    :ref:`Text file` 
rv.I, V     **| IMAGE |** file name | caption, scale, num;non, time;not      :ref:`Image file`
rv.I, V     **| IMAGE2 |** file1, file2 | c1,c2,s1,s2,n1,n2                  :ref:`Adjacent images`
rv.I, V     **| TABLE |** file name | title,width,head;nohead,num;non        :ref:`Table file`    
rv.V        **| VALTABLE |** file name | title, width, num;non               :ref:`Valtable file`
rv.V        **| VALSTOR |** file name | title, width, num;non                :ref:`Valstor file`
rv.V        **| PYTHON |** file name | args, var, type, label                :ref:`Function value`  
rv.V        **| FUNCTION |** function name | args, var, type, label          :ref:`Function value`  
rv.T        **| COPY |** abs src path | abs dest path | file pattern         :ref:`Copy file`
rv.T        **| SHELL |** abs file path | os, wait                           :ref:`Shell file`
rv.D        **| PUBLISH |** doc title | type                                 :ref:`Publish doc` 
rv.D        **| ATTACHPDF |** file name | front;back, title                  :ref:`Attach PDF`   
========== =============================================================== ========================

**Command File Paths**

================ ===================================== ======
   Command           Default Path [1]                   R/W
================ ===================================== ======
\| SCRIPT |         **rvreport-.../scripts** [2]        R/W
\| ARGS |           **rvreport-.../data**                R
\| TEXT |           **rvreport-.../data**                R 
\| IMAGE |          **rvreport-.../image**               R
\| IMAGE2 |         **rvreport-.../image**               R
\| TABLE |          **rvreport-.../data**                R
\| VALTABLE |       **rvreport-.../data**                R
\| VALSTOR |        **rv_stor/vals**                     R
\| ATTACHPDF |      **rvreport-.../data**                R
\| PUBLISH |        **rvreport-.../_published/** [3]     W
\| COPY |               os root                          R
\| SHELL |              os root                          R
================ ===================================== ======

[1] Path overrides are relative to the **rvreport-...** folder and include an initial /
[2] Output is written to **rvreport-.../data**   
[3] *docs* are written to subdirectories of **rvreport-../_published** for each type

----------------------------------

.. _project-folders-summary:

**[7]** Project Folders
---------------------------------------------------------------------
.. code-block:: bash

    [rivt-]project-Label/             project folder       
        ├── .help/                        help files
        ├── .vscode/                      optional VSCode settings
        ├── .git                          optional git repository
        ├── README.txt                    rivt-generated text report                  
        ├── [_rvpublic-reptname]/         rivt-generated public files
            ├── rvsrc/                        author source files          
            ├── rv-101-filename1.py           public rivt file
            ├── rv-102-filename2.py           public rivt file       
            ├── rv-201-filename3.py           public rivt file          
             ...
        ├── [rvreport-reptname]/          report folder               
            ├── [rivt-report]-1.py            report generating script
            ├── [rv101-]filename1.py          rivt file
            ├── [rv102-]filename2.py          rivt file       
            ├── [rv201-]filename3.py          rivt file          
                ...
            ├── [rvsrc]/                      author provided files and folders        
                ├── [data]/                         tables    
                    └── steel-vals.csv    
                ├── [downloads]/                    files to download      
                    └── conc-vals.txt 
                ├── [img]/                          images              
                    ├── favicon.png    
                    ├── covlogo1.png    
                    ├── runlogo1.png
                    ├── fig1.png
                    └── fig2.jpg                   
                ├── [scripts]/                      scripts
                    ├── beam1.py    
                    └── text.rst                                                                
                ├── tools/                          OS shell commands               
                    └── opensees.sh                                          
            ├── [_rvstor]/                   rivt-generated source files
                ├── [logs]/                          log files
                    ├── rv101-log.txt
                    └── rv102-log.txt
                ├── [sect]/                          sections not printed                    
                    ├── rv202-5d.txt  
                    ├── rv103-4t.txt                         
                    └── rv301-2r.txt               
                ├── [temp]/                          temp files
                    └── rv101-label3.tex
                ├── output.dat
                ├── v101-2.csv
                └── v102-3.csv         
            ├── [_published]/               rivt-published docs and reports
                ├── [docs]/                          html docs
                    ├── html auxiliary folders    
                    ├── index.html
                    ├── rv101-filename1.html      
                    ├── rv102-filename2.html                      
                    ├── rv201-filename3.html                        
                        ...     
                ├── [pdfdocs]/                       pdf docs
                    ├── pdf auxiliary folders     
                    ├── report-title.pdf
                    ├── rv101-filename1.pdf             
                    ├── rv102-filename1.pdf             
                    ├── rv201-filename3.pdf 
                        ...  
                └── [txtdocs]/                       text docs
                    ├── report-title.txt
                    ├── rv101-filename1.txt              
                    ├── rv102-filename1.txt             
                    ├── rv201-filename3.txt 
                        ...
            └── [_rstdocs]/                    rivt-generated rst files
                ├── _downloads/                    
                ├── _static/                                                       
                ├── rv101-filename1.rst            
                ├── rv102-filename2.rst                          
                ├── rv201-filename3.rst          
                    ...
        ├── [rvhandbk-]book-Label/             rivt handbook folder              
            ├── [_rstdocs]/                        rivt-generated rst files
                ├── _downloads/                    
                ├── _static/                                                       
                ├── rv101-filename1.rst            
                ├── rv102-filename2.rst                          
                ├── rv201-filename3.rst          
                  ...
            ├── [_txtdocs]/                        txt docs and handbook report
                ├── pdf auxiliary folders     
                ├── report-title.txt
                ├── rv101-filename1.txt             
                ├── rv102-filename1.txt             
                ├── rv201-filename3.txt
                  ...        
            ├── [_pdfdocs]/                        pdf docs and handbook report
                ├── pdf auxiliary folders     
                ├── report-title.pdf
                ├── rv101-filename1.pdf             
                ├── rv102-filename1.pdf             
                ├── rv201-filename3.pdf
                  ...
            └── [_rvstor]/                         rivt-generated source files
                ├── [logs]/                           log files
                    ├── rv101-log.txt
                    └── rv102-log.txt
                ├── [sect]/                           sections not printed                    
                    ├── rv202-5d.txt  
                    ├── rv103-4t.txt                         
                    └── rv301-2r.txt               
                ├── [temp]/                           temp files
                    └── rv101-label3.tex
                ├── [vals]/                           values files
                    ├── v101-2.csv
                    └── v102-3.csv         
                └── output.dat 
            ├── [bk1-]folder name                  handbook chapter folder
                ├── [rv001-]filename1.py              rivt file       
                ├── [downloads]/                      files to download      
                    └── conc-vals.txt 
                ├── [img]/                            page layout images              
                    ├── favicon.png    
                    ├── covlogo1.png    
                    ├── runlogo1.png
                    └── fig1.png
                ├── [data]/                           tables and values    
                    └── steel-vals.csv              
                    ├── v101-2.csv
                    └── v102-3.csv         
                ├── [scripts]/                        scripts
                    ├── beam1.py    
                    └── text.rst  
                └── tools/                            OS shell commands               
                    └── opensees.sh                           
            ├── [bk2-]folder name                  handbook chapter folder
                    ...        
            └── [bk3-]folder name                  handbook chapter folder
                    ...

.. _unit-definitions:

**[8]** Unit Definitions
---------------------------------------------------------------------------

.. code-block:: python

    # standard SI units ==== DO NOT MODIFY BETWEEN DOUBLE LINES  ============
    #
    # temperature - relative degree, not offset
    K = new_unit("K", 0, "kelvin")
    CELSIUS = new_unit("deg C", K, "degree Celsius")
    FAHR = new_unit("degF", K * 9.0 / 5, "degree Fahrenheit")
    # time
    sec = S = new_unit("sec", 0, "second")
    HZ = new_unit("Hz", 1 / S, "hertz")
    # length
    m = M = new_unit("m", 0, "meter")
    nm = new_unit("nm", 10**-9 * M, "nanometer")
    um = new_unit("um", 10**-6 * M, "micrometer")
    mm = new_unit("mm", 10**-3 * M, "millimeter")
    cm = new_unit("cm", 10**-2 * M, "centimeter")
    dm = new_unit("dm", 10**-1 * M, "decimeter")
    # mass
    kg = KG = new_unit("kg", 0, "kilogram")
    gram = new_unit("gram", 10**-3 * KG, "gram")
    rad = new_unit("rad", M / M, "radian")
    sr = new_unit("sr", M**2 / M**2, "steradian")
    mol = new_unit("mol", 0, "mole")
    # force
    N = new_unit("N", M * KG / S**2, "newton")
    cd = new_unit("cd", 0, "candela")
    lm = new_unit("lm", cd * sr, "lumen")
    lx = new_unit("lx", lm / M**2, "lux")
    # charge
    J = new_unit("J", N * M, "joule")
    W = new_unit("W", J / S, "watt")
    A = new_unit("A", 0, "ampere")
    mA = new_unit("mA", 10**-3 * A, "milliampere")
    C = new_unit("C", S * A, "coulomb")
    VO = new_unit("V", W / A, "volt")
    F = new_unit("F", C / VO, "farad")
    OHM = new_unit("ohm", VO / A, "ohm")
    SIEMENS = new_unit("siemens", A / VO, "siemens")
    WB = new_unit("Wb", VO * SIEMENS, "weber")
    TS = new_unit("TS", WB / M**2, "tesla")
    HENRY = new_unit("H", WB / A, "henry")
    #
    #
    # ============  DO NOT MODIFY FILE ABOVE THIS LINE  ===========================
    #
    # --------------------------------------------------- metric
    #
    g = new_unit("G", 9.80665 * M / S**2, "gravity acceleration")
    # pressure
    PA = new_unit("PA", N / M**2, "pascal")
    MPA = new_unit("MPA", PA * (10**6), "megapascals")
    kPA = new_unit("kPA", PA * (10**3), "kilopascals")
    # force
    kN = new_unit("kN", N * (10**3), "kilonewton")
    MN = new_unit("mN", N * (10**6), "meganewton")
    km = new_unit("kM", M * (10**3), "kilometer")
    kN_m3 = new_unit("kN_m3", kN / (M**3), "kilonewton per cubic meter")
    kN_m = new_unit("kN_m", kN / M, "kilonewton per meter")
    kN_cm = new_unit("kN_cm", kN / cm, "kilonewton per centimeter")
    mkN = new_unit("mkN", (kN * M), "meter-kilonewton")
    # area
    sqm = new_unit("sqm", (M**2), "square meter")
    cm2 = new_unit("cm2", (cm**2), "square centimeter")
    cm3 = new_unit("cm3", (cm**3), "cubic centimeter")
    cm4 = new_unit("cm4", (cm**4), "cm to fourth power")
    #
    # ------------------------------------------------- imperial
    #
    # length
    inch = new_unit("inch", M / 39.370079, "inch")
    ft = new_unit("ft", M / 3.2808399, "foot")
    miles = new_unit("miles", ft * 5280, "miles")
    # mass
    lbm = new_unit("lbm", KG / 2.2046226, "pound-mass")
    # force
    lbf = new_unit("lbf", 4.4482216 * N, "pound-force")
    kips = new_unit("kips", lbf * 1000.0, "kilopound")
    # moments
    ftkips = new_unit("ft-kip", ft * lbf * 1000.0, "foot-kips")
    inkips = new_unit("in-kips", inch * lbf * 1000.0, "inch-kips")
    # linear force
    k_in = new_unit("k_in", kips / inch, "kips per inch")
    k_ft = new_unit("k_ft", kips / ft, "kips per foot")
    p_in = new_unit("lb_in", lbf / inch, "pounds per inch")
    p_ft = new_unit("lb_ft", lbf / ft, "pounds per foot")
    # area
    sf = new_unit("sf", ft**2, "square feet")
    in2 = new_unit("in2", inch**2, "square inches")
    in3 = new_unit("in3", inch**3, "cubic inches")
    in4 = new_unit("in4", inch**4, "inches to fourth")
    # pressure
    p_sf = new_unit("p_sf", lbf / ft**2, "pounds per square foot")
    p_si = new_unit("p_si", lbf / inch**2, "pounds per square inch")
    k_sf = new_unit("k_sf", kips / ft**2, "kips per square foot")
    k_si = new_unit("k_si", kips / inch**2, "kips per square inch")
    # density
    p_ci = new_unit("p_ci", lbf / inch**3, "pounds per cubic inch")
    p_cf = new_unit("p_cf", lbf / ft**3, "pounds per cubic ft")
    # time
    hr = new_unit("hr", 60 * 60 * sec, "hours")
    # velocity
    mph = new_unit("mph", miles / hr, "miles per hour")
    fps = new_unit("fps", ft / sec, "feet per second")

----------------------

.. _rivt-depend:

**[9]** rivt Python Dependencies
---------------------------------------------------------------------------

The minimum Python version is *3.14*. In addition to *rivtlib*, *rivt* packages
include the following categories:

=============================================== ================================
    IDE and REPL                                     description
=============================================== ================================
  "pyzo>=4.20.0"                                   a lightweight IDE
  "ipython>=8.16.2"                                interactive Python shell
  "ipykernel>=6.28.1"                              Jupyter kernel for Python
=============================================== ================================

=============================================== ================================
    Image and Compilation                            description
=============================================== ================================
  "pyside6>=6.10.1"                                QT bindings
  "fastcore>=1.8.16"                               code simplification                                
  "pillow>=11.2.1"                                 image processing
=============================================== ================================

=============================================== ================================
    Symbolic, Numerical Processing                   description
=============================================== ================================
  "matplotlib>=3.10.1"                             data visualization
  "sympy>=1.13.3"                                  symbolic analysis
  "numpy>=2.2.5"                                   numerical processing
  "scipy>=1.16.3"                                  numerical analysis
  "pandas>=2.2.3"                                  data analysis   
=============================================== ================================

=============================================== ================================
    Formatting                                       description
=============================================== ================================
  "tabulate>=0.9.0"                                format tables  
  "docutils>=0.21.2"                               reStructuredText processing  
  "reportlab>=4.4.0"                               PDF document generation
  "rst2pdf>=0.103.1"                               PDF document generation
  "pypdf>=1.0.3"                                   PDF document manipulation
  "Sphinx>=8.2.3"                                  HTML/PDF doc  generation  
  "pydata-sphinx-theme>=0.16.1"                    HTML document generation  
  "sphinx-copybutton>=0.5.2"                       HTML document generation  
  "sphinx_design>=0.6.1"                           HTML document generation  
  "sphinx-favicon>=1.0.1"                          HTML document generation  
  "sphinx-togglebutton>=0.3.2"                     HTML document generation  
  "sphinxcontrib-applehelp>=2.0.0"                 HTML document generation 
  "sphinxcontrib-devhelp>=2.0.0"                   HTML document generation
  "sphinxcontrib-email>=0.3.6"                     HTML document generation
  "sphinxcontrib-htmlhelp>=2.1.0"                  HTML document generation
  "sphinxcontrib-jquery>=4.1"                      HTML document generation
  "sphinxcontrib-jsmath>=1.0.1"                    HTML document generation
  "sphinxcontrib-qthelp>=2.0.0"                    HTML document generation
  "sphinxcontrib-serializinghtml>=2.0.0"           HTML document generation
=============================================== ================================        


.. toctree::
    :maxdepth: 1
    :hidden:

    rvF02-terms.rst
    rvF03-faq.rst
