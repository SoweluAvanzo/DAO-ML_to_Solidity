import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.solidity.optimized.solidity_translator_optimized as sol_transl_opt


class SolidityTranslatorOptimizedJinja(sol_transl_opt.SolidityTranslatorOptimized):
    """
    All of this subclasses bear the responsibility of declaring and defining which kind of templates they are using
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_converter_type: str = None,
                 key_converter_version: str = None,
                 key_converter_target: str = None
                 ):
        super().__init__(
            pipeline_item_data,
            key_model,
            key_converter_type,
            key_converter_version,
            key_converter_target
        )
