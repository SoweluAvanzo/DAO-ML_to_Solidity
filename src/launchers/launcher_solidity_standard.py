
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
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions
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
    config = configs.TranslatorConfigs()

    # TODO : sistemare gli input
    config.model_format = pb_shared.ModelPersistanceFormat.XML

    # 1) input
    config.input_config.source_uri = "Travelhive_final_model"
    config.input_config.persistance_type = pb_shared.PersistanceType.FILE
    config.input_config.file_base_folder = consts_t.DEFAULT_BASE_FOLDER_INPUT

    # 2) model generation
    config.model_gen_config.xml_schema_filename = "XSD_DAO_ML"
    config.model_gen_config.xml_schema_extension = "xsd"
    config.folder_voting_protocols = consts_t.DEFAULT_FOLDER_TEMPLATES_VOTING_PROTOCOL
    config.base_template_folder = consts_t.DEFAULT_BASE_FOLDER_TEMPLATES

    #
    # 3&4) preprocessing & output

    # output

    persistance_type_file = pb_shared.PersistanceType.FILE
    output_folder_base_path: str = files.concat_folder_filename(
        '.', 'out')

    solidity_output_configuration = translator_process.OutputConfiguration(
        pb_shared.PersistanceType.FILE,
        pb_o.OutputType.JINJA_COMPILATION,
        additional_data=pb_o.AdditionalDataFileJinja(
            folder_output_path_base=output_folder_base_path
        )
    )

    # .. solidity
    ppc_solidity = configs.PostprocessingConfigs()
    ppc_solidity.post_processing_transformation = pb_pp.PostProcessingTransformation.SOLIDITY
    ppc_solidity.version_translator = jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value
    ppc_solidity.translator_solidity_subtype = transl_types_sol.TranslationTypesSolidity.OPTIMIZED.value
    # TODO: is there a way to generalize the following?
    ppc_solidity.version_translation_target = "1.0.0"
    oc_solidity = configs.OutputConfigs()
    oc_solidity.output_type = pb_o.OutputType.JINJA_COMPILATION
    # TODO: CONTINUE THE OUTPUT
    ppopc_solidity = configs.PostprocessingOutputPairConfigs(
        postprocessingConfigs=ppc_solidity
    )

    # .. TODO solidity hardhat tests
    ppc_solidity_hardhat_tests = configs.PostprocessingConfigs()
    ppc_solidity_hardhat_tests.post_processing_transformation = pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS
    ppc_solidity_hardhat_tests.version_translator = jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value
    # TODO: is there a way to generalize the following?
    ppc_solidity_hardhat_tests.version_translation_target = "1.0.0"
    ppopc_solidity_hardhat_tests = configs.PostprocessingOutputPairConfigs(
        postprocessingConfigs=ppc_solidity_hardhat_tests
    )

    # .. TODO asm
    ppc_asm = configs.PostprocessingConfigs()
    ppc_asm.post_processing_transformation = pb_pp.PostProcessingTransformation.ASM
    ppc_asm.version_translator = t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value
    ppc_asm.version_translation_target = t_j_asm_1_0_0.TARGET_VERSION
    ppopc_asm = configs.PostprocessingOutputPairConfigs(
        postprocessingConfigs=ppc_asm
    )

    all_postprocessingOutputPairConfigs: list[configs.PostprocessingOutputPairConfigs] = [
        ppopc_solidity,
        ppopc_solidity_hardhat_tests,
        ppopc_asm
    ]
    config.all_postprocessingOutputPairConfigs = all_postprocessingOutputPairConfigs

    # config.output_persistance_type = persistance_type_file
    # config.output_source_uri =

    tp = launcher_config.new_translator_process(
        config,
        logger=logger
    )

    logger.print_msg("START\n\n")
    tp.translate()
    logger.print_msg("\n\nEND")

#
#
#


#
#
#


if __name__ == "__main__":
    main()
