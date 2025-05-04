import os
# import files.file_utils as fu
import  output.TextFileOutput as tfo

base_path =  os.path.join('.', 'outttt', 'ooouuuttt')
filename = 'outt'
extension = 'txt'


lines = [
    "Ciao Mamma",
    "sto facendo dei test",
    "testo i moduli"
]

t_f_o = tfo.TextFileOutput()

print("start")
t_f_o.to_file(lines, base_path, filename, extension)

print("fine")
