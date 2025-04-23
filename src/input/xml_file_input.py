
from src.input.txt_file_input import TextFileInput

class TextFileInputXML(TextFileInput):
    def __init__(self, filepath, xml_version="1.0"):
        super().__init__(filepath)
        self.xml_version = xml_version
        # TODO: altro?
        # 2025-04-06 nothing else
    