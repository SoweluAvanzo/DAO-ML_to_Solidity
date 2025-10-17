import src.pipeline.pipeline_item as pi

import src.utilities.errors as e_c


class TemplateBase(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, key_template_instance_data: str = None):
        """
        Base class for each template(s)-based compilers. Each implementation might be based on one or more different templates; that's
        why no template name nor skeleton is involved at this level of class-implementation.
        @param key_template_instance_data : the input's key of a class/map/dict holding the values to populate the current instance of this template.
        """
        # @param key_template_skeleton : the input's key of the data structure holding the representation of a template (each of its parts, like loops, lists, arrays)
        super().__init__(pipeline_item_data)
        self.optional_external_data = optional_external_data
        self.key_template_instance_data = key_template_instance_data

    def compile_template(self, instance_data: dict, additional_data=None):
        raise Exception(
            f"{e_c.ERROR_TEXT__NOT_IMPLEMENTED} on instance: {type(instance_data)}")

    def run(self, inputs):
        print(
            f"running TemplateBase ({type(self)}) with key: {self.get_key()}")
        return self.compile_template(\
            # inputs[self.key_template_name] if self.key_template_name else self.get_ith_input(0), \
            # inputs[self.key_template_skeleton] if self.key_template_skeleton else self.get_ith_input(1),
            inputs[self.key_template_instance_data] if self.key_template_instance_data else self.get_ith_input(
                0),
            additional_data=inputs
        )
