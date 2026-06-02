**F.1** AI
=====================

.. raw:: html

   <hr>

.. figure::  _static/img/rivt-ai1.png
    :class: dark-light
    :scale: 20%
    :align: center
    :alt: rivt logo
    
.. raw:: html

   <hr>


**[1]** *rivt* in an AI context
------------------------------------------------------------------------ 

*rivt* is a Python library and language that takes Python and text strings as
input. This makes *rivt* a natural fit for using AI to generate *rivt* input.

For some context a summary of relevant AI models and tools is provided
:ref:`here <aiback>`.  In brief, AI starts with a few large foundational models
that provide the basis for many different agents, tools and UI's that are used
to generate useful content. 

Effective approaches for using AI to generate complete *rivt files* for specific
project requirements is currently being explored. *rivt* AI agents are planned
for release as a software service in the latter part of 2026.

------------------------------------


**[2]** Current AI Use Cases
----------------------------------------------------------------------- 

The *VSCode IDE* is used to develop *rivt*. *VSCode* is integrated with
*Microsoft Copilot*, an AI coding assistant powered by the *OpenAI*
:ref:`foundation model <aiback>`. *Copilot*  is aware of *rivt markdown* and is
able to make editing and content suggestions. More importantly, *Copilot* can be
used to generate tables, equations and models that can be directly
used in *rivt* documents.

------------------------------------


**[3]** Example - Data Table
-----------------------------------------------------------------------

.. topic:: Prompt -  "Generate a csv table of weight values per unit length 
           of Douglas Fir 2x joists"

   **Example Output as reST**

   .. code-block:: text

      =========  ================  ================  ========== ==================
      Nominal    ActualWidth_in    ActualDepth_in    Area_in2    Weight_lb_per_ft
      =========  ================  ================  ========== ==================
      2x2        1.5               1.5               2.25             0.53125
      2x4        1.5               3.5               5.25             1.23958
      2x6        1.5               5.5               8.25             1.94875
      2x8        1.5               7.25              10.875           2.56771
      2x10       1.5               9.25              13.875           3.275
      2x12       1.5               11.25             16.875           3.98438
      4x4        3.5               3.5               12.25            2.89236
      =========  ================  ================  ========== ==================

------------------------------------

**[4]** Example - Python Function 
------------------------------------------------------------------------

.. topic:: Copilot Prompt -  "write a python function that checks a 
           wood column using NDS"

      **Example Output**

      .. code-block:: python

      """
   
      **Python Script**
      
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


-------------------------

**[5]** Example - SAP2000 Model
------------------------------------------------------------------------

.. topic:: Copilot Prompt -  "write a Python sap2000 script for a SDOF 
           mass-spring system as an s2k file that opens and 
           imports the model via COM.
          
   **SAP2000 S2K SDOF Model with COM**
   
   .. code-block:: python

      """Create and open a SDOF SAP2000 v14 model via the SAP2000 COM API.

      This script generates an SDOF `.s2k` text file and uses COM automation to open it in
      SAP2000 v14. The model is a single lumped mass attached to a fixed ground via a
      linear spring link.

      Requirements:
      - SAP2000 v14 installed on Windows
      - comtypes installed in Python

      Usage:
         python sap_models/generate_sdof_sap2000_com.py --out sap_models/sdof_model_v14.s2k
      """

      import argparse
      import sys
      from pathlib import Path

      try:
         from comtypes.client import CreateObject, GetActiveObject
      except ImportError as exc:
         raise SystemExit(
            'Missing dependency: install comtypes with `pip install comtypes`'
         ) from exc


      S2K_TEMPLATE = '''! SAP2000 database text file - simple SDOF model
      ! Target: SAP2000 v14
      UNITS N M KG C

      ! Joint coordinates: Joint: 1 = mass node, Joint: 2 = ground
      JOINT COORDINATES 2
      1 0.0 0.0 0.0
      2 0.0 0.0 -1.0
      END

      ! Joint restraints - ground (joint 2) fully fixed, joint 1 free
      JOINT RESTRAINTS 1
      2 1 1 1 1 1 1
      END

      ! Joint mass (applied at joint 1) - mass in global Z translation
      JOINT MASS 1
      1 0.0 0.0 {mass}
      END

      ! Link property: linear spring in translation along global Z (k in N/m)
      LINK PROPERTIES 1
      1 "SDOF_SPRING" 0 0 0 0 0 0 0 1 0 {k}
      END

      ! Link objects: connect joint 1 to joint 2 using link property 1
      LINK OBJECTS 1
      1 1 2 1 0
      END

      ! Define a static load case (dead) with no loads - useful placeholder
      LOAD CASES 1
      "DEAD" 0 0 0 0 0 0 0
      END

      ! Save file
      '''


      def write_s2k(outpath: Path, mass: float, stiffness: float) -> None:
         content = S2K_TEMPLATE.format(mass=mass, k=stiffness)
         outpath.write_text(content)


      def get_sap2000_helper():
         try:
            helper = GetActiveObject('SAP2000v1.Helper')
         except OSError:
            helper = CreateObject('SAP2000v1.Helper')
         if helper is None:
            raise RuntimeError('Could not obtain SAP2000 helper object.')
         return helper


      def create_sap_object(helper):
         for progid in ('SAP2000v1.SapObject', 'CSI.SAP2000.API.SapObject'):
            try:
                  sap_obj = helper.CreateObject(progid)
                  if sap_obj is not None:
                     return sap_obj
            except Exception:
                  continue
         raise RuntimeError('Could not create SAP2000 COM SapObject. Check SAP2000 v14 installation.')


      def open_model_in_sap2000(outpath: Path, show_window: bool = True) -> None:
         helper = get_sap2000_helper()
         sap_object = create_sap_object(helper)

         # Start SAP2000 application if required.
         try:
            sap_object.ApplicationStart()
         except Exception:
            pass

         sap_model = sap_object.SapModel
         if show_window:
            sap_object.ApplicationStart()  # ensure GUI opens

         if not outpath.exists():
            raise FileNotFoundError(f'Could not find model file: {outpath}')

         print(f'Opening SAP2000 model: {outpath}')
         sap_model.File.OpenFile(str(outpath))
         print('Model opened successfully.')


      def main():
         parser = argparse.ArgumentParser(description='Create and open a SAP2000 v14 SDOF model via COM API.')
         parser.add_argument('--mass', type=float, default=1000.0, help='Lumped mass in kg')
         parser.add_argument('--stiffness', type=float, default=1e6, help='Spring stiffness in N/m')
         parser.add_argument('--out', type=Path, default=Path('sap_models/sdof_model_v14.s2k'), help='Output .s2k filename')
         parser.add_argument('--no-gui', action='store_true', help='Do not open SAP2000 GUI after creating the file')
         args = parser.parse_args()

         outpath = args.out
         outpath.parent.mkdir(parents=True, exist_ok=True)
         write_s2k(outpath, args.mass, args.stiffness)
         print(f'Wrote model file: {outpath.resolve()}')

         if not args.no_gui:
            open_model_in_sap2000(outpath, show_window=True)


      if __name__ == '__main__':
         main()

--------------------------

**[6]** Example - OpenSees Model
------------------------------------------------------------------------

.. topic:: Copilot Prompt -  "write an opensees Python model to analyze a SDOF 
           mass nonlinear-spring model with time series input and output 
           helpers"  
          
   **OpenSees SDOF Nonlinear Model**
   
   .. code-block:: python

      """One-degree-of-freedom OpenSeesPy model with a nonlinear spring and time series input.

      This script builds a SDOF model with:
      - a lumped mass at the moving node,
      - a zero-length nonlinear spring element between the mass node and a fixed ground node,
      - input as a time series acceleration record applied as ground motion,
      - transient analysis with Newmark integration.

      Usage examples:
         python opensees_models/sdof_nonlinear_spring.py --duration 5.0 --dt 0.01
         python opensees_models/sdof_nonlinear_spring.py --input-file accel.txt --dt 0.01

      Requirements:
         pip install openseespy numpy
      """

      import argparse
      from pathlib import Path

      import numpy as np

      try:
         import openseespy.opensees as ops
      except ImportError as exc:
         raise SystemExit(
            'OpenSeesPy is required. Install with `pip install openseespy`.') from exc


      def try_import_matplotlib():
         try:
            import matplotlib.pyplot as plt
         except ImportError as exc:
            raise SystemExit(
                  'Matplotlib is required for plotting. Install with `pip install matplotlib`.') from exc
         return plt


      def build_sdof_model(mass=1000.0, stiffness=1.0e6, fy=1000.0, b=0.01, damping_ratio=0.0):
         """Build the SDOF model in OpenSeesPy."""
         ops.wipe()
         ops.model('basic', '-ndm', 2, '-ndf', 3)

         # Node 1 is fixed ground. Node 2 is the mass node.
         ops.node(1, 0.0, 0.0)
         ops.node(2, 0.0, 0.0)
         ops.fix(1, 1, 1, 1)
         ops.mass(2, mass, 0.0, 0.0)

         # Nonlinear spring material: bilinear Steel01.
         E = stiffness
         ops.uniaxialMaterial('Steel01', 1, fy, E, b)

         # Zero-length spring between ground and mass in DOF 1 (horizontal direction).
         ops.element('zeroLength', 1, 1, 2, '-mat', 1, '-dir', 1)

         # Optional damping via Rayleigh damping if a nonzero damping ratio is provided.
         if damping_ratio > 0.0:
            omega = np.sqrt(stiffness / mass)
            alpha = 2.0 * damping_ratio * omega
            ops.rayleigh(alpha, 0.0, 0.0, 0.0)


      def create_ground_motion_time_series(accel, dt, ts_tag=1):
         """Create a Path time series for ground acceleration input."""
         ops.timeSeries('Path', ts_tag, '-dt', dt, '-values', *accel)
         return ts_tag


      def apply_uniform_excitation(ts_tag, direction=1):
         """Apply the time series as uniform excitation in the specified DOF."""
         ops.pattern('UniformExcitation', 1, direction, '-accel', ts_tag)


      def configure_analysis(dt, tol=1e-8, max_iter=20):
         ops.constraints('Plain')
         ops.numberer('RCM')
         ops.system('BandGeneral')
         ops.test('NormDispIncr', tol, max_iter)
         ops.algorithm('Newton')
         ops.integrator('Newmark', 0.5, 0.25)
         ops.analysis('Transient')


      def run_analysis(n_steps, dt):
         if ops.analyze(n_steps, dt) != 0:
            raise RuntimeError('OpenSees transient analysis failed.')


      def write_recorders(output_dir: Path):
         output_dir.mkdir(parents=True, exist_ok=True)
         disp_file = output_dir / 'displacement.txt'
         accel_file = output_dir / 'acceleration.txt'
         ops.recorder('Node', '-file', str(disp_file),
                     '-time', '-node', 2, '-dof', 1, 'disp')
         ops.recorder('Node', '-file', str(accel_file),
                     '-time', '-node', 2, '-dof', 1, 'accel')
         return disp_file, accel_file


      def load_acceleration_series(path: Path):
         values = np.loadtxt(path, dtype=float)
         if values.ndim > 1:
            values = values[:, 0]
         return values


      def load_response_history(path: Path):
         data = np.loadtxt(path, dtype=float)
         if data.ndim == 1:
            return np.arange(data.shape[0]), data
         return data[:, 0], data[:, 1]


      def plot_response_history(disp_file: Path, accel_file: Path, output_dir: Path, show=False, save=False):
         plt = try_import_matplotlib()
         time_d, disp = load_response_history(disp_file)
         time_a, accel = load_response_history(accel_file)

         fig, axs = plt.subplots(2, 1, sharex=True, figsize=(9, 6))
         axs[0].plot(time_d, disp, 'b-', label='Displacement')
         axs[0].set_ylabel('Displacement')
         axs[0].grid(True)
         axs[0].legend()

         axs[1].plot(time_a, accel, 'r-', label='Acceleration')
         axs[1].set_ylabel('Acceleration')
         axs[1].set_xlabel('Time [s]')
         axs[1].grid(True)
         axs[1].legend()

         fig.suptitle('SDOF Response Histories')
         fig.tight_layout(rect=[0, 0.03, 1, 0.95])

         if save:
            image_path = output_dir / 'response_history.png'
            fig.savefig(image_path, dpi=150)
            print(f'Saved plot: {image_path}')

         if show:
            plt.show()
         else:
            plt.close(fig)


      def sample_sine_acceleration(duration, dt, amplitude=0.5, frequency=1.0):
         time = np.arange(0.0, duration + dt, dt)
         return amplitude * np.sin(2.0 * np.pi * frequency * time)


      def main():
         parser = argparse.ArgumentParser(
            description='Run a nonlinear OpenSeesPy SDOF model with time series input.')
         parser.add_argument('--mass', type=float,
                              default=1000.0, help='Lumped mass (kg)')
         parser.add_argument('--stiffness', type=float,
                              default=1.0e6, help='Initial spring stiffness (N/m)')
         parser.add_argument('--yield-force', type=float,
                              default=1000.0, help='Spring yield force (N)')
         parser.add_argument('--post-yield-ratio', type=float,
                              default=0.01, help='Post-yield stiffness ratio')
         parser.add_argument('--damping-ratio', type=float,
                              default=0.0, help='Rayleigh damping ratio')
         parser.add_argument('--dt', type=float, default=0.01,
                              help='Time step for analysis (s)')
         parser.add_argument('--duration', type=float, default=5.0,
                              help='Analysis duration when using synthetic input (s)')
         parser.add_argument('--input-file', type=Path,
                              help='Optional acceleration time history file (one column)')
         parser.add_argument('--output-dir', type=Path, default=Path(
            'opensees_models/results'), help='Directory for output recorders')
         parser.add_argument('--acc-amplitude', type=float, default=0.5,
                              help='Synthetic acceleration amplitude (units of g)')
         parser.add_argument('--acc-frequency', type=float, default=1.0,
                              help='Synthetic acceleration frequency (Hz)')
         parser.add_argument('--plot', action='store_true',
                              help='Show response plots after analysis')
         parser.add_argument('--save-plot', action='store_true',
                              help='Save response plot to the output directory')
         args = parser.parse_args()

         if args.input_file:
            accel = load_acceleration_series(args.input_file)
            dt = args.dt
         else:
            accel = sample_sine_acceleration(
                  args.duration, args.dt, args.acc_amplitude, args.acc_frequency)
            dt = args.dt

         build_sdof_model(
            mass=args.mass,
            stiffness=args.stiffness,
            fy=args.yield_force,
            b=args.post_yield_ratio,
            damping_ratio=args.damping_ratio,
         )

         create_ground_motion_time_series(accel, dt)
         apply_uniform_excitation(ts_tag=1, direction=1)
         configure_analysis(dt)
         disp_file, accel_file = write_recorders(args.output_dir)

         n_steps = len(accel)
         run_analysis(n_steps, dt)

         print('Analysis complete.')
         print(f'Displacement output: {disp_file}')
         print(f'Acceleration output: {accel_file}')

         if args.plot or args.save_plot:
            plot_response_history(disp_file, accel_file, args.output_dir,
                                    show=args.plot, save=args.save_plot)


      if __name__ == '__main__':
         main()



.. toctree::
    :maxdepth: 1
    :hidden:

    rvF02-aibackgrnd.rst
