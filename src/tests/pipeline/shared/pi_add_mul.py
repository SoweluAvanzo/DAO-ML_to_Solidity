import src.pipeline.pipeline_item as pi


class PIAddMult(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, scalar: int = None, is_addition=True):
        super().__init__(pipeline_item_data)
        self.scalar = scalar
        self.is_addition = is_addition

    def run(self, inputs: dict):
        partial = (
            0 if self.is_addition else 1) if self.scalar is None else self.scalar
        for dep in self.get_dependencies():
            input_data = inputs[dep] if dep in inputs else 0
            if (input_data is not None) and (isinstance(input_data, int) or isinstance(input_data, float)):
                if self.is_addition:
                    partial += input_data
                else:
                    partial *= input_data
        return partial

    def repr_inner(self):
        return \
            """
                "is_addition": {0},
                "scalar": {1}
            """.format('true' if self.is_addition else 'false', self.scalar)
