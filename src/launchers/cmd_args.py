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

    parser.add_argument(
        "-f", "--file",
        "--file-name", "--file_name",
        "--file-path", "--file_path",
        type=str,
        help="file name/path of the (XML?) DAO (Diagram, actually) You need to process",
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
        "-xml_v", "--xml_version",
        type=str,
        help="Version of the XML standard",
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
    # TODO: add Databse URI / API endpoint parameters

    parser.add_argument(
        "-of", "--output", "--output-folder", "--output_folder",
        type=str,
        help="folder path for all ouputs",
        required=False
    )
    parser.add_argument(
        "-tf", "--templates-folder", "--templates_folder", "--template-folder", "--template_sfolder",
        "-tfb", "--templates-folder-base", "--templates_folder_base", "--template-folder-base", "--template_sfolder_base",
        type=str,
        help="folder (base) path for all template files; could be an absolute path or a relative path.",
        required=False
    )
    parser.add_argument(
        "-fvp", "--folder-voting", "--folder-voting-protocols", "--folder_voting", "--folder_voting_protocols",
        type=str,
        help="folder (base) path for all template files; could be an absolute path or a relative path.",
        required=False
    )

    args = parser.parse_args()

    cmd_configs = configs.TranslatorConfigs()
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
        if args.input_format:
            match(args.input_format):
                case pb_shared.ModelPersistanceFormat.JSON.value:
                    cmd_configs.input_config.format = pb_shared.ModelPersistanceFormat.JSON
                case _:  # every other cases
                    cmd_configs.input_config.format = pb_shared.ModelPersistanceFormat.XML

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
