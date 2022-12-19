import os
import fnmatch
for file in os.listdir("."):
   if fnmatch.fnmatch(file, "c[0-9][0-9][0-9][0-9]_*.py"):
        print(file)