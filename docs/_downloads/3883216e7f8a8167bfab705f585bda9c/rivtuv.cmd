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
REM (4) download example project into new folder
mkdir rivt-example01
cd rivt-example01
curl -L "https://drive.usercontent.google.com/download?id=1XdTdRmnT9Y_vIZP7pcIrKKXgnaEbMfxY&confirm" -o "rv001-single-doc.py"
curl -L "https://drive.usercontent.google.com/download?id=1hMJvnlO-DZPKqnacnM_JkMltCzU7tBNE&confirm" -o "sectprop.py"
curl -L "https://drive.usercontent.google.com/download?id=1ZtzhR3jt5ce9KQEmfcTINeLLZfmCnStd&confirm" -o "beam1.png"
curl -L "https://drive.usercontent.google.com/download?id=1kcY7VuTGO573P6GnzYOrt6UiQLkJRS3h&confirm" -o "beam1.csv"
 
REM (5)run example (no quotes) "pyzo-example"
cmd /k