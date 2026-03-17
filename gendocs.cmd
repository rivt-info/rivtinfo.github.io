echo Y | rmdir docs /S
sphinx-build -E rstdocs docs 
make pdf
copy /y CNAME .\docs\
copy /y .nojekyll .\docs\
xcopy /y .\rstdocs\README.txt .\docs\
