import src.pipeline.pipeline_item as pi

import src.utilities.utils as u


class PIExceptionRaiser(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData,
                 key_error_input: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data, printer_debug=printer_debug)
        self.key_error_input = key_error_input

    def run(self, inputs):
        err_text = inputs[self.key_error_input] if ((self.key_error_input is not None) and (
            self.key_error_input in inputs)) else self.get_ith_input(inputs, 0)
        if err_text is None:
            return None
        if isinstance(err_text, Exception):
            self.print_error(err_text)
            raise err_text
        if isinstance(err_text, str) and (err_text != ""):
            self.print_error(err_text)
            raise Exception(err_text)
        if isinstance(err_text, list) and (len(err_text) > 0):
            self.print_error(err_text)
            raise Exception("\n".join(err_text))
        return None

    def repr_inner(self):
        return f"\"key_error_input\":{self.key_error_input}"
