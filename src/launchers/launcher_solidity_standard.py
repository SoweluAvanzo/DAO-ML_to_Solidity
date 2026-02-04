
import src.launchers.cmd_args as cmd_args
import src.translator_process as translator_process
import src.launchers.launcher_configurable as launcher_config
import src.configurations as configs

import src.phases_builders.shared as pb_shared
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o

import src.postprocessing.model_translation.solidity.translation_types_solidity as transl_types_sol
import src.postprocessing.model_translation.solidity.optimized.jinja.s_t_jinja_optimized_versions as jinja_opt_versions
import src.postprocessing.model_translation.asm.translator_asm_versions as t_asm_versions
import src.postprocessing.model_translation.asm.t_j_asm_1_0_0 as t_j_asm_1_0_0
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as t_prov_by_name
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.tpbn_txt_file as template_by_name_txt
import src.postprocessing.consts_template as consts_t

import src.files.file_utils as files
import src.utilities.logger_debug as logger_debug

logger = logger_debug.LoggerDebug(
    class_name=__name__
)


def main():
    """
    Default version and configuration of the pipeline
    """
    external_unique_key_producer: pb_shared.KeyUniqueProducer = pb_shared.KeyUniqueProducerSimpleSequential()
    config = configs.TranslatorConfigs(
        external_unique_key_producer=external_unique_key_producer
    )

    base_template_folder = consts_t.DEFAULT_BASE_FOLDER_TEMPLATES
    # TODO : sistemare gli input
    config.model_format = pb_shared.ModelPersistanceFormat.XML

    # 1) input
    config.input_config.source_uri = "Travelhive_final_model"
    config.input_config.persistance_type = pb_shared.PersistanceType.FILE
    config.input_config.file_base_folder = consts_t.DEFAULT_BASE_FOLDER_INPUT

    # 2) model generation
    config.model_gen_config.xml_schema_filename = "XSD_DAO_ML"
    config.model_gen_config.xml_schema_extension = "xsd"
    config.model_gen_config.xml_schema_folder = files.concat_folder_filename(
        '.',  # 'src', 'parsers', 'xml'
        'data'
    )

    #
    # 3&4) preprocessing & output

    # output

    output_folder_base_path: str = files.concat_folder_filename(
        '.', 'out')

    oc_all = configs.OutputConfigs()
    oc_all.output_uri = output_folder_base_path
    oc_all.output_type = pb_o.OutputType.JINJA_COMPILATION
    oc_all.persistance_type = pb_shared.PersistanceType.FILE

    # .. solidity
    ppc_solidity = configs.PostprocessingConfigs()
    ppc_solidity.post_processing_transformation = pb_pp.PostProcessingTransformation.SOLIDITY
    ppc_solidity.version_translator = jinja_opt_versions.SolidityTranslatorJinjaOptimizedVersions.JO_1_0_0.value
    ppc_solidity.translator_solidity_subtype = transl_types_sol.TranslationTypesSolidity.OPTIMIZED.value
    ppc_solidity.base_template_folder = base_template_folder
    ppc_solidity.folder_voting_protocols_solidity = consts_t.DEFAULT_FOLDER_TEMPLATES_VOTING_PROTOCOL
    # TODO: is there a way to generalize the following?
    ppc_solidity.version_translation_target = "1.0.0"
    oc_solidity = configs.OutputConfigs()
    oc_solidity.output_type = pb_o.OutputType.JINJA_COMPILATION
    ppopc_solidity = configs.PostprocessingOutputPairConfigs(
        postprocessingConfigs=ppc_solidity,
        outputConfigs=oc_all
    )

    # .. solidity hardhat tests
    ppc_solidity_hardhat_tests = configs.PostprocessingConfigs()
    ppc_solidity_hardhat_tests.post_processing_transformation = pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS
    ppc_solidity_hardhat_tests.version_translator = jinja_opt_versions.SolidityTranslatorJinjaOptimizedVersions.JO_1_0_0.value
    ppc_solidity_hardhat_tests.base_template_folder = base_template_folder
    ppc_solidity_hardhat_tests.folder_voting_protocols_solidity = consts_t.DEFAULT_FOLDER_TEMPLATES_VOTING_PROTOCOL
    # TODO: is there a way to generalize the following?
    ppc_solidity_hardhat_tests.version_translation_target = "1.0.0"
    ppopc_solidity_hardhat_tests = configs.PostprocessingOutputPairConfigs(
        postprocessingConfigs=ppc_solidity_hardhat_tests,
        outputConfigs=oc_all
    )

    # .. asm
    ppc_asm = configs.PostprocessingConfigs()
    ppc_asm.post_processing_transformation = pb_pp.PostProcessingTransformation.ASM
    ppc_asm.version_translator = t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value
    ppc_asm.version_translation_target = t_j_asm_1_0_0.TARGET_VERSION
    ppc_asm.base_template_folder = base_template_folder
    ppopc_asm = configs.PostprocessingOutputPairConfigs(
        postprocessingConfigs=ppc_asm,
        outputConfigs=oc_all
    )
    # .. JSON
    ppc_json = configs.PostprocessingConfigs()
    ppc_json.post_processing_transformation = pb_pp.PostProcessingTransformation.JSON

    oc_json = configs.OutputConfigs()
    oc_json.output_uri = output_folder_base_path
    oc_json.output_type = pb_o.OutputType.PLAIN_STRING
    oc_json.persistance_type = pb_shared.PersistanceType.FILE
    ppopc_json = configs.PostprocessingOutputPairConfigs(
        postprocessingConfigs=ppc_json,
        outputConfigs=oc_json
    )

    # now, the list of PostProcessing and Output pairs

    all_postprocessingOutputPairConfigs: list[configs.PostprocessingOutputPairConfigs] = [
        ppopc_solidity,
        ppopc_solidity_hardhat_tests,
        ppopc_asm,
        ppopc_json
    ]
    config.all_postprocessingOutputPairConfigs = all_postprocessingOutputPairConfigs

    tp: translator_process.TranslatorProcess = None
    tc: launcher_config.TranslatorAndConfigurations = launcher_config.new_translator_process(
        config,
        instantiate_new_translator_process=True,
        logger=logger
    )
    tp = tc.translator_process
    logger.print_msg("START\n\n")
    tp.translate(
        tc.translation_configuration
    )
    logger.print_msg("\n\nEND")

#
#
#


#
#
#

# python -m ./src/launchers/launcher_solidity_standard > lss.txt
# python -m src.launchers.launcher_solidity_standard > lss.txt
if __name__ == "__main__":
    main()
