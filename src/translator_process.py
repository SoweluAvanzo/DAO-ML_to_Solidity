from typing import Type

import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi

import src.phases_builders.shared as pb_shared
import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phases as phases
import src.phases_builders.phase_builder as pb
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o

import src.utilities.extended_enum as ex_enum
import src.utilities.errors as e_c

import src.utilities.utils as u

#
#
#


class SubPhaseConfiguration:
    def __init__(self,
                 phase: phases.TranslationPhases,
                 subphase: psv.PhaseSubstepVariants,
                 additional_data: pb.AdditionalDataSubPhase
                 ):
        self.phase = phase
        self.subphase = subphase
        self.additional_data = additional_data

#


class InputConfiguration(SubPhaseConfiguration):
    def __init__(self, input_source_type: pb_shared.PersistanceType, input_type: pb_i_f.InputType,
                 additional_data: pb_i_f.AdditionalDataInput
                 ):
        super().__init__(
            phases.TranslationPhases.INPUT_FETCHING,
            pb_i_f.input_source_type(input_source_type, input_type),
            additional_data
        )
        self.input_source_type = input_source_type
        self.input_type = input_type


class ModelConfiguration(SubPhaseConfiguration):
    def __init__(self,  model_generator_format: pb_m_g.ModelGeneratorFormat,
                 additional_data: pb_m_g.AdditionalDataModelGeneration
                 ):
        super().__init__(
            phases.TranslationPhases.MODEL_GENERATION,
            model_generator_format,
            additional_data
        )


class PostprocessingConfiguration(SubPhaseConfiguration):
    def __init__(self,  post_processing_transformation: pb_pp.PostProcessingTransformation,
                 additional_data: pb_pp.AdditionalDataPostProcessing
                 ):
        super().__init__(
            phases.TranslationPhases.TRANSLATION_CONVERSION_POSTPROCESSING,
            post_processing_transformation,
            additional_data
        )


class OutputConfiguration(SubPhaseConfiguration):
    def __init__(self, output_persistance_type: pb_shared.PersistanceType, output_type: pb_o.OutputType,
                 additional_data: pb_o.AdditionalDataOutput
                 ):
        super().__init__(
            phases.TranslationPhases.OUTPUT,
            pb_o.output_destination_type(output_persistance_type, output_type),
            additional_data
        )
        self.output_persistance_type = output_persistance_type
        self.output_type = output_type


#


class PostprocessingOutput:
    """
    This class is used to configure the DAO's model transformation and the subsequent output destination.
    This way, You can prepare different transformations and save the results in similar and/or different outputs 
    (file, DataBases, API-related storage systems like cloud-based ones, etc). The latter can be accomplished
    by simply recycling the
    """

    def __init__(self,
                 postprocessing_configuration: PostprocessingConfiguration,
                 output_configuration: OutputConfiguration,
                 additional_data=None
                 ):
        self.postprocessing_configuration = postprocessing_configuration
        self.output_configuration = output_configuration
        self.additional_data = additional_data


#


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
                 input_configuration: InputConfiguration,
                 model_configuration: ModelConfiguration,
                 postprocessing_output_configurations: list[PostprocessingOutput],

                 generate_tests=True,  # only when applicable
                 # TODO altro?
                 printer_debug: u.PrinterDebug = None,
                 external_unique_key_producer: pb_shared.KeyUniqueProducer = None
                 ):
        self.printer_debug = printer_debug
        self.key_unique_producer = self.new_key_unique_producer(
        ) if external_unique_key_producer is None else external_unique_key_producer
        self.input_configuration = input_configuration
        self.model_configuration = model_configuration
        self.postprocessing_output_configurations = postprocessing_output_configurations
        self.generate_tests = generate_tests
        #
        self.current_phase: TranslationPhases = None
        self.translation_pipeline: pmp.PipelineManager = None
        self.postprocessing_data_by_transformation: dict[str, pb.AdditionalDataSubPhase] = {
        }

    def print_error(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_error(msg)

    def print_msg(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_msg(msg)

    def __digest_set_enum(self, s: set, e_t: Type[ex_enum.ExtendedEnum]) -> set[str]:
        """
        @deprecated
        Transform a set of "something", whose elements might (each individually and independently) be
        a string or an "e_t" (whatever that class might be; still always extending "ExtendedEnum"), into
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

    #

    # override-designed methods

    #

    def new_key_unique_producer(self) -> pb_shared.KeyUniqueProducer:
        return pb_shared.KeyUniqueProducerSimpleSequential()

    def build_phase_input(self):
        """
        Override-designed
        """
        return pb_i_f.InputFactory(self.key_unique_producer, printer_debug=self.printer_debug)

    def build_phase_model_generation(self):
        """
        Override-designed
        """
        return pb_m_g.ModelGeneratorFactory(self.key_unique_producer, printer_debug=self.printer_debug)

    def build_phase_postprocessing(self):
        """
        Override-designed
        """
        return pb_pp.PostProcessingFactory(self.key_unique_producer, printer_debug=self.printer_debug)

    def build_phase_output(self):
        """
        Override-designed
        """
        return pb_o.OutputFactory(self.key_unique_producer, printer_debug=self.printer_debug)

    def builder_from_phase(self, phase: phases.TranslationPhases) -> pb.PipelineItemFactory:
        match phase:
            case phases.TranslationPhases.INPUT_FETCHING:
                return self.build_phase_input()
            case phases.TranslationPhases.MODEL_GENERATION:
                return self.build_phase_model_generation()
            case phases.TranslationPhases.TRANSLATION_CONVERSION_POSTPROCESSING:
                return self.build_phase_postprocessing()
            case phases.TranslationPhases.OUTPUT:
                return self.build_phase_output()
        raise Exception(f"Unrecognized phase: {phase}")

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

    #

    #

    def translate(self) -> dict:
        if self.translation_pipeline is None:
            self.translation_pipeline = self.build_translation_pipeline()
        return self.translation_pipeline.runPipeline()

    #

    def build_translation_pipeline(self) -> pmp.PipelineManager:
        self.print_msg("Building the translation pipeline")
        pm = pmp.PipelineManager(printer_debug=self.printer_debug)

        # function to add items to the pipeline
        def add_pi_s(items):
            for item in items:
                pm.addItem(item)

        #
        # 1) input
        k_input = f"k_input__{self.key_unique_producer.new_unique_key()}"
        input_data = self.input_configuration.additional_data
        pf_input = self.builder_from_phase(
            phases.TranslationPhases.INPUT_FETCHING)
        input_items = pf_input.new_pipeline_items(
            pi.PIData(k_input, None),
            input_data
        )
        add_pi_s(input_items)
        # clean the memory
        input_data = None
        pf_input = None
        input_items = None

        #
        # 2) model generation
        k_model_generator = f"k_model_generator__{self.key_unique_producer.new_unique_key()}"
        mg_data = self.model_configuration.additional_data
        pf_model_generator = self.builder_from_phase(
            phases.TranslationPhases.MODEL_GENERATION)
        model_items = pf_model_generator.new_pipeline_items(
            pi.PIData(k_model_generator, [k_input]),
            mg_data
        )
        add_pi_s(model_items)
        # clean the memory
        mg_data = None
        pf_model_generator = None
        model_items = None

        #
        # 3-4) postprocessing and output

        # ... k_model_generator is defined, somehow ...
        pp_factory = self.builder_from_phase(
            phases.TranslationPhases.TRANSLATION_CONVERSION_POSTPROCESSING)
        output_factory = self.builder_from_phase(
            phases.TranslationPhases.OUTPUT)

        for poc in self.postprocessing_output_configurations:
            pp_conf: PostprocessingConfiguration = poc.postprocessing_configuration
            pp_subphase: pb_pp.PostProcessingTransformation = pp_conf.subphase
            pp_data: pb_pp.AdditionalDataPostProcessing = pp_conf.additional_data
            o_conf: OutputConfiguration = poc.output_configuration
            o_subphase: pb_o.OutputDestinationType = o_conf.subphase
            o_data: pb_o.AdditionalDataOutput = o_conf.additional_data

            # 3) postprocessing
            pp_data.k_model_generator = k_model_generator
            pp_t_name = pp_subphase.value
            k_pp_t = f"k_pp_t__{pp_t_name}__{self.key_unique_producer.new_unique_key()}"
            pp_items = pp_factory.new_pipeline_items(
                pi.PIData(k_pp_t, [k_model_generator]),
                pp_data
            )
            pp_output_producer: pi.PipelineItem = pp_items[-1]
            add_pi_s(pp_items)

            # 4) output
            o_name = pp_subphase.value
            k_o = f"k_o__{o_name}__{self.key_unique_producer.new_unique_key()}"
            # the last one is the "compiler", or whatever it is that produces the output
            key_output_holder = pp_output_producer.get_key()
            o_data.key_output_holder = key_output_holder
            o_items = output_factory.new_pipeline_items(
                pi.PIData(k_o, [key_output_holder]),
                o_data
            )
            add_pi_s(o_items)
            # clean the memory
            pp_conf = None
            pp_subphase = None
            pp_data = None
            pp_t_name = None
            pp_items = None
            pp_output_producer = None
            k_pp_t = None
            o_conf = None
            o_subphase = None
            o_data = None
            o_name = None
            k_o = None
            key_output_holder = None
            o_items = None

        # DONE
        return pm


# python -m src.translator_process
if __name__ == "__main__":
    printer_debug = u.PrinterDebug()
    printer_debug.print_msg("START A TEST ... of what?")
