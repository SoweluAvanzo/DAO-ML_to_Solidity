import time

import src.pipeline.pipeline_item as pip


class PISleep(pip.PipelineItem):
    def __init__(self, key, dependencies=None, milliseconds=0):
        super().__init__(key, dependencies)
        self.milliseconds = milliseconds

    def run(self, inputs):
        time.sleep(self.milliseconds)
        return inputs

    def repr_inner(self):
        return """ "milliseconds": {0}""".format(str(self.milliseconds))
