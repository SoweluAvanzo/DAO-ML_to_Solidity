import src.pipeline.pipeline_item as pi

import src.utilities.utils as u


class BaseOutput(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug
        )

    def to_output(self, what, additional_data: dict) -> bool:
        return False

    def run(self, inputs: dict):
        try:
            index_what_to_print = 0
            key_what_to_print = self.get_dependencies()[index_what_to_print]
            what_to_print = self.get_ith_input(inputs, index_what_to_print)
            additional_data = {
                input_key: input_value
                for input_key, input_value in inputs.items()
                if input_key != key_what_to_print
            }
            self.print_msg(
                f"\nDEBUG: calling 'to_output' from the 'run' method originally defined in 'base_output' in {type(self)} with key ({self.get_key()})")
            return self.to_output(what_to_print, additional_data)
        except Exception as e:
            print("ERROR on output:")
            print(e)
            import traceback
            traceback.print_exception(e)
