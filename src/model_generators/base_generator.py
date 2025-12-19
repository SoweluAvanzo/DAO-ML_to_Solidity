import src.pipeline.pipeline_item as pi
import src.utilities.utils as u
import src.utilities.errors as e_c


class BaseGenerator(pi.PipelineItem):
    """
    Works as a pre-processing
    """

    def __init__(self, pipeline_item_data: pi.PIData, printer_debug: u.PrinterDebug = None):
        super().__init__(pipeline_item_data, printer_debug=printer_debug)

    def generate(self, additional_input=None):
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def run(self, inputs):
        return self.generate(self.get_ith_input(inputs, 0))
