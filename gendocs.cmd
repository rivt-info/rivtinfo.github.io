echo Y | rmdir docs /S
sphinx-build rstdocs docs -E
copy /y CNAME .\docs\
copy /y .nojekyll .\docs\
xcopy /y .\rstdocs\README.txt .\docs\
