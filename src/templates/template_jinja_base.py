from jinja2 import Template

import src.pipeline.pipeline_item as pi
import src.templates.template_base as tb

class TemplateJinjaBase(tb.TemplateBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, key_template_name:str=None, key_template_definition:str=None, key_template_instance_data:str=None):
        super().__init__(pipeline_item_data, optional_external_data, key_template_name, key_template_definition, key_template_instance_data)
        
    def compile_template(self, name:str, template_definition, instance_data:dict):
        if not isinstance(template_definition, str):
            if isinstance(template_definition, list):
                template_definition = "\n".join(template_definition)
            else:
                try:
                    template_definition = "\n".join(iter(template_definition))
                except TypeError as te:
                    print('template_definition is not iterable')
                    print(te)
                    raise Exception(f"The template_definition is not a string: {type(template_definition)}")
        
        template = Template(template_definition)
        return  template.render( \
                **instance_data \
            ).splitlines()