@echo on
REM Windows 10 and above
REM (1) change directory
REM (2) create venv if not already created
REM (3) install rivt from PyPI
REM (4) run example
REM set report folder
SET rvfolder=rivt-start
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
REM (3) install rivt from pypi
uv pip install rivtlib
REM (4) download an example project into a new folder 
