import src.pipeline.pipeline_item as pi

class PIInputToArray(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def run(self, inputs):
        return [inputs[dep] for dep in self.get_dependencies()]

    def repr_inner(self):
        return ""
