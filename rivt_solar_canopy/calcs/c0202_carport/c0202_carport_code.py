#! python
# %%
import rivtlib.rv_lib as rv
rv.D("pdf", "default", "Code Minimums - Carport Renovations", "21")

# %%
rv.I("""[01] Structural Deficiencies
 
    The carport is a post and beam structure that was connected primarily by
    gravity and friction and a few nails and screws with minimal capacity.

    In addition there was significant post decay. Initially the posts were
    supported on spread footings and the parking area was gravel. At some point
    a few decades ago, the posts were encapsulated with a concrete slab up to 8
    or 9 inches to provide a better parking surface. The encapsulating concrete
    trapped water around the columns bases which caused serious decay and
    eventually led to partial column failure, 90% section loss in some cases
    and differential settlement up to 7 inches.
    
    || image | carport01.jpg | 90
    Carport [f]_

    """)
rv.I("""[02]  Carport Repairs and Strengthening

    Beam to beam, post to beam and brace to beam and post connections were
    strengthened with 1/8" galvanized angles or plates that were attached with
    lag bolts or galvanized threaded rods or bolts.

    The carport was shored and leveled, the decayed bottom of the posts were
    removed and new concrete foundations that raised the bottom of the posts
    above the parking slab were installed to prevent further decay.  Each post
    was postively anchored with double (orthogonal) bases.
    
    || image | carport1.jpg | 80
    Carport North Elevation [f]_

    || image | carport2.jpg | 80
    Carport West Elevation  [f]_ 

    """)
rv.V("""[03]  Seismic Model Inputs - CBC Requirements
 
    Seismic demands on the carport were analyzed using a 3D FEM model (ETABS).
    The model includes the geometry, loads and stiffness associated with the
    post, beams and roof. Column bases, beam to post, and brace connections
    were modeled as pins.

    The in-plane stiffness of the T&G roof is taken as 300 pounds/inch/inch
    using test data from [USDA1972]. 

    [USDA1972] USDA Forest Products Laboratory. 1972. "Shear Stiffness Of Two-Inch 
    Wood Decks For Roof Systems", U.S.D.A. Forest  Service RESEARCH  PAPER, 
    FPL 155 1972 

    || table | gm_values.csv | 30,L | [:]

    Base shear coefficients [t]_
    SDS = 1.0               |  | short period design
    R1 = 3.25               |  | reduction factor
    omega = 2               |  | overstrength factor
    
    Seismic coefficent [e]_
    C_s = SDS/R1            |  

    """)
# %%
