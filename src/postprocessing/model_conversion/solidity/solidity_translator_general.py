import src.pipeline.pipeline_item as pi

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c


class TranslatedCommittee:
    def __init__(self, committee:c.Committee, committee_specific_data:dict):
        self.committee = committee
        self.committee_specific_data = committee_specific_data
        self.additional_modules_instances_by_name:dict[str, list[dict]] = [] # as of "translator.py # CommitteeTranslator", there are A LOT of additional templates to be created for each Committee

class TranslatedDAO:
    def __init__(self, dao:d.DAO, dao_specific_data:dict):
        self.dao = dao
        self.dao_specific_data = dao_specific_data
        self.committees_by_id:dict[str, TranslatedCommittee] = {}

class TranslatedDiagram:
    def __init__(self, diagram:dm.DiagramManager, diagram_specific_data:dict):
        self.diagram = diagram
        self.diagram_specific_data = diagram_specific_data
        self.daos_by_id:dict[str, TranslatedDAO] = {}
    def add_translated_dao(self, dao_translated: TranslatedDAO):
        self.daos_by_id[dao_translated.dao.get_id()] = dao_translated


class TranslatorGeneral(pi.PipelineItem):
    """
    Superclass of all other Solidity Translators
    """
    def __init__(self, pipeline_item_data: pi.PIData, key_model:str=None):
        super().__init__(pipeline_item_data)
        self.key_model = key_model


    def translate(self, model:dm.DiagramManager, additional_data=None) -> TranslatedDiagram:
        return None

    def run(self, inputs):
        return self.translate(\
            inputs[self.key_model] if self.key_model is not None else self.get_ith_input(inputs, 0), \
            inputs)
