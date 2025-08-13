import src.pipeline.pipeline_item as pi

class BaseOutput(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, base_destination:str):
        super().__init__(pipeline_item_data)
        self.base_destination = base_destination

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        return False

    def run(self, inputs:dict):
        try:
            index_what_to_print = 0
            key_what_to_print = self.get_dependencies()[index_what_to_print]
            what_to_print = self.get_ith_input(inputs, index_what_to_print)
            additional_data = { input_key: input_value for input_key, input_value in inputs.items() if input_key != key_what_to_print }
            return self.to_output(what_to_print, self.base_destination, additional_data)
        except Exception as e:
            print("ERROR on output:")
            print(e)
            import traceback
            traceback.print_exception(e)

    def repr_inner(self):
        return \
        """
            {0},
            "base_destination": {1}
        """.format( \
            super().repr_inner(), \
            self.base_destination
        )
       
    