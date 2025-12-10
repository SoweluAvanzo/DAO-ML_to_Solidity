
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.shared as pb_shared

import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_any_value as pval

import src.postprocessing.model_translation.model_translator_configurable as mcc
import src.postprocessing.model_translation.translation_types as tt
import src.postprocessing.model_translation.solidity.voting_protocols_list_loader as pi_vpll
import src.postprocessing.model_translation.solidity.solidity_translator_configurable as pp_mt_sol_c
import src.postprocessing.model_translation.solidity.translation_types_solidity as transl_types_sol
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions
import src.postprocessing.model_translation.solidity.tests.jinja.solidity_tests_translator_jinja_hardhat as sol_test_t
import src.postprocessing.model_translation.asm.t_j_asm_1_0_0 as t_j_asm_1_0_0
import src.postprocessing.model_translation.asm.translator_asm_versions as t_asm_versions

import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.tpbn_txt_file as template_by_name_txt
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_sol_t_j_1_0_0 as c_sol_t_j_1_0_0
import src.postprocessing.output_preparation.compilers.solidity.tests.templates.jinja.c_sol_tests_t_j as c_sol_tests_t_j
import src.postprocessing.output_preparation.compilers.asm.templates.jinja.c_j_asm as c_asm_t_j
import src.postprocessing.output_preparation.json.model_to_json as pp_o_json


import src.output.text_file_output as tfo
import src.output.jinja_text_file_output as jtfo

import src.utilities.utils as u
import src.postprocessing.consts_template as consts_t
import src.utilities.extended_enum as ee
import src.utilities.errors as e_c


class OutputType(psv.PhaseSubstepVariants):
    PLAIN_STRING = "str"  # i.e., something a simple ".txt" file could accept
    JINJA_COMPILATION = "jinja"
    # YAML="yaml"
    # BSON = "bson"
    # BINARY = "bytes"


REVERSE_MAPPING_OutputType = {
    v.value: v for v in OutputType}


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


def output_destination_type(i_s: pb_shared.PersistanceType, o_t: OutputType) -> OutputDestinationType:
    if i_s == pb_shared.PersistanceType.FILE:
        if o_t == OutputType.PLAIN_STRING:
            return OutputDestinationType.FILE_STRING
        elif o_t == OutputType.JINJA_COMPILATION:
            return OutputDestinationType.FILE_JINJA
    raise Exception(
        f"Unknown/unmanaged output & destination-type pair: < {i_s} ; {o_t} >")


class AdditionalDataOutput(pb_shared.AdditionalDataSubPhase):
    def __init__(self, phase_step_variant: OutputDestinationType, key_output_holder: str = None):
        super().__init__(phase_step_variant)
        self.key_output_holder = key_output_holder

#


class AdditionalDataFile(AdditionalDataOutput):
    def __init__(self, phase_step_variant: OutputDestinationType,
                 folder_output_path_base: str,
                 key_output_holder: str = None
                 ):
        super().__init__(phase_step_variant,
                         key_output_holder=key_output_holder
                         )
        self.folder_output_path_base = folder_output_path_base


class AdditionalDataFileString(AdditionalDataFile):
    def __init__(self,
                 folder_output_path_base: str,
                 key_output_holder: str = None
                 ):
        super().__init__(OutputDestinationType.FILE_STRING, folder_output_path_base,
                         key_output_holder=key_output_holder
                         )


class AdditionalDataFileJinja(AdditionalDataFile):
    def __init__(self,
                 folder_output_path_base: str,
                 key_output_holder: str = None
                 ):
        super().__init__(OutputDestinationType.FILE_JINJA, folder_output_path_base,
                         key_output_holder=key_output_holder
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

    #

    def new_pipeline_item_from_variant(self,
                                       phase_step_variant_and_data: pb_shared.AdditionalDataSubPhase
                                       ) -> pb.PipelineItemsGenerated:
        if not isinstance(phase_step_variant_and_data, AdditionalDataOutput):
            raise Exception(
                f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataOutput, got: {type(phase_step_variant_and_data)}")
        # the real factory
        if phase_step_variant_and_data.phase_step_variant == OutputDestinationType.FILE_JINJA:
            if not isinstance(phase_step_variant_and_data, AdditionalDataFileJinja):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataFileJinja, got: {type(phase_step_variant_and_data)}")
            return self.new_file_jinja(phase_step_variant_and_data)
        elif phase_step_variant_and_data.phase_step_variant == OutputDestinationType.FILE_STRING:
            if not isinstance(phase_step_variant_and_data, AdditionalDataFileString):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataFileString, got: {type(phase_step_variant_and_data)}")
            key_output_holder = phase_step_variant_and_data.key_output_holder
            if phase_step_variant_and_data.key_output_holder is None:
                raise Exception(
                    f"ERROR: missing key_output_holder for output {phase_step_variant_and_data.phase_step_variant.name}")
            k_additional_output_data = self.new_unique_key(
                "k_additional_output_data__output_txt")
            self.print_msg(
                f"\n\n\n OUTPUTTING FILE_STRING with key_output_holder: {key_output_holder}")
            additional_metadata = {
                tfo.KEY_OPEN_FILE_MODE: tfo.MODE_VALUES_WRITE_array[0]
            }
            additional_output_data = pval.PIAnyValue(
                pi.PIData(k_additional_output_data, [key_output_holder]), additional_metadata)
            k_model_text_to_file_output = self.new_unique_key(
                "k_model_text_to_file_output")
            model_text_to_file_output = tfo.TextFileOutput(
                pi.PIData(
                    k_model_text_to_file_output,
                    [key_output_holder, k_additional_output_data]
                ),
                base_destination=phase_step_variant_and_data.folder_output_path_base,
                # write_mode_key=k_additional_output_data,
                printer_debug=self.printer_debug
            )
            return pb.PipelineItemsGenerated(
                [
                    additional_output_data,
                    model_text_to_file_output
                ],
                k_model_text_to_file_output
            )
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                        " : " + phase_step_variant_and_data.phase_step_variant.value)
