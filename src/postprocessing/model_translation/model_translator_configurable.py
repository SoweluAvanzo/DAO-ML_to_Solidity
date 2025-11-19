import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.shared.model_translator_base as mcb
import src.postprocessing.model_translation.shared.translation_result_base as crb
import src.postprocessing.model_translation.translation_types as ct
import src.model.diagram_manager as dm

import src.utilities.utils as u


class ModelTranslatorConfigurable(mcb.ModelTranslatorBase):
    """
    TODO: should be the actual translator, a refactored one which implements
    the whole translator selection process depending on some configuration
    """
    KEY_ADDITIONAL_DATA_TARGET_VERSION = "target_version"
    __KEY__SOLIDITY_TRANSLATOR_CONFIGURABLE = "solidity_translator_configurable"
    __KEY__ASM_TRANSLATOR_CONFIGURABLE = "asm_translator_configurable"

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_translator_type: str = None,
                 key_translator_version: str = None,
                 key_translator_target: str = None,
                 additional_data: dict = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         key_model=key_model,
                         printer_debug=printer_debug
                         )
        self.key_translator_type = key_translator_type
        self.key_translator_version = key_translator_version
        self.key_translator_target = key_translator_target
        self.additional_data = additional_data

    #

    def get_default_translator_type(self, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        return ct.TranslationTypes.SOLIDITY.value

    def get_translator_type(self, diagram: dm.DiagramManager, additional_data: dict = None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        translator_type = additional_data[self.key_translator_type] if self.key_translator_type is not None \
            and self.key_translator_type in additional_data else \
            self.get_ith_input(additional_data, 1)
        if translator_type is None:
            translator_type = self.get_default_translator_type(additional_data)
        return translator_type

    #

    def new_solidity_translator_configurable(self, additional_data: dict = None):
        """
        Returns a Solidity-aware configurable translator, which is useful to drill down the specific properties
        (like language / target versions) from the eventual sub-implementations
        """
        import src.postprocessing.model_translation.solidity.solidity_translator_configurable as stc
        return stc.SolidityTranslatorConfigurable(self.pipeline_item_data,
                                                  key_model=self.key_model,
                                                  key_translator_type=self.key_translator_type,
                                                  key_translator_version=self.key_translator_version,
                                                  key_translator_target=self.key_translator_target,
                                                  key_translator_solidity_subtype=None,
                                                  printer_debug=self.printer_debug
                                                  )

    def new_asm_translator_configurable(self, additional_data: dict = None):
        import src.postprocessing.model_translation.asm.t_j_asm_configurable as t_j_asm_c
        return t_j_asm_c.TranslatorJinjaASMConfigurable(
            self.pipeline_item_data,
            key_model=self.key_model,
            optional_external_data=additional_data,
            printer_debug=self.printer_debug
        )

    def get_default_translator_version(self, translator_type: str, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        translator_version: str = None
        if translator_type is not None:
            instance_key: str = None
            stc_instance: ModelTranslatorConfigurable = None
            match translator_type:
                case ct.TranslationTypes.SOLIDITY.value:
                    instance_key = ModelTranslatorConfigurable.__KEY__SOLIDITY_TRANSLATOR_CONFIGURABLE
                    stc_instance = self.new_solidity_translator_configurable(
                        additional_data)
                case ct.TranslationTypes.ASM.value:
                    instance_key = ModelTranslatorConfigurable.__KEY__ASM_TRANSLATOR_CONFIGURABLE
                    stc_instance = self.new_asm_translator_configurable(
                        additional_data)
            if additional_data is not None:
                additional_data[instance_key] = stc_instance
            translator_version = stc_instance.get_default_translator_version(
                translator_type, additional_data=additional_data)
        if translator_version is None:
            raise Exception(
                f"Can't define a proper default translator version for translator type: {translator_type}")
        return translator_version

    def get_translator_version(self, diagram: dm.DiagramManager, translator_type: str, additional_data: dict = None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        translator_version = additional_data[self.key_translator_version] if self.key_translator_version is not None \
            and self.key_translator_version in additional_data else \
            self.get_ith_input(additional_data, 2)
        if translator_version is None:
            translator_version = self.get_default_translator_version(
                translator_type, additional_data)
        return translator_version

    #

    def get_default_translator_target(self, translator_type: str, translator_version: str, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        raise Exception(
            f"Too much details needed to implement get_default_translator_target for {self.__class__.__name__}")

    def get_translator_target(self, diagram: dm.DiagramManager, translator_type: str, translator_version: str, additional_data: dict = None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        translator_target = additional_data[self.key_translator_target] if self.key_translator_target is not None \
            and self.key_translator_target in additional_data else \
            self.get_ith_input(additional_data, 3)
        if translator_target is None:
            translator_target = self.get_default_translator_target(
                translator_type, translator_version, additional_data)
        return translator_target

    #

    def select_implementation(self, diagram: dm.DiagramManager, translator_type: str, translator_version: str, translator_target: str, additional_data: dict = None) -> mcb.ModelTranslatorBase:
        impl = None
        if additional_data is None:
            additional_data = {}
        match translator_type:
            case ct.TranslationTypes.SOLIDITY.value:
                import src.postprocessing.model_translation.solidity.solidity_translator_configurable as stc
                stc_instance: stc.SolidityTranslatorConfigurable = None
                # recycle the "configurable" implementation if available
                if ModelTranslatorConfigurable.__KEY__SOLIDITY_TRANSLATOR_CONFIGURABLE in additional_data:
                    stc_instance = additional_data[ModelTranslatorConfigurable.__KEY__SOLIDITY_TRANSLATOR_CONFIGURABLE]
                else:
                    stc_instance = self.new_solidity_translator_configurable(
                        additional_data)
                    additional_data[ModelTranslatorConfigurable.__KEY__SOLIDITY_TRANSLATOR_CONFIGURABLE] = stc_instance
                impl = stc_instance.select_implementation(
                    diagram, translator_type, translator_version, translator_target, additional_data)
            case ct.TranslationTypes.ASM.value:
                import src.postprocessing.model_translation.asm.t_j_asm_configurable as t_j_asm_c
                asm_t_c_instance: t_j_asm_c.TranslatorJinjaASMConfigurable = None
                # recycle the "configurable" implementation if available
                if ModelTranslatorConfigurable.__KEY__ASM_TRANSLATOR_CONFIGURABLE in additional_data:
                    asm_t_c_instance = additional_data[ModelTranslatorConfigurable.__KEY__ASM_TRANSLATOR_CONFIGURABLE]
                else:
                    asm_t_c_instance = self.new_asm_translator_configurable(
                        additional_data)
                    additional_data[ModelTranslatorConfigurable.__KEY__ASM_TRANSLATOR_CONFIGURABLE] = asm_t_c_instance
                impl = asm_t_c_instance.select_implementation(
                    diagram, translator_type, translator_version, translator_target, additional_data)
        # TODO
        if impl is None:
            raise Exception("TODO : still to be implemented 2025-08-06")
        return impl

    def translate(self, diagram: dm.DiagramManager, additional_data: dict = None) -> crb.ModelConversionResultBase:
        if additional_data is None:
            additional_data = {}
        if self.additional_data is not None:
            additional_data = {
                **additional_data,
                **(self.additional_data)
            }
        # get the trio of translator discriminators
        translator_type = self.get_translator_type(diagram, additional_data)
        translator_version = self.get_translator_version(
            diagram, translator_type, additional_data)
        translator_target = self.get_translator_target(
            diagram, translator_type, translator_version, additional_data)
        # get the implementation
        implementation: mcb.ModelTranslatorBase = self.select_implementation(
            diagram, translator_type, translator_version, translator_target, additional_data)
        if implementation is None:
            return None
        if ModelTranslatorConfigurable.KEY_ADDITIONAL_DATA_TARGET_VERSION not in additional_data:
            additional_data[ModelTranslatorConfigurable.KEY_ADDITIONAL_DATA_TARGET_VERSION] = translator_target
        # do the actual translation
        return implementation.translate(diagram, additional_data)
