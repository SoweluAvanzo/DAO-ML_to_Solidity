import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.model_converter_base as mcb
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

 


class TranslatedCommittee(mcb.ModelConversionResultBase):
    def __init__(self, committee:c.Committee, committee_specific_data:dict):
        self.committee = committee
        self.committee_specific_data = committee_specific_data
        self.additional_modules_instances_by_name:dict[str, list[dict]] = [] # as of "translator.py # CommitteeTranslator", there are A LOT of additional templates to be created for each Committee
    def get_id(self) -> str:
        return self.committee.get_id()

class TranslatedDAO(mcb.ModelConversionResultBase):
    def __init__(self, dao:d.DAO, dao_specific_data:dict):
        self.dao = dao
        self.dao_specific_data = dao_specific_data
        self.committees_by_id:dict[str, TranslatedCommittee] = {}
    def get_id(self) -> str:
        return self.dao.get_id()

class TranslatedDiagram(mcb.ModelConversionResultBase):
    def __init__(self, diagram:dm.DiagramManager, diagram_specific_data:dict):
        self.diagram = diagram
        self.diagram_specific_data = diagram_specific_data
        self.daos_by_id:dict[str, TranslatedDAO] = {}
    def add_translated_dao(self, dao_translated: TranslatedDAO):
        self.daos_by_id[dao_translated.dao.get_id()] = dao_translated
    def get_id(self) -> str:
        return self.diagram.get_id()


class TranslatorGeneral(mcb.ModelConverterBase):
    """
    Superclass of all other Solidity Translators.
    """
    def __init__(self, pipeline_item_data: pi.PIData, key_model:str=None):
        super().__init__(pipeline_item_data, key_model)
