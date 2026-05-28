**A.2 Example 1**
=========================

.. _rivt-examples:

**[1]** Examples
-----------------------------------------------
 
Three examples are provided.

- Example 1
    This single doc example file illustrates common API functions and rivt
    markup. The %% marks indicate sections that can be interactively processed
    as cells (similar to a Jupyter Notebook). They can be created with a
    shortcut provided by *rivt extensions* . They also provide an interactive
    table of contents for navigating in VSCode.  

    The rivt file is followed by a screenshot of the same rivt file in VSCode 
    with syntax highlights, and the rivt text doc output.

    - The entire project can be downloaded here or here. 
    - The PDF output is here.
    - The HTML output is here.

- Example 2
    A single doc example that illustrates use of Python functions,

- Example 3
    An example *rivt report*. Reports are assembled through a customized 
    report script - *rivt-report.py* stored in the *rivt-report* folder.

---------------------

**[2]** rivt file - Ex. 1
--------------------------------------------------

.. code-block:: python

    # %% import
    import rivtlib.rvapi as rv

    # The following settings are needed if defaults (in parenthesis) need to
    # be changed. A leading hash (#) and trailing semicolon (;) are required.

    # rv set_width = 80  ; character width of text output (80)
    # rv no_tag = true ; if false, an API tag is added to section number (true)


    # %% rv.I("""Summary
    rv.I("""Summary  

        This rivt file example calculates the maximum stress and deflection in a
        simply supported, uniformly loaded beam. It also serves as an annotated
        example of a rivt doc with multiple sections that is not part of a report.

        The example illustrates the use of some of the most common API functions,
        commands and tags. Further details are provided in the 
        _[U] rivt user manual, https://www.rivt.info].

        The file may be formatted as a text, PDF or HTML doc by changing the type
        parameter in the PUBLISH command at the end of each rivt file (Doc-API
        *rv.D*). Published files are found in the *_published* folder.

        """)

    # %% rv.I("""Load Combinations
    rv.I("""Load Combinations 

        ## Indented comments with double hashes will not appear in the doc
        ## An inline table contained in a TABLE block is written to a CSV file. 
        _[[TABLE]]  ASCE 7-05 Load Effects
        ============= ================================================
        Equation No.    Load Combination
        ============= ================================================
        16-1           1.4(D+F)
        16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
        16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
        ============= ================================================
        _[[END]]

        """)

    # %% rv.V("""Loads and Geometry
    rv.V("""Loads and Geometry 
        
        Successive value definitions are formatted as a table. Variable
        values are defined with the define operator. The line tag [T] labels and
        numbers the table.
        
        Define Unit Loads _[T]
        D_1 ==: 3.8 * psf | psf, kPA, 2 | joists DL         
        D_2 ==: 2.1 * psf | psf, kPA, 2 | plywood DL          
        D_3 ==: 10.0 * psf | psf, kPA, 2 | partitions DL       
        D_4 ==: 2 * 1.5 * klf | klf, kN_m, 2 | fixed machinery DL
        L_1 ==: 40 * psf | psf, kPA, 2 | ASCE7-O5 LL
        b_1 ==: 10 * inch | inch, mm, 2 | beam width
        h_1 ==: 18 * inch | inch, mm, 2 | beam depth
        E_1 ==: 29000 * ksi | ksi, MPA, 2 | modulus of elasticity
        Fb_1 ==: 20000 * psqin | psqin, MPA, 2 | allowable stress   
        
        The VALTABLE command reads variable values from a file in the rvsrc
        folder. The description is used as the table title. The range specifies the
        starting and ending line to be read from the file (0:0 means all lines).

        | VALTABLE | rvsrc/beam1.csv | Beam Geometry, 0:0

        ## The IMAGE command inserts an image file with caption, % scale, num;non option 
        | IMAGE | rvsrc/beam1.png | Beam Diagram, 60, num

        Uniform Distributed Loads _[C]
        dl_1 <=: 1.2 * (spc_1 * (D_1 + D_2 + D_3) + D_4) | klf, kN_m, 2 | Dead load [ASCE7-05 2.3.2]

        ll_1 <=: 1.6 * spc_1 * L_1 | klf, kN_m, 2 | Live load [ASCE7-05 2.3.2]
        
        omega_1 <=: dl_1 + ll_1 | klf, kN_m, 2 | Total load [ASCE7-05 2.3.2]
        
        """)

    # %% rv.V("""Beam Stress
    rv.V("""Beam Response

        The following lines import the beam geometry from an external file, 
        calculate section properties from imported functions and calculate 
        the maximum moment, bending stress and mid-span deflection. 

        | PYTHON | rvsrc/sectprop.py | Beam functions

        section_1 :=: rectsect(b_1, h_1) | in3, cm3, 2 | rectangle - S (sectprop.py)

        inertia_1 :=: rectinertia(b_1, h_1) | in4, cm4, 1 | rectangle - I (sectprop.py)

        | IMAGE2 | rvsrc/ss-beam2.png, rvsrc/ss-beam1.png | Moment diagram, Deflection diagram,46,54,num,num

        ##  The line tag [M] formats the equation using utf-8 text.
        σ1 = M1 / S1 _[M]  Maximum bending stress  formula
            
        m_1 <=: omega_1 * spn_1**2 / 8 | ftkips, mkN, 2 | Mid-span UDL moment 
        
        fb_1 <=: m_1 / section_1 | psqin, MPA, 1 | Bending stress 

        fb_1 < Fb_1 | ksi, 2, OK, >>> NOT OK | Stress ratio 

        delta_1 :=: midspan_delta(spn_1, omega_1, E_1, inertia_1) | inch, mm, 2 | mid-span deflection (sectprop.py)

        """)


    # %% rv.D("""Publish Doc
    rv.D("""Publish Doc 
        
        A rivt file may be published as a text, PDF or HTML doc by changing the
        PUBLISH type parameter to text, pdf or html. The PUBLISH command follows the
        METADATA block. 
        
        Published files are found in sub-folders of the _published folder. A text
        version of the doc or report is is always written to the rivt and
        _rivt-public folders as a README.txt file which is displayed on the
        first page of a GitHub repo. 
        
        _[[METADATA]] 
        [doc]
        authors = R Holland
        version = 1.0.0a11
        repo = https://github.com/rivt-info/rivt-single-doc
        license = https://opensource.org/license/mit/
        copyright = -
        fork1_authors = -
        fork1_version = -
        fork1_repo = -
        fork1_license = https://opensource.org/license/mit/
        
        [layout]
        title = UDL Beam
        subtitle =  Example 1 - rivt Doc  
        copyright = --
        client = Attn: User Example
        coverlogo = rvsrc/logo1.png
        coverlogo_size = 50
        runninglogo = rvsrc/logo2.png
        runninglabel = rivt
        project_ref = proj. 0001
        pdf_pagesize = letter
        pdf_margins = 1in, 1in, 1in, 1in 
        pdf_link_underline = true

        [process]
        private_heading = true ; if false, default heading changed to public
        keep_files = true ; if false, files in folders with leading "_" are deleted
        auto_cfg = true ; if false, config files are not updated from rivt file
        _[[END]]
        
        | PUBLISH | Example 1 - rivt Doc | pdf

        """)

--------------------------


**[3]** Screenshot - VSCode rivt file
--------------------------------------
    
    
**rivt file in VSCode (click and zoom to enlarge)**


.. figure::  _static/img/example1.png
    :class: dark-light
    :scale: 25%
    :align: center
    :alt: rivt file



-----------------------------


**[4]** rivt text doc
-------------------------------------------------

This is the text form of the *doc*.

- The *PDF doc* is here.
- The *HTML doc* is here.

.. code-block:: text

    --------------------------------------------------------------------------------
    Example 1 - rivt Doc | R Holland | v-1.0.0a11 | 2026-05-27 - 08:45AM
    --------------------------------------------------------------------------------


    1.1  Summary
    --------------------------------------------------------------------------------
    
    This rivt file example calculates the maximum stress and deflection in a
    simply supported, uniformly loaded beam. It also serves as an annotated
    example of a rivt doc with multiple sections that is not part of a report.
    
    The example illustrates the use of some of the most common API functions,
    commands and tags. Further details are provided in the
    rivt user manual, https://www.rivt.info .
    
    The file may be formatted as a text, PDF or HTML doc by changing the type
    parameter in the PUBLISH command at the end of each rivt file (Doc-API
    *rv.D*). Published files are found in the *_published* folder.
    
    

    1.2  Load Combinations
    --------------------------------------------------------------------------------
    
    Table 1: ASCE 7-05 Load Effects (stored: t001-1.csv)
    ============= ================================================ 
    Equation No.    Load Combination 
    ============= ================================================ 
    16-1           1.4(D+F) 
    16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R) 
    16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W) 
    ============= ================================================ 

    
    

    1.3  Loads and Geometry
    --------------------------------------------------------------------------------
    
    Successive value definitions are formatted as a table. Variable
    values are defined with the define operator. The line tag [T] labels and
    numbers the table.
    

    Table 2: Define Unit Loads
    ==========  ===============  =============  =====================
    variable    value            [value]        description
    ==========  ===============  =============  =====================
    D_1         3.80 psf         0.18 kPA       joists DL
    D_2         2.10 psf         0.10 kPA       plywood DL
    D_3         10.00 psf        0.48 kPA       partitions DL
    D_4         3.00 klf         43.78 kN_m     fixed machinery DL
    L_1         40.00 psf        1.92 kPA       ASCE7-O5 LL
    b_1         10.00 inch       254.00 mm      beam width
    h_1         18.00 inch       457.20 mm      beam depth
    E_1         29000.00 ksi     199947.96 MPA  modulus of elasticity
    Fb_1        20000.00 lb_in2  137.90 MPA     allowable stress
    ==========  ===============  =============  =====================
    
    The VALTABLE command reads variable values from a file in the rvsrc
    folder. The description is used as the table title. The range specifies the
    starting and ending line to be read from the file (0:0 means all lines).
    

    Table 3: Beam Geometry (rvsrc/beam1.csv)
    ==========  ========  =========  =============
    variable    value     [value]    description
    ==========  ========  =========  =============
    spc_1       2.00 ft   0.61 m     beam spacing
    spn_1       16.00 ft  4.88 m     beam span
    ==========  ========  =========  =============

    
            ----------------------------------------
    Fig. 1 - Beam Diagram
            ----------------------------------------

    
                            Uniform Distributed Loads                            


    ┌  Eq-1 | Dead load [ASCE7-05 2.3.2]
    │
    │     dl₁ = 1.2⋅(D₄ + spc₁⋅(D₁ + D₂ + D₃))
    └

    dl₁ = 3.64 klf    [dl₁] = 53.09 kN_m  | Dead load [ASCE7-05 2.3.2]

    ==================  ============  =========  =============  ==========
    D₄                  spc₁          D₁         D₃             D₂
    ==================  ============  =========  =============  ==========
    3.00 klf            2.00 ft       3.80 psf   10.00 psf      2.10 psf
    —————               —————         —————      —————          —————
    fixed machinery DL  beam spacing  joists DL  partitions DL  plywood DL
    ==================  ============  =========  =============  ==========
    

    ┌  Eq-2 | Live load [ASCE7-05 2.3.2]
    │
    │     ll₁ = 1.6⋅L₁⋅spc₁
    └

    ll₁ = 0.13 klf    [ll₁] = 1.87 kN_m  | Live load [ASCE7-05 2.3.2]

    ===========  ============
    L₁           spc₁
    ===========  ============
    40.00 psf    2.00 ft
    —————        —————
    ASCE7-O5 LL  beam spacing
    ===========  ============
    

    ┌  Eq-3 | Total load [ASCE7-05 2.3.2]
    │
    │     ω₁ = dl₁ + ll₁
    └

    ω₁ = 3.77 klf    [ω₁] = 54.96 kN_m  | Total load [ASCE7-05 2.3.2]

    ==========================  ==========================
    ll₁                         dl₁
    ==========================  ==========================
    128.00 ft·psf               3.64 klf
    —————                       —————
    Live load [ASCE7-05 2.3.2]  Dead load [ASCE7-05 2.3.2]
    ==========================  ==========================
    
    

    1.4  Beam Response
    --------------------------------------------------------------------------------
    
    The following lines import the beam geometry from an external file,
    calculate section properties from imported functions and calculate
    the maximum moment, bending stress and mid-span deflection.
    

    Table 4: Beam functions (rvsrc/sectprop.py)

    ==========================  =====================================================
    Function                    Docstring
    ==========================  =====================================================
    rectsect(b, d)              section modulus of rectangle
    rectinertia(b, d)           moment of inertia of rectangle
    midspan_delta(ln, w, e, i)  mid-span deflection of simply supported beam with UDL
    ==========================  =====================================================

    

    ┌  Eq-4 | rectangle - S (sectprop.py)
    │
    │     section₁ = rectsect(b₁, h₁)
    └

    section₁ = 540.00 in3   [section₁] = 8849.01 cm3  | rectangle - S (sectprop.py)

    ==========  ==========
    h₁          b₁
    ==========  ==========
    18.00 inch  10.00 inch
    —————       —————
    beam depth  beam width
    ==========  ==========
    

    ┌  Eq-5 | rectangle - I (sectprop.py)
    │
    │     inertia₁ = rectinertia(b₁, h₁)
    └

    inertia₁ = 4860.0 in4   [inertia₁] = 202288.5 cm4  | rectangle - I (sectprop.py)

    ==========  ==========
    h₁          b₁
    ==========  ==========
    18.0 inch   10.0 inch
    —————       —————
    beam depth  beam width
    ==========  ==========
    
            ----------------------------------------
    Fig. 2 - Moment diagram  | Fig. 3 - Deflection diagram   
    files: rvsrc/ss-beam2.png, rvsrc/ss-beam1.png
            ----------------------------------------

    
    ┌  Eq-6 |   Maximum bending stress  formula
    │
    │          M₁
    │     σ₁ = ──
    │          S₁
    └


    

    ┌  Eq-7 | Mid-span UDL moment
    │
    │                 2
    │          ω₁⋅spn₁ 
    │     m₁ = ────────
    │             8    
    └

    m₁ = 120.52 ftkip    [m₁] = 163.40 mkN  | Mid-span UDL moment

    =========  ===========================
    spn₁       ω₁
    =========  ===========================
    16.00 ft   3.77 klf
    —————      —————
    beam span  Total load [ASCE7-05 2.3.2]
    =========  ===========================
    

    ┌  Eq-8 | Bending stress
    │
    │              m₁   
    │     fb₁ = ────────
    │           section₁
    └

    fb₁ = 2678.2 lb_in2    [fb₁] = 18.5 MPA  | Bending stress

    ===========================  ===================
    section₁                     m₁
    ===========================  ===================
    540.0 inch3                  120.5 ft2·klf
    —————                        —————
    rectangle - S (sectprop.py)  Mid-span UDL moment
    ===========================  ===================
    
    ┌  Eq-9 | Stress ratio
    │
    │     fb_1 < Fb_1
    └

    ▮  ========  =========  ===========  =======  ============
    ▮  fb₁       Fb₁        ratio L/R    check    reference
    ▮  ========  =========  ===========  =======  ============
    ▮  2.68 ksi  20.00 ksi  0.133908     OK       Stress ratio
    ▮  ========  =========  ===========  =======  ============


    

    ┌  Eq-10 | mid-span deflection (sectprop.py)
    │
    │     δ₁ = midspan_δ(spn₁, ω₁, E₁, inertia₁)
    └

    δ₁ = 0.04 inch   [δ₁] = 1.00 mm  | mid-span deflection (sectprop.py)

    =========  ===========================  =====================  ===========================
    spn₁       ω₁                           E₁                     inertia₁
    =========  ===========================  =====================  ===========================
    16.00 ft   3.77 klf                     29000.00 ksi           4860.00 inch4
    —————      —————                        —————                  —————
    beam span  Total load [ASCE7-05 2.3.2]  modulus of elasticity  rectangle - I (sectprop.py)
    =========  ===========================  =====================  ===========================
 
 
