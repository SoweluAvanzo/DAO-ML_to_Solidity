import src.postprocessing.model_translation.shared.translation_result_subpart as crsp
import src.model.base_entity as base_entity_module


class TranslatedSubpartTemplated(crsp.TranslatedSubpart):
    def __init__(self, entity: base_entity_module.BaseEntity, entity_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(entity, entity_specific_data, is_convertible=is_convertible)
        self.template_filename_input: str = ""
        self.template_filename_output: str = ""
        self.template_full_folders_path_from_base: str = ""

    def get_alternative_name(self):
        return self.template_filename_output
