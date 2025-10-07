import src.pipeline.pipeline_item as pi
import src.pipeline.utilities.pi_any_value as pi_val

class PIStr(pi_val.PIAnyValue):
    def __init__(self, pipeline_item_data: pi.PIData, val=""):
        super().__init__(pipeline_item_data, val)

    def run(self, inputs):
        return self.val

