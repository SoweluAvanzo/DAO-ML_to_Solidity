
#import src.model.base_entity as be

class ModelToTemplateMapperBase: 
    """
    @ deprecated: each Converter MUST be template-aware, so it's its own responsibility to do a proper mapping
    This is one of the crucial aspect of templates: sometimes, specific instances or sub-fields require one or more
    templates to be populate, compiled and produced.
    This class serves as a bridge between those two worlds.
    """

    def has_template_filename_for_key(self, entity_or_id_name_classname):
        return False

    def get_template_filename_by_key(self, \
            entity_or_id_name_classname, # : be.BaseEntity,
            additional_data=None \
            ) -> dict[str, str]:
        """
        For a given model's entity (or anything, Python don't actually type-check, so a name,
        ID, name of the class, or fabricated identifier), returns all the templates name / path
        it needs (or just a single template name/path; again, no type-check is performed),
        mapped by some kind of identifier (like the entity's ID). 
        """
        raise Exception(f"Not implemented yet in current class: {self.__class__.__name__}")
