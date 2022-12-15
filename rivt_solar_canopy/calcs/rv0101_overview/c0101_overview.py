#! python
# %%
import rivt.rivtapi as rv

rv.R("""Summary | Calculation Overview | none | 1

    The project includes renovations, repairs and alterations to
    improve the function and seismic resistance of a single story, wood framed
    residence with an attached car port and under-house storage space.
    
    Alterations include remodeling the kitchen, bathroom and living room;
    adding a new bathroom and exterior laundry enclosure. Renovations include
    installing a retaining wall, sidewalk and exterior hand-rail; replacing the
    carport foundations and driveway; and seismically strengthening the
    carport framing and residence foundation walls. The work did not
    change the building foot print.
    
    """)
# %%
rv.I(""" Background | default
    
    The structural calculations address remodeling, repair and strengthening of
    a single family residence.
    
    The single family residence dates to the 1940's and was built on two
    combined lots with an average grade of about 1 in 6. It has a reinforced
    concrete strip foundation, under house storage, plywood sheathed perimeter
    walls, and a flat T&G plank roof (under an original tar and gravel membrane
    overlaid with foam) supported by interior posts and beams. The car port
    structure is also a post and beam structure with roof planks.

    During the prior decades the carport posts had significantly decayed below
    the slab line, leading to uneven carport roof settlement up to 6 inches. In
    addition surface sliding had piled soil up to a foot deep causing the lower
    part of the siding to decay. Decayed portions were removed and replaced and
    a planter/retaining structure was designed to retain the sliding and
    prevent further decay.

    The residence foundation was seismically vulnerable. Two sides of the floor
    diaphragm were directly supported on the strip foundation but the other two
    sides were supported on stud walls up to 6 feet tall. The framed foundation
    walls had very little in-plane strength which made the entire structure
    vulnerable to earthquake damage from first floor twisting. Each of the two
    framed walls had a single minimal compression brace that could not
    prevent seismic translation. Four new shear walls were added.
    
    In summary, over the course of the last five years work was done to
    mitigate safety hazards including seismic vulnerabilities and wood decay,
    and improve living spaces.
    
    || insert | table | project_area.syk | 60,l | [2,1,3]  

    || insert | image1 | house01.jpg | 60,r 
    Residence viewed from Loring Drive [f]_

    """)
# %%
rv.I("""Building Codes and Site | default
    
    The residence is under the jurisdiction of Marin County, California which
    uses the 2019 California Building Code and the 2019 California
    Residential Code to permit construction work.

    || table | cbc2019_stds.xlsx | 53,L | [:]
    
    || image | site01.jpg, site02.jpg | 35,35

    Site map - Marin County web site _[f]
    Site map - Google Earth _[f]

    [page]_
    
    """)
rv.V("""Drawing List
 
    || insert | text | drawing_list.txt | literal

    || inset | image | residence01.jpg | 90
    Residence and Carport _[f]

    [page]_

    """)
rv.V("""References 
 
    || insert | text | references.txt | literal

    [page]_

    """)
rv.T("""Math and Text Abbreviations 
 
    || insert | text | abbrev_all.txt | raw

    """)
rv.X(""" Math and Text Abbreviations 
 
    || insert | text | abbrev_all.txt | raw

    """)
