import src.pipeline.pipeline_item as pi
import src.model.diagram_manager as dm
import src.postprocessing.model_conversion.shared.model_converter_base as mcb
import src.postprocessing.model_conversion.model_converter_configurable as mcc
#import src.postprocessing.model_conversion.solidity.solidity_translator_general as sol_transl_general
import src.postprocessing.model_conversion.solidity.conversion_types_solidity as tts


class SolidityConverterConfigurable(mcc.ModelConverterConfigurable):
    """
    TODO: should be the actual translator, a refactored one which implements
    the whole translator selection process depending on some configuration
    """
    __KEY__SOLIDITY_CONVERTER_OPTIMIZED = "solidity_converter_optimized"
    
    def __init__(self, pipeline_item_data: pi.PIData, \
                key_model:str=None, \
                key_converter_type:str=None, \
                key_converter_version:str=None, \
                key_converter_target:str=None, \
                key_converter_solidity_subtype:str=None \
            ):
        super().__init__(pipeline_item_data, key_model, \
                key_converter_type, \
                key_converter_version, \
                key_converter_target \
            )
        self.key_converter_solidity_subtype = key_converter_solidity_subtype


    def get_default_converter_solidity_subtype(self, additional_data:dict=None) -> str:
        """
        Override-designed
        """
        return tts.TranslationTypesSolidity.OPTIMIZED.value
    
    def get_converter_solidity_subtype(self, diagram:dm.DiagramManager, additional_data:dict=None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        converter_subtype = additional_data[self.key_converter_solidity_subtype] if self.key_converter_solidity_subtype is not None \
            and self.key_converter_solidity_subtype in additional_data else \
            self.get_ith_input(additional_data, 4)
        if converter_subtype is None:
            converter_subtype = self.get_default_converter_solidity_subtype(additional_data)
        return converter_subtype
    
    def new_solidity_converter_optimized(self, additional_data = None):
        import src.postprocessing.model_conversion.solidity.optimized.solidity_converter_optimized_configurable as sol_conv_opt_c
        return sol_conv_opt_c.SolidityConverterOptimizedConfigurable(self.pipeline_item_data, self.key_model, \
                self.key_converter_type, self.key_converter_version, self.key_converter_target)
    
    def get_default_converter_version(self, converter_type:str, additional_data:dict=None) -> str:
        converter_solidity_subtype = self.get_default_converter_solidity_subtype(additional_data)
        if converter_solidity_subtype == tts.TranslationTypesSolidity.OPTIMIZED.value:
            sco = self.new_solidity_converter_optimized(additional_data)
            if additional_data is not None:
                additional_data[SolidityConverterConfigurable.__KEY__SOLIDITY_CONVERTER_OPTIMIZED] = sco
            return sco.get_default_converter_version(converter_type, additional_data)
        # get_default_converter_target
        return None
    """
    def select_implementation(self, translation_type:str, version:str, additional_metadata=None) -> sol_transl_general.SolidityConverterGeneral
        #TODO 2025/08/03 DA FAREEEEEEEEEEE
        converter_subtype = self.get_converter_solidity_subtype(di)
        tts.TranslationTypesSolidity
        return None
    """
    
    def select_implementation(self, diagram:dm.DiagramManager, converter_type:str, converter_version:str, converter_target:str, additional_data:dict=None) -> mcb.ModelConverterBase:
        impl = None
        converter_solidity_subtype = self.get_converter_solidity_subtype(diagram, additional_data)
        match converter_solidity_subtype:
            case tts.TranslationTypesSolidity.OPTIMIZED.value:
                import src.postprocessing.model_conversion.solidity.optimized.solidity_converter_optimized_configurable as sol_conv_opt_c
                sco_instance:sol_conv_opt_c.SolidityConverterOptimizedConfigurable = None
                if additional_data is not None and SolidityConverterConfigurable.__KEY__SOLIDITY_CONVERTER_OPTIMIZED in additional_data:
                    sco_instance = additional_data[SolidityConverterConfigurable.__KEY__SOLIDITY_CONVERTER_OPTIMIZED]
                else:
                    sco_instance = self.new_solidity_converter_optimized(additional_data)
                impl = sco_instance.select_implementation(diagram, converter_type, converter_version, converter_target, additional_data)
        # TODO
        if impl is None:
            raise Exception("TODO : still to be implemented 2025-08-06")
        return impl
