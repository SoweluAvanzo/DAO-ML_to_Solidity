
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


import src.input.xml_file_input as xml_f_i
import src.input.txt_file_input as txt_f_i

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


def output_destination_type(i_s: pb_shared.PersistanceType, o_t: OutputType) -> OutputDestinationType:
    if i_s == pb_shared.PersistanceType.FILE:
        if o_t == OutputType.PLAIN_STRING:
            return OutputDestinationType.FILE_STRING
        elif o_t == OutputType.JINJA_COMPILATION:
            return OutputDestinationType.FILE_JINJA
    raise Exception(
        f"Unknown/unmanaged output & destination-type pair: < {i_s} ; {o_t} >")


class InputFactory(pb.PipelineItemFactory):

    def __init__(self, printer_debug: u.PrinterDebug = None):
        super().__init__(printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return OutputDestinationType

    def new_pipeline_item_from_variant(self, pi_data: pi.PIData,
                                       additional_data: pb.AdditionalDataSubPhase
                                       ) -> list[pi.PipelineItem]:
        # the real factory
        if additional_data.phase_step_variant == OutputDestinationType.FILE_JINJA:
            return None  # TODO DO IT
        elif additional_data.phase_step_variant == OutputDestinationType.FILE_STRING:
            return None  # TODO DO IT
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
