import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.shared.model_translator_base as mcb
import src.postprocessing.model_translation.solidity.solidity_translator_configurable as stc
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as j_o_v
import src.postprocessing.model_translation.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as toj_1_0_0
import src.model.diagram_manager as dm

import src.utilities.utils as u


class SolidityTranslatorOptimizedConfigurable(stc.SolidityTranslatorConfigurable):

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_translator_type: str = None,
                 key_translator_version: str = None,
                 key_translator_target: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        """
        @param key_translator_version: version of the translation inside THIS very framework
        @param key_translator_target: version of the language ("Solidity"?), framework, tool, etc
        """
        super().__init__(pipeline_item_data,
                         key_model=key_model,
                         key_translator_type=key_translator_type,
                         key_translator_version=key_translator_version,
                         key_translator_target=key_translator_target,
                         key_translator_solidity_subtype=None,
                         printer_debug=printer_debug
                         )

    def get_default_translator_version(self, translator_type: str, additional_data: dict = None) -> str:
        return j_o_v.JinjaOptimizedVersions.JO_1_0_0.value

    def get_default_translator_target(self, translator_type: str, translator_version: str, additional_data: dict = None) -> str:
        return toj_1_0_0.VERSION

    def new_subclass_instance(self, translator_version: str, additional_data: dict = None):
        self.print_error(
            f"in {type(self)}, called new_subclass_instance with translator_version = {translator_version}")
        translator_instance = None
        match translator_version:
            case j_o_v.JinjaOptimizedVersions.JO_1_0_0.value:
                translator_instance = toj_1_0_0.SolidityTranslatorOptimizedJinja_1_0_0(
                    self.get_pipeline_item_data(),
                    self.key_model,
                    self.key_translator_type,
                    self.key_translator_version,
                    self.key_translator_target,
                    printer_debug=self.printer_debug
                )
            case _:
                self.print_error(
                    f"in {type(self)}, unable to select new_subclass_instance with translator_version = {translator_version}")
        return translator_instance

    def select_implementation(self, diagram: dm.DiagramManager, translator_type: str, translator_version: str, translator_target: str, additional_data: dict = None) -> mcb.ModelTranslatorBase:
        return self.new_subclass_instance(translator_version, additional_data)

    """
        raise Exception(f"(Solidity)SolidityTranslatorOptimized can't select its own delegator for translator type ({translator_type}) and version ({version}): instantiate another one.")
    """
