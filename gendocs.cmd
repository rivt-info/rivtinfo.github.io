echo Y | rmdir ./docs /S
sphinx-build -E ./rstdocs ./docs 
copy /y CNAME docs
copy /y .nojekyll docs
copy /y README.rst docs
