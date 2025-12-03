
import src.phases_builders.shared as pb_shared
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o

import src.utilities.utils as u


class InputConfigs(u.ToStringable):
    def __init__(self, json_data: dict = None):
        self.persistance_type: pb_shared.PersistanceType = \
            pb_shared.PersistanceType.FILE if (json_data is None) or ("persistance_type" not in json_data) \
            else json_data["persistance_type"]
        self.source_uri: str = None if (json_data is None) or ("source_uri" not in json_data) \
            else json_data["source_uri"]
        # optional
        self.additional_data: dict = None if (json_data is None) or ("additional_data" not in json_data) \
            else json_data["additional_data"]
        # ... input-specifics
        self.file_base_folder: str = None if (json_data is None) or ("file_base_folder" not in json_data) \
            else json_data["file_base_folder"]
        self.file_extension: str = "xml" if (json_data is None) or ("file_extension" not in json_data) \
            else json_data["file_extension"]
        self.xml_version: str = "1.0.0" if (json_data is None) or ("xml_version" not in json_data) \
            else json_data["xml_version"]


class ModelGenerationConfig(u.ToStringable):
    def __init__(self, json_data: dict = None):
        self.xml_schema_folder: str = "xsd" if (json_data is None) or ("xml_schema_folder" not in json_data) \
            else json_data["xml_schema_folder"]
        self.xml_schema_filename: str = "XSD_DAO_ML" if (json_data is None) or ("xml_schema_filename" not in json_data) \
            else json_data["xml_schema_filename"]
        self.xml_schema_extension: str = "xsd" if (json_data is None) or ("xml_schema_extension" not in json_data) \
            else json_data["xml_schema_extension"]


class PostprocessingConfigs(u.ToStringable):
    def __init__(self, json_data: dict = None):
        pass  # TODO


class OutputConfigs(u.ToStringable):
    def __init__(self, json_data: dict = None):
        pass  # TODO

#


class PostprocessingOutputPairConfigs(u.ToStringable):
    def __init__(self,
                 json_data: dict = None,
                 postprocessingConfigs: PostprocessingConfigs = None,
                 outputConfigs: OutputConfigs = None,
                 ):
        self.postprocessingConfigs = postprocessingConfigs
        self.outputConfigs = outputConfigs


class TranslatorConfigs(u.ToStringable):
    def __init__(self, json_data: dict = None):
        self.model_format: pb_shared.ModelPersistanceFormat = pb_shared.ModelPersistanceFormat.XML \
            if (json_data is None) or ("model_format" not in json_data) \
            else json_data["model_format"]
        self.input_config = InputConfigs(
            json_data=None
            if (json_data is None) or ("input_config" not in json_data)
            else json_data["input_config"]
        )
        self.model_gen_config = ModelGenerationConfig(
            json_data=None
            if (json_data is None) or ("model_gen_config" not in json_data)
            else json_data["model_gen_config"]
        )

        # output (?)
        self.all_postprocessingOutputPairConfigs: list[PostprocessingOutputPairConfigs] = [
        ]
        self.output_persistance_type: pb_shared.PersistanceType = pb_shared.PersistanceType.FILE  # as default
        self.output_source_uri: str = None
        self.output_additional_data: dict = None
        # other
        self.folder_voting_protocols: str = None
        self.base_template_folder: str = None

    def addPostprocessingOutputPairConfigs(self, postprocessingOutputPairConfigs: PostprocessingOutputPairConfigs):
        self.all_postprocessingOutputPairConfigs.append(
            postprocessingOutputPairConfigs)

    def __str__(self):
        return self.to_string()
