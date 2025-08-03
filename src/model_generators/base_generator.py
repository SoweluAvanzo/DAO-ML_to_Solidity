import src.pipeline.pipeline_item as pi

class BaseGenerator(pi.PipelineItem):
    """
    Works as a pre-processing
    """
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def generate(self, additional_input=None):
        return None

    def run(self, inputs):
        return self.generate(self.get_ith_input(inputs, 0))
