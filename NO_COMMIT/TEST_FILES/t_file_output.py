#import files.FileManager2 as fm
#from ...files import FileManager as fm
#from .. import fm # -> ImportError: attempted relative import with no known parent package

import os
import sys
cwddd = os.getcwd()
sys.path.extend([cwddd, os.path.join(cwddd, "modules_utils")])
import modules_utils as mu
mu.preload_modules(["files", "output"])

# ... then, importo all the necessary modules
import files.FileManager2 as fm
import output.TextFileOutput as tfo

print("START")


folder_base = "./out_test/"
t_f_o = tfo.TextFileOutput(folder_base)

print("TextFileOutput creato")


empty_template_renderer = {}
file_m = fm.FileManager2(folder_path=folder_base, file_output=t_f_o, template_renderer=empty_template_renderer)

print("FileManager creato")


lines = [
    "Ciao Mamma",
    "sto facendo dei test",
    "testo i moduli"
]

filename = "out_test_file_manager_text"
extension = "txt"

print(".... printing to file:", filename, extension)

done = file_m.to_output(lines, filename, extension)

print("... done?", done)
