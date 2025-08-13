
from jinja2 import Template
from FileHandler import get_base_folder, concat_folder_filename

import templates_py.basic_template as bt
import output.OutputManager as om
import DiagramManager2 as dm


class SolidityJinjaTemplate(bt.BasicTemplate):
    '''
    refactor "TemplateRenderer" as this class
    @deprecated
    '''

    def __init__(self, template_name="", filename=""):
            super().__init__(template_name, filename)
            self.extension = "jinja"
    
    # TODO
    def render(self, diagram_manager:dm.DiagramManager2, data=None, output_manager:om.OutputManager=None):
        data_dict = data if data is not None else {}
        # filename = data["filename"] if "filename" in data_dict else self.filename # TODO: IS IT ACTUALLY NEEDED?



'''
class TemplateRenderer:
    def __init__(self, folder_base:str=None, extension:str=None):
        # TODO: super().__init__(???)
        self.folder_base = folder_base
        self.extension = extension

    def render_template(self, data_dict:dict[str,any], filename: str, extension:str=None, folder_base:str=None) -> list[str]:
        if folder_base == None:
            folder_base = get_base_folder(self.folder_base)
        if extension == None:
            extension = self.extension
        if extension == None: # still None?
            extension = 'jinja' #default
        rendered_lines:list[str] = []
        with open( concat_folder_filename(folder_base, f"{filename}.{extension}"), 'r', encoding='utf-8') as f:
            template_content = f.read()
            template = Template(template_content)
            
            rendered_lines = template.render( \
                **data_dict
            ).splitlines()
        return rendered_lines
'''
