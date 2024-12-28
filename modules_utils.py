
import os
import sys

current_working_directory = os.getcwd() # WARNING: no path-separator at the end!

paths_map = { x:x for x in sys.path }

def preload_modules(modules_list: list):
    sys.path.extend([
        os.path.join(current_working_directory, module_name)
        for module_name in modules_list
            if module_name not in paths_map
    ])
