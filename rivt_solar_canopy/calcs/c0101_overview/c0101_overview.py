#! python
# %%
import rivt.rivtapi as rv

rv.R("""Overview | Solar Canopy - Loads | inter | 1

    This permitting document describes the structural design of a solar canopy
    located on a residential site in the City of Larkspur, County of Marin,
    California. The document includes the structural design of a concrete slab
    and stem wall, a steel tube frame, and attachment of solar panels to the
    frame.
    
    || project | proj_info.txt | default

    The report is divided into four divisions:

    - 01 Loads
    - 02 Foundation
    - 03 Frame
    - 04 Panel clips

    """)
# %%
rv.I("""-Building Codes and Site | default
    
    The canopy is under the approval jurisdiction of the City of Fairfax,
    California which adopted the 2019 California Building Code [CBC] and the
    2019 California Residential Code [CRC] as the basis for permiting
    construction work. The canopy is designed under the requirements of the
    CBC.

    || table | cbc2019_stds.xlsx | 53,L | [:]
    
    || image2 | site01.jpg | 35 | site02.jpg | 35 
    Site map - Marin County web site [f]_
    Site map - Google Earth [f]_

    _[new]
    
    
    """)

rv.V("""Load Combinations 
 
    Basic loads and load combinations are derived from the California Building
    and Residential Codes.

    || table | load_types01.csv | 30,L | [:]

    || table | asce7_load_comb.csv | 55,C | [:]

    [page]_
    
    """)
# %%
rv.V("""Gravity Loads and Seismic Mass
 
    || config | nosub | 2,2
    
                                                       Roof unit dead loads [t]_
    || value | dlroof0.csv

                                                      Floor unit dead loads [t]_
    || value | dlfloor0.csv

                                              Interior wall unit dead loads [t]_
    || value | dlintwall0.csv

                                              Exterior wall unit dead loads [t]_
    || value | dlextwall0.csv
    
                                                                      Areas [t]_
    arearf1 = 1700             | SF, SM | roof area 
    areaflr1 = 1200            | SF, SM | floor area
    htwall1 = 9                | FT, M    | wall height   
    lenwall1 = 110             | FT, M    | interior wall length 
    lenwall2 = 155             | FT, M    | exterior wall length 2

    Roof weight [e]_                    
    rfwt1 = arearf1 * roofdl1                           |LBF, KN

    Floor weight [e]_
    flrwt1 = areaflr1 * floordl1                        |LBF, KN   

    Partition weight [e]_
    partwt1 =  htwall1 * lenwall1 * intwalldl1          |LBF, KN

    Exterior wall weight [e]_                               
    exwallwt1 = htwall1 * lenwall2 * extwalldl1         |LBF, KN

    Total building weight [e]_
    totwt1 = rfwt1 + flrwt1 + partwt1 + exwallwt1       |LBF, KN
    
    """)
# %%
rv.V("""Material Densities - Seismic Models

    Because the T&G roof is relatively more flexible, the effective floor load
    for seismic models is calculated as the sum of the floor and all of the
    partition weight.

    Floor load including partitions [e]_  
    eflrdl1 = (flrwt1 + partwt1)/(areaflr1)             |PSF, KPA

    Effective floor, roof and wall densities [e]_  
    eflrdens1 = eflrdl1/(0.5*IN)                        |PCI, KNCM

    erfdens1 = roofdl1/(1.5*IN)                         |PCI, KNCM

    ewalldens1 = extwalldl1/(0.5*IN)                    |PCI, KNCM
    
    """)
# %%
rv.V("""References 
 
    || insert | text | references.txt | literal

    [page]_

    """)

rv.V("""-Drawing List 
 
    || insert | text | drawing_list.txt | literal

    || inset | image | residence01.jpg | 90
    Residence and Carport [f]_

    [page]_

    """)

rv.T("""-Math and Text Abbreviations 
 
    || insert | text | abbrev_all.txt | raw

    """)
