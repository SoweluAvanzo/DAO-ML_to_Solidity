import src.pipeline.pipeline_item as pi


class BaseValidator(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData ):
        super().__init__(pipeline_item_data)

    def validate(self, input:dict) -> bool:
        return False
    
    def run(self, inputs: dict):
        return self.validate(inputs[self.get_dependencies()[0]])
