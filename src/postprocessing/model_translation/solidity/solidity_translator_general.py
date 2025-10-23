
import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.model_translator_subparts as tms
import src.postprocessing.model_translation.shared.translation_result_model as trm

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

import src.utilities.errors as e_c


class SolidityTranslatorGeneral(tms.ModelTranslatorSubparts):
    """
    Superclass of all other Solidity Translators.
    """

    def __init__(self, pipeline_item_data: pi.PIData, key_model: str = None):
        super().__init__(pipeline_item_data, key_model)

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

    def translate_DAO(self, diagram: dm.DiagramManager, dao: d.DAO, additional_data=None) -> trm.TranslatedDAO:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def translate_Diagram(self, diagram: dm.DiagramManager, additional_data=None) -> trm.TranslatedDiagram:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
