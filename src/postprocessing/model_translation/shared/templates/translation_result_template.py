import src.postprocessing.model_translation.shared.translation_result_subpart as crsp
import src.model.base_entity as base_entity_module


class TranslatedSubpartTemplated(crsp.TranslatedSubpart):
    """
    Defines a sub-part that is being translated.
    It specifies additional fields related to the template consumed as input and the produced output:
    the name of both of them, and the folder path from a base path towards the input file from which
    the supposed template is retrieved. Those values are suggestions and can be overwritten/ignored.
    """

    def __init__(self, entity: base_entity_module.BaseEntity, entity_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(entity, entity_specific_data, is_convertible=is_convertible)
        self.template_filename_input: str = ""
        self.translated_name_output: str = ""
        self.suggested_input_template_folders_path_from_base: str = ""

    def get_alternative_name(self):
        return self.translated_name_output
