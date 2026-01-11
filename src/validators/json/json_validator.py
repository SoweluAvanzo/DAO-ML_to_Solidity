import src.pipeline.pipeline_item as pi
import src.validators.diagram_model_validator as dmv

import src.utilities.utils as u


class JSONValidator(dmv.DiagramModelValidator):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )
