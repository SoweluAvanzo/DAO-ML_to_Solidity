import os
from FileHandler import get_base_folder, concat_folder_filename

class TextFileOutput: # TODO: (BaseOutput_XYZ)
    def __init__(self, folder_base:str=None):
        # TODO: super().__init__(???)
        self.folder_base = folder_base

    def to_file(self, filename:str, lines:list[str], extension="txt", folder_base:str=None):
        if folder_base == None:
            folder_base = get_base_folder(self.folder_base)
        with open( concat_folder_filename(folder_base, f"{filename}.{extension}"), 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
                f.flush()
