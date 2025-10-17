
import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.model_translator_base as mcb
import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt

import src.model.diagram_manager as dm
import src.model.dao as d

import src.utilities.errors as e_c


class SolidityTestsTranslator(mcb.ModelTranslatorBase):
    def __init__(self, pipeline_item_data: pi.PIData, key_model: str = None):
        super().__init__(pipeline_item_data, key_model=key_model)

    def translate_DAO_test(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None) -> trmt.TranslatedDAOTemplated:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def translate_Diagram_test(self, diagram: dm.DiagramManager, additional_data=None) -> trmt.TranslatedDiagramTemplated:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def translate(self, model: dm.DiagramManager, additional_data=None) -> trmt.TranslatedDiagramTemplated:
        diagram_converted = self.translate_Diagram_test(model)
        for dao in model.daoByID.values():
            dao_converted = self.translate_DAO_test(model, dao)
            diagram_converted.add_translated_dao(dao_converted)
        return diagram_converted
