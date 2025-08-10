import src.postprocessing.output_preparation.templates.jinja.model_to_template_mapper_jinja as mttmr_j
#import src.model.base_entity as be

class ModelToTemplateMapperJinja_1_0_0(mttmr_j.ModelToTemplateMapperJinja):
    """
    @Deprecated: this responsiblity has been delegated to the appropriate Jinja compiler since they MUST know what template they will populate
    """
    def __init__(self, version="1.0.0"):
        super().__init__(version)
    
    