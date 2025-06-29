import src.pipeline.pipeline_item as pi
import src.templates.basic_template as bt

class TemplateJinjaSolidity(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, key_template_name:str=None, key_template_definition:str=None, key_template_instance_data:str=None):
        super().__init__(pipeline_item_data, optional_external_data, key_template_name, key_template_definition, key_template_instance_data)

    def compile_template(self, name:str, template_definition, instance_data:dict):
        # TODO - 29/06/2025 : invoke the Jinja classes and functions to compile the template and obtain
        # the (hugely-long) string to output
        return None