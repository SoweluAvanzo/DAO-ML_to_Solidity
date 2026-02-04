
import src.postprocessing.output_preparation.compilers.shared.compiled_unit_with_id as cuwid
import src.postprocessing.output_preparation.compilers.shared.compiled_model_data as cmd

KEY_OUTPUT_FULL_PATH = "output_full_path"


class CompiledWithOutputPath(cuwid.CompiledUnitWithID):
    def __init__(self, id: str, compiled: dict,
                 output_full_path: str = "",
                 ):
        super().__init__(id, compiled)
        self.output_full_path = output_full_path

    def __tojson__(self, **kwargs):
        obj = super().__tojson__(**kwargs)
        obj[KEY_OUTPUT_FULL_PATH] = self.output_full_path
        return obj

#


class CompiledGovernanceAreaTemplated(cmd.CompiledGovernanceAreaData):
    def __init__(self, id: str, compiled: dict,
                 output_full_path: str = "",
                 ):
        cmd.CompiledGovernanceAreaData.__init__(self, id, compiled)
        CompiledWithOutputPath.__init__(
            self, id, compiled,
            output_full_path=output_full_path,
        )


class CompiledCommitteeTemplated(cmd.CompiledCommitteeData, CompiledWithOutputPath):
    def __init__(self, id: str, compiled: dict,
                 output_full_path: str = "",
                 ):
        cmd.CompiledCommitteeData.__init__(self, id, compiled)
        CompiledWithOutputPath.__init__(
            self, id, compiled,
            output_full_path=output_full_path,
        )


class CompiledDAOTemplated(cmd.CompiledDAOData, CompiledWithOutputPath):
    def __init__(self, id: str, compiled: dict,
                 output_full_path: str = "",
                 ):
        cmd.CompiledDAOData.__init__(self, id, compiled)
        CompiledWithOutputPath.__init__(
            self, id, compiled,
            output_full_path=output_full_path,
        )


class CompiledDiagramTemplated(cmd.CompiledDiagramData, CompiledWithOutputPath):
    def __init__(self, id: str, compiled: dict = None,
                 output_full_path: str = "",
                 can_diagram_be_compiled=False
                 ):
        cmd.CompiledDiagramData.__init__(
            self, id, compiled,
            can_diagram_be_compiled=can_diagram_be_compiled
        )
        CompiledWithOutputPath.__init__(
            self, id, compiled,
            output_full_path=output_full_path,
        )
