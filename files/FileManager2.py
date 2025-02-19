#from output.OutputManager import OutputManager
import output.OutputManager as om
import output.TextFileOutput as tfo

import os
def get_base_folder(folder_base):
    return folder_base if folder_base != None else os.getcwd()

#import templates_py.TemplateRenderer as tr


'''
Classe proxy che raccoglie varie classi di utility che gestiscono file e offre
servizi assimilabili a tale tematica 
'''
class FileManager2(om.OutputManager):
    def __init__(self, folder_path, file_output=None, template_renderer=None):
        super().__init__()
        self.folder_path = get_base_folder(folder_path)
        self.text_file_output = tfo.TextFileOutput(self.folder_path) if file_output is None else file_output
        #self.template_renderer = tr.TemplateRenderer(self.folder_path) if template_renderer is None else template_renderer

    def to_output(self, lines:list, filename: str, extension:str=None):
        self.text_file_output.to_file(filename, lines, extension, self.folder_path)
        return True

    def save_from_template(self, data_dict, filename_template, filename_output, extension_template='jinja', extension_output='js') -> bool:
        lines = data_dict['lines'] # self.template_renderer.render_template(data_dict, filename_template, extension_template, self.folder_path)
        if lines == None:
            raise Exception(f"None lines while rendering template named: '{filename_template}'.")
        self.to_output(lines, filename_output, extension_output)
        return True
