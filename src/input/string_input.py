import src.input.input_base as ib
import src.pipeline.pipeline_item as pi

class StringInput(ib.InputBase):
    '''
    Toy example: requires a list of strings and returns it, after storing them
    '''
    def __init__(self, pipeline_item_data: pi.PIData, predefined_string_list:list):
        super().__init__(pipeline_item_data)
        self.strings = predefined_string_list

    def get_input_as_iterable(self):
        return (s for s in self.strings)