#import os
#from FileHandler import get_base_folder, concat_folder_filename, check_and_make_folder
import output.OutputManager as om


import os
def check_and_make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
def get_base_folder(folder_base):
    return folder_base if folder_base != None else os.getcwd()
def concat_folder_filename(*parts):
    return os.path.join(*parts)

class TextFileOutput(om.OutputManager):
    def __init__(self, folder_base:str=None):
        super().__init__(default_destination=folder_base)

    def to_output(self, what:any, destination: any) -> any:
        with open(destination , 'w') as f:
            for line in what:
                f.write(line)
                f.write('\n')
                f.flush()


    def to_file(self, filename:str, lines, extension="txt", folder_base:str=None):
        if folder_base == None:
            folder_base = get_base_folder(self.default_destination)
        check_and_make_folder(folder_base)
        full_path = concat_folder_filename(folder_base, f"{filename}.{extension}")
        self.to_output(lines, full_path)
