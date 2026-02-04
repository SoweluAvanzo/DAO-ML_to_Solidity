import src.postprocessing.model_translation.shared.translation_result_subpart as crsp

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
import src.model.governance_area as ga


class TranslatedGovernanceArea(crsp.TranslatedSubpart):
    def __init__(self, governance_area: ga.GovernanceArea, governance_area_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(governance_area, governance_area_specific_data,
                         is_convertible=is_convertible
                         )

    def get_specific_data_name(self):
        return "governance_area_specific_data"


class TranslatedCommittee(crsp.TranslatedSubpart):
    def __init__(self, committee: c.Committee, committee_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(committee, committee_specific_data,
                         is_convertible=is_convertible
                         )

    def get_specific_data_name(self):
        return "committee_specific_data"


class TranslatedDAO(crsp.TranslatedSubpart):
    def __init__(self, dao: d.DAO, dao_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(dao, dao_specific_data,
                         is_convertible=is_convertible
                         )
        self.committees_by_id: dict[str, TranslatedCommittee] = {}
        self.governance_area_by_id: dict[str, TranslatedGovernanceArea] = {}

    def get_specific_data_name(self):
        return "dao_specific_data"

    def add_translated_committee(self, committee_translated: TranslatedCommittee):
        self.committees_by_id[committee_translated.entity.get_id(
        )] = committee_translated

    def add_translated_governance_area(self, governance_area_translated: TranslatedGovernanceArea):
        self.governance_area_by_id[governance_area_translated.entity.get_id(
        )] = governance_area_translated

    def toJSON(self):
        o = super().toJSON()
        o["committees_by_id"] = {
            i: self.committees_by_id[i].toJSON() for i in self.committees_by_id.keys()}
        o["governance_area_by_id"] = {
            i: self.governance_area_by_id[i].toJSON() for i in self.governance_area_by_id.keys()}
        return o


class TranslatedDiagram(crsp.TranslatedSubpart):
    def __init__(self, diagram: dm.DiagramManager, diagram_specific_data: dict,
                 is_convertible: bool = True
                 ):
        super().__init__(diagram, diagram_specific_data,
                         is_convertible=is_convertible
                         )
        self.daos_by_id: dict[str, TranslatedDAO] = {}

    def get_specific_data_name(self):
        return "diagram_specific_data"

    def add_translated_dao(self, dao_translated: TranslatedDAO):
        self.daos_by_id[dao_translated.entity.get_id()] = dao_translated

    def toJSON(self):
        o = super().toJSON()
        o["daos_by_id"] = {i: self.daos_by_id[i].toJSON()
                           for i in self.daos_by_id.keys()}
        return o
