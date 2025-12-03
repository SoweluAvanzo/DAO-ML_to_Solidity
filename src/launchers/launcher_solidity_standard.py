
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
external_unique_key_producer: pb_shared.KeyUniqueProducer = pb_shared.KeyUniqueProducerSimpleSequential()


def main():
    config = configs.TranslatorConfigs()

    # TODO : sistemare gli input
    config.model_format = pb_shared.ModelPersistanceFormat.XML
    # input
    config.input_config.source_uri = "Travelhive_final_model"
    config.input_config.persistance_type = pb_shared.PersistanceType.FILE
    config.input_config.file_base_folder = consts_t.DEFAULT_BASE_FOLDER_INPUT
    # model generation
    config.model_gen_config.xml_schema_filename = "XSD_DAO_ML"
    config.model_gen_config.xml_schema_extension = "xsd"
    config.folder_voting_protocols = consts_t.DEFAULT_FOLDER_TEMPLATES_VOTING_PROTOCOL
    config.base_template_folder = consts_t.DEFAULT_BASE_FOLDER_TEMPLATES
    #
    # preprocessing & output
    config.output_persistance_type = pb_shared.PersistanceType.FILE
    config.output_source_uri = files.concat_folder_filename(
        '.', 'out')

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
