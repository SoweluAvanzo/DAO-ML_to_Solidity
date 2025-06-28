
import src.pipeline.pipeline_item as pi
import src.utilities.utils as u
import src.model.diagram_manager as dm


class ModelToSolidity(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, translation_data=None):
        super().__init__(pipeline_item_data)
        self.translation_data = translation_data


    def run(self, inputs):
        diagram_manager:dm.DiagramManager = self.get_ith_input(0)
        """
        
          for dao_id in diagram_manager.daoByID.keys():
            dao = diagram_manager.get_dao_by(dao_id)
            dao_name = dao.dao_name
            # the translator uses the selected translation logic
            #if diamond_enabled.get()==True:
            #    translator = SolidityTranslator(dao, translation_logic.get(), diamond=True)  
            #elif diamond_enabled.get()==False:
            translator = SolidityTranslator(dao, translation_logic , diamond=False)
            #else:
            tests_translator = TestGeneratorOptimized(dao, translation_logic == 'optimized', translator)
            contracts_to_write.append(TranslationData(dao_name, dao_name, translator, tests_translator))
             
            #contracts_to_write.extend(all_translated_smart_contract__tests)
            
        
        """

        return None