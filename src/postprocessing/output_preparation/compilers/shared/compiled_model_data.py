from typing import Generator

import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd


class CompiledCommitteeData(cgd.CompiledUnitWithID):
    def __init__(self, id: str, template_name: str, compiled: dict):
        super().__init__(id, template_name, compiled)

    def get_all_compiled_subparts_as_generator(self) -> Generator[cgd.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        yield None


class CompiledDAOData(cgd.CompiledUnitWithID):
    def __init__(self, id: str, template_name: str, compiled: dict):
        super().__init__(id, template_name, compiled)
        self.committees_by_id: dict[str, CompiledDAOData] = {}

    def add_committee(self, committee_data: CompiledCommitteeData):
        self.committees_by_id[committee_data.id] = committee_data

    def get_all_compiled_subparts_as_generator(self) -> Generator[cgd.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        if (self.committees_by_id is None) or (len(self.committees_by_id) <= 0):
            yield None
            return
        for committee_id, committee_translated in self.committees_by_id.items():
            if committee_translated is not None:
                yield committee_translated
                for sp in committee_translated.get_all_compiled_subparts_as_generator():
                    yield sp


class CompiledDiagramData(cgd.CompiledUnitWithID):
    def __init__(self, id: str, template_name: str, compiled: dict, can_diagram_be_compiled=True):
        super().__init__(id, template_name, compiled)
        self.daos_by_id: dict[str, CompiledDAOData] = {}
        self.can_diagram_be_compiled = can_diagram_be_compiled

    def add_dao(self, dao_data: CompiledDAOData):
        self.daos_by_id[dao_data.id] = dao_data
