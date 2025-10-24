import src.pipeline.pipeline_item as pi


class PIExceptionRaiser(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, key_error_input: str = None):
        super().__init__(pipeline_item_data)
        self.key_error_input = key_error_input

    def run(self, inputs):
        err_text = inputs[self.key_error_input] if ((self.key_error_input is not None) and (
            self.key_error_input in inputs)) else self.get_ith_input(inputs, 0)
        if err_text is None:
            return None
        if isinstance(err_text, Exception):
            raise err_text
        if isinstance(err_text, str):
            raise Exception(err_text)
        if isinstance(err_text, list):
            raise Exception("\n".join(err_text))
        return None

    def repr_inner(self):
        return f"\"key_error_input\":{self.key_error_input}"
