import src.pipeline.pipeline_item as pi


class PIChainStoreReleaserBranching(pi.PipelineItem):
    """
    Used inthe context of building a PIChained, it gather the value took as input ONCE
    and then returns it over and over, allowing to feed branches and resume them
    """

    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)
        self.has_stored = False
        self.prev_key: str = None
        self.val = None

    def run(self, inputs):
        if self.has_stored:
            return self.val
        for k, v in inputs.items():
            self.has_stored = True
            self.prev_key = k
            self.val = v
            return v
