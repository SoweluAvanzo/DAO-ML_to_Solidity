import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.solidity_translator_general as sol_transl_general
import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg
import src.model.diagram_manager as dm

class TranslatorOptimized(sol_transl_general.TranslatorGeneral):
    
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def translate(self, model:dm.DiagramManager, additional_data:dict=None) -> stg.TranslatedDiagram:
        # See " optimized_translator.py # OptimizedSolidityTranslator"
        diagram_specific_data_translated = None

        # TODO: tutto il resto della traduzione (il Diagram Manager nello specifico)

        td = stg.TranslatedDiagram(model, diagram_specific_data_translated)

        # TODO: tutto il resto della traduzione (DAO e Committees [saranno in un ciclo])

        return td


class TranslationInstanceDataDAOOptimized( mts.TranslationInstanceDataDAOBase ):
    def __init__(self, dao_name):
        super().__init__(dao_name)

    def toJSON(self):
        a = super().toJSON()
        a[] TODO PROSEGUIIIIII
        return a