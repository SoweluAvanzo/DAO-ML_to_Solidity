import src.pipeline.pipeline_item as pi

class PIAddMult(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, scalar=0, is_addition=True):
        super().__init__(pipeline_item_data)
        self.scalar = scalar
        self.is_addition = is_addition

    def run(self, inputs: dict):
        if self.is_addition:
            partial = self.scalar
            for dep in self.get_dependencies():
                input_data = inputs[dep] if dep in inputs else 0
                partial += input_data
            return partial
        return self.scalar * inputs[self.get_dependencies()[0]]  # input['value'] if 'value' in input else 0

    def repr_inner(self):
        return \
            """
                "is_addition": {0},
                "scalar": {1}
            """.format('true' if self.is_addition else 'false', self.scalar)
