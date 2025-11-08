import src.pipeline.pipeline_item as pi

import src.utilities.utils as u


class ChainData:
    def __init__(self, key: str, pit: pi.PipelineItem, chain_dependencies: list[str] = None):
        self.key = key
        self.pit = pit
        self.chain_dependencies = chain_dependencies
        # linked_list-alike
        self.prev_cd: ChainData = None
        self.next_cd: ChainData = None


class PIChained(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, chains_of_pi: list[pi.PipelineItem],
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data, printer_debug=printer_debug)
        # self.chains_of_pi = chains_of_pi
        # chain building:
        self.chain: list[ChainData] = [None]*len(chains_of_pi)
        index = 0
        prev_deps = pipeline_item_data.dependencies  # === to "self.get_dependencies()"
        prev_cd: ChainData = None
        for pi_c in chains_of_pi:
            key_c = f"k_{index}"
            cd = ChainData(key_c, pi_c,
                           chain_dependencies=prev_deps
                           )
            # linked_list-alike append
            cd.prev_cd = prev_cd
            if prev_cd is not None:
                prev_cd.next_cd = cd
            prev_cd = cd
            self.chain[index] = cd
            prev_deps = [key_c]
            index += 1
        # now, "prev_cd" is the "top of the stack" (LIFO structure)

    def run(self, inputs: dict):
        # basically, simulates a little linear "Pipeline Manager", BUT without using it directly
        # to avoid circular imports
        inputs_for_next = inputs
        output_run = None
        for pi_c in self.chain:
            if self.is_debug:
                print()
            try:
                pipeline_item: pi.PipelineItem = pi_c.pit
                # leverage the "dependencies mechanism" BUT preserve the original ones
                original_dependencies = pipeline_item.get_dependencies()
                pipeline_item.get_pipeline_item_data().dependencies = pi_c.chain_dependencies
                # each output of the previous step is the input of the next
                output_run = pipeline_item.run(inputs_for_next)
                # set them back again
                pipeline_item.get_pipeline_item_data().dependencies = original_dependencies
                # the following dictionary simulates the internal working of the "PipelineManager",
                #  which provides as "inputs" a dict whose keys are the dependencies and the
                #  values are their outputs
                inputs_for_next = {pi_c.key: output_run}
            except Exception as e:
                import traceback
                traceback.print_exception(e)
                return None
        inputs_for_next = None  # discard the last one
        return output_run
