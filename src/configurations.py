
import src.phases_builders.shared as pb_shared


class TranslatorConfigs:
    def __init__(self):
        # input
        self.input_source_type: pb_shared.PersistanceType = pb_shared.PersistanceType.FILE  # as default
        self.input_source_uri: str = None
        self.input_additional_data: dict = None
        # ... input-specifics
        self.xml_version: str = "1.0.0"

        # output (?)
        self.output_source_type: pb_shared.PersistanceType = pb_shared.PersistanceType.FILE  # as default
        self.output_source_uri: str = None
        self.output_additional_data: dict = None
        # other
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
