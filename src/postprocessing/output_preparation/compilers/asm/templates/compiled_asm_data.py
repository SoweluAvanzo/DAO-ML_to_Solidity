
import src.postprocessing.output_preparation.compilers.shared.compiled_model_data as cmd


class CompiledASM_DAO(cmd.CompiledDAOData):
    def __init__(self, id: str, template_name: str, compiled: dict):
        super().__init__(id, template_name, compiled)


class CompiledASM_Diagram(cmd.CompiledDiagramData):
    def __init__(self, id: str, template_name: str, compiled: dict, can_diagram_be_compiled=True):
        super().__init__(id, template_name, compiled,
                         can_diagram_be_compiled=can_diagram_be_compiled)
