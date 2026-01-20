import src.pipeline.pipeline_item as pi

import src.utilities.utils as u


class PIChainStoreReleaserBranching(pi.PipelineItem):
    """
    Used in the context of building a PIChained, it gather the value took as input ONCE
    and then returns it over and over, allowing to feed branches and resume them,
    therefore mutating a "chain" into a "mono-rooted-tree".
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )
        self.has_stored = False
        self.prev_key: str = None
        self.val = None

    def run(self, inputs):
        if self.has_stored:
            return self.val
        # get the value to store-and-pass
        v = self.get_ith_input(inputs, 0)
        self.print_msg(
            f"storing data from key ({self.get_dependencies()[0]}) of type: {type(v)}")
        self.val = v
        self.has_stored = True
        return v
