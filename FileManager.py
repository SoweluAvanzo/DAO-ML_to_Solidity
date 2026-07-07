from OutputManager import OutputManager
from FileHandler import get_base_folder
from TextFileOutput import TextFileOutput
from TemplateRenderer import TemplateRenderer


'''
Classe proxy che raccoglie varie classi di utility che gestiscono file e offre
servizi assimilabili a tale tematica 
'''
class FileManager(OutputManager):
    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = get_base_folder(folder_path)
        self.text_file_output = TextFileOutput(self.folder_path)
        self.template_renderer = TemplateRenderer(self.folder_path)

    def to_output(self, lines:list[str], filename: str, extension:str=None):
        self.text_file_output.to_file(filename, lines, extension, self.folder_path)
        return True

    def save_into_template(self, data_dict, filename_template, filename_output, extension_template='jinja', extension_output='js') -> bool:
        lines = self.template_renderer.render_template(data_dict, filename_template, extension_template, self.folder_path)
        if lines == None:
            raise Exception(f"None lines while rendering template named: '{filename_template}'.")
        self.to_output(lines, filename_output, extension_output)
        return True
