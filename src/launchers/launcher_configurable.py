# TUTTO configurabile da argomenti di linea di comando

import src.translator_process as translator_process
import src.launchers.cmd_args as cmd_args
import src.configurations as configs

import src.utilities.utils as u


def new_translator_process(
    logger: u.PrinterDebug = None,
    source_filename_default: str = None,
    output_folder_default: str = None,
    folder_voting_protocols: str = None,
    base_template_folder: str = None,
) -> translator_process.TranslatorProcess:

    # 1) Input
    if source_filename_default is None:
        raise Exception(f"Missing mandatory paramter: source_filename_default")
    source_filename = source_filename_default
    EXTENSION_XML = "xml"
    source_fullpath = files.concat_folder_filename(
        '.', 'data', f"{source_filename}.{EXTENSION_XML}")

    input_configuration = translator_process.InputConfiguration(
        input_source_type=pb_shared.PersistanceType.FILE,
        input_type=pb_i_f.InputType.XML,
        additional_data=pb_i_f.FileXMLAdditionalDataSubPhase(
            filepath=source_fullpath,
            xml_version="1.0.0",
            should_strip_line=True
        )
    )

    # 2) Model

    FILE_NAME_XML_SCHEMA = "XSD_DAO_ML"
    EXTENSION_XML_SCHEMA = "xsd"
    file_path_xml_schema = files.concat_folder_filename(
        '.', 'data', f"{FILE_NAME_XML_SCHEMA}.{EXTENSION_XML_SCHEMA}")
    model_configuration = translator_process.ModelConfiguration(
        pb_m_g.ModelGeneratorFormat.XML,
        additional_data=pb_m_g.ModelXMLGeneratordData(
            file_path_xml_schema
        )
    )

    # 3-4) Postprocessing + Output

    if folder_voting_protocols is None:
        raise Exception(f"Missing mandatory paramter: folder_voting_protocols")

    if base_template_folder is None:
        raise Exception(f"Missing mandatory paramter: base_template_folder")

    templates_provider: t_prov_by_name.TemplateProviderByName = template_by_name_txt.TemplateProviderFromTxtFile(
        base_template_folder=base_template_folder
    )

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

    postprocessing_output_configurations: list[translator_process.PostprocessingOutput] = [
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
