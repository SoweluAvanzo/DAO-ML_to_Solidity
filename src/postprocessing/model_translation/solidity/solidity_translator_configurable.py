import src.pipeline.pipeline_item as pi

import src.model.diagram_manager as dm

import src.postprocessing.model_translation.shared.model_translator_base as mcb
import src.postprocessing.model_translation.model_translator_configurable as mcc
import src.postprocessing.model_translation.solidity.translation_types_solidity as tts

import src.utilities.utils as u


class SolidityTranslatorConfigurable(mcc.ModelTranslatorConfigurable):
    """
    TODO: should be the actual translator, a refactored one which implements
    the whole translator selection process depending on some configuration
    """
    __KEY__SOLIDITY_TRANSLATOR_OPTIMIZED = "solidity_translator_optimized"

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_translator_type: str = None,
                 key_translator_version: str = None,
                 key_translator_target: str = None,
                 key_translator_solidity_subtype: str = None,
                 key_force_governance_area_split: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data, key_model,
                         key_translator_type,
                         key_translator_version,
                         key_translator_target,
                         printer_debug=printer_debug
                         )
        self.key_translator_solidity_subtype = key_translator_solidity_subtype
        self.key_force_governance_area_split = key_force_governance_area_split

    def get_default_translator_solidity_subtype(self, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        return tts.TranslationTypesSolidity.OPTIMIZED.value

    def get_translator_solidity_subtype(self, diagram: dm.DiagramManager, additional_data: dict = None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        translator_subtype = additional_data[self.key_translator_solidity_subtype] if self.key_translator_solidity_subtype is not None \
            and self.key_translator_solidity_subtype in additional_data else \
            self.get_ith_input(additional_data, 4)
        if translator_subtype is None:
            translator_subtype = self.get_default_translator_solidity_subtype(
                additional_data)
        return translator_subtype

    def new_solidity_translator_optimized(self, additional_data=None):
        import src.postprocessing.model_translation.solidity.optimized.solidity_translator_optimized_configurable as sol_conv_opt_c
        return sol_conv_opt_c.SolidityTranslatorOptimizedConfigurable(
            self.pipeline_item_data,
            key_model=self.key_model,
            key_translator_type=self.key_translator_type,
            key_translator_version=self.key_translator_version,
            key_translator_target=self.key_translator_target,
            printer_debug=self.printer_debug
        )

    def get_default_translator_version(self, translator_type: str, additional_data: dict = None) -> str:
        translator_solidity_subtype = self.get_default_translator_solidity_subtype(
            additional_data)
        if translator_solidity_subtype == tts.TranslationTypesSolidity.OPTIMIZED.value:
            sco = self.new_solidity_translator_optimized(additional_data)
            if additional_data is not None:
                additional_data[SolidityTranslatorConfigurable.__KEY__SOLIDITY_TRANSLATOR_OPTIMIZED] = sco
            return sco.get_default_translator_version(translator_type, additional_data)
        # get_default_translator_target
        return None
    """
    def select_implementation(self, translation_type:str, version:str, additional_metadata=None) -> sol_transl_general.SolidityTranslatorGeneral
        #TODO 2025/08/03 DA FAREEEEEEEEEEE
        translator_subtype = self.get_translator_solidity_subtype(di)
        tts.TranslationTypesSolidity
        return None
    """

    def select_implementation(self, diagram: dm.DiagramManager, translator_type: str, translator_version: str, translator_target: str, additional_data: dict = None) -> mcb.ModelTranslatorBase:
        impl = None
        translator_solidity_subtype = self.get_translator_solidity_subtype(
            diagram, additional_data)
        match translator_solidity_subtype:
            case tts.TranslationTypesSolidity.OPTIMIZED.value:
                import src.postprocessing.model_translation.solidity.optimized.solidity_translator_optimized_configurable as sol_conv_opt_c
                sco_instance: sol_conv_opt_c.SolidityTranslatorOptimizedConfigurable = None
                if additional_data is not None and SolidityTranslatorConfigurable.__KEY__SOLIDITY_TRANSLATOR_OPTIMIZED in additional_data:
                    self.print_msg(
                        "recycling the solidity translator optimized instance")
                    sco_instance = additional_data[SolidityTranslatorConfigurable.__KEY__SOLIDITY_TRANSLATOR_OPTIMIZED]
                else:
                    sco_instance = self.new_solidity_translator_optimized(
                        additional_data)
                self.print_error(
                    f"solidity translator optimized invoking select_implementation of sco_instance type: {type(sco_instance)}, with : translator_type: {translator_type}, translator_version: {translator_version}, translator_target: {translator_target}, ")
                impl = sco_instance.select_implementation(
                    diagram, translator_type, translator_version, translator_target, additional_data)
                if impl is None:
                    self.print_error(
                        f"solidity translator optimized implementation is still None! sco_instance type: {type(sco_instance)}")
        # TODO
        if impl is None:
            raise Exception(
                f"TODO : {translator_solidity_subtype} still to be implemented 2025-08-06")
        return impl
