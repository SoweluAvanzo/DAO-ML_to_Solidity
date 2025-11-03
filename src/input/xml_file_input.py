
from src.input.txt_file_input import TextFileInput
import src.pipeline.pipeline_item as pi

DEFAULT_VERSION_XML_FILE_INPUT = "1.0"


class TextFileInputXML(TextFileInput):
    def __init__(self, pipeline_item_data: pi.PIData, filepath=None, xml_version=DEFAULT_VERSION_XML_FILE_INPUT, should_strip_line=False):
        super().__init__(pipeline_item_data, filepath, should_strip_line=should_strip_line)
        self.xml_version = DEFAULT_VERSION_XML_FILE_INPUT if xml_version is None else xml_version
        # TODO: altro?
        # 2025-04-06 nothing else
