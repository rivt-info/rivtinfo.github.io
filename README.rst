rivtlib
========

**rivtlib is alpha software. Some features are not complete and the program has
bugs.**


*rivt* is an extensible, open-source Python tool for writing engineering
documents with a focus on reuse. Python knowledge is not required but *rivt*
capabilities can be extended with Python scripts that access scientific and
engineering libraries. In addition to many types of source files including
images, scripts, data and pdf files, rivt uses four types of primary files and
folders:

.. code-block:: text

                        | A rivt file (.py) is a Python file file that imports
   rivt file            | the rivtlib Python package and compiles to a text,
                        | PDF or HTML doc.

                        | A rivt project folder contains setting and 
   rivt project folder  | configuration files for the IDE and version control, 
                        | as well as one or more rvbook or rvreport folders.

                        | A rivtbook folder is a collection of rivt files with
   rvbook folder        | common subject matter organized to simplify selection
                        | selection of files and resources for inclusion in rivt 

                        | A rivt report folder is a collection of rivt files
   rvreport folder      | organized for publication of rivt docs and reports
                        | as text, html or PDF files.

   






