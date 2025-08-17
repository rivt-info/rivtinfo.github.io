echo Y | rmdir docs /S
sphinx-build rstdocs docs -E
echo F | xcopy /y CNAME .\docs\CNAME
echo F | xcopy /y .nojekyll .\docs\.nojekyll
echo F | xcopy /y .\rstdocs\README.txt .\docs\README.txt


