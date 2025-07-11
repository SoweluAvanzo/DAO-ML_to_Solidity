

import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg
import src.postprocessing.model_conversion.solidity.optimized.solidity_translator_optimized_jinja as sol_transl_opt_jinja
import src.postprocessing.model_conversion.model_converter_base as mcb
import src.model.enums.relation_type as rt
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

VERSION = "1.0.0"

class TranslatorOptimizedJinja_1_0_0(sol_transl_opt_jinja.TranslatorOptimizedJinja):
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

    def translate(self, diagram, additional_data:dict=None) -> mcb.ModelConversionResultBase:
        #raise Exception("TranslatorOptimizedJinja_1_0_0 translation NOT IMPLEMENTED YET")
        return self.translate_diagram_solidity(diagram, additional_data)


        # TODO THE REAL TRANSLATION!

        """
        # See " optimized_translator.py # OptimizedSolidityTranslator"
        
        OptimizedSolidityTranslator
        -> def translate(self)
    
            # at first, translate all Committees
            ct = CommitteeTranslator(self.context)
            - for c in self.context.dao.committees.values():
            - - translated_committee = ct.translateCommittee(c, proposal_permission_index , voting_permission_index, optimized=True) 
        
            - for condition in self.context.dao.conditions:

                ConditionTranslator
                -> file_name_and_path = template_path + "ConditionImplementation" + extension + ".jinja"
                - - -> extension = ".sol" ?
                - - -> template_path = 

        
        """




    def translate_diagram_solidity(self, diagram:dm.DiagramManager, additional_data:dict=None) -> stg.TranslatedDiagram:
        diagram_specific_data_translated = {}
        td = self.new_translated_diagram(diagram, diagram_specific_data_translated) 
        diagram_specific_data_translated["uniqueID"] = diagram.uniqueID
        diagram_specific_data_translated["relations_by_dao"] = { \
            dao_id: [ \
                #note: the rt.RelationType instance can be retrieved back by writing :
                #    rt.RelationType[ name_of_enum_instance ]
                ( rel_data[0].name if isinstance(rel_data[0], rt.RelationType) else f"{rel_data[0]}", rel_data[1], rel_data[2] ) \
                for rel_data in diagram.relations_by_dao[dao_id] \
                ] \
            for dao_id in diagram.relations_by_dao.keys()
        }
        # TODO: fare il controGraphGenerator, somehow, se necessario
        # dao
        for dao_id in diagram.daoByID.keys():
            dao = diagram.daoByID[dao_id]
            translated_dao = self.translate_DAO_solidity(diagram, dao)
            td.add_translated_dao(translated_dao)
        return td

    def translate_DAO_solidity(self, diagram: dm.DiagramManager, dao: d.DAO) -> stg.TranslatedDAO:
        dao_specific_data_translated = {}
        dao_translated = self.new_translated_dao(diagram, dao, dao_specific_data_translated) 
        # TODO: completare il resto della traduzione
        
        return dao_translated

    def translate_committee_solidity(self, diagram: dm.DiagramManager, dao: d.DAO, committee: c.Committee) -> stg.TranslatedDAO:
        committee_specific_data_translated = {}
        committee_translated = self.new_translated_committee(diagram, dao, committee, committee_specific_data_translated)
        # TODO: completare il resto della traduzione
        return committee_translated

