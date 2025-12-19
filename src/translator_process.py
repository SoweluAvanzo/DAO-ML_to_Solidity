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

import src.input.txt_file_input_cacheable as txt_f_i_caching

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
                 additional_data: pb_shared.AdditionalDataSubPhase
                 ):
        self.phase = phase
        self.subphase = subphase
        self.additional_data = additional_data

#


class InputConfiguration(SubPhaseConfiguration):
    def __init__(self, input_persistance_type: pb_shared.PersistanceType,
                 input_format: pb_shared.ModelPersistanceFormat,
                 additional_data: pb_i_f.AdditionalDataInput
                 ):
        super().__init__(
            phases.TranslationPhases.INPUT_FETCHING,
            pb_i_f.input_persistance_type_format(
                input_persistance_type, input_format),
            additional_data
        )
        self.input_persistance_type = input_persistance_type
        self.input_format = input_format


class ModelConfiguration(SubPhaseConfiguration):
    def __init__(self,  model_generator_format: pb_shared.ModelPersistanceFormat,
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
        # keep the data for any possible use
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


class TranslationConfiguration:
    """
    Class aimed to hold all TranslatorProcess's configurations
    """

    def __init__(self,
                 input_configuration: InputConfiguration,
                 model_configuration: ModelConfiguration,
                 postprocessing_output_configurations: list[PostprocessingOutput],
                 # TODO altro?
                 external_unique_key_producer: pb_shared.KeyUniqueProducer = None,
                 is_resetting_cache=False
                 ):
        self.external_unique_key_producer = external_unique_key_producer
        self.input_configuration = input_configuration
        self.model_configuration = model_configuration
        self.postprocessing_output_configurations = postprocessing_output_configurations
        self.is_resetting_cache = is_resetting_cache


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
                 printer_debug: u.PrinterDebug = None
                 ):
        self.printer_debug = printer_debug
        #
        # additional things, cases specific
        self.txt_file_input_caching = txt_f_i_caching.TextFileInputCacheable(
            pi.PIData("empty", dependencies=None),
            printer_debug=printer_debug,
        )

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

    def reset_cache(self):
        self.txt_file_input_caching.clear_cache()

    #

    def build_phase_input(self,
                          translation_configs: TranslationConfiguration,
                          key_unique_producer: pb_shared.KeyUniqueProducer
                          ):
        """
        Override-designed
        """
        return pb_i_f.InputFactory(
            key_unique_producer,
            printer_debug=self.printer_debug,
            file_input_caching=self.txt_file_input_caching
        )

    def build_phase_model_generation(self,
                                     translation_configs: TranslationConfiguration,
                                     key_unique_producer: pb_shared.KeyUniqueProducer
                                     ):
        """
        Override-designed
        """
        return pb_m_g.ModelGeneratorFactory(key_unique_producer, printer_debug=self.printer_debug)

    def build_phase_postprocessing(self,
                                   translation_configs: TranslationConfiguration,
                                   key_unique_producer: pb_shared.KeyUniqueProducer
                                   ):
        """
        Override-designed
        """
        return pb_pp.PostProcessingFactory(key_unique_producer, printer_debug=self.printer_debug)

    def build_phase_output(self,
                           translation_configs: TranslationConfiguration,
                           key_unique_producer: pb_shared.KeyUniqueProducer
                           ):
        """
        Override-designed
        """
        return pb_o.OutputFactory(key_unique_producer, printer_debug=self.printer_debug)

    def builder_from_phase(self,
                           phase: phases.TranslationPhases,
                           translation_configs: TranslationConfiguration,
                           key_unique_producer: pb_shared.KeyUniqueProducer
                           ) -> pb.PipelineItemFactory:
        match phase:
            case phases.TranslationPhases.INPUT_FETCHING:
                return self.build_phase_input(translation_configs, key_unique_producer)
            case phases.TranslationPhases.MODEL_GENERATION:
                return self.build_phase_model_generation(translation_configs, key_unique_producer)
            case phases.TranslationPhases.TRANSLATION_CONVERSION_POSTPROCESSING:
                return self.build_phase_postprocessing(translation_configs, key_unique_producer)
            case phases.TranslationPhases.OUTPUT:
                return self.build_phase_output(translation_configs, key_unique_producer)
        raise Exception(f"Unrecognized phase: {phase}")

    #

    #

    def translate(self, translation_configs: TranslationConfiguration) -> dict:
        if translation_configs.is_resetting_cache:
            self.reset_cache()
        translation_pipeline: pmp.PipelineManager = self.build_translation_pipeline(
            translation_configs)
        return translation_pipeline.runPipeline()

    #

    def build_translation_pipeline(self, translation_configs: TranslationConfiguration) -> pmp.PipelineManager:
        self.print_msg("Building the translation pipeline")
        pm = pmp.PipelineManager(printer_debug=self.printer_debug)

        key_unique_producer: pb_shared.KeyUniqueProducer = self.new_key_unique_producer()\
            if translation_configs.external_unique_key_producer is None \
            else translation_configs.external_unique_key_producer

        # function to add items to the pipeline
        def add_pi_s(items: list[pi.PipelineItem]):
            for item in items:
                self.print_msg(f"adding PipelineItem of type {type(item)} ...")
                self.print_msg(f"\t ... of key: {item.get_key()}")
                pm.addItem(item)

        #
        # 1) input
        self.print_msg("building input phase")
        input_data: pb_i_f.AdditionalDataInput = translation_configs.input_configuration.additional_data
        pf_input = self.builder_from_phase(
            phases.TranslationPhases.INPUT_FETCHING,
            translation_configs,
            key_unique_producer
        )
        input_p_g: pb.PipelineItemsGenerated = pf_input.new_pipeline_items(
            input_data)
        input_items = input_p_g.pipeline_items
        k_input = input_p_g.key_last_pi
        add_pi_s(input_items)
        # clean the memory
        input_data = None
        pf_input = None
        input_p_g = None
        input_items = None

        #
        # 2) model generation
        self.print_msg("building model generation phase")
        mg_data: pb_m_g.AdditionalDataModelGeneration = translation_configs.model_configuration.additional_data
        mg_data.key_input_provider = k_input
        pf_model_generator = self.builder_from_phase(
            phases.TranslationPhases.MODEL_GENERATION,
            translation_configs,
            key_unique_producer
        )
        mg_p_g: pb.PipelineItemsGenerated = pf_model_generator.new_pipeline_items(
            mg_data)
        model_items = mg_p_g.pipeline_items
        k_model_generator = mg_p_g.key_last_pi
        add_pi_s(model_items)
        # clean the memory
        mg_data = None
        pf_model_generator = None
        mg_p_g = None
        model_items = None

        #
        # 3-4) postprocessing and output
        self.print_msg("building postprocessing and output phase")
        pp_factory = self.builder_from_phase(
            phases.TranslationPhases.TRANSLATION_CONVERSION_POSTPROCESSING,
            translation_configs,
            key_unique_producer
        )
        output_factory = self.builder_from_phase(
            phases.TranslationPhases.OUTPUT,
            translation_configs,
            key_unique_producer
        )
        for poc in translation_configs.postprocessing_output_configurations:
            pp_conf: PostprocessingConfiguration = poc.postprocessing_configuration
            pp_subphase: pb_pp.PostProcessingTransformation = pp_conf.subphase
            pp_data: pb_pp.AdditionalDataPostProcessing = pp_conf.additional_data
            pp_data.k_model_generator = k_model_generator
            o_conf: OutputConfiguration = poc.output_configuration
            o_subphase: pb_o.OutputDestinationType = o_conf.subphase
            o_data: pb_o.AdditionalDataOutput = o_conf.additional_data

            # 3) postprocessing
            pp_data.k_model_generator = k_model_generator
            pp_t_name = pp_subphase.value
            k_pp_t = f"k_pp_t__{pp_t_name}__{key_unique_producer.new_unique_key()}"
            self.print_msg(f"\t postprocessing key: {k_pp_t}")
            pp_p_g: pb.PipelineItemsGenerated = pp_factory.new_pipeline_items(
                pp_data)
            pp_items = pp_p_g.pipeline_items
            k_pp_output_producer: pb.PipelineItemsGenerated = pp_p_g.key_last_pi
            add_pi_s(pp_items)

            # 4) output
            o_name = pp_subphase.value
            k_o = f"k_o__{o_name}__{key_unique_producer.new_unique_key()}"
            # the last one is the "compiler", or whatever it is that produces the output
            key_output_holder = k_pp_output_producer
            o_data.key_output_holder = key_output_holder
            o_data.key_diagram_model_producer = k_model_generator
            self.print_msg(f"\t output key: {k_o}")
            o_p_g: pb.PipelineItemsGenerated = output_factory.new_pipeline_items(
                o_data)
            o_items = o_p_g.pipeline_items
            add_pi_s(o_items)
            # clean the memory
            pp_conf = None
            pp_subphase = None
            pp_data = None
            pp_t_name = None
            pp_items = None
            pp_p_g = None
            k_pp_output_producer = None
            k_pp_t = None
            o_conf = None
            o_subphase = None
            o_data = None
            o_name = None
            k_o = None
            key_output_holder = None
            o_p_g = None
            o_items = None

        # DONE
        return pm
