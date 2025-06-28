import src.pipeline.pipeline_item as pi

class PIAnyValue(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, val=None):
        super().__init__(pipeline_item_data)



class TranslatorGeneral(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)


    def translate(self, additional_data=None):
        return None

    def run(self, inputs):
        return self.translate(inputs)
    