import src.pipeline.pipeline_item as pi
import src.model.diagram_manager as dm
import src.postprocessing.model_translation.shared.conversion_result_base as crb


class ModelTranslatorBase(pi.PipelineItem):
    """
    A class that defines the base of a conversion/translation process.
    Some of its sublasses might actually delegate to different kinds or versions
    of translators.
    """

    def __init__(self, pipeline_item_data: pi.PIData, key_model: str = None):
        super().__init__(pipeline_item_data)
        self.key_model = key_model

    def translate(self, model: dm.DiagramManager, additional_data=None) -> crb.ModelConversionResultBase:
        raise Exception(
            f"convert function not implemented yet in {type(self)}")

    def run(self, inputs):
        return self.translate(
            inputs[self.key_model] if self.key_model is not None else self.get_ith_input(
                inputs, 0),
            inputs)
