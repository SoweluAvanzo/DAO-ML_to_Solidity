import src.pipeline.pipeline_item as pi

class BaseOutput(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, base_destination:str):
        super().__init__(pipeline_item_data)
        self.base_destination = base_destination

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        return False

    def run(self, inputs:dict):
        return self.to_output(inputs)

    def repr_inner(self):
        return \
        """
            {0},
            "base_destination": {1}
        """.format( \
            super().repr_inner(), \
            self.base_destination
        )
       
    