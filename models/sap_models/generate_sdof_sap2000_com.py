#!/usr/bin/env python3
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
