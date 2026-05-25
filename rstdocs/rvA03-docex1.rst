**A.3 Example**
=========================

**[1]** Example Files
-----------------------------------------------
 
The example files illustrate the common API functions and rivt markup syntax. 
*rivt files* may be published as single documents or compiled into reports. 
Reports are assembled through a customized report script (*rivt-report.py*). 
Examples 1 and 2 are single docs. Example 3 is a small report. They are available

------------------


**[2]** Example 1
----------------------------------------------

This is a single rivt file that publishes a single doc. It illustrates 
the common API functions and rivt markup syntax.


**2-1** rivt file - Ex. 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the *rivt file* for Example 1.

.. code-block:: python

    #! python
    import rivtlib.rvapi as rv

    # rv singledoc: True

    # %% loads
    rv.I("""Load Combinations 

        ASCE 7-05 Load Effects _[T]
        ============= ================================================
        Equation No.    Load Combination
        ============= ================================================
        16-1           1.4(D+F)
        16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
        16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
        ============= ================================================

        | IMAGE | beam.png | Beam Geometry, .65, num

        Bending Stress Formula _[E]
        σ1 = M1 / S1 _[M]

        """)
    # %% values
    rv.V("""Loads and Geometry 

        Beam Loads _[T]
        D_1 =: 3.8*psf | psf, kPA, 2 | joists DL         
        D_2 =: 2.1*psf | psf, kPA, 2 | plywood DL          
        D_3 =: 10.0*psf | psf, kPA, 2 | partitions DL       
        D_4 =: 2*0.5*klf |klf, kN_m , 2 | fixed machinery  DL
        L_1 =: 40*psf | psf, kPA, 2 | ASCE7-O5 LL 
        
        | VALTABLE | beam1-v.csv | Beam Geometry, 0:0, num

        Uniform Distributed Loads
        dl_1 <=: 1.2 * (W_1 * (D_1 + D_2 + D_3) + D_4) | klf, kN_m, 2 | dead load : ASCE7-05 2.3.2  _[E]

        ll_1 <=: 1.6 * W_1 * L_1 | klf, kN_m, 2 | live load : ASCE7-05 2.3.2 _[E]
        
        omega_1 <=: dl_1 + ll_1 | klf, kN_m, 2 | total load : ASCE7-05 2.3.2 _[E]

        """)
    # %% section properties
    rv.V("""Beam Section Properties

        | PYTHON | sectprop.py | nodocstring

        section_1 <=: rectsect(10*inch, 18*inch) | in3, cm3, 2 | function: rect sect modulus _[E]

        inertia_1 <=: rectinertia(10*inch, 18*inch) | in4, cm4, 1 | function: rect moment inertia _[E]

        """)
    # %% force
    rv.V("""Force and Stress
            
            m_1 <=: omega_1 * S_1**2 / 8 | ftkips, mkN, 2 | mid-span UDL moment _[E]

            fb_1 <=: m_1 / section_1 | psi, MPA, 1 | bending stress _[E]

            fb_1 < 10*ksi | ok, not ok, blue, red, right _[E]
        
        """)
    # %% tool
    rv.T("""Metadata

        _[[PYTHON]] 
        rv_metaD = {
        "authors": "rholland",
        "version": "0.7.2",
        "email": "rod.h.holland@gmail.com",
        "repo": "https://github.com/rivt-info/rivt-single-doc",
        "license": "https://opensource.org/license/mit/",
        "fork1": ["author", "version", "email", "repo"],
        "fork2": [],
        }
        _[[END]]

        """)
    # %% doc
    rv.D("""Publish Doc 

        _[[LAYOUT]]
            logopathP: logo.png 
            pdfheaderL: [docnameS, pageS, totalpageS]
            footerL: [logoO, dateO, timeO, filenameS, versionS]
        _[[END]]
        
        | PUBLISH | rivt | rst2pdf

        """)

--------------------------


**2-2** Example 1 - text doc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

This is the output for Example 1.


.. code-block:: text

    this is a code block
 


**[3]** Example 2
-------------------------

 This is a report. It illustrates use of the rivt-report.py script.
 


 

