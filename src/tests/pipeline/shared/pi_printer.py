import src.pipeline.pipeline_item as pip


class PIPrinter(pip.PipelineItem):
    def __init__(self, key, dependencies=None, text="", from_input=False):
        super().__init__(key, dependencies)
        self.text = text
        self.from_input = from_input

    def run(self, inputs):
        t = inputs[self.dependencies[0]] if self.from_input else self.text
        print(f"printing: {t}")
        return inputs

    def repr_inner(self):
        return """ "text":"{0}" """.format(self.text)
