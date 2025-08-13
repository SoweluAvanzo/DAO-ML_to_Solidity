
import os
import sys

current_working_directory = os.getcwd() # WARNING: no path-separator at the end!

paths_map = { x:x for x in sys.path }

def preload_modules(modules_list: list, base_path:str=None):
    if base_path is None:
        base_path = current_working_directory
    sys.path.extend([
        os.path.join(base_path, module_name)
        for module_name in modules_list
            if module_name not in paths_map
    ])
