import src.input.input_base as ib

class FileInput(ib.InputBase):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.file = None
    
    def open_file(self):
        if self.file is not None: # TODO: how to check for closed files?
            return self.file
        try:
            return open(self.filepath, 'r')
        except Exception as err :
            print(err)
            return None
        