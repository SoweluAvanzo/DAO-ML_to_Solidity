import src.pipeline.pipeline_item as pi

class ValidatorBase(pi.PipelineItem):
    def __init__(self, key:str):
        super().__init__(key)

    def validate(self, input:any) -> bool:
        return False
    
    def run(self, inputs):
        return self.validate(inputs)
