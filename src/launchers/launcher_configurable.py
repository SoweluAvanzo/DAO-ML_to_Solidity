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

# import src.launchers.cmd_args as cmd_args
import src.configurations as configs

import src.files.file_utils as files
import src.utilities.utils as u
import src.utilities.errors as e_c


def non_none(what, name):
    if what is None:
        raise Exception(f"Missing mandatory paramter: {name}")


def prepare_input(
    config: configs.TranslatorConfigs,
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
        case pb_shared.PersistanceType.FILE:
            file_extension: str = config.input_config.file_extension \
                if config.input_config.file_extension is not None else \
                input_format.value
            fbf: str = config.input_config.file_base_folder
            if fbf is None:
                fbf = consts_t.DEFAULT_BASE_FOLDER_INPUT
            source_fullpath = files.concat_folder_filename(
                fbf,
                f"{source_uri}.{file_extension}"
            )
            match(input_format):
                case pb_shared.ModelPersistanceFormat.XML:
                    non_none(config.input_config.xml_version,
                             "input_config.xml_version")
                    input_additional_data = pb_i_f.FileXMLAdditionalDataSubPhase(
                        filepath=source_fullpath,
                        xml_version=config.input_config.xml_version,
                        should_strip_line=True
                    )
                case pb_shared.ModelPersistanceFormat.JSON:
                    input_additional_data = pb_i_f.FileJSONAdditionalDataSubPhase(
                        filepath=source_fullpath,
                        should_strip_line=True
                    )
                case _:
                    raise Exception(
                        e_c.ERROR_TEXT__NOT_IMPLEMENTED + ": " + input_format.name)
        case pb_shared.PersistanceType.DATABASE:
            # TODO: upon future developments, make use of the source_uri
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + pb_shared.PersistanceType.DATABASE.name)
        case _:
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + input_persistance_type.name)
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
        case pb_shared.ModelPersistanceFormat.XML:
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
        case pb_shared.ModelPersistanceFormat.JSON:
            return translator_process.ModelConfiguration(
                pb_shared.ModelPersistanceFormat.JSON,
                additional_data=pb_m_g.ModelJSONGeneratordData()
            )
        case _:
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + input_format.name)


def additional_data_from_PostProcessingTransformation(
    config: configs.TranslatorConfigs,
    ppc: configs.PostprocessingConfigs,
    templates_provider: t_prov_by_name.TemplateProviderByName,
    logger: u.PrinterDebug = None
) -> pb_pp.AdditionalDataPostProcessing:
    base_template_folder: str = ppc.base_template_folder

    add_data: pb_pp.AdditionalDataPostProcessing = None
    match(ppc.post_processing_transformation):
        case pb_pp.PostProcessingTransformation.SOLIDITY:
            non_none(base_template_folder, "base_template_folder")
            folder_voting_protocols: str = ppc.folder_voting_protocols_solidity
            non_none(folder_voting_protocols, "folder_voting_protocols")
            non_none(ppc.version_translator, "ppc.version_translator")
            non_none(ppc.translator_solidity_subtype,
                     "ppc.translator_solidity_subtype")
            non_none(ppc.version_translation_target,
                     "ppc.version_translation_target")
            add_data = pb_pp.AdditionalDataSolidity(  # TODO 05-12-2025 PUT ALL PARAMETERS IN THE CONFIGURATION
                folder_voting_protocols,
                templates_provider=templates_provider,
                folder_templates=base_template_folder,
                version_translator=ppc.version_translator,
                translator_solidity_subtype=ppc.translator_solidity_subtype,
                version_translation_target=ppc.version_translation_target
            )
        case pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS:
            non_none(base_template_folder, "base_template_folder")
            non_none(ppc.version_translator, "ppc.version_translator")
            non_none(ppc.version_translation_target,
                     "ppc.version_translation_target")
            add_data = pb_pp.AdditionalDataSolidityHardhatTests(
                templates_provider=templates_provider,
                folder_templates=base_template_folder,
                version_translator=ppc.version_translator,
                version_translation_target=ppc.version_translation_target
            )
        case pb_pp.PostProcessingTransformation.ASM:
            non_none(base_template_folder, "base_template_folder")
            non_none(ppc.version_translator, "ppc.version_translator")
            non_none(ppc.version_translation_target,
                     "ppc.version_translation_target")
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
    post_processing_transformation: pb_pp.PostProcessingTransformation,
    logger: u.PrinterDebug = None
) -> pb_o.AdditionalDataOutput:
    add_data: pb_o.AdditionalDataOutput = None
    non_none(post_processing_transformation, "post_processing_transformation")
    non_none(oc.persistance_type, "oc.persistance_type")
    non_none(oc.output_type, "oc.output_type")
    non_none(oc.output_uri,
             "oc.output_uri")
    match(oc.persistance_type):
        case pb_shared.PersistanceType.FILE:
            match(oc.output_type):
                case pb_o.OutputType.JINJA_COMPILATION:
                    non_none(oc.output_uri,
                             "output_uri")
                    add_data = pb_o.AdditionalDataFileJinja(
                        folder_output_path_base=oc.output_uri,
                        postprocessing_producing_output=post_processing_transformation

                    )
                case pb_o.OutputType.PLAIN_STRING:
                    non_none(oc.output_uri,
                             "output_uri")
                    add_data = pb_o.AdditionalDataFileString(
                        folder_output_path_base=oc.output_uri,
                        postprocessing_producing_output=post_processing_transformation
                    )
        case pb_shared.PersistanceType.DATABASE:
            raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                            ": " + oc.persistance_type.name)
    return add_data


def prepare_ppt_o(
    config: configs.TranslatorConfigs,
    logger: u.PrinterDebug = None
) -> list[translator_process.PostprocessingOutput]:
    # recycle the instances by base pat
    templates_provider_by_base_path: dict[str,
                                          t_prov_by_name.TemplateProviderByName] = {}

    def new_template_provider(base_path: str):
        if base_path is None:
            return None
        if base_path in templates_provider_by_base_path:
            return templates_provider_by_base_path[base_path]
        templates_provider = template_by_name_txt.TemplateProviderFromTxtFile(
            base_template_folder=base_path
        )  # TODO: find a way to  generalize it
        templates_provider_by_base_path[base_path] = templates_provider
        return templates_provider

    return [
        translator_process.PostprocessingOutput(
            translator_process.PostprocessingConfiguration(
                ppopc.postprocessingConfigs.post_processing_transformation,
                additional_data=additional_data_from_PostProcessingTransformation(
                    config,
                    ppopc.postprocessingConfigs,
                    new_template_provider(
                        ppopc.postprocessingConfigs.base_template_folder),
                    logger=logger
                )
            ),
            translator_process.OutputConfiguration(
                ppopc.outputConfigs.persistance_type,
                ppopc.outputConfigs.output_type,
                additional_data=additional_data_from_Output(
                    config,
                    ppopc.outputConfigs,
                    ppopc.postprocessingConfigs.post_processing_transformation,
                    logger=logger
                )
            ),
            additional_data=None
        )
        for ppopc in config.all_postprocessingOutputPairConfigs
    ]

#


class TranslatorAndConfigurations:
    def __init__(self,
                 translator_process: translator_process.TranslatorProcess,
                 translation_configuration: translator_process.TranslationConfiguration
                 ):
        self.translator_process = translator_process
        self.translation_configuration = translation_configuration


def new_translator_process(
    config: configs.TranslatorConfigs,
    instantiate_new_translator_process=True,
    logger: u.PrinterDebug = None
) -> TranslatorAndConfigurations:

    # 1) Input
    input_configuration: translator_process.InputConfiguration = prepare_input(
        config,
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

    non_none(config.all_postprocessingOutputPairConfigs,
             "config.all_postprocessingOutputPairConfigs")

    postprocessing_output_configurations: list[translator_process.PostprocessingOutput] = prepare_ppt_o(
        config,
        logger=logger
    )

    # THE TRANSLATOR PROCESS
    return TranslatorAndConfigurations(
        translator_process.TranslatorProcess(
            printer_debug=logger
        ) if instantiate_new_translator_process else None,
        translator_process.TranslationConfiguration(
            input_configuration,
            model_configuration,
            postprocessing_output_configurations,
            external_unique_key_producer=config.external_unique_key_producer,
            is_resetting_cache=False
        )
    )
