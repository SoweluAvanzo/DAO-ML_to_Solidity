
import src.postprocessing.output_preparation.templates.model_to_template_mapper_base as mtt_mapper_b
#import src.model.base_entity as be

class ModelToTemplateMapperJinja(mtt_mapper_b.ModelToTemplateMapperBase): 
    """
    @deprecated : all this responsibility is moved onto the specific translators, since they MUST know what data to produce
    
    This is one of the crucial aspect of templates: sometimes, specific instances or sub-fields require one or more
    templates to be populate, compiled and produced.
    This class serves as a bridge between those two worlds.
    """
    def __init__(self, version="1.0.0"):
        super().__init__()
        self.version = version

    def has_template_filename_for_key(self, entity_or_id_name_classname):
        return False

    def get_template_filename_by_key(self, \
            entity_or_id_name_classname, # : be.BaseEntity,
            additional_data=None \
            ) -> dict[str, str]: 
        raise Exception(f"TODOOOOOOOOOOOOOOOO IMPLEMENT ModelToTemplateMapperJinja")
