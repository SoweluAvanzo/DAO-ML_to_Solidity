
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv

import src.utilities.utils as u
import src.utilities.errors as e_c


class AdditionalDataSubPhase:
    def __init__(self, phase_step_variant: psv.PhaseSubstepVariants):
        if not isinstance(phase_step_variant, psv.PhaseSubstepVariants):
            raise Exception(
                f"Provided phase_step_variant is not an instance of PhaseSubstepVariants: {type(phase_step_variant)}")
        self.phase_step_variant = phase_step_variant


class PipelineItemFactory:
    """
    Base-class for an automated way of building a PipelineItem based on a
    PhaseSubstepVariants
    """

    def __init__(self, printer_debug: u.PrinterDebug = None):
        self.printer_debug = printer_debug

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def new_pipeline_item_from_variant(self, pi_data: pi.PIData, phase_step_variant_and_data: AdditionalDataSubPhase) -> pi.PipelineItem:
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def new_pipeline_item(self,
                          pi_data: pi.PIData,
                          phase_step_variant_and_data: AdditionalDataSubPhase
                          ) -> pi.PipelineItem:
        if (phase_step_variant_and_data is None):
            raise Exception(
                "Given phase_step_variant_and_data must not be None")
        if not isinstance(phase_step_variant_and_data, AdditionalDataSubPhase):
            raise Exception(
                f"Provided phase_step_variant_and_data is not an instance of AdditionalDataSubPhase: {type(phase_step_variant_and_data)}")

        if not isinstance(phase_step_variant_and_data.phase_step_variant, self.get_PhaseSubstepVariants_enum()):
            raise self.not_PSV_instance_exception(
                phase_step_variant_and_data.phase_step_variant)
        # the real factory
        p = self.new_pipeline_item_from_variant(
            pi_data,
            phase_step_variant_and_data
        )
        if p is None:
            raise Exception(
                f"Unknown phase_step_variant: {phase_step_variant_and_data.phase_step_variant}")
        return p

    def not_PSV_instance_exception(self, psv: psv.PhaseSubstepVariants) -> Exception:
        return Exception(f"Given phase_step_variant is not an instance of {type(self.get_PhaseSubstepVariants_enum())}, but is: {type(psv)}")
