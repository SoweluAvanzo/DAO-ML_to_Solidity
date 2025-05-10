import src.pipeline.pipeline_item as pi

class InputBase(pi.PipelineItem):
    def __init__(self, key:str):
        super().__init__(key)

    def get_input(self) -> list:
        '''
        Returns a list of data to be taken as input (or, similarly, an iterable).
        Each row should be a String.
        Could consume the result from #get_input_as_iterable(self) 
        '''
        input_iterable = self.get_input_as_iterable()
        if input_iterable is None:
            return None
        return [x for x in input_iterable]

    def get_input_as_iterable(self):
        '''
        Returns the input as a stream, an iterable of strings
        '''
        return None
        
    def run(self, inputs:dict) -> any:
        return self.get_input()
