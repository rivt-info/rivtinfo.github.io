# comment
# %%
import rivtlib.rv_lib as rv

rv.D("pdf", "default", "Carport Seismic Model", "37")

rv.I("""[01]  Carport Seismic Demands 

    || image | elements.jpg | 70
    Column and Brace Numbers [f]_

    || image | beams2.jpg | 50
    Beam Numbers [f]_
        
    || image | pins.jpg | 90
    Element Pin Connections [f]_

    || image | forceA.jpg | 90
    Axial Forces - Transverse Seismic [f]_

    || image | forceB.jpg | 90
    Axial Forces - Longitudinal Seismic [f]_

    || image | deltA.jpg | 90
    Deformations - Transverse Seismic (visually amplified) [f]_

    || image | deltB.jpg | 90
    Deformations - Longitudinal Seismic (visually amplified) [f]_

    || text | cp_echo.txt | literal

    || text | cp_str.txt | literal

    || text | cp_eig.txt | literal

    || text | cp_str.txt | literal

    """)
rv.I("""[02]  Seismic D-C Ratios for Braces
    
    Connection capacities evaluated using Woodworks 11.2.  The software does not
    allow a single bolt row so a two bolt configuration is analyzed and
    capacities are reduced by a factor of 2.

    || image | brace1.jpg | 65
    Brace plate reinforcement (two-bolt rows shown - one row analyzed) [f]_

    || text | braces.txt | literal

    """)
rv.I("""[03]  Seismic D-C Ratios for Beam Connections 

    Check beam to beam angle connection drag force load path. 

    || image | bmcon.jpg | 50

    || text | bmcon.txt | literal

    Check column connection shear load path to the foundation.

    || image | colcon.jpg | 50

    || text | colcon.txt | literal

    """)
rv.V("""[04] Seismic D-C Ratios for Column Base

    Check shear D-C at column base.

    V_total = 1     | KIP, KN | total base shear
    V_base = .25    | KIP, N | shear distributed over 4 columns
    f_c = 3         | KSI, MPA | concrete strength
    phi_v = 0.85    | - | capacity reduction
    
    concrete shear strength [e]_
    V_c = phi_v * 2 * (3000)**.5 * PSI      | KSI, MPA

    design shear capacity per column [e]_
    V_d = 4*IN * 7*IN * V_c                 | KIPS, MN

    D-C shear capacity at foundation [e]_
    V_dc = V_base / V_d                    | DC

    || image | base_detail.png | 70
    Column Base Detail [f]_

    """)

# %%
