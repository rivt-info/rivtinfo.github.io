.. raw:: latex

   ?x?vspace{.2in}   ?x?textbf{Structural Deficiencies}   ?x?hfill?x?textbf{SECTION 01}
   ?x?newline   ?x?vspace{.05in}   {?x?color{black}?x?hrulefill}


The carport is a post and beam structure that was connected primarily by
gravity and friction and a few nails and screws with minimal capacity.

In addition there was significant post decay. Initially the posts were
supported on spread footings and the parking area was gravel. At some point
a few decades ago, the posts were encapsulated with a concrete slab up to 8
or 9 inches to provide a better parking surface. The encapsulating concrete
trapped water around the columns bases which caused serious decay and
eventually led to partial column failure, 90% section loss in some cases
and differential settlement up to 7 inches.

.. image:: c:/Users/rodhh/Dropbox/projects/residence_remodel/rivtcalcs0001/docs/d02_code_min/carport01.jpg
   :width: 90%
   :align: left 



**Carport** ?x?hfill [ Fig: 0202.04 ]


.. raw:: latex

   ?x?vspace{.2in}   ?x?textbf{Carport Repairs and Strengthening}   ?x?hfill?x?textbf{SECTION 02}
   ?x?newline   ?x?vspace{.05in}   {?x?color{black}?x?hrulefill}


Beam to beam, post to beam and brace to beam and post connections were
strengthened with 1/8" galvanized angles or plates that were attached with
lag bolts or galvanized threaded rods or bolts.

The carport was shored and leveled, the decayed bottom of the posts were
removed and new concrete foundations that raised the bottom of the posts
above the parking slab were installed to prevent further decay.  Each post
was postively anchored with double (orthogonal) bases.

.. image:: c:/Users/rodhh/Dropbox/projects/residence_remodel/rivtcalcs0001/docs/d02_code_min/carport1.jpg
   :width: 80%
   :align: left 



**Carport North Elevation** ?x?hfill [ Fig: 0202.05 ]

.. image:: c:/Users/rodhh/Dropbox/projects/residence_remodel/rivtcalcs0001/docs/d02_code_min/carport2.jpg
   :width: 80%
   :align: left 



**Carport West Elevation** ?x?hfill [ Fig: 0202.06 ]


.. raw:: latex

   ?x?vspace{.2in}   ?x?textbf{Seismic Model Inputs - CBC Requirements}   ?x?hfill?x?textbf{SECTION 03}
   ?x?newline   ?x?vspace{.05in}   {?x?color{black}?x?hrulefill}


Seismic demands on the carport were analyzed using a 3D FEM model (ETABS).
The model includes the geometry, loads and stiffness associated with the
post, beams and roof. Column bases, beam to post, and brace connections
were modeled as pins.

The in-plane stiffness of the T&G roof is taken as 300 pounds/inch/inch
using test data from [USDA1972].

[USDA1972] USDA Forest Products Laboratory. 1972. "Shear Stiffness Of Two-Inch
Wood Decks For Roof Systems", U.S.D.A. Forest  Service RESEARCH  PAPER,
FPL 155 1972

**ASCE7-16; Risk II; Site D** ?x?hfill  [Table: 0202.03]

.. raw:: latex

  \begin{tabulary}{1.0\textwidth}{LL}
  \begin{tabular}{lr}
  \hline
   Parameter   &    Value \\
  \hline
   SS          &    1.512 \\
   S1          &    0.685 \\
   FA          &    1     \\
   FV          &    1.5   \\
   SMS         &    1.512 \\
   SM1         &    1.027 \\
   SDS         &    1.008 \\
   SD1         &    0.685 \\
   TL          &   12     \\
   PGA         &    0.603 \\
   PGAM        &    0.603 \\
   FPGA        &    1     \\
   LE          &    1     \\
  \hline
  \end{tabular}
  \end{tabulary}
  \vspace{.15in}

**Base shear coefficients** ?x?hfill  [Table: 0202.04]
:: 

  ==========  =======  =========  ===================
  variable      value    [value]  description
  ==========  =======  =========  ===================
  SDS            1.00       1.00  short period design
  R1             3.25       3.25  reduction factor
  omega          2.00       2.00  overstrength factor
  ==========  =======  =========  ===================




**Seismic coefficent** ?x?hfill [ Equ: 0202.02]

.. math:: 

  C_{s} = \frac{SDS}{R_{1}}

:: 

  ====================  ========  =====
          C_s              R1      SDS
  ====================  ========  =====
  0.31 [-]  [0.31 [-]]  3.25 [-]   [-]
  ====================  ========  =====




