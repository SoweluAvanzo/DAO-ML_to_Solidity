import src.translator_process as translator_process

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

import src.utilities.utils as u
import src.files.file_utils as files
# import src.utilities.logger_debug as logger_debug

logger = u.PrinterDebug()  # logger_debug.LoggerDebug(class_name=__name__)
external_unique_key_producer: pb_shared.KeyUniqueProducer = pb_shared.KeyUniqueProducerSimpleSequential()

# TODO setup the ...

# 1) Input

source_filename = "Travelhive_final_model"
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

folder_voting_protocols = consts_t.DEFAULT_FOLDER_TEMPLATES_VOTING_PROTOCOL
base_template_folder = consts_t.DEFAULT_BASE_FOLDER_TEMPLATES
templates_provider: t_prov_by_name.TemplateProviderByName = template_by_name_txt.TemplateProviderFromTxtFile(
    base_template_folder=base_template_folder
)

folder_output = files.concat_folder_filename('.', 'out')

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
        translator_process.OutputConfiguration(
            pb_shared.PersistanceType.FILE,
            pb_o.OutputType.JINJA_COMPILATION,
            additional_data=pb_o.AdditionalDataFileJinja(
                folder_output
            )
        )
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

logger.print_msg("START\n\n")
tp.translate()
logger.print_msg("\n\nEND")
