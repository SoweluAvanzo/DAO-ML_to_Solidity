import src.pipeline.pipeline_item as pi

class BaseOutput(pi.PipelineItem):
    def __init__(self, key:str, base_destination:str=None):
        super().__init__(key)
        self.base_destination = base_destination

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        return False

    def run(self, inputs):
        return self.to_output(inputs)
