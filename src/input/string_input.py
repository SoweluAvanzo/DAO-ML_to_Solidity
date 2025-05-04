import src.input.input_base as ib

class StringInput(ib.InputBase):
    '''
    Toy example: requires a list of strings and returns it, after storing them
    '''
    def __init__(self, key:str, predefined_string_list:list[str]):
        super().__init__(key)
        self.strings = predefined_string_list

    def get_input_as_iterable(self):
        return (s for s in self.strings)