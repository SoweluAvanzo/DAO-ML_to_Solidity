import src.input.input_base as ib
import src.pipeline.pipeline_item as pi

class FileInput(ib.InputBase):
    def __init__(self, pipeline_item_data: pi.PIData, filepath):
        super().__init__(pipeline_item_data)
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
        