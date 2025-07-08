import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.solidity_translator_general as sol_transl_general
import src.postprocessing.model_conversion.solidity.model_to_solidity as mts
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg
import src.model.enums.relation_type as rt
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

class TranslatorOptimized(sol_transl_general.TranslatorGeneral):
    
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def translate(self, diagram:dm.DiagramManager, additional_data:dict=None) -> stg.TranslatedDiagram:
        # See " optimized_translator.py # OptimizedSolidityTranslator"
        td = self.translate_diagram_solidity(diagram, additional_data)

        # TODO: tutto il resto della traduzione (DAO e Committees [saranno in un ciclo])

        return td


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


class TranslationInstanceDataDAOOptimized( mts.TranslationInstanceDataDAOBase ):
    """
    @deprecated
    """
    def __init__(self, dao_name):
        super().__init__(dao_name)

    def toJSON(self):
        a = super().toJSON()
        """ a[] TODO PROSEGUIIIIII """
        return a