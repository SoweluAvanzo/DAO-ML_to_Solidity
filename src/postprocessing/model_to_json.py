import json

import src.pipeline.pipeline_item as pi
import src.utilities.utils as u
import src.model.diagram_manager as dm


class JsonStringModelGenerator(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)


    def run(self, inputs):
        diagram_manager = self.get_ith_input(inputs, 0)
        if not isinstance(diagram_manager, dm.DiagramManager):
            raise Exception("Input must be of an instance of DiagramManager")
        return repr(diagram_manager)
