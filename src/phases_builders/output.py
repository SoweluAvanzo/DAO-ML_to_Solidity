
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.shared as pb_shared

import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_any_value as pval

# import src.postprocessing.model_translation.model_translator_configurable as mcc
# import src.postprocessing.model_translation.translation_types as tt
# import src.postprocessing.model_translation.solidity.voting_protocols_list_loader as pi_vpll
# import src.postprocessing.model_translation.solidity.solidity_translator_configurable as pp_mt_sol_c
# import src.postprocessing.model_translation.solidity.translation_types_solidity as transl_types_sol
# import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions
# import src.postprocessing.model_translation.solidity.tests.jinja.solidity_tests_translator_jinja_hardhat as sol_test_t
# import src.postprocessing.model_translation.asm.t_j_asm_1_0_0 as t_j_asm_1_0_0
# import src.postprocessing.model_translation.asm.translator_asm_versions as t_asm_versions

# import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.tpbn_txt_file as template_by_name_txt
# import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_sol_t_j_1_0_0 as c_sol_t_j_1_0_0
# import src.postprocessing.output_preparation.compilers.solidity.tests.templates.jinja.c_sol_tests_t_j as c_sol_tests_t_j
# import src.postprocessing.output_preparation.compilers.asm.templates.jinja.c_j_asm as c_asm_t_j
# import src.postprocessing.output_preparation.json.model_to_json as pp_o_json
import src.postprocessing.output_preparation.names_extractors as names_extr
# import src.postprocessing.consts_template as consts_t

import src.output.text_file_output as tfo
import src.output.jinja_text_file_output as jtfo

import src.utilities.utils as u
import src.utilities.extended_enum as ee
import src.utilities.errors as e_c


class OutputType(psv.PhaseSubstepVariants):
    PLAIN_STRING = "str"  # i.e., something a simple ".txt" file could accept
    JINJA_COMPILATION = "jinja"
    # YAML="yaml"
    # BSON = "bson"
    # BINARY = "bytes"


REVERSE_MAPPING_OutputType = {
    v.value: v for v in OutputType
}


class OutputDestinationType(psv.PhaseSubstepVariants):
    FILE_STRING = (pb_shared.PersistanceType.FILE.value,
                   OutputType.PLAIN_STRING.value)
    FILE_JINJA = (pb_shared.PersistanceType.FILE.value,
                  OutputType.JINJA_COMPILATION.value)
    # FILE_YAML
    # FILE_BSON
    # FILE_BINARY
    # API_STRING
    # API_JINJA
    # API_YAML
    # API_BSON
    # API_BINARY
    # DB_STRING
    # DB_JINJA
    # DB_YAML
    # DB_BSON
    # DB_BINARY


REVERSE_MAPPING_OutputDestinationType = {
    v.value: v for v in OutputDestinationType}


class NamesExtractorMethod(ee.ExtendedEnum):
    ENTITY_NAME = "name"  # the basic, default implementation


def output_destination_type(i_s: pb_shared.PersistanceType, o_t: OutputType) -> OutputDestinationType:
    if i_s == pb_shared.PersistanceType.FILE:
        if o_t == OutputType.PLAIN_STRING:
            return OutputDestinationType.FILE_STRING
        elif o_t == OutputType.JINJA_COMPILATION:
            return OutputDestinationType.FILE_JINJA
    raise Exception(
        f"Unknown/unmanaged output & destination-type pair: < {i_s} ; {o_t} >")


class AdditionalDataOutput(pb_shared.AdditionalDataSubPhase):
    def __init__(self, phase_step_variant: OutputDestinationType,
                 postprocessing_producing_output: pb_pp.PostProcessingTransformation = None,
                 key_output_holder: str = None,
                 key_diagram_model_producer: str = None
                 ):
        super().__init__(phase_step_variant)
        self.postprocessing_producing_output = postprocessing_producing_output
        self.key_output_holder = key_output_holder
        self.key_diagram_model_producer = key_diagram_model_producer

#


class AdditionalDataFile(AdditionalDataOutput):
    def __init__(self, phase_step_variant: OutputDestinationType,
                 folder_output_path_base: str,
                 postprocessing_producing_output: pb_pp.PostProcessingTransformation = None,
                 key_output_holder: str = None,
                 key_diagram_model_producer: str = None
                 ):
        super().__init__(phase_step_variant,
                         postprocessing_producing_output=postprocessing_producing_output,
                         key_output_holder=key_output_holder,
                         key_diagram_model_producer=key_diagram_model_producer
                         )
        self.folder_output_path_base = folder_output_path_base


class NamesExtractorJSON(names_extr.NamesExtractor):
    def __init__(self, pipeline_item_data,
                 printer_debug: u.PrinterDebug = None,
                 key_diagram_model: str = None,

                 ):
        super().__init__(pipeline_item_data,
                         printer_debug,
                         key_diagram_model
                         )

    def run(self, inputs) -> names_extr.NamesExtracted:
        ne: names_extr.NamesExtracted = super().run(inputs)
        return f"diagram__{ne.diagram_name}.{pb_shared.ModelPersistanceFormat.JSON.value}"
        # ne:names_extr.NamesExtracted = filename_extension


class AdditionalDataFileString(AdditionalDataFile):
    def __init__(self,
                 folder_output_path_base: str,
                 names_etraction_type: NamesExtractorMethod = None,
                 postprocessing_producing_output: pb_pp.PostProcessingTransformation = None,
                 key_output_holder: str = None,
                 key_diagram_model_producer: str = None
                 ):
        super().__init__(OutputDestinationType.FILE_STRING, folder_output_path_base,
                         postprocessing_producing_output=postprocessing_producing_output,
                         key_output_holder=key_output_holder,
                         key_diagram_model_producer=key_diagram_model_producer
                         )
        self.names_etraction_type = NamesExtractorMethod.ENTITY_NAME \
            if names_etraction_type is None else names_etraction_type


class AdditionalDataFileJinja(AdditionalDataFile):
    def __init__(self,
                 folder_output_path_base: str,
                 postprocessing_producing_output: pb_pp.PostProcessingTransformation = None,
                 key_output_holder: str = None,
                 key_diagram_model_producer: str = None
                 ):
        super().__init__(OutputDestinationType.FILE_JINJA, folder_output_path_base,
                         postprocessing_producing_output=postprocessing_producing_output,
                         key_output_holder=key_output_holder,
                         key_diagram_model_producer=key_diagram_model_producer
                         )

#


# class AdditionalDataDB(AdditionalDataOutput):
#    def __init__(self, phase_step_variant: OutputDestinationType,
#                 db_type: str,
#                 db_name: str,
#                 db_uri: str,
#                 db_config=None,
#                 db_interface=None # the actual connection to perform CRUD operations
#                 ):
#        super().__init__(phase_step_variant)
#        self.db_type = db_type
#        self.db_name = db_name
#        self.db_uri = db_uri
#        self.db_config = db_config
#        self.db_interface = db_interface
# TODO: add all other DB types


#
#
#

class OutputFactory(pb.PipelineItemFactory):

    def __init__(self, key_unique_producer: pb_shared.KeyUniqueProducer,
                 printer_debug: u.PrinterDebug = None):
        super().__init__(key_unique_producer, printer_debug=printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return OutputDestinationType

    #

    def new_file_jinja(self, phase_step_variant_and_data: AdditionalDataFileJinja
                       ) -> pb.PipelineItemsGenerated:
        k_model_jinja_to_file_output = self.new_unique_key(
            "k_model_jinja_to_file_output")
        key_output_holder = phase_step_variant_and_data.key_output_holder
        if phase_step_variant_and_data.key_output_holder is None:
            raise Exception(
                f"ERROR: missing key_output_holder for output {phase_step_variant_and_data.phase_step_variant.name}")
        self.print_msg(f"jinja key_output_holder: {key_output_holder}")
        key_base_folder_output_provider = self.new_unique_key(
            "key_base_folder_output_provider")
        base_folder_output_provider = pstr.PIStr(
            pi.PIData(key_base_folder_output_provider, None),
            val=phase_step_variant_and_data.folder_output_path_base
        )
        model_jinja_to_file_output = jtfo.JinjaTextFileOutput(
            pi.PIData(k_model_jinja_to_file_output, [
                      key_output_holder, key_base_folder_output_provider]),
            key_compiled_diagram=key_output_holder,
            key_base_destination=key_base_folder_output_provider
        )
        return pb.PipelineItemsGenerated(
            [
                model_jinja_to_file_output,
                base_folder_output_provider
            ],
            k_model_jinja_to_file_output
        )

    def new_file_string(self, phase_step_variant_and_data: AdditionalDataFileString
                        ) -> pb.PipelineItemsGenerated:
        key_output_holder = phase_step_variant_and_data.key_output_holder
        if phase_step_variant_and_data.key_output_holder is None:
            raise Exception(
                f"ERROR: missing key_output_holder for output {phase_step_variant_and_data.phase_step_variant.name}")
        if phase_step_variant_and_data.key_diagram_model_producer is None:
            raise Exception(
                f"ERROR: phase_step_variant_and_data.key_diagram_model_producer is None")
        k_additional_output_data = self.new_unique_key(
            "k_additional_output_data__output_txt")
        self.print_msg(
            f"\n\n\n OUTPUTTING FILE_STRING with key_output_holder: {key_output_holder}")
        additional_metadata = {
            tfo.KEY_OPEN_FILE_MODE: tfo.MODE_VALUES_WRITE_array[0]
        }
        additional_output_data = pval.PIAnyValue(
            pi.PIData(k_additional_output_data, [key_output_holder]),
            additional_metadata
        )
        # names_extractor
        names_extractor: names_extr.NamesExtractor = None
        k_names_extractor: str = None
        if (phase_step_variant_and_data.names_etraction_type is None) or \
                (phase_step_variant_and_data.names_etraction_type == NamesExtractorMethod.ENTITY_NAME):
            k_names_extractor = self.new_unique_key("k_names_extractor")
            pi_data_n_e = pi.PIData(
                k_names_extractor,
                [phase_step_variant_and_data.key_diagram_model_producer]
            )
            match(phase_step_variant_and_data.postprocessing_producing_output):
                case(pb_pp.PostProcessingTransformation.JSON):
                    names_extractor = NamesExtractorJSON(
                        pi_data_n_e,
                        printer_debug=self.printer_debug,
                        key_diagram_model=phase_step_variant_and_data.key_diagram_model_producer
                    )
                case _:
                    names_extractor = names_extr.NamesExtractor(
                        pi_data_n_e,
                        printer_debug=self.printer_debug,
                        key_diagram_model=phase_step_variant_and_data.key_diagram_model_producer
                    )
        k_model_text_to_file_output = self.new_unique_key(
            "k_model_text_to_file_output")
        if names_extractor is None:
            raise Exception(
                f"ERROR: a Names Extractor must be defined to output a text file (k_model_text_to_file_output key: {k_model_text_to_file_output})")
        k_base_destination_provider = self.new_unique_key(
            "k_base_destination_provider")
        base_destination_provider = pstr.PIStr(
            pi.PIData(k_base_destination_provider, None),
            val=phase_step_variant_and_data.folder_output_path_base
        )
        model_text_to_file_output = tfo.TextFileOutput(
            pi.PIData(
                k_model_text_to_file_output,
                [key_output_holder, k_base_destination_provider,
                    k_additional_output_data, k_names_extractor]
            ),
            key_base_destination=k_base_destination_provider,
            # write_mode_key=k_additional_output_data,
            printer_debug=self.printer_debug,
            key_filename_extension=k_names_extractor
        )
        return pb.PipelineItemsGenerated(
            [
                additional_output_data,
                base_destination_provider,
                names_extractor,
                model_text_to_file_output
            ],
            k_model_text_to_file_output
        )

    #

    def new_pipeline_item_from_variant(self,
                                       phase_step_variant_and_data: pb_shared.AdditionalDataSubPhase
                                       ) -> pb.PipelineItemsGenerated:
        if not isinstance(phase_step_variant_and_data, AdditionalDataOutput):
            raise Exception(
                f"ERROR: Wrong class for given phase_step_variant_and_data: expected AdditionalDataOutput, got: {type(phase_step_variant_and_data)}")
        # the real factory
        if phase_step_variant_and_data.phase_step_variant == OutputDestinationType.FILE_JINJA:
            if not isinstance(phase_step_variant_and_data, AdditionalDataFileJinja):
                raise Exception(
                    f"ERROR: Wrong class for given phase_step_variant_and_data: expected AdditionalDataFileJinja, got: {type(phase_step_variant_and_data)}")
            return self.new_file_jinja(phase_step_variant_and_data)
        elif phase_step_variant_and_data.phase_step_variant == OutputDestinationType.FILE_STRING:
            if not isinstance(phase_step_variant_and_data, AdditionalDataFileString):
                raise Exception(
                    f"ERROR: Wrong class for given phase_step_variant_and_data: expected AdditionalDataFileString, got: {type(phase_step_variant_and_data)}")
            return self.new_file_string(phase_step_variant_and_data)
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                        " : " + phase_step_variant_and_data.phase_step_variant.value)
