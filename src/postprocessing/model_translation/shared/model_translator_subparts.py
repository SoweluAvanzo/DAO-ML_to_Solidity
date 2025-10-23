import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.model_translator_base as mtb
import src.postprocessing.model_translation.shared.translation_result_base as crb
import src.postprocessing.model_translation.shared.translation_result_model as trm

import src.model.diagram_manager as dm
import src.model.dao as d

import src.utilities.errors as e_c


class ModelTranslatorSubparts(mtb.ModelTranslatorBase):
    def __init__(self, pipeline_item_data: pi.PIData, key_model: str = None):
        super().__init__(pipeline_item_data)
        self.key_model = key_model

    def translate_DAO(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None) -> trm.TranslatedDAO:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def translate_Diagram(self, diagram: dm.DiagramManager, additional_data=None) -> trm.TranslatedDiagram:
        print(
            f"on class ModelTranslatorSubparts, calling translate_Diagram with self is of type : {type(self)}")
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def translate(self, model: dm.DiagramManager, additional_data=None) -> trm.TranslatedDiagram:
        print(
            f"on class ModelTranslatorSubparts, self is of type : {type(self)}")
        diagram_converted = self.translate_Diagram(
            model, additional_data=additional_data)
        for dao in model.daoByID.values():
            dao_converted = self.translate_DAO(
                model, dao, additional_data=additional_data)
            diagram_converted.add_translated_dao(dao_converted)
        return diagram_converted
