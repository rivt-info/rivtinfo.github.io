# %%
import rivtlib.rv_lib as rv
rv.D("dev", "default", "Residence Seismic Model", "24")

rv.I("""[01]  Seismic Demands for Exterior Walls

    || image | mode01.jpg | 100
    First Mode Deformation (visually amplified) [f]_

    || image | mode02.jpg | 100
    Second Mode Deformation (visually amplified) [f]_

    || image | mode03.jpg | 100
    Third Mode Deformation (visually amplified) [f]_

    || image | w107.jpg | 90
    SW7 - South Shear Wall Elements SW101 [f]_

    || image | w102_104_106.jpg | 90
    SW2, SW4, SW6 West Shear Wall Elements - SW102, SW104, SW106 [f]_

    || image | w101.jpg | 90
    SW1 North Shear Wall Elements - SW101 [f]_

    || image | w108_109.jpg | 90
    SW8 East Shear Wall Elements - SW108 [f]_

    ETABS Input Summary [t]_
    || text | res_summ.txt | literal

    ETABS Eigenvalues [t]_
    || text | res_eig.txt | literal

    ETABS Story Shears [t]_
    || text | story_shear.txt | literal
    
    ETABS Force and Displacement Summary [t]_
    || text | res_summ.txt | literal

    ETABS Eigenvalues [t]_
    || text | res_eig.txt | literal

    ETABS Story Shears [t]_
    || text | story_shear.txt | literal

    """)
rv.V("""[02]  Seismic Capacities and D-C ratios for Exterior Walls
 
    || table | awc4_3a.csv | 60,L | [:]
    
    || table | awc4_335adjust.csv | 60,L | [:]

    || text | awc4_335adjust.txt | literal

     From table 4.3A the nominal unit strength of the shear walls is 520 plf.
     From table 4.3.3.5 the effective strength is between 50 and 100 percent of
     the nominal strength.

    || table | ext_shearwall.csv | 60,L | [:]

    [page]_

    **D-C ratios are shown for 6" oc boundary nails and estimated DC ratios if
    the existing 12" oc nailing is taken to have half the capacity. If the
    capacity is reduced by half to account for the 12" oc boundary nailing the
    shear walls have the capacity to meet the design loads.**
    
    || table | first_shear_dc.csv | 60,L | [:]

    """)
# %%
rv.I("""[03]  Seismic D-C ratios for Foundation Walls

    Foundation retrofits included Simpson retrofit foundation plates (URFP) and
    plywood shear walls with boundary nailing at 4" oc (see table 0201.05).  The
    URFP capacity is 1500 lbs and the shear wall capacity is 960 plf.

    || image | north_fnd.jpg | 90
    SW1 - North Elevation URFP [f]_     

    || image | west_fnd.jpg | 90
    SW4, SW6 - West Elevation URFP [f]_     

    || image | sw11_sw12.jpg | 90
    SW11, SW12 - South Elevation [f]_     

    || image | sw13_sw14.jpg | 90
    SW13, SW14 - East Elevation [f]_     

    || table | fnd_shear_dc.csv | 30,L | [:]
         
    """)
