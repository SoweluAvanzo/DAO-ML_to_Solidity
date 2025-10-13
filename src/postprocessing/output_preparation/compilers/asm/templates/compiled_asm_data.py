
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd


class CompiledASM_DAO(cgd.CompiledUnitWithID):
    def __init__(self, id: str, template_name: str, compiled: dict):
        super().__init__(id, template_name, compiled)


class CompiledASM_Diagram(cgd.CompiledUnitWithID):
    def __init__(self, id: str, template_name: str, compiled: dict):
        super().__init__(id, template_name, compiled)
