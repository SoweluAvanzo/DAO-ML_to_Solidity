import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.solidity_translator_general as sol_transl_general


class TranslatorOptimizedDiamond(sol_transl_general.TranslatorGeneral):
    
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def translate(self, additional_data=None):
        raise Exception("Not implemented yet : TranslatorOptimizedDiamond")
