
import src.pipeline.pipeline_item as pi

import src.phases_builders.shared as pb_shared
import src.phases_builders.phase_step_variants as psv

import src.utilities.utils as u
import src.utilities.errors as e_c


class PipelineItemsGenerated:
    def __init__(self, pipeline_items: list[pi.PipelineItem], key_output_for_next_step: str):
        self.pipeline_items = pipeline_items
        self.key_output_for_next_step = key_output_for_next_step


class PipelineItemFactory:
    """
    Base-class for an automated way of building a PipelineItem based on a
    PhaseSubstepVariants
    """

    def __init__(self, key_unique_producer: pb_shared.KeyUniqueProducer,
                 printer_debug: u.PrinterDebug = None):
        self.printer_debug = printer_debug
        self.key_unique_producer = key_unique_producer

    def print_msg(self, msg):
        self.printer_debug.print_msg(msg)

    def print_error(self, err):
        self.printer_debug.print_error(err)

    def new_unique_key(self, base_key: str = None) -> str:
        """
        Proxy-like method invoking the instance of KeyUniqueProducer
        """
        k = self.key_unique_producer.new_unique_key()
        return k if base_key is None else f"{base_key}_{k}"

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        """
        Return the class/type of the enumeration of the substep variants this PipelineItem Factory relies on.
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def new_pipeline_item_from_variant(self, phase_step_variant_and_data: pb_shared.AdditionalDataSubPhase) -> PipelineItemsGenerated:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def new_pipeline_items(self,
                           phase_step_variant_and_data: pb_shared.AdditionalDataSubPhase
                           ) -> PipelineItemsGenerated:
        """
        Returns a list of PipelineItems, where the first one uses the given "PIData" and every one else
        is just in need to be added to the graph.
        SHOULD NOT BE OVERRIDDEN
        """
        if (phase_step_variant_and_data is None):
            raise Exception(
                "Given phase_step_variant_and_data must not be None")
        if not isinstance(phase_step_variant_and_data, pb_shared.AdditionalDataSubPhase):
            raise Exception(
                f"Provided phase_step_variant_and_data is not an instance of AdditionalDataSubPhase: {type(phase_step_variant_and_data)}")
        if not isinstance(phase_step_variant_and_data.phase_step_variant, self.get_PhaseSubstepVariants_enum()):
            raise self.not_PSV_instance_exception(
                phase_step_variant_and_data.phase_step_variant)
        # the real factory
        p = self.new_pipeline_item_from_variant(
            phase_step_variant_and_data
        )
        if p is None:
            raise Exception(
                f"Unknown phase_step_variant: {phase_step_variant_and_data.phase_step_variant}")
        return p

    def not_PSV_instance_exception(self, psv: psv.PhaseSubstepVariants) -> Exception:
        return Exception(f"Given phase_step_variant is not an instance of {type(self.get_PhaseSubstepVariants_enum())}, but is: {type(psv)}")
