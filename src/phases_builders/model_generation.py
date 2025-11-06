
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb

import src.model_generators.xml_string_model_generator as xsmg
import src.model_generators.json_string_model_generator as jsmg


class ModelGenerator(psv.PhaseSubstepVariants):
    XML = "xml"
    JSON = "json"


class InputFactory(pb.PipelineItemFactory):

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return ModelGenerator

    def new_pipeline_item(self, phase_step_variant: psv.PhaseSubstepVariants, pi_data: pi.PIData, additional_data: dict = None) -> pi.PipelineItem:
        if not isinstance(phase_step_variant, ModelGenerator):
            raise self.not_PSV_instance_exception(phase_step_variant)
        # the real factory
        if additional_data is None:
            additional_data = {}
        if phase_step_variant == ModelGenerator.XML:
            return xsmg.XmlStringModelGenerator(pi_data)
        elif phase_step_variant == ModelGenerator.JSON:
            return jsmg.JsonStringModelGenerator(pi_data)
        raise Exception(f"Unknown phase_step_variant: {phase_step_variant}")
