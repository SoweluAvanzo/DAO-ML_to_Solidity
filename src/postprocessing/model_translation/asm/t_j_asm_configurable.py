import src.pipeline.pipeline_item as pi


import src.postprocessing.model_translation.translation_types as tt
import src.postprocessing.model_translation.shared.model_translator_base as mcb
import src.postprocessing.model_translation.shared.model_translator_subparts as mts

import src.postprocessing.model_translation.asm.t_j_asm_1_0_0 as t_j_asm_1_0_0
import src.postprocessing.model_translation.asm.translator_asm_versions as t_asm_versions


import src.model.diagram_manager as dm

import src.utilities.utils as u


class TranslatorJinjaASMConfigurable(mts.ModelTranslatorSubparts):
    """
    Base class for all ASM Translators (all of them are templates[Jinja]-based).
    """

    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_model: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         key_model=key_model,
                         printer_debug=printer_debug
                         )
        self.optional_external_data = optional_external_data

    #

    def get_default_translator_target(self, translator_type: str, translator_version: str, additional_data: dict = None) -> str:
        return t_j_asm_1_0_0.TARGET_VERSION

    def get_default_translator_type(self, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        return tt.TranslationTypes.ASM.value

    def get_default_translator_version(self, translator_type: str, additional_data: dict = None) -> str:
        return t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value

    def new_subclass_instance(self, translator_version: str, additional_data: dict = None):
        translator_instance = None
        match translator_version:
            case t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value:
                translator_instance = t_j_asm_1_0_0.TranslatorJinjaASM_1_0_0(self.pipeline_item_data,
                                                                             key_model=self.key_model,
                                                                             optional_external_data=additional_data,
                                                                             printer_debug=self.printer_debug
                                                                             )
        return translator_instance

    def select_implementation(self, diagram: dm.DiagramManager, translator_type: str, translator_version: str, translator_target: str, additional_data: dict = None) -> mcb.ModelTranslatorBase:
        return self.new_subclass_instance(translator_version, additional_data)
