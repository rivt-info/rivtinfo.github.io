@echo on
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
REM download rivt install file
curl  https://raw.githubusercontent.com/rivt-info/rivt-win-install/refs/heads/main/rivt-install.cmd -O   
REM (2) make venv
uv venv
REM activate venv
call .venv/scripts/activate
REM (3) install rivt from GitHub
uv pip install git+https://github.com/rivtlib-dev/rivtlib#subdirectory=src
REM download example project into new folder
mkdir example1
cd (4) example1
curl https://raw.githubusercontent.com/rivt-info/rivt-simple-single-doc/refs/heads/main/rv0000-simple-single-doc.py -O
curl https://github.com/rivt-info/rivt-simple-single-doc/blob/main/beam.png?raw=true -O -L
REM run example with (no quotes) "python rv0000-simple-single-doc.py"
cmd /k
