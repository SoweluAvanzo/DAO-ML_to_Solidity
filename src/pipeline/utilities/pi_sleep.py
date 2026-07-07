import time

import src.pipeline.pipeline_item as pi

class PISleep(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, milliseconds=0):
        super().__init__(pipeline_item_data)
        self.milliseconds = milliseconds

    def run(self, inputs):
        time.sleep(self.milliseconds)
        return inputs

    def repr_inner(self):
        return \
            """
                "milliseconds": {0}
            """.format(str(self.milliseconds))
