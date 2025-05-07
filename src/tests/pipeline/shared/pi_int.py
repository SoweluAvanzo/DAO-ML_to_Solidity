import src.pipeline.pipeline_item as pip


class PIInt(pip.PipelineItem):
    def __init__(self, key, dependencies=None, val=0):
        super().__init__(key, dependencies)
        self.val = val

    def run(self, inputs):
        return self.val

    def repr_inner(self):
        return """ "val": {0}""".format(str(self.val))
