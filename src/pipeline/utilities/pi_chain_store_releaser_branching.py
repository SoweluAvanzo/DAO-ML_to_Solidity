import src.pipeline.pipeline_item as pi


class PIChainStoreReleaserBranching(pi.PipelineItem):
    """
    Used inthe context of building a PIChained, it gather the value took as input ONCE
    and then returns it over and over, allowing to feed branches and resume them,
    therefore mutating a "chain" into a "mono-rooted-tree".
    """

    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)
        self.has_stored = False
        self.prev_key: str = None
        self.val = None

    def run(self, inputs):
        if self.has_stored:
            return self.val
        # get the value to store-and-pass
        v = self.get_ith_input(inputs, 0)
        self.val = v
        self.has_stored = True
        return v
