
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd
import src.postprocessing.output_preparation.compilers.shared.compiled_model_data as cmd


class CompiledSolidityTest_Committee(cmd.CompiledCommitteeData):
    def __init__(self, id: str, output_full_path: str, compiled: dict):
        super().__init__(id, output_full_path, compiled)


class CompiledSolidityTest_DAO(cmd.CompiledDAOData):
    def __init__(self, id: str, output_full_path: str, compiled: dict):
        super().__init__(id, output_full_path, compiled)


class CompiledSolidityTest_Diagram(cmd.CompiledDiagramData):
    def __init__(self, id: str, output_full_path: str, compiled: dict, can_diagram_be_compiled=True):
        super().__init__(id, output_full_path, compiled,
                         can_diagram_be_compiled=can_diagram_be_compiled)
