
import src.pipeline.pipeline_item as pi
import src.pipeline.pipeline_items_chained as pc
import src.pipeline.utilities.pi_chain_store_releaser_branching as pi_chain_store
import src.pipeline.utilities.pi_exception_raiser as perrr

import src.phases_builders.shared as pb_shared
import src.phases_builders.phases as phases
import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb

import src.validators.validation_result_to_errors as vete
import src.validators.xml.xml_dao_validator as xvi
import src.model_generators.xml_string_model_generator as xsmg
import src.model_generators.json_string_model_generator as jsmg

import src.utilities.utils as u
import src.utilities.errors as e_c


class ModelGeneratorFormat(psv.PhaseSubstepVariants):
    XML = "xml"
    JSON = "json"


class AdditionalDataModelGeneration(pb.AdditionalDataSubPhase):
    def __init__(self, phase_step_variant: ModelGeneratorFormat,
                 key_input_provider: str = None
                 ):
        super().__init__(phase_step_variant)
        self.key_input_provider = key_input_provider


class ModelXMLGeneratordData(AdditionalDataModelGeneration):
    def __init__(self, file_path_xml_schema: str,
                 key_input_provider: str = None):
        super().__init__(ModelGeneratorFormat.XML, key_input_provider=key_input_provider)
        self.file_path_xml_schema = file_path_xml_schema


class ModelJSONGeneratordData(AdditionalDataModelGeneration):
    def __init__(self,
                 key_input_provider: str = None):
        super().__init__(ModelGeneratorFormat.JSON, key_input_provider=key_input_provider)

#


class ModelGeneratorFactory(pb.PipelineItemFactory):

    def __init__(self, key_unique_producer: pb_shared.KeyUniqueProducer,
                 printer_debug: u.PrinterDebug = None):
        super().__init__(key_unique_producer, printer_debug=printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return ModelGeneratorFormat

    def new_pipeline_item_from_variant(self,
                                       phase_step_variant_and_data: pb.AdditionalDataSubPhase
                                       ) -> pb.PipelineItemsGenerated:
        if phase_step_variant_and_data.phase_step_variant == ModelGeneratorFormat.XML:
            if not isinstance(phase_step_variant_and_data, ModelXMLGeneratordData):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected ModelXMLGeneratordData, got: {type(phase_step_variant_and_data)}")
            if phase_step_variant_and_data.file_path_xml_schema is None:
                raise Exception(
                    f"file_path_xml_schema is None, so can't retrieve the XML Schema file path")
            fpXMLs = phase_step_variant_and_data.file_path_xml_schema
            k_input = ModelXMLGeneratordData(
                phase_step_variant_and_data).key_input_provider
            # dummy value to pass null+isinstance checks
            empty_pi_d = pi.PIData(
                self.new_unique_key("k"), dependencies=None)
            validation_store = pi_chain_store.PIChainStoreReleaserBranching(
                pi.PIData(k_input)
            )
            xml_validator = xvi.XMLDaoValidator(
                empty_pi_d, fpXMLs, printer_debug=self.printer_debug)
            k_model_generator = self.new_unique_key(
                f"k_model_generator_{phase_step_variant_and_data.phase_step_variant.name}")
            model_generator = xsmg.XmlStringModelGenerator(
                pi.PIData(k_model_generator), printer_debug=self.printer_debug)
            validator_errors_extractor = vete.ValidationResultToErrorsExtractor(
                empty_pi_d,
                # "None" so that the errors extractor MUST rely on the chain
                # (i.e., retrieve the value from the inputs by the 0-th dependency)
                key_validation_result=None,
                printer_debug=self.printer_debug
            )
            v_exc_raiser = perrr.PIExceptionRaiser(empty_pi_d,
                                                   key_error_input=None,
                                                   printer_debug=self.printer_debug
                                                   )
            chain_pi: list[pi.PipelineItem] = [
                xml_validator,
                validation_store,  # ... setup the branching ...
                validator_errors_extractor,
                v_exc_raiser,
                validation_store,  # ... retrieve from the branching -> generate
                model_generator
            ]
            return pb.PipelineItemsGenerated(
                [
                    pc.PIChained(
                        xml_validator.get_pipeline_item_data(),
                        chain_pi,
                        printer_debug=self.printer_debug
                    )
                ],
                k_model_generator
            )
        elif phase_step_variant_and_data.phase_step_variant == ModelGeneratorFormat.JSON:
            k_input = ModelJSONGeneratordData(
                phase_step_variant_and_data).key_input_provider
            return pb.PipelineItemsGenerated(
                [jsmg.JsonStringModelGenerator(
                    pi.PIData(k_input)
                )],
                k_input
            )
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                        " : " + phase_step_variant_and_data.phase_step_variant.value)
