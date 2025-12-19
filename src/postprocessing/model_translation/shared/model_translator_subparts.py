import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.model_translator_base as mtb
import src.postprocessing.model_translation.shared.translation_result_base as crb
import src.postprocessing.model_translation.shared.translation_result_model as trm

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

import src.utilities.errors as e_c
import src.utilities.utils as u


class ModelTranslatorSubparts(mtb.ModelTranslatorBase):
    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )
        self.key_model = key_model

    def new_translated_diagram(self, diagram: dm.DiagramManager, other_data=None) -> trm.TranslatedDiagram:
        """
        Designed to be overridden
        """
        return trm.TranslatedDiagram(diagram, other_data)

    def new_translated_dao(self, diagram: dm.DiagramManager, dao: d.DAO, other_data=None) -> trm.TranslatedDAO:
        """
        Designed to be overridden
        """
        return trm.TranslatedDAO(dao, other_data)

    def new_translated_committee(self, diagram: dm.DiagramManager, dao: d.DAO, committee: c.Committee, other_data=None) -> trm.TranslatedCommittee:
        """
        Designed to be overridden
        """
        return trm.TranslatedCommittee(committee, other_data)

    def translate_dao(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None) -> trm.TranslatedDAO:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def translate_diagram(self, diagram: dm.DiagramManager, additional_data=None) -> trm.TranslatedDiagram:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def translate(self, model: dm.DiagramManager, additional_data=None) -> trm.TranslatedDiagram:
        diagram_converted = self.translate_diagram(
            model, additional_data=additional_data)
        for dao in model.daoByID.values():
            dao_converted = self.translate_dao(
                model, dao, additional_data=additional_data)
            diagram_converted.add_translated_dao(dao_converted)
        return diagram_converted
