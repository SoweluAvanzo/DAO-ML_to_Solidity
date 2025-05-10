import src.input.input_base as ib

class FileInput(ib.InputBase):
    def __init__(self, key:str, filepath):
        super().__init__(key)
        self.filepath = filepath
        self.file = None
    
    def open_file(self):
        if not (self.file is None): # TODO: how to check for closed files?
            return self.file
        try:
            f = open(self.filepath, 'r')
            self.file = f
            return f
        except Exception as err :
            print(err)
            return None                
        