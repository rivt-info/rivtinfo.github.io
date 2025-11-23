@echo on
REM Windows 10 and above - cmd file
REM (1) clear any existing project, (2) create new venv
REM (3) install rivt, (4) download example
REM set rivt folder
SET rvfolder=rivt-doc1
REM go to home directory
cd %HOMEPATH%
REM double check deactivation
uv deactivate
REM double check that old project is deleted
rmdir /s /q %rvfolder%
REM (1) clean cache 
uv cache clean
REM set up venv
mkdir %rvfolder%
REM change directory
cd %rvfolder%
REM (2) make venv
uv venv
REM activate venv
call .venv/scripts/activate
REM (3) install rivt from GitHub
uv pip install git+https://github.com/rivtlib-dev/rivtlib.git@main
REM (4) download example project into new folder
mkdir example1
cd example1
curl https://raw.githubusercontent.com/rivt-info/rivt-simple-doc/refs/heads/main/rv000-simple-doc.py -O
curl https://github.com/rivt-info/rivt-simple-doc/blob/main/beam.png?raw=true -O -L
curl https://github.com/rivt-info/rivt-simple-doc/blob/main/beam1-v.csv?raw=true -O -L
REM run example (no quotes) "python rv000-simple-doc.py"
cmd /k
