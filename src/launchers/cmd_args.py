import argparse

import src.phases_builders.shared as pb_shared

import src.utilities.utils as u


class CmdConfigs:
    def __init__(self):
        self.input_source_type: pb_shared.PersistanceType = pb_shared.PersistanceType.FILE  # as default
        self.input_source_uri: str = None
        self.input_additional_data: dict = None
        self.output_source_type: pb_shared.PersistanceType = pb_shared.PersistanceType.FILE  # as default
        self.output_source_uri: str = None
        self.output_additional_data: dict = None
        #
        self.folder_voting_protocols: str = None
        self.base_template_folder: str = None

    def get_input_source_type(self) -> pb_shared.PersistanceType:
        return self.input_source_type

    def get_input_source_uri(self) -> str:
        """
        For a file, that's the path, otherwise it could be a URI or a Database's connection string
        """
        return self.input_source_uri

    def get_input_additional_data(self) -> dict:
        return self.input_additional_data

    def get_output_source_type(self) -> pb_shared.PersistanceType:
        return self.output_source_type

    def get_output_source_uri(self) -> str:
        """
        For a file, that's the path, otherwise it could be a URI or a Database's connection string
        """
        return self.output_source_uri

    def get_output_additional_data(self) -> dict:
        return self.output_additional_data

    def get_folder_voting_protocols(self) -> str:
        return self.folder_voting_protocols

    def get_base_template_folder(self) -> str:
        return self.base_template_folder

    """

    def get_(self) -> :
        return self.
    
    """

    def to_string(self):
        return f"""
        {type(self)}:
            input_source_type: {self.input_source_type.name},
            input_source_uri: {self.input_source_uri},
            input_additional_data: {self.input_additional_data},
            output_source_type: {self.output_source_type.name},
            output_source_uri: {self.output_source_uri},
            output_additional_data: {self.output_additional_data},
            folder_voting_protocols: {self.folder_voting_protocols},
            base_template_folder: {self.base_template_folder},
        """

    def __str__(self):
        return self.to_string()

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

    cmd = CmdConfigs()
    if args.file:
        cmd.input_source_uri = args.file
    if args.output:
        cmd.output_source_uri = args.output
    if args.templates_folder:
        cmd.base_template_folder = args.templates_folder
    if "folder_voting_protocols" in args and args.folder_voting_protocols:
        cmd.folder_voting_protocols = args.folder_voting_protocols
    elif args.folder_voting:
        cmd.folder_voting_protocols = args.folder_voting

    if logger:
        logger.print_msg(cmd.to_string())

    return cmd
