**D.4 Example**
=========================

**[1]** rivt file
-----------------------------------------------


.. raw:: html

    <hr>

This is a small rivt file that publishes a single *doc* The report folders are
not used. It has 4 API functions - two of them are
published. The output is written to the terminal.

.. raw:: html

    <hr>

.. code-block:: python

    #! python
    # %% Start
    import rivtlib.rvapi as rv

    rv.M("""Meta Data
        
        rv_authD = {
            "authors": "rholland",
            "version": "0.6.1",
            "email": "rod.h.holland@gmail.com",
            "repo": "https://github.com/rivt-info/rivt-simple-single-doc",
            "license": "https://opensource.org/license/mit/",
            "fork1": ["", "", "", ""],
            }
        
        rv_headerL = ["date", "time", "file", "version"]

        rv_localB = True
        
        """)

    rv.I("""Load Combinations

        ASCE 7-05 Load Effects _[T]

        =============   ==============================================
        Equation No.    Load Combination
        =============   ==============================================
        16-1            1.4(D+F)
        16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
        16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
        =============   ==============================================

        | IMG | beam.png | 0.35, Beam Geometry _[F]
        """)

    # %%
    rv.V("""UDL and Beam Geometry

        Beam Loads and Properties _[T]
        D_1 := 3.8*PSF | PSF, KPA, 2 | joists DL         
        D_2 := 2.1*PSF | PSF, KPA, 2 | plywood DL          
        D_3 := 10.0*PSF | PSF, KPA, 2 | partitions DL       
        D_4 := 2*0.5*KLF | KLF, KNLM, 2 | fixed machinery  DL
        L_1 := 40*PSF | PSF, KPA, 2 | ASCE7-O5 LL 
        
        | VALUE | beam1-v.csv | Beam Geometry _[T]

        Total UDL factored dead load  _[E]
        dl_1 <= 1.2 * (W_1 *(D_1 + D_2 + D_3) + D_4) | KLF, KNLM, 2 | ASCE7-05 Eq. 16-2

        Total UDL factored live load  _[E]
        ll_1 <= 1.6 * W_1 * L_1 | KLF, KNLM, 2 | ASCE7-05 Eq. 16-2
        
        Total Load  _[E]
        omega_1 <= dl_1 + ll_1 | KLF, KNLM, 2 | ASCE7-05 Eq. 16-2

        Bending moment at mid-span  _[E]
        m_1 <= omega_1 * S_1**2 / 8 | KIP_FT, KN_M, 2 | mid-span UDL moment 

        """)

    # %%
    rv.S("""Publish Doc 

        | DOC | . | text, rivtdoc1.ini 
        
        """)

.. raw:: html

    <p id="api">&lt;i&gt;</p>

**[2]** Terminal output
-------------------------

.. raw:: html

    <hr>


.. code-block:: bash


    ----------------------------------------------------------
    rivtlib version: 0.6.1
    rivt file: rv000-simple-doc.py
    rivt file path: C:\Users\rodhh\rivt-doc1\example1
    ----------------------------------------------------------



    2025-10-10 | 05:54AM      rv000-simple-doc.py                           av-0.6.1
    ================================================================================


    [ 1 ] Load Combinations
    --------------------------------------------------------------------------------



    Table 1: ASCE 7-05 Load Effects

    =============   ==============================================
    Equation No.    Load Combination
    =============   ==============================================
    16-1            1.4(D+F)
    16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    =============   ==============================================

    <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=860x334 at 0x1376E1282F0>
    Fig. 1 -  Beam Geometry   [file: C:/Users/rodhh/rivt-doc1/example1/beam.png ]



    [ 2 ] UDL and Beam Geometry
    --------------------------------------------------------------------------------



    Table 2: Beam Loads and Properties

    ==========  =========  ==========  ===================
    variable        value     [value]  description
    ==========  =========  ==========  ===================
    D_1          3.80 psf    0.18 kpa  joists DL
    D_2          2.10 psf    0.10 kpa  plywood DL
    D_3         10.00 psf    0.48 kpa  partitions DL
    D_4            kip/ft  14.59 kN/m  fixed machinery  DL
    L_1         40.00 psf    1.92 kpa  ASCE7-O5 LL
    ==========  =========  ==========  ===================


    Table 3 - Beam Geometry[from file: beam1-v.csv]

    ==========  ========  =========  =============
    variable       value    [value]  description
    ==========  ========  =========  =============
    W_1          2.00 ft     0.61 m  beam spacing
    S_1         14.00 ft     4.27 m  beam span
    ==========  ========  =========  =============



    Eq. 1 - Total UDL factored dead load
                                                                ASCE7-05 Eq. 16-2
        dl₁ = 1.2⋅D₄ + 1.2⋅W₁⋅(D₁ + D₂ + D₃)

    ===========  ==========  ========  ========  =======  ======  =========
    dl_1       [dl_1 ]      D_2       D_1       W_1     D_4       D_3
    ===========  ==========  ========  ========  =======  ======  =========
    1.24 kip/ft  18.07 kN/m  2.10 psf  3.80 psf  2.00 ft  kip/ft  10.00 psf
    ===========  ==========  ========  ========  =======  ======  =========


    Eq. 2 - Total UDL factored live load
                                                                ASCE7-05 Eq. 16-2
        ll₁ = 1.6⋅L₁⋅W₁

    ===========  =========  =======  =========
    ll_1       [ll_1 ]     W_1       L_1
    ===========  =========  =======  =========
    0.13 kip/ft  1.87 kN/m  2.00 ft  40.00 psf
    ===========  =========  =======  =========


    Eq. 3 - Total Load
                                                                ASCE7-05 Eq. 16-2
        dl₁ = -ll₁ + ω₁

    ===========  ============  =============  ===========
    omega_1      [omega_1 ]       ll_1          dl_1
    ===========  ============  =============  ===========
    1.37 kip/ft   19.94 kN/m   128.00 ft·psf  1.24 kip/ft
    ===========  ============  =============  ===========


    Eq. 4 - Bending moment at mid-span
                                                                mid-span UDL moment
            2
            S₁ ⋅ω₁
        m₁ = ──────
            8

    ============  ==========  ===========  ========
        m_1         [m_1 ]      omega_1      S_1
    ============  ==========  ===========  ========
    33.47 kip-ft  45.38 kN-m  1.37 kip/ft  14.00 ft
    ============  ==========  ===========  ========



    [Publish Doc] : section skipped
