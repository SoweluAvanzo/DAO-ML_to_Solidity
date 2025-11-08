import src.pipeline.pipeline_item as pi
import src.utilities.utils as u


class BaseValidator(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, printer_debug: u.PrinterDebug = None):
        super().__init__(pipeline_item_data, printer_debug=printer_debug)

    def validate(self, input) -> bool:
        return False

    def run(self, inputs: dict):
        return self.validate(self.get_ith_input(inputs, 0))
