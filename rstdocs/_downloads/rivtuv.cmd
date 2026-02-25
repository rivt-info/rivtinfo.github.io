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
REM run example (no quotes) "pyzo-example"
cmd /k