import src.pipeline.pipeline_item as pi
# import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_translation.solidity.solidity_translator_general as stg
import src.postprocessing.model_translation.solidity.optimized.jinja.s_t_jinja_optimized_versions as j_o_v
# import src.model.diagram_manager as dm
import src.utilities.utils as u


class SolidityTranslatorOptimized(stg.SolidityTranslatorGeneral):

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_translator_type: str = None,
                 key_translator_version: str = None,
                 key_translator_target: str = None,
                 key_force_governance_area_split: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        """
        @param key_translator_version: version of the translation inside THIS very framework
        @param key_translator_target: version of the language ("Solidity"?), framework, tool, etc
        """
        super().__init__(pipeline_item_data,
                         key_model=key_model,
                         key_force_governance_area_split=key_force_governance_area_split,
                         printer_debug=printer_debug
                         )
        self.key_translator_type = key_translator_type
        self.key_translator_version = key_translator_version
        self.key_translator_target = key_translator_target
