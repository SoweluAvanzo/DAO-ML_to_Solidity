import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.jinja.t_j_base as tjb

"""
No differences at the moment from the super (Jinja Base) class.
"""
class TemplateJinjaPetriNets(tjb.TemplateJinjaBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None, key_template_name:str=None, key_template_skeleton:str=None, key_template_instance_data:str=None):
        super().__init__(pipeline_item_data, optional_external_data, key_template_name, key_template_skeleton, key_template_instance_data)
