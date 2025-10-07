import json
import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.model_converter_base as mcb
import src.model.base_entity as base_entity_module
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

#
# TRANSLATION OUTPUT
#

class TranslatedSubpart(mcb.ModelConversionResultBase):
    def __init__(self, entity: base_entity_module.BaseEntity, entity_specific_data:dict):
        self.entity: base_entity_module.BaseEntity = entity
        self.entity_specific_data = entity_specific_data
    def get_id(self) -> str:
        return self.entity.get_id()
    def get_specific_data_name(self):
        return ""
    def toJSON(self):
        return {
            f"{type(self.entity)}": self.entity.get_id(), # "get_id()" instead of "toJSON()" to not clutter the output
            f"{self.get_specific_data_name()}": {k:self.entity_specific_data[k] for k in self.entity_specific_data.keys() if not callable(self.entity_specific_data[k])}
        }
    def __repr__(self):
        return json.dumps(self.toJSON())
        
class TranslatedCommittee(TranslatedSubpart):
    def __init__(self, committee:c.Committee, committee_specific_data:dict):
        super().__init__(committee, committee_specific_data)
    def get_specific_data_name(self):
        return "committee_specific_data"

class TranslatedDAO(TranslatedSubpart):
    def __init__(self, dao:d.DAO, dao_specific_data:dict):
        super().__init__(dao, dao_specific_data)
        self.committees_by_id:dict[str, TranslatedCommittee] = {}
    def get_specific_data_name(self):
        return "dao_specific_data"
    def add_translated_committee(self, committee_translated: TranslatedCommittee):
        self.committees_by_id[committee_translated.entity.get_id()] = committee_translated
    def toJSON(self):
        o = super().toJSON()
        o["committees_by_id"] = { i: self.committees_by_id[i].toJSON() for i in self.committees_by_id.keys() }
        return o

class TranslatedDiagram(TranslatedSubpart):
    def __init__(self, diagram:dm.DiagramManager, diagram_specific_data:dict):
        super().__init__(diagram, diagram_specific_data)
        self.daos_by_id:dict[str, TranslatedDAO] = {}
    def get_specific_data_name(self):
        return "diagram_specific_data"
    def add_translated_dao(self, dao_translated: TranslatedDAO):
        self.daos_by_id[dao_translated.entity.get_id()] = dao_translated
    def toJSON(self):
        o = super().toJSON()
        o["daos_by_id"] = { i: self.daos_by_id[i].toJSON() for i in self.daos_by_id.keys() }
        return o

#
# THE ACTUAL TRANSLATOR
#


class SolidityConverterGeneral(mcb.ModelConverterBase):
    """
    Superclass of all other Solidity Translators.
    """
    def __init__(self, pipeline_item_data: pi.PIData, key_model:str=None):
        super().__init__(pipeline_item_data, key_model)

    def new_translated_diagram(self, diagram:dm.DiagramManager, other_data=None) -> TranslatedDiagram:
        """
        Designed to be overridden
        """
        return TranslatedDiagram(diagram, other_data)

    def new_translated_dao(self, diagram:dm.DiagramManager, dao:d.DAO, other_data=None) -> TranslatedDAO:
        """
        Designed to be overridden
        """
        return TranslatedDAO(dao, other_data)

    def new_translated_committee(self, diagram:dm.DiagramManager, dao:d.DAO, committee:c.Committee, other_data=None) -> TranslatedCommittee:
        """
        Designed to be overridden
        """
        return TranslatedCommittee(committee, other_data)
