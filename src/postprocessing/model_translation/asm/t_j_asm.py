import src.pipeline.pipeline_item as pi


import src.postprocessing.model_translation.shared.model_translator_base as mcb
import src.postprocessing.model_translation.shared.translation_result_base as crb
import src.postprocessing.model_translation.shared.templates.translation_result_template as crt
import src.postprocessing.consts_template as c_t

import src.model.dao as dao_m
import src.model.diagram_manager as diagram_manager_m


class TranslatedDAO_ASM_Jinja(crt.TranslatedSubpartTemplated):
    def __init__(self, dao: dao_m.DAO, dao_specific_data: dict,
                 is_convertible: bool = True
                 ):
        crt.TranslatedSubpartTemplated.__init__(
            self, dao, dao_specific_data, is_convertible=is_convertible)
        # dict of ( output_filename, compiled_template )
        """
        self.other_subparts_converted_by_name: dict[str,
            crt.TranslatedSubpartTemplated] = {}
        """


class TranslatedDiagram_ASM_Jinja(crt.TranslatedSubpartTemplated):
    def __init__(self, diagram: diagram_manager_m.DiagramManager, diagram_specific_data: dict,
                 is_convertible: bool = True
                 ):
        crt.TranslatedSubpartTemplated.__init__(
            self, diagram, diagram_specific_data, is_convertible=is_convertible)
        self.dao_converted_by_id: dict[str, TranslatedDAO_ASM_Jinja] = {}
        # dict of ( output_filename, compiled_template )
        """
        self.other_subparts_converted_by_name: dict[str,
            crt.TranslatedSubpartTemplated] = {}
        """

    def add_dao_converted(self, dao_c: TranslatedDAO_ASM_Jinja):
        self.dao_converted_by_id[dao_c.get_id()] = dao_c

#


class TranslatorJinjaASM(mcb.ModelTranslatorBase):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_model: str = None
                 ):
        super().__init__(pipeline_item_data,
                         key_model=key_model
                         )
        self.optional_external_data = optional_external_data

    def new_translated_diagram(self, diagram: diagram_manager_m.DiagramManager, other_data=None) -> TranslatedDiagram_ASM_Jinja:
        """
        Override-designed
        """
        return TranslatedDiagram_ASM_Jinja(diagram, other_data)

    def new_translated_dao(self, diagram: diagram_manager_m.DiagramManager, dao: dao_m.DAO, other_data=None) -> TranslatedDAO_ASM_Jinja:
        """
        Override-designed
        """
        return TranslatedDAO_ASM_Jinja(dao, other_data)

    #

    def translate_DAO_to_ASM(self, diagram: diagram_manager_m.DiagramManager,  dao: dao_m.DAO) -> TranslatedDAO_ASM_Jinja:
        """
        Override-designed
        """
        raise NotImplementedError(
            f"Current class ({type(self)}) still do not implement the translation")

    def translate_Diagram_to_ASM(self, diagram: diagram_manager_m.DiagramManager) -> TranslatedDiagram_ASM_Jinja:
        """
        Override-designed
        """
        diagram_specific_data = None
        diagram_converted = self.new_translated_diagram(
            diagram, other_data=diagram_specific_data)
        diagram_converted.template_filename_input = None  # TODO
        diagram_converted.template_filename_output = None  # TODO
        diagram_converted.template_full_folders_path_from_base = c_t.FOLDER_NAME_ASM
        return diagram_converted

    def translate(self, model: diagram_manager_m.DiagramManager, additional_data=None) -> crb.ModelConversionResultBase:
        diagram_converted = self.translate_Diagram_to_ASM(model)
        for dao in model.daoByID.values():
            dao_converted = self.translate_DAO_to_ASM(model, dao)
            diagram_converted.add_dao_converted(dao_converted)
        return diagram_converted
