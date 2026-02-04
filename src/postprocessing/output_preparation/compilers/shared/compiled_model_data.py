from typing import Generator

import src.postprocessing.output_preparation.compilers.shared.compiled_unit_with_id as cuwid
import src.postprocessing.output_preparation.compilers.shared.compiled_unit_multipart as cumult


class CompiledGovernanceAreaData(cumult.CompiledUnitMultipart):
    def __init__(self, id: str, compiled: dict):
        super().__init__(id, compiled)


class CompiledCommitteeData(cumult.CompiledUnitMultipart):
    def __init__(self, id: str, compiled: dict):
        super().__init__(id, compiled)


class CompiledDAOData(cumult.CompiledUnitMultipart):
    def __init__(self, id: str, compiled: dict):
        super().__init__(id, compiled)
        self.committees_by_id: dict[str, CompiledCommitteeData] = {}
        self.governance_areas_by_id: dict[str, CompiledGovernanceAreaData] = {}

    def add_committee(self, committee_data: CompiledCommitteeData):
        self.committees_by_id[committee_data.id] = committee_data

    def add_governance_area(self, governance_area_data: CompiledGovernanceAreaData):
        self.governance_areas_by_id[governance_area_data.id] = governance_area_data

    def get_all_compiled_subparts_as_generator(self) -> Generator[cuwid.CompiledUnitWithID, None, None]:
        if (self.committees_by_id is None) or (len(self.committees_by_id) <= 0):
            yield None
            return
        for committee_id, committee_translated in self.committees_by_id.items():
            if committee_translated is not None:
                yield committee_translated
                for sp in committee_translated.get_all_compiled_subparts_as_generator():
                    if sp is not None:
                        yield sp
        for governance_area_id, governance_area_translated in self.governance_areas_by_id.items():
            if governance_area_translated is not None:
                yield governance_area_translated
                for sp in governance_area_translated.get_all_compiled_subparts_as_generator():
                    if sp is not None:
                        yield sp


class CompiledDiagramData(cumult.CompiledUnitMultipart):
    def __init__(self, id: str, compiled: dict, can_diagram_be_compiled=True):
        super().__init__(id, compiled)
        self.daos_by_id: dict[str, CompiledDAOData] = {}
        self.can_diagram_be_compiled = can_diagram_be_compiled

    def add_dao(self, dao_data: CompiledDAOData):
        self.daos_by_id[dao_data.id] = dao_data

    def get_all_compiled_subparts_as_generator(self) -> Generator[cuwid.CompiledUnitWithID, None, None]:
        if (self.daos_by_id is None) or (len(self.daos_by_id) <= 0):
            yield None
            return
        for dao_id, dao_translated in self.daos_by_id.items():
            if dao_translated is not None:
                yield dao_translated
