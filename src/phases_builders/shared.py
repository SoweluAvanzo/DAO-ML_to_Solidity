
import src.phases_builders.phases as phases
import src.phases_builders.phase_builder as pb

import src.phases_builders.input_fetch as ph_i
import src.phases_builders.model_generation as ph_m
import src.phases_builders.postprocessing as ph_p
import src.phases_builders.output as ph_o
import src.phases_builders.phase_step_variants as psv

import src.utilities.utils as u


class PersistanceType(psv.PhaseSubstepVariants):
    FILE = "file"
    # PROGRAMMATIC_PROVIDER = "prog" # an external / runtine source, like constants or the value returned by a provider (or in-memory DB / map/dict)
    DATABASE = "db"
    # API="api" # of any kind: calling an HTTP API method, a WebSocket, an RSS-Feed, etc


#

class PhaseVariantsAndData:
    def __init__(self, phase: phases.TranslationPhases):
        if not isinstance(phase, phases.TranslationPhases):
            raise Exception(
                f"Provided phase is not an instance of TranslationPhases: {type(phase)}")
        self.phase = phase
        self.phase_variant_data_by_pv_name: dict[str,
                                                 pb.AdditionalDataSubPhase] = {}

    def add_phase_variant_data(self, phase_step_variant_data: pb.AdditionalDataSubPhase):
        if not isinstance(phase_step_variant_data, pb.AdditionalDataSubPhase):
            raise Exception(
                f"Provided phase_step_variant_data is not an instance of AdditionalDataSubPhase: {type(phase_step_variant_data)}")
        self.phase_variant_data_by_pv_name[phase_step_variant_data.phase_step_variant.name] = phase_step_variant_data
        return True

    def add_phase_variant_and_data(self, phase_step_variant: psv.PhaseSubstepVariants, additional_data: dict = None):
        return self.add_phase_variant_data(pb.AdditionalDataSubPhase(phase_step_variant, additional_data=additional_data))

#


def builder_from_phase(phase: phases.TranslationPhases, printer_debug: u.PrinterDebug = None) -> pb.PipelineItemFactory:
    if phase == phases.TranslationPhases.INPUT_FETCHING:
        return ph_i.InputFactory(printer_debug=printer_debug)
    elif phase == phases.TranslationPhases.MODEL_GENERATION:
        return ph_m.ModelGeneratorFactory(printer_debug=printer_debug)
    elif phase == phases.TranslationPhases.TRANSLATION_CONVERSION_POSTPROCESSING:
        return ph_p.PostProcessingFactory(printer_debug=printer_debug)
    elif phase == phases.TranslationPhases.OUTPUT:
        return ph_o.()
    else:
        raise Exception(f"Unrecognized phase: {phase}")
