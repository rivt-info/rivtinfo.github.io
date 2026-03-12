@echo on
REM Windows 10 and above
REM (1) change directory
REM (2) create venv if not already created
REM (3) install rivt from PyPI
REM (4) run example
REM set rivt folder
SET rvfolder=rivt-examples
REM (1) go to home directory
cd %HOMEPATH%
REM set up venv
mkdir %rvfolder%
REM change directory
cd %rvfolder%
REM (2) make venv
uv venv --allow-existing
REM activate venv
call .venv/scripts/activate
REM (3) install rivt from GitHub
uv pip install rivtlib
REM (4) download example project into new folder
mkdir rivt-example01
cd rivt-example01
curl -L "https://drive.usercontent.google.com/download?id=1smGH1eTfG-G2otpLBlrr4rnky2dzPdfo?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto&export=download&confirm=t" -o "beam1.csv" 
curl -L "https://drive.usercontent.google.com/download?id=1smGH1eTfG-G2otpLBlrr4rnky2dzPdfo?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto&export=download&confirm=t" -o "beam1.png" 
curl -L "https://drive.usercontent.google.com/download?id=1smGH1eTfG-G2otpLBlrr4rnky2dzPdfo?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto&export=download&confirm=t" -o "rv001-single-doc-py" 
curl -L "https://drive.usercontent.google.com/download?id=1smGH1eTfG-G2otpLBlrr4rnky2dzPdfo?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto&export=download&confirm=t" -o "sectprop.py" 
REM (5)run example (no quotes) "pyzo-example"
cmd /k