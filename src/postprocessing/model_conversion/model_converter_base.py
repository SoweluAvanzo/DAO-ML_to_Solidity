import src.pipeline.pipeline_item as pi
import src.model.diagram_manager as dm


class ModelConversionResultBase:
    def get_id(self) -> str:
        return None


class ModelConverterBase(pi.PipelineItem):
    """
    A class that defines the base of a conversion/translation process.
    Some of its sublasses might actually delegate to different kinds or versions
    of translators.
    """
    def __init__(self, pipeline_item_data: pi.PIData, key_model:str=None):
        super().__init__(pipeline_item_data)
        self.key_model = key_model

    
    def translate(self, model:dm.DiagramManager, additional_data=None) -> ModelConversionResultBase:
        return None

    def run(self, inputs):
        return self.translate(\
            inputs[self.key_model] if self.key_model is not None else self.get_ith_input(inputs, 0), \
            inputs)
