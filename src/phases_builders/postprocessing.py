
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb

import src.postprocessing.model_translation.asm as pp_mt_asm
import src.postprocessing.model_translation.solidity.solidity_translator_configurable as pp_mt_sol_c
import src.postprocessing.output_preparation.json.model_to_json as pp_o_json

import src.utilities.utils as u


class PostProcessingTransformation(psv.PhaseSubstepVariants):
    SOLIDITY = "sol"
    ASM = "asm"
    JSON = "json"
    # PETRI_NETS = "petri"


class PostProcessingFactory(pb.PipelineItemFactory):
    def __init__(self, printer_debug: u.PrinterDebug = None):
        super().__init__(printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return PostProcessingTransformation

    def new_pipeline_item_from_variant(self, phase_step_variant: psv.PhaseSubstepVariants, pi_data: pi.PIData,
                                       additional_data: dict = None
                                       ) -> pi.PipelineItem:
        if phase_step_variant == PostProcessingTransformation.SOLIDITY:
            # TODO: fare un "chained" di traduzione e compilazione usando :
            # - "pp_mt_sol_c" configurable
            # - e tirando fuori versione e modo (simple/optimized/diamond/...) etc dal dict "additional_data"
            pass
        elif phase_step_variant == PostProcessingTransformation.ASM:
            # TODO: come sopra, ma per l'ASM
            pass
        elif phase_step_variant == PostProcessingTransformation.JSON:
            return pp_o_json.JsonStringModelGenerator(pi_data,
                                                      string_output_required=False,
                                                      indent=additional_data["indent"]if "indent" in additional_data else None
                                                      )
        return None
