import src.pipeline.pipeline_item as pi

class BaseGenerator(pi.PipelineItem):
    def __init__(self, key:str, dependencies:list[str]=None):
        super().__init__(key, dependencies)
    

    def generate(self, additional_input=None):
        return None

    def run(self, inputs):
        return self.generate(inputs)
