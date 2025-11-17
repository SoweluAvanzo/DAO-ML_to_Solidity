
import src.pipeline.pipeline_item as pi
import src.pipeline.pipeline_items_chained as pc
import src.pipeline.utilities.pi_chain_store_releaser_branching as pi_chain_store
import src.pipeline.utilities.pi_exception_raiser as perrr

import src.phases_builders.phases as phases
import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb
import src.phases_builders.shared as pb_shared

import src.postprocessing.model_translation.solidity.voting_protocols_list_loader as pi_vpll
import src.postprocessing.model_translation.asm as pp_mt_asm
import src.postprocessing.model_translation.solidity.solidity_translator_configurable as pp_mt_sol_c
import src.postprocessing.output_preparation.json.model_to_json as pp_o_json


import src.postprocessing.model_translation.solidity.translation_types_solidity as transl_types_sol
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions

import src.utilities.utils as u
import src.utilities.extended_enum as ee


class PostProcessingTransformation(psv.PhaseSubstepVariants):
    SOLIDITY = "sol"
    ASM = "asm"
    JSON = "json"
    # PETRI_NETS = "petri"

#
#
#


class SolidityAdditionalDataKeys(ee.ExtendedEnum):
    VERSION_TRANSLATOR = "version_translator"
    VERSION_TRANSLATION_TARGET = "version_translation_target"


class AdditionalDataSolidity(pb.AdditionalDataSubPhase):
    def __init__(self,
                 folder_voting_protocols: str,
                 version_translator: str = jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value,
                 converter_solidity_subtype: str = transl_types_sol.TranslationTypesSolidity.OPTIMIZED.value,
                 version_translation_target: str = "1.0.0",
                 ):
        super().__init__(PostProcessingTransformation.SOLIDITY)
        self.folder_voting_protocols = folder_voting_protocols
        self.version_translator = version_translator
        self.converter_solidity_subtype = converter_solidity_subtype
        self.version_translation_target = version_translation_target


#
#
#

class PostProcessingFactory(pb.PipelineItemFactory):
    def __init__(self, printer_debug: u.PrinterDebug = None):
        super().__init__(printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return PostProcessingTransformation

    def new_pipeline_item_from_variant(self, phase_step_variant: psv.PhaseSubstepVariants, pi_data: pi.PIData,
                                       phase_step_variant_and_data: pb.AdditionalDataSubPhase
                                       ) -> pi.PipelineItem:
        if phase_step_variant == PostProcessingTransformation.SOLIDITY:
            if not isinstance(phase_step_variant_and_data, AdditionalDataSolidity):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataSolidity, got: {type(phase_step_variant_and_data)}")
            # TODO: fare un "chained" di traduzione e compilazione usando :
            # - "pp_mt_sol_c" configurable
            # - e tirando fuori versione e modo (simple/optimized/diamond/...) etc dal dict "additional_data"
            # (2025-11-17) E PRENDERE SPUNTO DA "t_file_1.py" DA RIGA 250 IN POI
            folder_voting_protocols = phase_step_variant_and_data.folder_voting_protocols
            version_translator = phase_step_variant_and_data.version_translator
            converter_solidity_subtype = phase_step_variant_and_data.converter_solidity_subtype
            version_translation_target = phase_step_variant_and_data.version_translation_target

            empty_pi_d = pi.PIData("k", dependencies=None)
            all_voting_protocols_loader = pi_vpll.VotingProtocolListLoader(
                empty_pi_d,
                folder_voting_protocols=folder_voting_protocols
            )
            chain_pi: list[pi.PipelineItem] = [
                all_voting_protocols_loader,
                validation_store,  # ... setup the branching ...
                validator_errors_extractor,
                v_exc_raiser,
                validation_store,  # ... retrieve from the branching -> generate
                model_generator
            ]
            return pc.PIChained(pi_data, chain_pi, printer_debug=self.printer_debug)
        elif phase_step_variant == PostProcessingTransformation.ASM:
            # TODO: come sopra, ma per l'ASM
            pass
        elif phase_step_variant == PostProcessingTransformation.JSON:
            return pp_o_json.JsonStringModelGenerator(pi_data,
                                                      string_output_required=False,
                                                      indent=additional_data["indent"]if "indent" in additional_data else None
                                                      )
        return None
