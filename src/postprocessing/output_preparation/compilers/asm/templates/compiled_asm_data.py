import src.postprocessing.output_preparation.compilers.shared.templates.compiled_model_data_templated as cmdt


class CompiledASM_DAO(cmdt.CompiledDAOTemplated):
    def __init__(self, id: str, compiled: dict, template_name: str):
        super().__init__(id, compiled,
                         output_full_path=template_name
                         )


class CompiledASM_Diagram(cmdt.CompiledDiagramTemplated):
    def __init__(self, id: str, compiled: dict, template_name: str,  can_diagram_be_compiled=True):
        super().__init__(id, compiled,
                         output_full_path=template_name,
                         can_diagram_be_compiled=can_diagram_be_compiled
                         )
