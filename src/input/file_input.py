import src.input.input_base as ib
import src.pipeline.pipeline_item as pi

class FileInput(ib.InputBase):
    def __init__(self, pipeline_item_data: pi.PIData, filepath=None):
        super().__init__(pipeline_item_data)
        self.filepath = filepath
        self.file = None
    
    def open_file(self):
        if not (self.file is None): # TODO: how to check for closed files?
            return self.file
        try:
            file_path = self.filepath if self.input_for_run is None or len(self.get_dependencies()) == 0 else self.get_ith_input(self.input_for_run, 0)
            f = open(file_path, 'r')
            self.file = f
            return f
        except Exception as err :
            print(err)
            return None                
        