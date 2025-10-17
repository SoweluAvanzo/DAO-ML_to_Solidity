import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_base as tjb


"""
No differences at the moment from the super (Jinja Base) class.
"""


class CompilerSolidityTemplateJinja(tjb.CompilerTemplateJinjaBase):
    """
    It fundamentally relies on an instance of ModelToTemplateMapperBase
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 optional_external_data=None,
                 key_template_instance_data: str = None,
                 key_template_skeleton: str = None,
                 key_diagram_model: str = None
                 ):
        if not isinstance(pipeline_item_data, pi.PIData):
            raise Exception(
                f"pipeline_item_data is not a PIData: {type(pipeline_item_data)}")
        super().__init__(
            pipeline_item_data,
            optional_external_data=optional_external_data,
            key_template_instance_data=key_template_instance_data,
            key_template_skeleton=key_template_skeleton
        )
        self.key_diagram_model = key_diagram_model

    #
