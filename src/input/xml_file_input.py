
from src.input.txt_file_input import TextFileInput
import src.pipeline.pipeline_item as pi

class TextFileInputXML(TextFileInput):
    def __init__(self, pipeline_item_data: pi.PIData, filepath=None, xml_version="1.0"):
        super().__init__(pipeline_item_data, filepath)
        self.xml_version = xml_version
        # TODO: altro?
        # 2025-04-06 nothing else
    