from typing import Type

import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.phases_builders.shared as pb_shared
import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phases as phases
import src.phases_builders.input_fetch as i_f
import src.phases_builders.model_generation as m_g
import src.phases_builders.phase_step_variants as psv

import src.utilities.extended_enum as ex_enum
import src.utilities.errors as e_c

import src.utilities.utils as u

#
#
#


class SubPhasesData:
    def __init__(self,
                 translation_phase: phases.TranslationPhases,
                 substeps: list[PhaseSubstep]
                 ):
        self.translation_phase = translation_phase
        self.substeps = substeps

#
#
#


class InputModelProvider:
    def __init__(self, input_source: i_f.InputSource, input_type: i_f.InputType, additional_data=None):
        self.input_source = input_source
        self.input_type = input_type
        self.input_source_type = i_f.input_source_type(
            input_source, input_type)
        self.additional_data = additional_data


def input_model_provider_from_source_type(input_source: i_f.InputSource, input_type: i_f.InputType, ):
    TODO


class PhaseBuildOutput:
    def __init__(self, phase: phases.TranslationPhases):
        # keys are "value" of psv.PhaseSubstepVariants elements (its subclasses)
        self.piKey_by_subphase: dict[str, str] = {}
        self.pi_created_by_key: dict[str, pi.PipelineItem] = {}


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
                 model_generator_data: m_g.ModelGeneratorFormat,
                 # model_transformations: set | list = None,
                 phases_data: list[SubPhasesData],
                 generate_tests=True,  # only when applicable
                 # TODO altro
                 #
                 printer_debug: u.PrinterDebug = None
                 ):
        self.printer_debug = printer_debug
        self.current_phase: TranslationPhases = None
        self.model_transformations = self.__digest_set_enum(
            ModelTransformation.list() if model_transformations is None else model_transformations, ModelTransformation)
        self.generate_tests = generate_tests
        self.translation_pipeline: pmp.PipelineManager = self._build_translation_pipeline()

    def print_error(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_error(msg)

    def print_msg(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_msg(msg)

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
                self.print_error(
                    f"ERRPR on getting enum set (of type: {e_t}): element # {i} is not a str nor an Enum value, but: {type(v)}")
            i += 1
        return set(a)

    def translate(self) -> dict:
        return self.translation_pipeline.runPipeline()

    #

    def _build_translation_pipeline(self) -> pmp.PipelineManager:
        pm = pmp.PipelineManager()

        # TODO: make use of the "shared.builder_from_phase(...)"
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_input(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        """
        Retuns a dictionary
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_model_generation(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        """
        Retuns a dictionary
        """

        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_postprocessing(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        """
        Retuns a dictionary
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def _build_phase_output(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        """
        Retuns a dictionary
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)


# python -m src.translator_process
if __name__ == "__main__":
    t = TranslatorProcess(model_transformations=[
        ModelTransformation.ASM, None, "jsOn", 3],
        printer_debug=u.PrinterDebug()
    )
