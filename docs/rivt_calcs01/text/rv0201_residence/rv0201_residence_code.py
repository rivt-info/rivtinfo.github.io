#! python
# %%
import rivtcalc.calc as rv

rv.D("dev", "default", "Code Minimums - Residence Renovations", "14")

# %%
rv.V("""[01]  Minimum Wall Sheathing CRC - First Floor
 
    The residence is sheathed in exterior 1/2" 5-ply plywood nailed with 8d
    common nails at 12" oc at edges and field. The boundary nailing capacity is
    half of the maximum spacing tabulated in the building codes. The residence
    is checked against the CRC prescriptive wall opening limits, assuming 6" oc
    (which is not the case) to assess the degree of wall continuity. A CBC
    analysis is performed in calculation 0301 which estimates the DC ratios for
    the 12" oc nailing.

    || image | mv_nail1a.jpg, mv_nail2a.jpg |40,56
    Existing shear wall nailing - 8d at 12" OC [f]_
    Existing shear wall nailing - 8d - 2-1/2" penetration [f]_

    The minimum solid wall percent is given in the following CRC table.

    || table | r602_3wallpercent.csv | 15,C | [:]

    The percent solid wall for each shear wall is:

    || table | solid_shearwall.csv | 15,R | [:]

    **Therefore, if edge nailing requirements are met the residence meets the
    prescriptive opening requirements of the CRC.**

    || image | shearwalls1d.jpg | 90
    First floor shear walls - north and west sides [f]_

    || image | shearwalls2d.jpg | 90
    First floor shear walls - south and east sides [f]_

    [page]_
    
    Check required basic fastener spacing:

    || table | r602_3fasten.csv | 30,L | [:]
    || text | r602_3fasten_notes.txt | literal 

    Check code required wind governed fastener spacing:

    || table | r602_3wind.csv | 30,C | [:]
    || text | r602_3wind_notes.txt | literal 
    
    **In order to meet the code prescriptive wind and seismic requirements the
    number of nails at the exterior sheathing panel boundaries need to be
    doubled - from 12" oc to 6" oc. Refer to CBC analysis in calculation 0301
    for an analysis of DC ratios with reduced capacity**

    """)
rv.V("""[02] Foundation - CRC Requirements 

    The existing foundation on the north and west side of the residence is a
    concrete strip footing directly supporting the floor joists. On the south side
    the floor joists are supported on 2x4 framed walls varying in height, up to
    6 feet. The framing is clad on the outside with 1x10 planks, spaced 1" apart
    for ventilation.

    The foundation has two significant seismic deficiency. The first is a
    significant torsional irregularity arising from lack of shear stiffness and
    strength on the south and east walls. The existing structure has only one
    compression brace along each wall and the spaced planks do not provide
    meaningful strength or stiffness. This irregularity is a deficiency whether
    the floor diaphragm is considered semi-rigid or flexible. The second is the
    lack of adequate anchorage of the sill plates to the foundation. Existing
    anchorage typically consists of only a single 1/2" anchor bolt and small
    washer every 3 or 4 feet. 

    **The torsional irregularities disqualify the foundation structure from
    following a CRC design process.**

    """)
# %%
rv.V("""[03]  Seismic Model Inputs - CBC Requirements
    
    || config | nosub | 2,2
 
    Seismic demands on the residence were analyzed using a 3D FEM model. The
    model includes the full relevant geometry, loads and stiffness of the
    walls, roof, floors and foundation.

    The in-plane stiffness of the T&G roof is taken as 300 pounds/inch/inch
    using test data from [USDA1972]. The in-plane stiffness of the plywood
    shear walls and subfloor is estimated at 1000 pounds/inch/inch after
    supplementary nailing, using values from CBC tables.

    [USDA1972] USDA Forest Products Laboratory. 1972. "Shear Stiffness Of Two-Inch 
    Wood Decks For Roof Systems", U.S.D.A. Forest  Service RESEARCH  PAPER, 
    FPL 155 1972 

    || table | awc4_3a.csv | 11,C | [:]
    || text | awc4_3a_notes.txt | literal

    The shear capacity adjustments for shear wall openings is taken from the
    AWC table below:

    || table | awc4_335adjust.csv | 20,C | [:]
    || text | awc4_335adjust.txt | literal

    || table | gm_values.csv | 30,L | [:]

    Base shear coefficient [t]_
    SDS = 1.0               | -,- | short period design
    R1 = 6.5                | -,- | reduction factor
    omega = 3               | -,- | overstrength factor
    
    Seismic coefficent [e]_
    C_s = SDS/R1            | -,-

    """)
# %%
