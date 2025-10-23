from typing import Type

import src.pipeline.pipeline_manager as pmp

import src.utilities.extended_enum as ex_enum
import src.utilities.errors as e_c


class TranslationPhases(ex_enum.ExtendedEnum):
    INPUT_FETCHING = "input"
    MODEL_GENERATION = "model"
    TRANSLATION_CONVERSION_POSTPROCESSING = "translation"
    OUTPUT = "output"

#


class ModelTransformation(ex_enum.ExtendedEnum):
    SOLIDITY = "sol"
    ASM = "asm"
    # JSON = "json"
    # PETRI_NETS = "petri"


class InputSource(ex_enum.ExtendedEnum):
    FILE = "file"
    PROGRAMMATIC_PROVIDER = "prog"  # basically, a
    # DATABASE="db"
    # API="api"


class InputType(ex_enum.ExtendedEnum):
    XML = "xml"
    JSON = "json"
    # YAML="yaml"
    # BSON = "bson"
    # BINARY = "bytes"

#


class InputModelProvider:
    def __init__(self, input_source: InputSource, input_type: InputType, additional_data=None):
        self.input_source = input_source
        self.input_type = input_type
        self.additional_data = additional_data

#

# TODO ; finire di preparare


class TranslatorProcess:
    """
    Class allowing to define the WHOLE translation process: as described in the Enum "TranslationPhases",
    it allows to define the input source and type (example: an XML string from a file, or a JSON from
    an API call), its related conversion into a Model, eventual post-processing sub-step(s) and, finally,
    all types of output;
    all in a single, unified execution process.

    It builds a "PipelineManager" and manages all sub-steps as "PipelineItem"(s).
    """

    def __init__(self,
                 input: InputModelProvider,
                 model_transformations: set | list = None,
                 generate_tests=True,  # only when applicable
                 # TODO altro
                 #
                 is_debug=True
                 ):
        self.is_debug = is_debug
        self.current_phase: TranslationPhases = None
        self.model_transformations = self.__digest_set_enum(
            ModelTransformation.list() if model_transformations is None else model_transformations, ModelTransformation)
        print(
            f"self.model_transformations: {', '.join(self.model_transformations)}")
        self.generate_tests = generate_tests
        self.translation_pipeline: pmp.PipelineManager = self._build_translation_pipeline()

    def __digest_set_enum(self, s: set, e_t: Type[ex_enum.ExtendedEnum]) -> set[str]:
        """
        Transform a set of "something", whose elements might (each individually and independently) be
        a string or an "e_t" (whatever that class might be; still always extendint "ExtendedEnum"), into
        a set of strings.
        """
        a: list[str] = []
        i = 0
        for v in s:
            if isinstance(v, str):
                a.append(v.strip().lower())
            elif isinstance(v, e_t):
                a.append(v.value)
            else:
                if self.is_debug:
                    print(
                        f"ERRPR on getting enum set (of type: {e_t}): element # {i} is not a str nor an Enum value, but: {type(v)}")
            i += 1
        return set(a)

    def translate(self) -> dict:
        return self.translation_pipeline.runPipeline()

    #

    def _build_translation_pipeline(self) -> pmp.PipelineManager:
        pm = pmp.PipelineManager()
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_input(self, pm: pmp.PipelineManager):
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_model_generation(self, pm: pmp.PipelineManager):
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_postprocessing(self, pm: pmp.PipelineManager):
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_output(self, pm: pmp.PipelineManager):
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)


# python -m src.translator_process
if __name__ == "__main__":
    t = TranslatorProcess(is_debug=True, model_transformations=[
        ModelTransformation.ASM, None, "jsOn", 3])
