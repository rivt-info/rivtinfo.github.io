echo Y | rmdir htmlpages /S
sphinx-build . htmlpages
echo F | xcopy /y CNAME .\htmlpages\CNAME
echo F | xcopy /y .nojekyll .\htmlpages\.nojekyll
