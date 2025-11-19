from typing import Type

import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phases as phases
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o
import src.phases_builders.shared as pb_shared

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
    def __init__(self, input_source: pb_shared.PersistanceType, input_type: pb_i_f.InputType,
                 additional_data=None
                 ):
        self.input_source = input_source
        self.input_type = input_type
        self.input_source_type = pb_i_f.input_source_type(
            input_source, input_type)
        self.additional_data = additional_data

#


class PostprocessingOutput:
    def __init__(self, postprocessing_type: pb_pp.PostProcessingTransformation, output_type: pb_shared.PersistanceTyp,
                 additional_data=None
                 ):
        self.postprocessing_type = postprocessing_type
        self.output_type = output_type
        self.additional_data = additional_data


#


def input_model_provider_from_source_type(input_source: pb_shared.PersistanceType, input_type: pb_i_f.InputType, ):
    TODO


"""
class PhaseBuildOutput:
    def __init__(self, phase: phases.TranslationPhases):
        # keys are "value" of psv.PhaseSubstepVariants elements (its subclasses)
        self.piKey_by_subphase: dict[str, str] = {}
        self.pi_created_by_key: dict[str, pi.PipelineItem] = {}
"""


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
                 model_generator_data: pb_m_g.ModelGeneratorFormat,
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
        self.translation_pipeline: pmp.PipelineManager = None

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
        if self.translation_pipeline is None:
            self.translation_pipeline = self.build_translation_pipeline()
        return self.translation_pipeline.runPipeline()

    #

    def build_translation_pipeline(self) -> pmp.PipelineManager:
        self.print_msg("Building the translation pipeline")
        pm = pmp.PipelineManager(printer_debug=self.printer_debug)

        # TODO: make use of the "shared.builder_from_phase(...)"

        # 1) input

        # 2) model generation
        # k_model_generator = ...

        # 3) postprocessing
        # ... k_model_generator is defined ...
        """
        pp_factory = ppf.PostProcessingFactory(printer_debug=self.printer_debug)
        for pp_t in self.postprocessing_transformations:
            pp_t_name = pp_t.value
            pp_data = self.postprocessing_data_by_transformation[pp_t_name]
            k_pp_t = f"k_pp_t__{pp_t_name}"
            pp_items = pb_pp.new_pipeline_items(pp_t, pi.PIData(k_pp_t, [k_model_generator]), pp_data)
            for pp_i in pp_items:
                pm.addItem(pp_i)
        """

        # 4) output

        raise pm

    """
    def _build_phase_input(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
    def _build_phase_model_generation(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
    def _build_phase_postprocessing(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
    def _build_phase_output(self, pm: pmp.PipelineManager) -> PhaseBuildOutput:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
    """


# python -m src.translator_process
if __name__ == "__main__":
    t = TranslatorProcess(model_transformations=[
        ModelTransformation.ASM, None, "jsOn", 3],
        printer_debug=u.PrinterDebug()
    )
