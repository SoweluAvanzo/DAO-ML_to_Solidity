
from src.input.file_input import FileInput

class TextFileInput(FileInput):
    def __init__(self, filepath):
        super().__init__(filepath)
    
    def get_input_as_iterable(self):
        file = self.open_file()
        for line in file:
            yield line.strip()
