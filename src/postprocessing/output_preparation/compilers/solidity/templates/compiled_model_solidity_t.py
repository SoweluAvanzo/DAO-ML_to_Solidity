import src.postprocessing.output_preparation.compilers.solidity.compiled_model_solidity as cms
import src.postprocessing.output_preparation.compilers.shared.templates.compiled_model_data_templated as cmdt


class CompiledSolidityGovernanceAreaTemplated(cms.CompiledSolidityGovernanceArea, cmdt.CompiledGovernanceAreaTemplated):
    def __init__(self, id: str,  compiled: dict, output_full_path: str = ""):
        cms.CompiledSolidityGovernanceArea.__init__(self, id, compiled)
        cmdt.CompiledGovernanceAreaTemplated.__init__(
            self,
            id, compiled,
            output_full_path=output_full_path
        )


class CompiledSolidityCommitteeTemplated(cms.CompiledSolidityCommittee, cmdt.CompiledCommitteeTemplated):
    def __init__(self, id: str,  compiled: dict, output_full_path: str = ""):
        cms.CompiledSolidityCommittee.__init__(self, id, compiled)
        cmdt.CompiledCommitteeTemplated.__init__(
            self,
            id, compiled,
            output_full_path=output_full_path
        )


class CompiledSolidityDAOTemplated(cms.CompiledSolidityDAO, cmdt.CompiledDAOTemplated):
    def __init__(self, id: str,  compiled: dict, output_full_path: str = ""):
        cms.CompiledSolidityDAO.__init__(self, id, compiled)
        cmdt.CompiledDAOTemplated.__init__(
            self,
            id, compiled,
            output_full_path=output_full_path
        )


class CompiledSolidityDiagramTemplated(cms.CompiledSolidityDiagram, cmdt.CompiledDiagramTemplated):
    def __init__(self, id: str,  compiled: dict = None, output_full_path: str = "", can_diagram_be_compiled=True):
        cms.CompiledSolidityDiagram.__init__(
            self,
            id, compiled,
            can_diagram_be_compiled=can_diagram_be_compiled
        )
        cmdt.CompiledDiagramTemplated.__init__(
            self,
            id, compiled,
            output_full_path=output_full_path
        )
