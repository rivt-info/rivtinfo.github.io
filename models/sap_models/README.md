# SDOF SAP2000 model (v14)

Files:

- `generate_sdof_s2k.py`: Python script to produce a `.s2k` text model (defaults: m=1000 kg, k=1e6 N/m).
- `generate_sdof_sap2000_com.py`: Python script that generates the `.s2k` file and opens it in SAP2000 v14 via COM.
- `sdof_model_v14.s2k`: Generated SAP2000 v14 text file for a simple mass-spring SDOF.

Usage:

1. Generate or customize the .s2k file with Python:

```bash
python sap_models/generate_sdof_s2k.py --mass 1000 --stiffness 1e6 --out sap_models/sdof_model_v14.s2k
```

2. Generate and open the model in SAP2000 via COM automation:

```bash
pip install comtypes
python sap_models/generate_sdof_sap2000_com.py --out sap_models/sdof_model_v14.s2k
```

3. Alternatively, open `sap_models/sdof_model_v14.s2k` in SAP2000 (v14):

- In SAP2000: File → Open → SAP2000 Text File (*.s2k), then select the `.s2k` file.

Notes:

- The provided `.s2k` is a minimal model: a single lumped mass (joint 1) connected to a fixed ground (joint 2) via a linear link property acting as a spring.
- If you want a Python script that drives SAP2000 via its COM API (automates SAP2000 directly), tell me and I'll provide one targeted for SAP2000 v14.
