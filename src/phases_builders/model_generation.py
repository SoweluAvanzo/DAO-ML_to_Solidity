
import src.pipeline.pipeline_item as pi
import src.pipeline.pipeline_items_chained as pc

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb

import src.validators.xml.xml_dao_validator as xvi
import src.model_generators.xml_string_model_generator as xsmg
import src.model_generators.json_string_model_generator as jsmg

KEY_ADDITIONAL_DATA__FILE_PATH_XML_SCHEMA = "k_a_d_FILE_PATH_XML_SCHEMA"


class ModelGeneratorFormat(psv.PhaseSubstepVariants):
    XML = "xml"
    JSON = "json"


class ModelGeneratorFactory(pb.PipelineItemFactory):

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return ModelGeneratorFormat

    def new_pipeline_item(self, phase_step_variant: psv.PhaseSubstepVariants, pi_data: pi.PIData, additional_data: dict = None) -> pi.PipelineItem:
        if not isinstance(phase_step_variant, ModelGeneratorFormat):
            raise self.not_PSV_instance_exception(phase_step_variant)
        # the real factory
        if additional_data is None:
            additional_data = {}
        if phase_step_variant == ModelGeneratorFormat.XML:
            if KEY_ADDITIONAL_DATA__FILE_PATH_XML_SCHEMA not in additional_data:
                raise Exception(
                    f"additional data is missing of the key for retrieving the XML Schema file path")
            fpXMLs = additional_data[KEY_ADDITIONAL_DATA__FILE_PATH_XML_SCHEMA]
            empty_pi_data = pi.PIData(None, dependencies=None)
            chain_validation_generation: pc.PIChained = None
            xml_validator = xvi.XMLDaoValidator(empty_pi_data, fpXMLs)
            model_generator = xsmg.XmlStringModelGenerator(pi_data, [
                xml_validator,
                model_generator
            ])
            # WHAT ABOUT "vete.ValidationResultToErrorsExtractor" and "perrr.PIExceptionRaiser" ?
            chain_validation_generation = pc.PIChained(pi_data)
            return chain_validation_generation
        elif phase_step_variant == ModelGeneratorFormat.JSON:
            return jsmg.JsonStringModelGenerator(pi_data)
        raise Exception(f"Unknown phase_step_variant: {phase_step_variant}")
