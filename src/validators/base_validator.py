import src.pipeline.pipeline_item as pi

import src.validators.validation_result as validation_res

import src.utilities.utils as u
import src.utilities.errors as e_c


class BaseValidator(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, printer_debug: u.PrinterDebug = None):
        super().__init__(pipeline_item_data, printer_debug=printer_debug)

    def validate(self, input) -> validation_res.ValidationResult:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def run(self, inputs: dict):
        return self.validate(self.get_ith_input(inputs, 0))
