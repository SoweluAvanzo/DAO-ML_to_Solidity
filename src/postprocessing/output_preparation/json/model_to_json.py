import json

import src.pipeline.pipeline_item as pi
import src.utilities.utils as u
import src.model.diagram_manager as dm


class ModelToJSON(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData,
                 string_output_required=False,
                 indent=None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug
        )
        self.string_output_required = string_output_required
        self.indent = indent

    def repr_inner(self):
        return f"string_output_required: {'true' if self.string_output_required else 'false'}"

    def run(self, inputs):
        self.print_msg(f"DUMPING JSON ....")
        diagram_manager = self.get_ith_input(inputs, 0)
        if diagram_manager is None:
            raise Exception(
                "JsonStringModelGenerator's diagram manager from input is None")
        if not isinstance(diagram_manager, dm.DiagramManager):
            raise Exception("Input must be of an instance of DiagramManager")
        json_ed = diagram_manager.toJSON()
        self.print_msg(diagram_manager.get_name())
        if self.string_output_required:
            json_ed = json.dumps(json_ed, indent=self.indent)
        return json_ed
