from jinja2 import Template

import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.templates.template_base as tb

class TemplateJinjaBase(tb.TemplateBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, key_template_name:str=None, key_template_skeleton:str=None, key_template_instance_data:str=None):
        super().__init__(pipeline_item_data, optional_external_data, key_template_name, key_template_skeleton, key_template_instance_data)
        
    def compile_template(self, name:str, template_skeleton, instance_data:dict):
        if not isinstance(template_skeleton, str):
            if isinstance(template_skeleton, list):
                template_skeleton = "\n".join(template_skeleton)
            else:
                try:
                    template_skeleton = "\n".join(iter(template_skeleton))
                except TypeError as te:
                    print('template_skeleton is not iterable')
                    print(te)
                    raise Exception(f"The template_skeleton is not a string: {type(template_skeleton)}")
        
        template = Template(template_skeleton)
        return  template.render( \
                **instance_data \
            ).splitlines()