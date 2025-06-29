import src.pipeline.pipeline_item as pi

class TemplateBase(pi.PipelineItem): 
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, key_template_name:str=None, key_template_definition:str=None, key_template_instance_data:str=None):
        """
        @param key_template_definition : the input's key of the data structure holding the representation of a template (each of its parts,
            like loops, lists, arra)
        @param key_template_instance_data : the input's key of a map/dict holding the values to populate the current instance of this template.
        """
        super().__init__(pipeline_item_data)
        self.optional_external_data = optional_external_data
        self.key_template_name = key_template_name
        self.key_template_definition = key_template_definition
        self.key_template_instance_data = key_template_instance_data

    def compile_template(self, name:str, template_definition, instance_data:dict):
        raise Exception("Not implemented yet")
    
    def run(self, inputs):
        return self.compile_template(\
            inputs[self.key_template_name if self.key_template_name else self.get_ith_input(0)], \
            inputs[self.key_template_definition if self.key_template_definition else self.get_ith_input(1)], \
            inputs[self.key_template_instance_data if self.key_template_instance_data else self.get_ith_input(2)] \
        )
