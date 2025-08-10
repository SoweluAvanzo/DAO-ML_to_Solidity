import src.input.input_base as ib
import src.pipeline.pipeline_item as pi
from contextlib import contextmanager

def open_file(name):
    f = open(name, 'w')
    

class FileInput(ib.InputBase):
    def __init__(self, pipeline_item_data: pi.PIData, filepath=None):
        super().__init__(pipeline_item_data)
        self.filepath = filepath
    
    @contextmanager
    def open_file(self):
        try:
            file_path = self.filepath if self.inputs_from_run is None or len(self.get_dependencies()) == 0 else self.get_ith_input(self.inputs_from_run, 0)
            f = open(file_path, 'r')
            try:
                yield f
            finally:
                f.close()
        except Exception as err :
            print(err)
            return None                
        