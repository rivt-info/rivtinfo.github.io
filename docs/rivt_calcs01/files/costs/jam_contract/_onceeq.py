
# Pyzo command lines:
# cd C:\\Users\\rhh\\Dropbox\\StructureLabs\\_projects\\mill_valley\\00_admin\\jam_contract
# run -m onceutf 0001.mvscope3.txt

""" 
this file contains Python equations from the on-c-e model 
 0001.mvscope3.txt

For interactive analysis copy and paste the entire file
into an Ipython Notebook cell or Komodo IDE interactive shell.

For interactive analysis in IPython in Komodo click on
the IP[y] toolbar button. The equations will be copied to
the sqlite history database and opened in the IPython interpreter.

For interactive analysis in the Pyzo shell copy and paste
the Pyzo command lines above - one at a time.  Copy and paste equations from this file into the shell for interactive analysis - one at a time
""" 
 
from __future__ import division
from __future__ import print_function
import os
import sys
from sympy import *
from numpy import *
import numpy.linalg as LA
from collections import OrderedDict
sys.path.append('C:\\Users\\rhh\\Dropbox\\StructureLabs\\_projects\\mill_valley\\00_admin\\jam_contract')
try:
   from unum import Unum
except:
 print('unum module not found')

try:
   from unitc import *
   print('unitc imported from directory')
except:
    try:
        from oncepy.unitc import *
        print('unitc imported from oncepy')
    except:
       print('unitc not found')
       pass


# begin equations
_vardef = []
