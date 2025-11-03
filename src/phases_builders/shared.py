
import src.phases_builders.phases as phases
import src.phases_builders.phase_builder as pb

import src.phases_builders.input_fetch as ph_i
import src.phases_builders.model_generation as ph_m
import src.phases_builders.postprocessing as ph_p
import src.phases_builders.output as ph_o


def builder_from_phase(phase: phases.TranslationPhases) -> pb.PipelineItemFactory:
    if phase == phases.TranslationPhases.INPUT_FETCHING:
        return ph_i.InputFactory()
    elif phase == phases.TranslationPhases.MODEL_GENERATION:
        return ph_m.()
    elif phase == phases.TranslationPhases.INPUT_FETCHING:
        return ph_p.()
    elif phase == phases.TranslationPhases.INPUT_FETCHING:
        return ph_o.()
    else:
        raise Exception(f"Unrecognized phase: {phase}")
