from typing import Generator

import src.postprocessing.output_preparation.compilers.shared.compiled_unit_with_id as cuwid


class CompiledUnitMultipart(cuwid.CompiledUnitWithID):
    def __init__(self, id: str, compiled: dict):
        super().__init__(id, compiled)

    def get_all_compiled_subparts_as_generator(self) -> Generator[cuwid.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        yield None
