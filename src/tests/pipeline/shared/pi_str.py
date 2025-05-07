import src.pipeline.pipeline_item as pip


class PIStr(pip.PipelineItem):
    def __init__(self, key, dependencies=None, val=""):
        super().__init__(key, dependencies)
        self.val = val

    def run(self, inputs):
        return self.val

    def repr_inner(self):
        return """ "val": {0}""".format(self.val)
