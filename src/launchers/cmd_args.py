import argparse

import src.configurations as configs

import src.utilities.utils as u

#


def get_args(logger: u.PrinterDebug = None):
    parser = argparse.ArgumentParser(
        description="CLI Parser for DAO-ML to Solidity Translator"
    )

    parser.add_argument(
        "-f", "--file",
        type=str,
        help="file path of the (XML?) DAO (Diagram, actually) You need to process",
        required=False
    )
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
    if args.file:
        cmd_configs.input_source_uri = args.file
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
