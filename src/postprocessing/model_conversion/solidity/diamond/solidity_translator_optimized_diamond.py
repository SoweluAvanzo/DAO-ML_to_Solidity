import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.solidity_converter_general as sol_transl_general


class SolidityConverterOptimizedDiamond(sol_transl_general.SolidityConverterGeneral):
    
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def convert(self, additional_data=None):
        raise Exception("Not implemented yet : SolidityConverterOptimizedDiamond")
