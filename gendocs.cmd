echo Y | rmdir docs /S
sphinx-build . docs
echo F | xcopy /y CNAME .\docs\CNAME
echo F | xcopy /y .nojekyll .\docs\.nojekyll
