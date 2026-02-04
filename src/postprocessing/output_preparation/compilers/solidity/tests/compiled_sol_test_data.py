
import src.postprocessing.output_preparation.compilers.shared.templates.compiled_model_data_templated as cmdt


class CompiledSolidityTest_GovernanceArea(cmdt.CompiledGovernanceAreaTemplated):
    def __init__(self, id: str, compiled: dict, output_full_path: str):
        super().__init__(id, compiled,
                         output_full_path=output_full_path
                         )


class CompiledSolidityTest_Committee(cmdt.CompiledCommitteeTemplated):
    def __init__(self, id: str, compiled: dict, output_full_path: str):
        super().__init__(id, compiled,
                         output_full_path=output_full_path
                         )


class CompiledSolidityTest_DAO(cmdt.CompiledDAOTemplated):
    def __init__(self, id: str, compiled: dict, output_full_path: str):
        super().__init__(id, compiled,
                         output_full_path=output_full_path
                         )


class CompiledSolidityTest_Diagram(cmdt.CompiledDiagramTemplated):
    def __init__(self, id: str, compiled: dict, output_full_path: str,  can_diagram_be_compiled=True):
        super().__init__(id, compiled,
                         output_full_path=output_full_path,
                         can_diagram_be_compiled=can_diagram_be_compiled
                         )
