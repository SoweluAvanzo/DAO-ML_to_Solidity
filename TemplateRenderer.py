
from jinja2 import Template
from FileHandler import get_base_folder, concat_folder_filename

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
