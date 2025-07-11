import src.pipeline.pipeline_item as pi
#import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_conversion.model_converter_base as mcb
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg
import src.postprocessing.model_conversion.solidity.optimized.solidity_translator_optimized_jinja as sto_j
import src.postprocessing.model_conversion.solidity.optimized.jinja.jinja_optimized_versions as j_o_v
import src.postprocessing.model_conversion.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as to_sol_j_1_0_0
import src.model.enums.relation_type as rt
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

class TranslatorOptimized(stg.TranslatorGeneral):
    
    def __init__(self, pipeline_item_data: pi.PIData, \
                key_model:str=None, \
                key_translator_type:str=None, \
                key_version:str=None
                ):
        super().__init__(pipeline_item_data, key_model)
        self.key_translator_type = key_translator_type
        self.key_version = key_version


    def select_delegator(self, diagram:dm.DiagramManager, translator_type:str, version:str,  additional_data:dict=None) -> mcb.ModelConverterBase:
        """
        Override designed
        """
        if translator_type == None or (isinstance(translator_type, str) and translator_type.lower() == "jinja"):
            jinja_transl = sto_j.TranslatorOptimizedJinja(self.get_pipeline_item_data(), \
                                self.key_model, \
                                self.key_translator_type, \
                                self.key_version, \
                                )
            deleg = jinja_transl.select_delegator(diagram, translator_type, version, additional_data)
            return deleg
        raise Exception(f"(Solidity)TranslatorOptimized can't select its own delegator for translator type ({translator_type}) and version ({version}): instantiate another one.")

    def translate(self, diagram:dm.DiagramManager, additional_data:dict=None) -> stg.TranslatedDiagram:
        if additional_data is None:
            additional_data = {}
        translator_type = additional_data[self.key_translator_type] if self.key_translator_type is not None \
            and None and self.key_translator_type in additional_data else \
            self.get_ith_input(additional_data, 1)
        if translator_type is None:
            translator_type = "jinj" # TODO: how to choose another default one? 
        translator_version = additional_data[self.key_version] if self.key_version is not None \
            and None and self.key_version in additional_data else \
            self.get_ith_input(additional_data, 2)
        if translator_version is None:
            translator_version = j_o_v.JinjaOptimizedVersions.JO_1_0_0.value

        # get the delegator
        deleg = self.select_delegator(diagram, translator_type, translator_version, additional_data)
        if deleg is None:
            return None

        # TODO: tutto il resto della traduzione (DAO e Committees [saranno in un ciclo])

        # td = self.translate_diagram_solidity(diagram, additional_data)
        return deleg.translate(diagram, additional_data)


    def new_translated_diagram(self, diagram:dm.DiagramManager, other_data=None) -> stg.TranslatedDiagram:
        """
        Designed to be overridden
        """
        return stg.TranslatedDiagram(diagram, other_data) 

    def new_translated_dao(self, diagram:dm.DiagramManager, dao:d.DAO, other_data=None) -> stg.TranslatedDAO:
        """
        Designed to be overridden
        """
        return stg.TranslatedDAO(dao, other_data) 

    def new_translated_committee(self, diagram:dm.DiagramManager, dao:d.DAO, committee:c.Committee, other_data=None) -> stg.TranslatedCommittee:
        """
        Designed to be overridden
        """
        return stg.TranslatedCommittee(committee, other_data) 

