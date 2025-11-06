import src.pipeline.pipeline_item as pi


class PIChained(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, chains_of_pi: list[pi.PipelineItem]):
        super().__init__(pipeline_item_data)
        self.chains_of_pi = chains_of_pi
        index = 0
        prev_deps = pipeline_item_data.dependencies
        for pi_c in self.chains_of_pi:
            key_c = f"k_{index}"
            pi_c.pipeline_item_data = pi.PIData(key_c, prev_deps)
            prev_deps = [key_c]
            index += 1

    def run(self, inputs: dict):
        # basically, simulates a little linear "Pipeline Manager", BUT without using it directly
        # to avoid circular imports
        output = inputs
        output_run = None
        for pi_c in self.chains_of_pi:
            try:
                # each output of the previous step is the input of the next
                output_run = pi_c.run(output)
                output = {pi_c.get_key(): output_run}
            except Exception as e:
                import traceback
                traceback.print_exception(e)
                return None
        output = None
        return {self.get_key(): output_run}
