
from src.input.file_input import FileInput
import src.pipeline.pipeline_item as pi

class TextFileInput(FileInput):
    def __init__(self, pipeline_item_data: pi.PIData, filepath=None):
        super().__init__(pipeline_item_data, filepath)
    
    def get_input_as_iterable(self):
        with self.open_file() as file:
            if file is None:
                yield None
            for line in file:
                yield line.strip()
