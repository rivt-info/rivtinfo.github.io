echo Y | rmdir docs /S
sphinx-build -E rstdocs docs 
copy /y CNAME .\docs
copy /y .nojekyll .\docs
REM xcopy /y .\rstdocs\README.txt .\docs
