import src.pipeline.pipeline_item as pi
# import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_translation.shared.model_converter_base as mcb
import src.postprocessing.model_translation.solidity.solidity_translator_configurable as stc
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as j_o_v
import src.postprocessing.model_translation.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as coj_1_0_0
import src.model.diagram_manager as dm


class SolidityTranslatorOptimizedConfigurable(stc.SolidityTranslatorConfigurable):

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

    def get_default_converter_version(self, converter_type: str, additional_data: dict = None) -> str:
        return j_o_v.JinjaOptimizedVersions.JO_1_0_0.value

    def new_subclass_instance(self, converter_version: str, additional_data: dict = None):
        converter_instance = None
        match converter_version:
            case j_o_v.JinjaOptimizedVersions.JO_1_0_0.value:
                converter_instance = coj_1_0_0.SolidityTranslatorOptimizedJinja_1_0_0(self.get_pipeline_item_data(),
                                                                                      self.key_model,
                                                                                      self.key_converter_type,
                                                                                      self.key_converter_version,
                                                                                      self.key_converter_target
                                                                                      )
        return converter_instance

    def select_implementation(self, diagram: dm.DiagramManager, converter_type: str, converter_version: str, converter_target: str, additional_data: dict = None) -> mcb.ModelTranslatorBase:
        return self.new_subclass_instance(converter_version, additional_data)

    """
        raise Exception(f"(Solidity)SolidityTranslatorOptimized can't select its own delegator for translator type ({translator_type}) and version ({version}): instantiate another one.")
    """
