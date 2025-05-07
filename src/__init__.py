import os
import sys

init_path_abs = os.path.abspath(__file__)
init_dirname = os.path.dirname( init_path_abs )

src_dirname = os.path.dirname( init_dirname )

parent_folder = os.path.abspath(os.path.join(src_dirname, os.pardir))
print(f"... appending the following parent_folder: _____ {parent_folder} ____")
sys.path.append(parent_folder)
parent_folder = f"{parent_folder}{os.path.sep}"
print(f"... appending the following parent_folder: _____ {parent_folder} ____")
sys.path.append(parent_folder)