import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.optimized.jinja.jinja_optimized_versions as j_o_v
import src.postprocessing.model_conversion.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as to_sol_j_1_0_0
import src.postprocessing.model_conversion.solidity.optimized.solidity_translator_optimized as sol_transl_opt
import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg
import src.model.enums.relation_type as rt
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

class TranslatorOptimizedJinja(sol_transl_opt.TranslatorOptimized):
    """
    All of this subclasses bear the responsibility of declaring and defining which kind of templates they are using
    """

    def __init__(self, pipeline_item_data: pi.PIData, \
                key_model:str=None, \
                key_translator_type:str=None, \
                key_version:str=None):
        super().__init__(\
            pipeline_item_data, \
            key_model, \
            key_translator_type, \
            key_version)


        #
    def select_delegator(self, diagram:dm.DiagramManager, translator_type:str, version:str,  additional_data:dict=None) -> mcb.ModelConverterBase:
        if version == j_o_v.JinjaOptimizedVersions.JO_1_0_0.value:
            return to_sol_j_1_0_0.TranslatorOptimizedJinja_1_0_0(self.get_pipeline_item_data(), \
                                                                self.key_model, \
                                                                self.key_translator_type, \
                                                                self.key_version)
        return None # no version found

