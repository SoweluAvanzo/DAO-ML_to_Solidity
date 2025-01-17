import sys
import os
src_path_abs = os.path.abspath(__file__)
print("src_path_abs", src_path_abs)
src_dirname = os.path.dirname( src_path_abs )
print("src_dirname", src_dirname)
sys.path.append(src_dirname)

from . import files
from . import input
from . import model
from . import output
from . import templates
#from . import utilities
