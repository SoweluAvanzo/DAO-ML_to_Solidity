import src.pipeline.pipeline_item as pi
import src.model.diagram_manager as dm
import src.postprocessing.output_preparation.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.templates.jinja.compiled_solidity as tcs
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg


"""
No differences at the moment from the super (Jinja Base) class.
"""
class TemplateJinjaSolidity(tjb.TemplateJinjaBase):
    """
    It fundamentally relies on an instance of ModelToTemplateMapperBase
    """
    def __init__(self, pipeline_item_data: pi.PIData, \
                optional_external_data=None, \
                key_diagram_instance_data:str=None, \
                key_template_skeleton:str=None, \
                key_diagram_model:str=None \
                ):
        super().__init__(pipeline_item_data, optional_external_data=optional_external_data,\
                key_diagram_instance_data=key_diagram_instance_data, \
                key_template_skeleton=key_template_skeleton \
            )
        self.key_diagram_model = key_diagram_model

    #

    def run(self, inputs):
        return self.compile_template(\
            self.get_ith_input(inputs, 0) if self.key_diagram_instance_data is None else inputs[self.key_diagram_instance_data], \
            additional_data=inputs \
        )
