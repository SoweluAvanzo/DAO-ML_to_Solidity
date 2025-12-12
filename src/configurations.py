
import src.phases_builders.shared as pb_shared
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o

import src.utilities.utils as u
import src.utilities.stringable_jsonable as s_j


class InputConfigs(s_j.StringableJsonable):
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


class ModelGenerationConfig(s_j.StringableJsonable):
    def __init__(self, json_data: dict = None):
        self.xml_schema_folder: str = "xsd" if (json_data is None) or ("xml_schema_folder" not in json_data) \
            else json_data["xml_schema_folder"]
        self.xml_schema_filename: str = "XSD_DAO_ML" if (json_data is None) or ("xml_schema_filename" not in json_data) \
            else json_data["xml_schema_filename"]
        self.xml_schema_extension: str = "xsd" if (json_data is None) or ("xml_schema_extension" not in json_data) \
            else json_data["xml_schema_extension"]


class PostprocessingConfigs(s_j.StringableJsonable):
    def __init__(self, json_data: dict = None):
        self.post_processing_transformation: pb_pp.PostProcessingTransformation = None if (json_data is None) or ("post_processing_transformation" not in json_data) \
            else json_data["post_processing_transformation"]
        self.version_translator: str = "1.0.0" if (json_data is None) or ("version_translator" not in json_data) \
            else json_data["version_translator"]
        self.version_translation_target: str = None if (json_data is None) or ("version_translation_target" not in json_data) \
            else json_data["version_translation_target"]
        # specific ones
        self.translator_solidity_subtype: str = None if (json_data is None) or ("translator_solidity_subtype" not in json_data) \
            else json_data["translator_solidity_subtype"]
        self.indent_json = 2 if (json_data is None) or ("indent_json" not in json_data) \
            else json_data["indent_json"]


class OutputConfigs(s_j.StringableJsonable):
    def __init__(self, json_data: dict = None):
        self.output_type: pb_o.OutputType =  \
            pb_o.OutputType.JINJA_COMPILATION if (json_data is None) or ("output_type" not in json_data) \
            else json_data["output_type"]
        self.persistance_type: pb_shared.PersistanceType = \
            pb_shared.PersistanceType.FILE if (json_data is None) or ("persistance_type" not in json_data) \
            else json_data["persistance_type"]
        # file-specific info
        self.folder_output_path_base_file: str = None if (json_data is None) or ("folder_output_path_base_file" not in json_data) \
            else json_data["folder_output_path_base_file"]

#


class PostprocessingOutputPairConfigs(s_j.StringableJsonable):
    def __init__(self,
                 json_data: dict = None,
                 postprocessingConfigs: PostprocessingConfigs = None,
                 outputConfigs: OutputConfigs = None,
                 ):
        self.postprocessingConfigs = postprocessingConfigs
        self.outputConfigs = outputConfigs


class TranslatorConfigs(s_j.StringableJsonable):
    def __init__(self,
                 json_data: dict = None,
                 external_unique_key_producer: pb_shared.KeyUniqueProducer = None
                 ):
        self.external_unique_key_producer = pb_shared.KeyUniqueProducerSimpleSequential() \
            if external_unique_key_producer is None \
            else external_unique_key_producer
        self.model_format: pb_shared.ModelPersistanceFormat = pb_shared.ModelPersistanceFormat.XML \
            if (json_data is None) or ("model_format" not in json_data) \
            else json_data["model_format"]
        # input
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
