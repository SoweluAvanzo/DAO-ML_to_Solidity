import src.pipeline.pipeline_item as pi
# import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_translation.solidity.solidity_translator_general as stg
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as j_o_v
# import src.model.diagram_manager as dm


class SolidityTranslatorOptimized(stg.SolidityTranslatorGeneral):

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_converter_type: str = None,
                 key_converter_version: str = None,
                 key_converter_target: str = None
                 ):
        """
        @param key_converter_version: version of the translation inside THIS very framework
        @param key_converter_target: version of the language ("Solidity"?), framework, tool, etc
        """
        super().__init__(pipeline_item_data, key_model)
        self.key_converter_type = key_converter_type
        self.key_converter_version = key_converter_version
        self.key_converter_target = key_converter_target
