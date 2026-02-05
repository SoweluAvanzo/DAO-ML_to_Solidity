import src.pipeline.pipeline_item as pi
import src.postprocessing.model_translation.solidity.optimized.solidity_translator_optimized as sol_transl_opt

import src.utilities.utils as u


class SolidityTranslatorOptimizedJinja(sol_transl_opt.SolidityTranslatorOptimized):
    """
    All of this subclasses bear the responsibility of declaring and defining which kind of templates they are using
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_translator_type: str = None,
                 key_translator_version: str = None,
                 key_translator_target: str = None,
                 key_force_governance_area_split: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(
            pipeline_item_data,
            key_model=key_model,
            key_translator_type=key_translator_type,
            key_translator_version=key_translator_version,
            key_translator_target=key_translator_target,
            key_force_governance_area_split=key_force_governance_area_split,
            printer_debug=printer_debug
        )
