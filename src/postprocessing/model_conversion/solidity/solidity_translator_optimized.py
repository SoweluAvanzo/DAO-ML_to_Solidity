import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.solidity_translator_general as sol_transl_general
import src.postprocessing.model_conversion.solidity.model_to_solidity as mts


class TranslatorOptimized(sol_transl_general.TranslatorGeneral):
    
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def translate(self, additional_data=None):

        # See " optimized_translator.py # OptimizedSolidityTranslator"
        return None


class TranslationInstanceDataDAOOptimized( mts.TranslationInstanceDataDAOBase ):
    def __init__(self, dao_name):
        super().__init__(dao_name)

    def toJSON(self):
        a = super().toJSON()
        a[] TODO PROSEGUIIIIII
        return a