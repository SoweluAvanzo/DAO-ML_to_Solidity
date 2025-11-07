
import src.pipeline.pipeline_item as pi
import src.pipeline.pipeline_items_chained as pc
import src.pipeline.utilities.pi_chain_store_releaser_branching as pi_chain_store
import src.pipeline.utilities.pi_exception_raiser as perrr

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb

import src.validators.validation_result_to_errors as vete
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

    def new_pipeline_item(self, phase_step_variant: psv.PhaseSubstepVariants, pi_data: pi.PIData,
                          additional_data: dict = None
                          ) -> pi.PipelineItem:
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
            # dummy value to pass null+isinstance checks
            empty_pi_d = pi.PIData("k", dependencies=None)
            validation_store = pi_chain_store.PIChainStoreReleaserBranching(
                empty_pi_d)
            xml_validator = xvi.XMLDaoValidator(empty_pi_d, fpXMLs)
            model_generator = xsmg.XmlStringModelGenerator(pi_data,)
            validator_errors_extractor = vete.ValidationResultToErrorsExtractor(
                empty_pi_d,
                # "None" so that the errors extractor MUST rely on the chain
                # (i.e., retrieve the value from the inputs by the 0-th dependency)
                key_validation_result=None
            )
            v_exc_raiser = perrr.PIExceptionRaiser(empty_pi_d,
                                                   key_error_input=None
                                                   )
            chain_pi: list[pi.PipelineItem] = [
                xml_validator,
                validation_store,  # ... setup the branching ...
                validator_errors_extractor,
                v_exc_raiser,
                validation_store,  # ... retrieve from the branching -> generate
                model_generator
            ]
            return pc.PIChained(pi_data, chain_pi)
        elif phase_step_variant == ModelGeneratorFormat.JSON:
            return jsmg.JsonStringModelGenerator(pi_data)
        raise Exception(f"Unknown phase_step_variant: {phase_step_variant}")
