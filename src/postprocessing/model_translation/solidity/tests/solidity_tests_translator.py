
import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.model_translator_subparts as mts
import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c


#


class TranslatedCommittee_SolidityTest(trmt.TranslatedCommitteeTemplated):
    def __init__(self, committee: c.Committee, committee_specific_data: dict, is_convertible=True):
        super().__init__(committee, committee_specific_data, is_convertible)
        # nothing more to add there, right now


class TranslatedDAO_SolidityTest(trmt.TranslatedDAOTemplated):
    def __init__(self, dao: d.DAO, dao_specific_data: dict, is_convertible=True):
        super().__init__(dao, dao_specific_data, is_convertible)
        # nothing more to add there, right now


class TranslatedDiagram_SolidityTest(trmt.TranslatedDiagramTemplated):
    def __init__(self, diagram: dm.DiagramManager, diagram_specific_data, is_convertible=True):
        super().__init__(diagram, diagram_specific_data, is_convertible)
        # nothing more to add there, right now

#


class SolidityTestsTranslator(mts.ModelTranslatorSubparts):
    def __init__(self, pipeline_item_data: pi.PIData, key_model: str = None):
        super().__init__(pipeline_item_data, key_model=key_model)
