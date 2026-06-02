#!/usr/bin/env python3
"""Generate a SAP2000 v14 .s2k text model for a SDOF mass-spring system.

Defaults: mass=1000 kg, stiffness=1e6 N/m, single joint at origin connected to ground.
This script writes `sdof_model_v14.s2k` in the same folder.
"""
import argparse
from pathlib import Path


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


def write_s2k(outpath: Path, mass: float, k: float) -> None:
    content = S2K_TEMPLATE.format(mass=mass, k=k)
    outpath.write_text(content)


def main() -> None:
    p = argparse.ArgumentParser(description='Generate SDOF SAP2000 .s2k file')
    p.add_argument('--mass', type=float, default=1000.0, help='Lumped mass in kg')
    p.add_argument('--stiffness', type=float, default=1e6, help='Spring stiffness in N/m')
    p.add_argument('--out', type=str, default='sdof_model_v14.s2k', help='Output .s2k filename')
    args = p.parse_args()

    outpath = Path(args.out)
    write_s2k(outpath, args.mass, args.stiffness)
    print(f'Wrote {outpath.resolve()} (mass={args.mass} kg, k={args.stiffness} N/m)')


if __name__ == '__main__':
    main()
