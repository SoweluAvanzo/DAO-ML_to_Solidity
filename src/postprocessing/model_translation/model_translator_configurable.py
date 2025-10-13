import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.shared.model_converter_base as mcb
import src.postprocessing.model_translation.shared.conversion_result_base as crb
import src.postprocessing.model_translation.translation_types as ct
import src.model.diagram_manager as dm


class ModelTranslatorConfigurable(mcb.ModelTranslatorBase):
    """
    TODO: should be the actual translator, a refactored one which implements
    the whole translator selection process depending on some configuration
    """
    KEY_ADDITIONAL_DATA_TARGET_VERSION = "target_version"
    __KEY__SOLIDITY_CONVERTER_CONFIGURABLE = "solidity_converter_configurable"

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_converter_type: str = None,
                 key_converter_version: str = None,
                 key_converter_target: str = None,
                 additional_data: dict = None
                 ):
        super().__init__(pipeline_item_data, key_model)
        self.key_converter_type = key_converter_type
        self.key_converter_version = key_converter_version
        self.key_converter_target = key_converter_target
        self.additional_data = additional_data

    #

    def get_default_converter_type(self, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        return ct.TranslationTypes.SOLIDITY.value

    def get_converter_type(self, diagram: dm.DiagramManager, additional_data: dict = None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        converter_type = additional_data[self.key_converter_type] if self.key_converter_type is not None \
            and self.key_converter_type in additional_data else \
            self.get_ith_input(additional_data, 1)
        if converter_type is None:
            converter_type = self.get_default_converter_type(additional_data)
        return converter_type

    #

    def new_solidity_converter_configurable(self, additional_data: dict = None):
        import src.postprocessing.model_translation.solidity.solidity_translator_configurable as stc
        return stc.SolidityTranslatorConfigurable(self.pipeline_item_data, self.key_model,
                                                  self.key_converter_type, self.key_converter_version, self.key_converter_target)

    def get_default_converter_version(self, converter_type: str, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        c_v = None
        if converter_type is not None:
            match converter_type:
                case ct.TranslationTypes.SOLIDITY.value:
                    stc_instance = self.new_solidity_converter_configurable(
                        additional_data)
                    if additional_data is not None:
                        additional_data[ModelTranslatorConfigurable.__KEY__SOLIDITY_CONVERTER_CONFIGURABLE] = stc_instance
                    c_v = stc_instance.get_default_converter_version(
                        converter_type, additional_data=additional_data)
                # TODO 2025-08-06 add ASM one
        if c_v is None:
            raise Exception(
                f"Can't define a proper default converter version for converter type: {converter_type}")
        return c_v

    def get_converter_version(self, diagram: dm.DiagramManager, converter_type: str, additional_data: dict = None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        converter_version = additional_data[self.key_converter_version] if self.key_converter_version is not None \
            and self.key_converter_version in additional_data else \
            self.get_ith_input(additional_data, 2)
        if converter_version is None:
            converter_version = self.get_default_converter_version(
                converter_type, additional_data)
        return converter_version

    #

    def get_default_converter_target(self, converter_type: str, converter_version: str, additional_data: dict = None) -> str:
        """
        Override-designed
        """
        raise Exception(
            f"Too much details needed to implement get_default_converter_target for {self.__class__.__name__}")

    def get_converter_target(self, diagram: dm.DiagramManager, converter_type: str, converter_version: str, additional_data: dict = None) -> str:
        """
        Override-designed, despite having a default implementation
        """
        converter_target = additional_data[self.key_converter_target] if self.key_converter_target is not None \
            and self.key_converter_target in additional_data else \
            self.get_ith_input(additional_data, 3)
        if converter_target is None:
            converter_target = self.get_default_converter_target(
                converter_type, converter_version, additional_data)
        return converter_target

    #

    def select_implementation(self, diagram: dm.DiagramManager, converter_type: str, converter_version: str, converter_target: str, additional_data: dict = None) -> mcb.ModelTranslatorBase:
        impl = None
        match converter_type:
            case ct.TranslationTypes.SOLIDITY.value:
                import src.postprocessing.model_translation.solidity.solidity_translator_configurable as stc
                stc_instance: stc.SolidityTranslatorConfigurable = None
                if additional_data is not None and ModelTranslatorConfigurable.__KEY__SOLIDITY_CONVERTER_CONFIGURABLE in additional_data:
                    stc_instance = additional_data[ModelTranslatorConfigurable.__KEY__SOLIDITY_CONVERTER_CONFIGURABLE]
                else:
                    stc_instance = self.new_solidity_converter_configurable(
                        additional_data)
                impl = stc_instance.select_implementation(
                    diagram, converter_type, converter_version, converter_target, additional_data)
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
        converter_type = self.get_converter_type(diagram, additional_data)
        converter_version = self.get_converter_version(
            diagram, converter_type, additional_data)
        converter_target = self.get_converter_target(
            diagram, converter_type, converter_version, additional_data)
        # get the implementation
        implementation: mcb.ModelTranslatorBase = self.select_implementation(
            diagram, converter_type, converter_version, converter_target, additional_data)
        if implementation is None:
            return None
        if ModelTranslatorConfigurable.KEY_ADDITIONAL_DATA_TARGET_VERSION not in additional_data:
            additional_data[ModelTranslatorConfigurable.KEY_ADDITIONAL_DATA_TARGET_VERSION] = converter_target
        return implementation.translate(diagram, additional_data)
