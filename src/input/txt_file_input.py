
from src.input.file_input import FileInput
import src.pipeline.pipeline_item as pi


class TextFileInput(FileInput):
    def __init__(self, pipeline_item_data: pi.PIData, filepath=None, should_strip_line=False):
        super().__init__(pipeline_item_data, filepath)
        self.should_strip_line = should_strip_line

    def get_input_as_iterable(self):
        with self.open_file() as file:
            f = file
            if f is None:
                print(f" FILE IS NONE: {self.filepath}")
                yield None
            else:
                for line in f:
                    yield line.strip() if self.should_strip_line else line
