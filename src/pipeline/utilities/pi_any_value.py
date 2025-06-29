import src.pipeline.pipeline_item as pi

class PIAnyValue(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, val=None):
        super().__init__(pipeline_item_data)
        self.val = val

    def run(self, inputs):
        print("ANY VALUE")
        print(self.val)
        return self.val

    def repr_inner(self):
        return \
            """
                "val": {0}
            """.format(repr(self.val) if self.val is not None else 'null')
