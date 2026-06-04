**A.2 | Example 2**
=========================

.. _rivt-example2:

**[1]** Example 2 - single doc
-----------------------------------------------

This example file illustrates use of external functions. 

- The entire project can be downloaded here or here.
- The PDF output is here.
- The HTML output is here.

------------------


**[2]** rivt file - Ex. 2
--------------------------------------------------

.. code-block:: python


    #! python
    # %% import
    import rivtlib.rvapi as rv

    # The following settings are needed if defaults (in parenthesis) need to
    # be changed. A leading hash (#) and trailing semicolon (;) are required.

    # rv set_width = 80  ; character width of text output (80)
    # rv no_tag = true ; if false, an API tag is added to section number (true)

    # %% project description
    rv.I("""Project description
        
        Design of embedded pole foundation for the flagpole design example in
        Appendix A of NAAMM/FP 1001-07, "Guide Specifications for Design of Metal
        Flagpoles" Embedded pole foundation design is per 2024 IBC Eq 6-1 and Table
        18-I-A. Soil properites are per Table 1806.2 in the 2024 IBC

    """)

    # %% design input
    rv.V("""Design input 
        

        | IMAGE | rvsrc/image1.png | Calculation Diagram, 30, num 

        Design input _[T]
        Mbase ==: 24.835 * ftkips |ftkips, mkN, 2 | moment at base of flagpole
        P ==: 24.835 * kips |kips,kN,2| horizontal load
        b ==: 24 * inch |inch, cm, 2 | width of concrete drilled pier
        PFP ==: 200 * pcf | pcf, kN_m3, 2| allowable lateral bearing pressure - sandy gravel  
        h ==: 1 * ft | ft, m, 2| height
        d ==: 10 * ft | ft, m, 2| initial guess for embedment depth   

        ## add d as an argument to carry units in function
        | PYTHON | rvsrc/pole_embed.py | Iterative functions
        
        depth_1 :=: Depth_nonconstrained (d, P, h, b, PFP, 2) | ft, m, 2 | Required embed - nonconstrained
        
        depth_2 :=: Depth_constrained (d, P, h, b, PFP) | ft, m, 2 | Required embed - constrained

    """)

    # %% publish doc
    rv.D("""Publish doc

        _[[METADATA]] 
        [doc]
        authors = R Ward
        version = 1.0.0a11
        repo = -
        license = https://opensource.org/license/mit/
        copyright = -
        fork1_authors = -
        fork1_version = -
        fork1_repo = -
        fork1_license = https://opensource.org/license/mit/

        [layout]
        title = UDL Beam
        subtitle =  Example 2 - rivt Doc  
        copyright = --
        client = User Example
        coverlogo = logo2.png
        coverlogo_size = 50
        runninglogo = rwlogo.png
        runninglabel = Robert Ward SE
        project_ref = proj. 0001
        pdf_pagesize = letter
        pdf_margins = 1in, 1in, 1in, 1in 
        pdf_link_underline = true

        [process]
        private_heading = true ; if false, default heading changed to public
        keep_files = true ; if false, files in folders with leading "_" are deleted
        auto_cfg = true ; if false, config files are not updated from rivt file
        _[[END]]
        

        | PUBLISH | Flag Pole Foundation | text

    """)

--------------------------


**[3]** rivt text doc
-------------------------------------------------

This is the text form of the *doc*.

- The *PDF doc* is here.
- The *HTML doc* is here.

.. code-block:: text

    --------------------------------------------------------------------------------
    Flag Pole Foundation | R Ward | v-1.0.0a11 | 2026-05-28 - 01:12AM
    --------------------------------------------------------------------------------


    0.1  Project description
    --------------------------------------------------------------------------------
    
    Design of embedded pole foundation for the flagpole design example in
    Appendix A of NAAMM/FP 1001-07, "Guide Specifications for Design of Metal
    Flagpoles" Embedded pole foundation design is per 2024 IBC Eq 6-1 and Table
    18-I-A. Soil properites are per Table 1806.2 in the 2024 IBC
    
    

    0.2  Design input
    --------------------------------------------------------------------------------
    
    
            ----------------------------------------
    Fig. 1 - Calculation Diagram
            ----------------------------------------

    

    Table 1: Design input
    ==========  ===========  ===========  =================================================
    variable    value        [value]      description
    ==========  ===========  ===========  =================================================
    Mbase       24.84 ftkip  33.67 mkN    moment at base of flagpole
    P           24.84 kips   110.47 kN    horizontal load
    b           24.00 inch   60.96 cm     width of concrete drilled pier
    PFP         200.00 pcf   31.42 kN_m3  allowable lateral bearing pressure - sandy gravel
    h           1.00 ft      0.30 m       height
    d           10.00 ft     3.05 m       initial guess for embedment depth
    ==========  ===========  ===========  =================================================
    

    Table 2: Iterative functions (rvsrc/pole_embed.py)

    ============================================  ================================================
    Function                                      Docstring
    ============================================  ================================================
    Depth_nonconstrained(d, P, h, dia, PFP, tol)  Calculate required pole embedment using Eq. 18-1
    Depth_constrained(d, P, h, dia, PFP)          Calculate required pole embedment using Eq. 18-2
    ============================================  ================================================

    

    ┌  Eq-1 | Required embed - nonconstrained
    │
    │     depth₁ = Depth_nonconstrained(d, P, h, b, PFP, 2)
    └

    depth₁ = 15.28 ft   [depth₁] = 4.66 m  | Required embed - nonconstrained

    ===============  ======  =========================  ===========================  ==============================
    P                h       PFP                        d                            b
    ===============  ======  =========================  ===========================  ==============================
    24.84 kips       ft      200.00 pcf                 10.00 ft                     24.00 inch
    —————            —————   —————                      —————                        —————
    horizontal load  height  allowable lateral bearing  initial guess for embedment  width of concrete drilled pier
    -                -       pressure - sandy gravel    depth                        -
    ===============  ======  =========================  ===========================  ==============================
    

    ┌  Eq-2 | Required embed - constrained
    │
    │     depth₂ = Depth_constrained(d, P, h, b, PFP)
    └

    depth₂ = 6.41 ft   [depth₂] = 1.95 m  | Required embed - constrained

    ===============  ======  =========================  ===========================  ==============================
    P                h       PFP                        d                            b
    ===============  ======  =========================  ===========================  ==============================
    24.84 kips       ft      200.00 pcf                 10.00 ft                     24.00 inch
    —————            —————   —————                      —————                        —————
    horizontal load  height  allowable lateral bearing  initial guess for embedment  width of concrete drilled pier
    -                -       pressure - sandy gravel    depth                        -
    ===============  ======  =========================  ===========================  ==============================
    
    
    