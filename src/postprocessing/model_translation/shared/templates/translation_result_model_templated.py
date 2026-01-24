import src.postprocessing.model_translation.shared.templates.translation_result_template as crt
import src.postprocessing.model_translation.shared.translation_result_model as trm

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
import src.model.governance_area as ga


class TranslatedGovernanceAreaTemplated(crt.TranslatedSubpartTemplated, trm.TranslatedGovernanceArea):
    def __init__(self, governance_area: ga.GovernanceArea, governance_area_specific_data: dict,
                 voting_protocol_specific_data: dict = None,
                 is_convertible: bool = True
                 ):
        crt.TranslatedSubpartTemplated.__init__(
            self, governance_area, governance_area_specific_data, is_convertible=is_convertible)
        trm.TranslatedGovernanceArea.__init__(
            self, governance_area, governance_area_specific_data, is_convertible=is_convertible)
        # TODO: (2025-01-24) WHAT TO PUT THERE? ALL PERMISSIONS (' IDs) MANAGED BY THIS G.A.?


class TranslatedCommitteeTemplated(crt.TranslatedSubpartTemplated, trm.TranslatedCommittee):
    def __init__(self, committee: c.Committee, committee_specific_data: dict,
                 voting_protocol_specific_data: dict = None,
                 is_convertible: bool = True
                 ):
        crt.TranslatedSubpartTemplated.__init__(
            self, committee, committee_specific_data, is_convertible=is_convertible)
        trm.TranslatedCommittee.__init__(
            self, committee, committee_specific_data, is_convertible=is_convertible)
        self.voting_protocol_specific_data = voting_protocol_specific_data


class TranslatedDAOTemplated(crt.TranslatedSubpartTemplated, trm.TranslatedDAO):
    def __init__(self, dao: d.DAO, dao_specific_data: dict,
                 is_convertible: bool = True
                 ):
        crt.TranslatedSubpartTemplated.__init__(
            self, dao, dao_specific_data, is_convertible=is_convertible)
        trm.TranslatedDAO.__init__(
            self, dao, dao_specific_data, is_convertible=is_convertible)


class TranslatedDiagramTemplated(crt.TranslatedSubpartTemplated, trm.TranslatedDiagram):
    def __init__(self, diagram: dm.DiagramManager, diagram_specific_data: dict,
                 is_convertible: bool = True
                 ):
        crt.TranslatedSubpartTemplated.__init__(
            self, diagram, diagram_specific_data, is_convertible=is_convertible)
        trm.TranslatedDiagram.__init__(
            self, diagram, diagram_specific_data, is_convertible=is_convertible)
