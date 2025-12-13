import argparse

import src.configurations as configs

import src.phases_builders.shared as pb_shared
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o

import src.utilities.extended_enum as ex_enum
import src.utilities.utils as u
import src.utilities.errors as e_c


def __tbf_combos():
    # leads to 16 combinations
    t_f_b = ["base", "template", "folder"]
    t_f_b_extended = [*t_f_b, "templates"]  # the plural
    seps = ["-", "_"]
    # the result was pre-computed, so the lenght is known in advance
    tbfc = [None] * (8 * len(seps))
    i = 0
    for a in t_f_b_extended:
        for b in t_f_b:
            for c in t_f_b:
                if (a != b) and (a != c) and (b != c) \
                        and (not a.startswith(b)) and (not a.startswith(c)):
                    combination = [a, b, c]
                    for sep in seps:
                        tbfc[i] = f"--{sep.join(combination)}"
                        i += 1
    tbfc.sort()
    return tbfc


global templates_base_folder_combinations
templates_base_folder_combinations = __tbf_combos()


def __enum_case_insensitive_list(e: type[ex_enum.ExtendedEnum]):
    s = set(e.list())
    for k in list(map(lambda c: c.name, e)):
        s.add(k)
    return list(s)


def __cj(l: list):
    ", ".join(l)


def __enum_comma_list(e: type[ex_enum.ExtendedEnum]):
    return __cj(__enum_case_insensitive_list(e))

#


def get_args(logger: u.PrinterDebug = None):
    parser = argparse.ArgumentParser(
        description="CLI Parser for DAO-ML Translator"
    )

    # input

    parser.add_argument(
        "-f", "--file",
        "--file-name", "--file_name",
        "--file-path", "--file_path",
        type=str,
        help="file name/path of the (XML?) DAO (Diagram, actually) You need to process",
        required=False
    )
    parser.add_argument(
        "-if", "--input_base_folder", "--input-base-folder", "--input-folder", "--input_folder",
        type=str,
        help="folder path acting as the starting point for all inputs",
        required=False
    )
    l_if = __enum_case_insensitive_list(pb_shared.ModelPersistanceFormat)
    parser.add_argument(
        "-i_f", "--input_format",
        "--input-format",
        type=str,
        help=f"Format of the input in which the model has been encoded; currently the accepted values are the following ones: {__cj(l_if)}",
        choices=l_if,
        required=False
    )
    parser.add_argument(
        "-fie", "--file_input_extension", "--file-input-extension",
        type=str,
        help="Extension of the input file",
        required=False
    )
    l_pt = __enum_case_insensitive_list(pb_shared.PersistanceType)
    parser.add_argument(
        "-pt", "--persistance_type", "--persistance-type",
        type=str,
        help=f"Types of persistance units to read the model from or to save the produced output; currently it accepts: {__enum_comma_list(pb_shared.PersistanceType)}",
        choices=l_pt,
        required=False
    )
    # ... xml
    parser.add_argument(
        "-xml_v", "--xml_version", "--xml-version",
        type=str,
        help="Version of the XML standard (as input)",
        required=False
    )
    # TODO: add Databse URI / API endpoint parameters

    # model generation
    # ... xml, currently (2025-12-12) no other formats have some configurations
    parser.add_argument(
        "--xml_schema_folder", "--xml-schema-folder",
        type=str,
        help="Folder path holding the XML schema file",
        required=False
    )
    parser.add_argument(
        "--xml_schema_filename", "--xml-schema-filename",
        type=str,
        help="Folder path holding the XML schema file",
        required=False
    )
    parser.add_argument(
        "--xml_schema_extension", "--xml-schema-extension",
        type=str,
        help="Extension of the XML schema file",
        required=False
    )

    # postprocessing

    ppt_options = pb_pp.PostProcessingTransformation.list()
    parser.add_argument(
        "-pp", "-ppt",
        "--post_processing", "--post_processing_transformation",
        "--post-processing", "--post-processing-transformation",
        type=str,
        help=f"Post-processing phase, one(+) of the following: [{', '.join(ppt_options)}]",
        required=True,
        choices=ppt_options,
        action="append"
    )
    parser.add_argument(
        "-vt", "-vtr", "--version_translator", "--version-translator",
        type=str,
        help="Version of the translator. Defaults to '1.0.0'",
        default="1.0.0",
        required=False
    )
    parser.add_argument(
        "-vta", "-vtt",
        "--version_translation_target",  "--version-translation-target",
        "--version_translation",  "--version-translation",
        "--version_target",  "--version-target",
        type=str,
        help="Version of what is being produced as output; multiple evolutions might co-exists (in futrher developments). Defaults to '1.0.0'",
        default="1.0.0",
        required=False
    )
    parser.add_argument(
        "-tf", "--templates-folder", "--templates_folder", "--template-folder", "--template_folder",
        "-ft", "--folder_templates", "--folder-templates", "--folder_template", "--folder-template",
        "-tfb", "-btf", "-ftb",
        *templates_base_folder_combinations,
        type=str,
        help="folder (base) path for all template files; could be an absolute path or a relative path.",
        required=False
    )
    # json
    parser.add_argument(
        "-tss", "--translator_solidity_subtype", "--translator-solidity-subtype",
        help="Indentation",
        default="1.0.0",
        required=False
    )
    # ... solidity
    parser.add_argument(
        "-ij", "--indent_json", "--indent-json",
        help="Indentation for JSON dumping",
        default=None,
        required=False
    )

    # output

    parser.add_argument(
        "-of", "--output", "--output-folder", "--output_folder",
        type=str,
        help="folder path for all ouputs",
        required=False
    )
    parser.add_argument(
        "-fvp", "--folder-voting", "--folder-voting-protocols", "--folder_voting", "--folder_voting_protocols",
        type=str,
        help="folder (base) path for all template files; could be an absolute path or a relative path.",
        required=False
    )

    # ---------

    args = parser.parse_args()

    cmd_configs = configs.TranslatorConfigs()

    # input

    if args.persistance_type:
        match(args.persistance_type):
            case pb_shared.PersistanceType.DATABASE.value:
                raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED + ": Database")
            case pb_shared.PersistanceType.FILE.value:
                pass  # see below
            case _:
                raise Exception(
                    f"{e_c.ERROR_TEXT__NOT_IMPLEMENTED} : {args.persistance_type}")

    if args.file:
        cmd_configs.input_config.source_uri = args.file
        cmd_configs.input_config.persistance_type = pb_shared.PersistanceType.FILE
        if args.input_base_folder:
            cmd_configs.input_config.file_base_folder = args.input_base_folder
    if args.input_format:
        match(args.input_format):
            case pb_shared.ModelPersistanceFormat.JSON.value:
                cmd_configs.model_format = pb_shared.ModelPersistanceFormat.JSON
                cmd_configs.input_config.file_extension = pb_shared.ModelPersistanceFormat.JSON.value \
                    if args.file_input_extension is None else args.file_input_extension
            case _:  # every other cases
                cmd_configs.model_format = pb_shared.ModelPersistanceFormat.XML
                cmd_configs.input_config.file_extension = pb_shared.ModelPersistanceFormat.XML.value \
                    if args.file_input_extension is None else args.file_input_extension
                if args.xml_version:
                    cmd_configs.input_config.xml_version = args.xml_version

    # model
    if cmd_configs.model_format == pb_shared.ModelPersistanceFormat.XML:
        if args.xml_schema_folder:
            cmd_configs.model_gen_config.xml_schema_folder = args.xml_schema_folder
        else:
            raise Exception(
                f"XML has been choosen as the input / model generation format, but no xml_schema_folder has been set")
        if args.xml_schema_filename:
            cmd_configs.model_gen_config.xml_schema_filename = args.xml_schema_filename
        else:
            raise Exception(
                f"XML has been choosen as the input / model generation format, but no xml_schema_filename has been set")
        if args.xml_schema_extension:
            cmd_configs.model_gen_config.xml_schema_extension = args.xml_schema_extension
        else:
            raise Exception(
                f"XML has been choosen as the input / model generation format, but no xml_schema_extension has been set")

    # postprocessing & output

    if args.output:
        cmd_configs.output_source_uri = args.output
    if args.templates_folder:
        cmd_configs.base_template_folder = args.templates_folder
    if "folder_voting_protocols" in args and args.folder_voting_protocols:
        cmd_configs.folder_voting_protocols = args.folder_voting_protocols
    elif args.folder_voting:
        cmd_configs.folder_voting_protocols = args.folder_voting

    if logger:
        logger.print_msg(cmd_configs.to_string())

    return cmd_configs
