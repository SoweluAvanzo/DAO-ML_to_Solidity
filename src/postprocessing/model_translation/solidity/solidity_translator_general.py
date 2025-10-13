
import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.shared.model_converter_base as mcb
import src.postprocessing.model_translation.shared.conversion_result_subpart as crsp
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c

#
# TRANSLATION OUTPUT
#


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

#
# THE ACTUAL TRANSLATOR
#


class SolidityTranslatorGeneral(mcb.ModelTranslatorBase):
    """
    Superclass of all other Solidity Translators.
    """

    def __init__(self, pipeline_item_data: pi.PIData, key_model: str = None):
        super().__init__(pipeline_item_data, key_model)

    def new_translated_diagram(self, diagram: dm.DiagramManager, other_data=None) -> TranslatedDiagram:
        """
        Designed to be overridden
        """
        return TranslatedDiagram(diagram, other_data)

    def new_translated_dao(self, diagram: dm.DiagramManager, dao: d.DAO, other_data=None) -> TranslatedDAO:
        """
        Designed to be overridden
        """
        return TranslatedDAO(dao, other_data)

    def new_translated_committee(self, diagram: dm.DiagramManager, dao: d.DAO, committee: c.Committee, other_data=None) -> TranslatedCommittee:
        """
        Designed to be overridden
        """
        return TranslatedCommittee(committee, other_data)
