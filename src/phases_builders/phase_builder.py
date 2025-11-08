
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv

import src.utilities.utils as u
import src.utilities.errors as e_c


class PipelineItemFactory:
    """
    Base-class for an automated way of building a PipelineItem based on a
    PhaseSubstepVariants
    """

    def __init__(self, printer_debug: u.PrinterDebug = None):
        self.printer_debug = printer_debug

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def new_pipeline_item(self, phase_step_variant: psv.PhaseSubstepVariants, pi_data: pi.PIData, additional_data: dict = None) -> pi.PipelineItem:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def not_PSV_instance_exception(self, psv: psv.PhaseSubstepVariants) -> Exception:
        return Exception(f"Given phase_step_variant is not an instance of {type(self.get_PhaseSubstepVariants_enum())}, but is: {type(psv)}")
