import typing
from typing import Generator

import src.postprocessing.output_preparation.compilers.shared.compiled_unit_with_id as cuwid
import src.postprocessing.output_preparation.compilers.shared.compiled_model_data as cmd
# import src.postprocessing.output_preparation.compilers.shared.templates.compiled_model_data_templated as cmdt

KEY_DAO_COMMITTEES = "committees"
KEY_DAO_GOVERNANCE_AREASS = "governance_areas"
KEY_DAOS_BY_ID = "daos_by_id"


class CompiledSolidityGovernanceArea(cmd.CompiledGovernanceAreaData):
    def __init__(self, id: str, compiled: dict):
        super().__init__(id, compiled)
    # TODO: (04-02-2026) altro?


class CompiledSolidityCommittee(cmd.CompiledCommitteeData):
    def __init__(self, id: str,  compiled: dict):
        super().__init__(id, compiled)
        self.compiled_conditions_by_name: dict[str,
                                               cuwid.CompiledUnitWithID] = {}

    def get_committee_id_from_data(self, committee_data: dict) -> str:
        """
        Overridable
        """
        if isinstance(committee_data, CompiledSolidityCommittee):
            return committee_data.id
        return committee_data[cuwid.KEY_ID] if isinstance(committee_data, dict) and cuwid.KEY_ID in committee_data else self.id

    def get_all_compiled_subparts_as_generator(self) -> Generator[cuwid.CompiledUnitWithID, None, None]:
        if (self.compiled_conditions_by_name is None) or (len(self.compiled_conditions_by_name) <= 0):
            yield None
        for cc in self.compiled_conditions_by_name.values():
            yield cc


class CompiledSolidityDAO(cmd.CompiledDAOData):
    def __init__(self, id: str,  compiled: dict):
        super().__init__(id, compiled)
        self.interfaces_and_dao_related_compiled_contracts: dict[str, cuwid.CompiledUnitWithID] = {
        }

    def get_dao_id_from_data(self, dao_data) -> str:
        """
        Overridable
        """
        if isinstance(dao_data, CompiledSolidityDAO):
            return dao_data.id
        return dao_data[cuwid.KEY_ID] if isinstance(dao_data, dict) and cuwid.KEY_ID in dao_data else self.id

    def get_dao_committees_from_data(self, dao_data: dict) -> dict[str, CompiledSolidityCommittee]:
        """
        Overridable
        """
        return self.committees_by_id  # dao_data[KEY_DAO_COMMITTEES]

    def get_dao_governance_areas_from_data(self, dao_data: dict) -> dict[str, CompiledSolidityGovernanceArea]:
        """
        Overridable
        """
        return self.governance_areas_by_id  # dao_data[KEY_DAO_GOVERNANCE_AREASS]

    def get_committee_id_from_data(self, committee_data: dict):
        return typing.cast(CompiledSolidityCommittee, committee_data).get_committee_id_from_data(committee_data) \
            if isinstance(committee_data, CompiledSolidityCommittee) \
            else committee_data[cuwid.KEY_ID]

    def get_all_compiled_subparts_as_generator(self) -> Generator[cuwid.CompiledUnitWithID, None, None]:
        for sp in super().get_all_compiled_subparts_as_generator():
            if sp is not None:
                yield sp
        if (self.interfaces_and_dao_related_compiled_contracts is None) or (len(self.interfaces_and_dao_related_compiled_contracts) <= 0):
            yield None
        for i_dr_cc in self.interfaces_and_dao_related_compiled_contracts.values():
            yield i_dr_cc

    def add_committee_data_to_dao(self, committee_data: dict):
        """
        Overrides the super().add_committee(committee_data)
        """
        committees = self.get_dao_committees_from_data(self.compiled)
        c_id = self.get_committee_id_from_data(committee_data)
        committees[c_id] = committee_data

    def add_governance_area_to_dao(self, governance_area_data: dict):
        """
        Overrides the super().add_governance_area(governance_area_data)
        """
        governance_areas = self.get_dao_governance_areas_from_data(
            self.compiled)
        c_id = self.get_governance_area_id_from_data(governance_area_data)
        governance_areas[c_id] = governance_area_data

    def __tojson__(self, **kwargs):
        j = super().__tojson__()
        j[KEY_DAO_COMMITTEES] = {
            c.id: c.__tojson__() for c in self.get_dao_committees_from_data(self.compiled).values()
        }
        j[KEY_DAO_GOVERNANCE_AREASS] = {
            ga.id: ga.__tojson__() for ga in self.get_dao_governance_areas_from_data(self.compiled).values()
        }
        governance_areas
        return j


class CompiledSolidityDiagram(cmd.CompiledDiagramData):
    def __init__(self, id: str,  compiled: dict = None, can_diagram_be_compiled=True):
        super().__init__(id, compiled)
        self.can_diagram_be_compiled = can_diagram_be_compiled

    def get_daos_compiled_by_id(self):
        return self.daos_by_id

    def add_dao(self, dao_data: CompiledSolidityDAO):
        self.daos_by_id[dao_data.get_dao_id_from_data(
            dao_data)] = dao_data

    def get_dao_by_id(self, dao_id: str) -> dict:
        return self.daos_by_id[dao_id]

    def add_committee_data_to_dao(self, dao_id: str, committee_data: CompiledSolidityCommittee):
        dao = self.get_dao_by_id(dao_id)
        if isinstance(dao, CompiledSolidityDAO):
            dao.add_committee_data_to_dao(committee_data)

    def __tojson__(self, **kwargs):
        j = super().__tojson__()
        j[KEY_DAOS_BY_ID] = {
            c.id: c.__tojson__() for c in self.get_daos_compiled_by_id().values()
        }
        return j
