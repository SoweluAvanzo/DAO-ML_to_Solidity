import src.postprocessing.model_translation.shared.translation_result_subpart as crsp

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c


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

    def get_specific_data_name(self):
        return "dao_specific_data"

    def add_translated_committee(self, committee_translated: TranslatedCommittee):
        self.committees_by_id[committee_translated.entity.get_id(
        )] = committee_translated

    def toJSON(self):
        o = super().toJSON()
        o["committees_by_id"] = {
            i: self.committees_by_id[i].toJSON() for i in self.committees_by_id.keys()}
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
