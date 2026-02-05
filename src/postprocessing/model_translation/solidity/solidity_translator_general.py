
import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.model_translator_subparts as tms

import src.utilities.utils as u


class SolidityTranslatorGeneral(tms.ModelTranslatorSubparts):
    """
    Superclass of all other Solidity Translators.
    At this level of class hirerachy, no further details are added
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_force_governance_area_split: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         key_model=key_model,
                         printer_debug=printer_debug
                         )
        self.key_force_governance_area_split = key_force_governance_area_split
