# TUTTO configurabile da argomenti di linea di comando

import src.translator_process as translator_process

import src.phases_builders.shared as pb_shared
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o

import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as t_prov_by_name
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.tpbn_txt_file as template_by_name_txt
import src.postprocessing.consts_template as consts_t

import src.launchers.cmd_args as cmd_args
import src.configurations as configs

import src.files.file_utils as files
import src.utilities.utils as u
import src.utilities.errors as e_c


def non_none(what, name):
    if what is None:
        raise Exception(f"Missing mandatory paramter: {name}")


def prepare_input(
    config: configs.TranslatorConfigs,
    folder_voting_protocols: str,
    base_template_folder: str,
    logger: u.PrinterDebug = None
) -> translator_process.InputConfiguration:
    # input
    source_uri: str = config.input_config.source_uri
    input_persistance_type: pb_shared.PersistanceType = config.input_config.persistance_type
    input_format: pb_shared.ModelPersistanceFormat = config.model_format
    non_none(source_uri, "source_uri")
    non_none(input_persistance_type, "input_persistance_type")
    non_none(input_format, "input_format")

    input_additional_data: pb_i_f.AdditionalDataInput = None
    match(input_persistance_type):
        case pb_shared.PersistanceType.FILE.value:
            non_none(config.input_config.file_extension,
                     "input_config.file_extension")
            fbf: str = config.input_config.file_base_folder
            if fbf is None:
                fbf = consts_t.DEFAULT_BASE_FOLDER_INPUT
            source_fullpath = files.concat_folder_filename(
                fbf,
                f"{source_uri}.{config.input_config.file_extension}"
            )
            match(input_format):
                case pb_shared.ModelPersistanceFormat.XML.value:
                    non_none(config.input_config.xml_version,
                             "input_config.xml_version")
                    input_additional_data = pb_i_f.FileXMLAdditionalDataSubPhase(
                        filepath=source_fullpath,
                        xml_version=config.input_config.xml_version,
                        should_strip_line=True
                    )
                case pb_shared.ModelPersistanceFormat.JSON.value:
                    input_additional_data = pb_i_f.FileJSONAdditionalDataSubPhase(
                        filepath=source_fullpath,
                        should_strip_line=True
                    )
                case _:
                    raise Exception(
                        e_c.ERROR_TEXT__NOT_IMPLEMENTED + ": " + input_format)
        case pb_shared.PersistanceType.DATABASE.value:
            # TODO: upon future developments, make use of the source_uri
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + pb_shared.PersistanceType.DATABASE.name)
        case _:
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + input_persistance_type)
    return translator_process.InputConfiguration(
        input_persistance_type=input_persistance_type,
        input_format=input_format,
        additional_data=input_additional_data
    )


def prepare_model(
    config: configs.TranslatorConfigs,
    input_format: pb_shared.ModelPersistanceFormat,
    logger: u.PrinterDebug = None
) -> translator_process.ModelConfiguration:
    match(input_format):
        case pb_shared.ModelPersistanceFormat.XML.value:
            non_none(config.model_gen_config.xml_schema_folder,
                     "model_gen_config.xml_schema_folder")
            non_none(config.model_gen_config.xml_schema_filename,
                     "model_gen_config.xml_schema_filename")
            non_none(config.model_gen_config.xml_schema_extension,
                     "model_gen_config.xml_schema_extension")
            file_path_xml_schema = files.concat_folder_filename(
                config.model_gen_config.xml_schema_folder,
                f"{config.model_gen_config.xml_schema_filename}.{config.model_gen_config.xml_schema_extension}"
            )
            return translator_process.ModelConfiguration(
                pb_shared.ModelPersistanceFormat.XML,
                additional_data=pb_m_g.ModelXMLGeneratordData(
                    file_path_xml_schema
                )
            )
        case pb_shared.ModelPersistanceFormat.JSON.value:
            return translator_process.ModelConfiguration(
                pb_shared.ModelPersistanceFormat.JSON,
                additional_data=pb_m_g.ModelJSONGeneratordData()
            )
        case _:
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + input_format)


def additional_data_from_PostProcessingTransformation(
    config: configs.TranslatorConfigs,
    ppc: configs.PostprocessingConfigs,
    templates_provider,
    base_template_folder: str,
    folder_voting_protocols: str,
    logger: u.PrinterDebug = None
) -> pb_pp.AdditionalDataPostProcessing:
    add_data: pb_pp.AdditionalDataPostProcessing = None
    match(ppc.post_processing_transformation):
        case pb_pp.PostProcessingTransformation.SOLIDITY:
            non_none(ppc.version_translator)
            non_none(ppc.translator_solidity_subtype)
            non_none(ppc.version_translation_target)
            add_data = pb_pp.AdditionalDataSolidity(  # TODO 05-12-2025 PUT ALL PARAMETERS IN THE CONFIGURATION
                folder_voting_protocols,
                templates_provider=templates_provider,
                folder_templates=base_template_folder,
                version_translator=ppc.version_translator,
                translator_solidity_subtype=ppc.translator_solidity_subtype,
                version_translation_target=ppc.version_translation_target
            )
        case pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS:
            non_none(ppc.version_translator)
            non_none(ppc.version_translation_target)
            add_data = pb_pp.AdditionalDataSolidityHardhatTests(
                templates_provider=templates_provider,
                folder_templates=base_template_folder,
                version_translator=ppc.version_translator,
                version_translation_target=ppc.version_translation_target
            )
        case pb_pp.PostProcessingTransformation.ASM:
            non_none(ppc.version_translator)
            non_none(ppc.version_translation_target)
            add_data = pb_pp.AdditionalDataASM(
                templates_provider=templates_provider,
                folder_templates=base_template_folder,
                version_translator=ppc.version_translator,
                version_translation_target=ppc.version_translation_target
            )
        case pb_pp.PostProcessingTransformation.JSON:
            # non_none(ppc.indent_json)
            add_data = pb_pp.AdditionalDataJSON(
                indent=2 if ppc.indent_json is None else ppc.indent_json
            )
        # FUTURE: case pb_pp.PostProcessingTransformation.PETRI_NETS:
    return add_data


def additional_data_from_Output(
    config: configs.TranslatorConfigs,
    oc: configs.OutputConfigs,
    templates_provider: t_prov_by_name.TemplateProviderByName,
    base_template_folder: str,
    folder_voting_protocols: str,
    logger: u.PrinterDebug = None
) -> pb_o.AdditionalDataOutput:
    add_data: pb_o.AdditionalDataOutput = None

    # TODO 05-12-2025 DO THE configs.OutputConfigs

    match(oc.persistance_type):
        case pb_shared.PersistanceType.FILE.value:
            match(oc.output_type):
                case pb_o.OutputType.PLAIN_STRING:
                    raise Exception(
                        e_c.ERROR_TEXT__NOT_IMPLEMENTED + " TODOOOOOOOOO")
                case pb_o.OutputType.JINJA_COMPILATION:
                    raise Exception(
                        e_c.ERROR_TEXT__NOT_IMPLEMENTED + " TODOOOOOOOOO")
        case pb_shared.PersistanceType.DATABASE.value:
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + oc.persistance_type)
    return add_data


def prepare_ppt_o(
    config: configs.TranslatorConfigs,
    # inherited from PPT
    templates_provider: t_prov_by_name.TemplateProviderByName,
    base_template_folder: str,
    folder_voting_protocols: str,
    # inherited from Output

    #
    logger: u.PrinterDebug = None
) -> list[translator_process.PostprocessingOutput]:
    return [
        translator_process.PostprocessingOutput(
            translator_process.PostprocessingConfiguration(
                ppopc.postprocessingConfigs.post_processing_transformation,
                additional_data_from_PostProcessingTransformation(
                    config,
                    ppopc.postprocessingConfigs,
                    logger=logger
                ),
                translator_process.OutputConfiguration(
                    ppopc.outputConfigs.persistance_type,
                    ppopc.outputConfigs.output_type,
                    additional_data=additional_data_from_Output(
                        config,
                        ppopc.postprocessingConfigs,
                        ppopc.outputConfigs,
                        templates_provider,
                        base_template_folder,
                        folder_voting_protocols,
                        logger=logger
                    )
                )
            )
        )
        for ppopc in config.all_postprocessingOutputPairConfigs
    ]

#


def new_translator_process(
    config: configs.TranslatorConfigs,
    logger: u.PrinterDebug = None
) -> translator_process.TranslatorProcess:
    """
    TODO: sistemare gli input

    """

    folder_voting_protocols: str = config.folder_voting_protocols
    base_template_folder: str = config.base_template_folder

    # 1) Input
    input_configuration: translator_process.InputConfiguration = prepare_input(
        config,
        folder_voting_protocols,
        base_template_folder,
        logger=logger
    )

    # 2) Model
    input_format = input_configuration.input_format
    model_configuration: translator_process.ModelConfiguration = prepare_model(
        config,
        input_format=input_format,
        logger=logger
    )

    # 3-4) Postprocessing + Output

    non_none(folder_voting_protocols, "folder_voting_protocols")
    non_none(base_template_folder, "base_template_folder")

    templates_provider: t_prov_by_name.TemplateProviderByName = template_by_name_txt.TemplateProviderFromTxtFile(
        base_template_folder=base_template_folder
    )  # TODO: find a way to  generalize it

    non_none(config.all_postprocessingOutputPairConfigs,
             "config.all_postprocessingOutputPairConfigs")

    if output_folder_default is None:
        raise Exception(f"Missing mandatory paramter: output_folder_default")
    folder_output = output_folder_default

    solidity_output_configuration = translator_process.OutputConfiguration(
        pb_shared.PersistanceType.FILE,
        pb_o.OutputType.JINJA_COMPILATION,
        additional_data=pb_o.AdditionalDataFileJinja(
            folder_output
        )
    )

    postprocessing_output_configurations: list[translator_process.PostprocessingOutput] = prepare_ppt_o(
        config,
        templates_provider,
        base_template_folder,
        folder_voting_protocols,
        logger=logger
    )

    postprocessing_output_configurations_OLD: list[translator_process.PostprocessingOutput] = [
        # solidity
        translator_process.PostprocessingOutput(
            translator_process.PostprocessingConfiguration(
                pb_pp.PostProcessingTransformation.SOLIDITY,
                additional_data=pb_pp.AdditionalDataSolidity(
                    folder_voting_protocols,
                    templates_provider=templates_provider,
                    folder_templates=base_template_folder,
                    version_translator=jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value,
                    translator_solidity_subtype=transl_types_sol.TranslationTypesSolidity.OPTIMIZED.value,
                    version_translation_target="1.0.0"
                )
            ),
            solidity_output_configuration
        ),
        # solidity hardhat test
        translator_process.PostprocessingOutput(
            translator_process.PostprocessingConfiguration(
                pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS,
                additional_data=pb_pp.AdditionalDataSolidityHardhatTests(
                    templates_provider=templates_provider,
                    folder_templates=base_template_folder,
                    version_translator=jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value,
                    version_translation_target="1.0.0"
                )
            ),
            solidity_output_configuration
        ),
        # ASM
        translator_process.PostprocessingOutput(
            translator_process.PostprocessingConfiguration(
                pb_pp.PostProcessingTransformation.ASM,
                additional_data=pb_pp.AdditionalDataASM(
                    templates_provider=templates_provider,
                    folder_templates=base_template_folder,
                    version_translator=t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value,
                    version_translation_target=t_j_asm_1_0_0.TARGET_VERSION
                )
            ),
            solidity_output_configuration
        ),
    ]

    # THE TRANSLATOR PROCESS

    # python -m src.launchers.launcher_solidity_standard > lss.txt

    tp = translator_process.TranslatorProcess(
        input_configuration,
        model_configuration,
        postprocessing_output_configurations,
        #
        printer_debug=logger,
        external_unique_key_producer=external_unique_key_producer
    )
