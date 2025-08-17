echo Y | rmdir docs /S
sphinx-build rstdocs docs -E
echo F | scopy /y CNAME .\docs\CNAME
echo F | scopy /y .nojekyll .\docs\.nojekyll
echo F | scopy /y .\rstdocs\README.txt .\docs\README.txt


