**F.2 | Scripts**
=================================  


**[2]** Example - Python Function 
------------------------------------------------------------------------


.. topic:: Copilot Prompt -  "write a Python function that checks a 
           wood column using NDS"

   .. code-block:: text

      ======================================================================
      NDS Wood Column Design Results
      ======================================================================

      Example: 4x4 DF-L Grade #1, pinned-pinned, 6 ft span
      ----------------------------------------------------------------------
      Applied axial stress: 244.9 psi
      Adjusted compression strength: 493.7 psi
      Applied bending stress (y): 906.8 psi
      DC ratio: 0.310
      Governing axis: x
      Design: ✓ PASS

      Intermediate values:
      Load duration factor (CD): 1.00
      Moisture factor (CM): 1.00
      Size factor (CF): 1.10
      Stability factor (Cp): 0.3325
      Slenderness ratio (critical): 71.3
      Critical slenderness Cc: 117.9
 
   .. code-block:: python

      """
      NDS Wood Column Design Checker

      Implements National Design Specification (NDS) for Wood Construction
      column checking. Handles solid sawn lumber and engineered lumber columns
      with various loading conditions.

      Reference: NDS 2024 Edition
      """

      import numpy as np
      from dataclasses import dataclass
      from enum import Enum
      from typing import Tuple, Optional, List
      from math import sqrt, pi


      class LoadDuration(Enum):
         """Load duration categories per NDS."""
         PERMANENT = 0.9
         TEN_YEAR = 1.0
         TWO_MONTH = 1.15
         SEVEN_DAY = 1.25
         IMPACT = 1.6


      class Moisture(Enum):
         """Moisture service conditions."""
         DRY = 1.0           # <12% EMC (interior)
         WET = 0.8           # ≥12% EMC (exterior/wet)


      class LumberGrade(Enum):
         """Common lumber grades and their properties (reference values for 2x4
         Douglas Fir-Larch)."""
         GRADE_1 = {"Fc_prime": 1350, "E": 1900000, "CD_factor": 1.0}
         GRADE_2 = {"Fc_prime": 1100, "E": 1700000, "CD_factor": 1.0}
         GRADE_3 = {"Fc_prime": 600, "E": 1500000, "CD_factor": 1.0}
         SEL_STRUCT = {"Fc_prime": 1500, "E": 2000000, "CD_factor": 1.0}


      @dataclass
      class LumberSection:
         """Properties of a wood column section."""
         b: float  # Width (inches or mm)
         d: float  # Depth (inches or mm)
         Fc_prime: float  # Reference compression parallel to grain (psi or MPa)
         E: float  # Modulus of elasticity (psi or MPa)

         @property
         def area(self) -> float:
            """Cross-sectional area."""
            return self.b * self.d

         @property
         def Ix(self) -> float:
            """Second moment of inertia about x-axis (strong axis)."""
            return self.b * self.d**3 / 12

         @property
         def Iy(self) -> float:
            """Second moment of inertia about y-axis (weak axis)."""
            return self.d * self.b**3 / 12

         @property
         def rx(self) -> float:
            """Radius of gyration about x-axis."""
            return sqrt(self.Ix / self.area)

         @property
         def ry(self) -> float:
            """Radius of gyration about y-axis."""
            return sqrt(self.Iy / self.area)


      class WoodColumnChecker:
         """
         NDS-based column checker for solid sawn lumber.
         """

         def __init__(self, section: LumberSection):
            """
            Initialize column checker.

            Args:
                  section: LumberSection object with geometric and material properties
            """
            self.section = section

         def check_column(
            self,
            length: float,
            axial_load: float,
            load_duration: LoadDuration = LoadDuration.TEN_YEAR,
            moisture: Moisture = Moisture.DRY,
            Ke_x: float = 1.0,
            Ke_y: float = 1.0,
            lateral_load_x: float = 0.0,
            lateral_load_y: float = 0.0
         ) -> dict:
            """
            Check NDS column adequacy.

            Args:
                  length: Column length (same units as section dimensions)
                  axial_load: Axial compression force (lbs or N)
                  load_duration: Load duration factor
                  moisture: Moisture service condition
                  Ke_x: Effective length factor about x-axis (default 1.0)
                  Ke_y: Effective length factor about y-axis (default 1.0)
                  lateral_load_x: Lateral load perpendicular to x-axis (optional)
                  lateral_load_y: Lateral load perpendicular to y-axis (optional)

            Returns:
                  Dictionary with:
                     - stress: Applied compression stress
                     - Fc_star: Adjusted compression strength
                     - utilization: Stress ratio
                     - governing_axis: 'x' or 'y' (which controls)
                     - details: Dictionary with all intermediate calculations
                     - passes: Boolean, True if design is adequate
            """

            # Calculate adjustment factors
            CD = load_duration.value  # Load duration factor
            CM = moisture.value       # Moisture factor

            # Size adjustment factors (approximate for 2" nominal)
            CF = self._size_adjustment_factor()

            # Lateral stability (compression perpendicular to grain)
            Cc = self._compute_critical_slenderness_ratio()

            # Calculate slenderness ratios
            Le_x = Ke_x * length
            Le_y = Ke_y * length

            lambda_x = Le_x / self.section.rx if self.section.rx > 0 else 0
            lambda_y = Le_y / self.section.ry if self.section.ry > 0 else 0

            # Determine governing slenderness ratio
            lambda_crit = max(lambda_x, lambda_y)
            governing_axis = 'x' if lambda_x >= lambda_y else 'y'

            # Stability factor (Cp) - accounts for column buckling
            Cp = self._stability_factor(lambda_crit, Cc)

            # Adjusted compression strength parallel to grain
            Fc_star = self.section.Fc_prime * CD * CM * CF * Cp

            # Applied stress
            fc = axial_load / self.section.area

            # Primary bending moment stresses (if lateral loads present)
            fb_x = 0
            fb_y = 0

            if lateral_load_x != 0:
                  M_x = lateral_load_x * length**2 / 8
                  fb_x = M_x / (self.section.Ix / (self.section.d / 2))

            if lateral_load_y != 0:
                  M_y = lateral_load_y * length**2 / 8
                  fb_y = M_y / (self.section.Iy / (self.section.b / 2))

            # Bending strength adjustment
            Fb_star_x = self._bending_strength(lateral_load_x != 0) * CD * CM
            Fb_star_y = self._bending_strength(lateral_load_y != 0) * CD * CM

            # Interaction formula (NDS Section 3.9)
            # For combined bending and axial stress
            if fb_x > 0 or fb_y > 0:
                  # Euler buckling stress
                  Fe = pi**2 * self.section.E * CM / (lambda_crit**2)

                  # Interaction check
                  utilization = (fc / Fc_star)**2
                  if Fb_star_x > 0:
                     utilization += (fb_x / Fb_star_x) * (fc / (Fe - fc))
                  if Fb_star_y > 0:
                     utilization += (fb_y / Fb_star_y) * (fc / (Fe - fc))
            else:
                  # Pure compression
                  utilization = fc / Fc_star if Fc_star > 0 else float('inf')

            passes = utilization <= 1.0

            details = {
                  'CD': CD,
                  'CM': CM,
                  'CF': CF,
                  'Cp': Cp,
                  'lambda_x': lambda_x,
                  'lambda_y': lambda_y,
                  'lambda_crit': lambda_crit,
                  'Cc': Cc,
                  'fc': fc,
                  'Fc_star': Fc_star,
                  'fb_x': fb_x,
                  'fb_y': fb_y,
                  'Fb_star_x': Fb_star_x,
                  'Fb_star_y': Fb_star_y,
                  'Fe': Fe if lateral_load_x != 0 or lateral_load_y != 0 else None,
            }

            return {
                  'stress': fc,
                  'Fc_star': Fc_star,
                  'utilization': utilization,
                  'governing_axis': governing_axis,
                  'details': details,
                  'passes': passes
            }

         def _stability_factor(self, lambda_crit: float, Cc: float) -> float:
            """
            Calculate stability factor (Cp) per NDS Section 3.7.1.

            Cp = (1 + (lambda/Cc)²) / (2c) - sqrt(((1 + (lambda/Cc)²) / (2c))² -
            (lambda/Cc)² / c) where c = 0.8 for sawn lumber
            """
            if lambda_crit <= Cc:
                  # Short column range
                  c = 0.8
                  x = (lambda_crit / Cc)**2
                  Cp = (1 + x) / (2*c) - sqrt(((1 + x)/(2*c))**2 - x/c)
            else:
                  # Long column range (Johnson formula)
                  Cp = 0.877 / (lambda_crit)**2

            return max(Cp, 0.0)

         def _compute_critical_slenderness_ratio(self) -> float:
            """
            Calculate critical slenderness ratio per NDS.
            Cc = π * sqrt(E / Fc_prime)
            """
            return pi * sqrt(self.section.E / self.section.Fc_prime)

         def _size_adjustment_factor(self) -> float:
            """
            Size adjustment factor CF per NDS.
            Approximate: CF = 1.0 for typical 2" nominal lumber.
            More precise values require reference to specific grade/size.
            """
            # Simplified: typical sizes
            if self.section.b <= 3.5:
                  return 1.1
            elif self.section.b <= 5.5:
                  return 1.05
            else:
                  return 1.0

         def _bending_strength(self, with_load: bool) -> float:
            """Reference bending strength (approximate)."""
            if not with_load:
                  return 0
            # Typical reference strength ~1000 psi for sawn lumber
            return 1000


      class EngineerWoodColumn:
         """
         Engineered wood products column checker (simplified).
         Handles LVL, glulam, etc.
         """

         def __init__(self, section: LumberSection):
            self.section = section
            self.checker = WoodColumnChecker(section)

         def check_glulam_column(
            self,
            length: float,
            axial_load: float,
            load_duration: LoadDuration = LoadDuration.TEN_YEAR,
            moisture: Moisture = Moisture.DRY,
            Ke: float = 1.0
         ) -> dict:
            """
            Check glulam beam column per NDS (simplified).
            Glulam has additional factors for temperature, load sharing, etc.
            """
            results = self.checker.check_column(
                  length, axial_load, load_duration, moisture,
                  Ke_x=Ke, Ke_y=Ke
            )

            # Additional glulam factors (simplified)
            # CT = 1.0 for normal temperature
            # Cv = load sharing factor (typically 1.15 for multi-member)

            return results


      # Example usage and test cases
      if __name__ == "__main__":

         print("=" * 70)
         print("NDS Wood Column Design Checker")
         print("=" * 70)
         print("\nExample 1: 4x4 DF-L Grade #1, pinned-pinned, 6 ft span")
         print("-" * 70)

         section_1 = LumberSection(
            b=3.5,      # actual 4" nominal width
            d=3.5,      # actual 4" nominal depth
            Fc_prime=1350,  # Grade #1 DF-L compression strength
            E=1900000   # Modulus of elasticity
         )

         checker_1 = WoodColumnChecker(section_1)
         results_1 = checker_1.check_column(
            length=72,  # 6 feet = 72 inches
            axial_load=3000,  # 3 kips
            load_duration=LoadDuration.TEN_YEAR,
            moisture=Moisture.DRY,
            Ke_x=1.0,
            Ke_y=1.0,
            lateral_load_y=10  # 10 lbs/in lateral load
         )

         print(f"Applied axial stress: {results_1['stress']:.1f} psi")
         print(f"Adjusted compression strength: {results_1['Fc_star']:.1f} psi")
         print(
            f"Applied bending stress (y): {results_1['details']['fb_y']:.1f} psi")
         print(f"Utilization ratio: {results_1['utilization']:.3f}")
         print(f"Governing axis: {results_1['governing_axis']}")
         print(f"Design: {'✓ PASS' if results_1['passes'] else '✗ FAIL'}")
         details = results_1['details']
         print(f"\nIntermediate values:")
         print(f"  Load duration factor (CD): {details['CD']:.2f}")
         print(f"  Moisture factor (CM): {details['CM']:.2f}")
         print(f"  Size factor (CF): {details['CF']:.2f}")
         print(f"  Stability factor (Cp): {details['Cp']:.4f}")
         print(f"  Slenderness ratio (critical): {details['lambda_crit']:.1f}")
         print(f"  Critical slenderness Cc: {details['Cc']:.1f}")

