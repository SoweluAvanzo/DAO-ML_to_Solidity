
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
import src.validators.json.json_validator as jvi
import src.model_generators.xml_string_model_generator as xsmg
import src.model_generators.json_string_model_generator as jsmg

import src.utilities.utils as u
import src.utilities.errors as e_c


class AdditionalDataModelGeneration(pb_shared.AdditionalDataSubPhase):
    def __init__(self, phase_step_variant: pb_shared.ModelPersistanceFormat,
                 key_input_provider: str = None
                 ):
        super().__init__(phase_step_variant)
        self.key_input_provider = key_input_provider


class ModelXMLGeneratordData(AdditionalDataModelGeneration):
    def __init__(self, file_path_xml_schema: str,
                 key_input_provider: str = None):
        super().__init__(pb_shared.ModelPersistanceFormat.XML,
                         key_input_provider=key_input_provider)
        self.file_path_xml_schema = file_path_xml_schema


class ModelJSONGeneratordData(AdditionalDataModelGeneration):
    def __init__(self,
                 key_input_provider: str = None):
        super().__init__(pb_shared.ModelPersistanceFormat.JSON,
                         key_input_provider=key_input_provider)

#


class ModelGeneratorFactory(pb.PipelineItemFactory):

    def __init__(self, key_unique_producer: pb_shared.KeyUniqueProducer,
                 printer_debug: u.PrinterDebug = None):
        super().__init__(key_unique_producer, printer_debug=printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return pb_shared.ModelPersistanceFormat

    def new_pipeline_item_from_variant(self,
                                       phase_step_variant_and_data: pb_shared.AdditionalDataSubPhase
                                       ) -> pb.PipelineItemsGenerated:
        if phase_step_variant_and_data.phase_step_variant == pb_shared.ModelPersistanceFormat.XML:
            if not isinstance(phase_step_variant_and_data, ModelXMLGeneratordData):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected ModelXMLGeneratordData, got: {type(phase_step_variant_and_data)}")
            if phase_step_variant_and_data.file_path_xml_schema is None:
                raise Exception(
                    f"file_path_xml_schema is None, so can't retrieve the XML Schema file path")
            fpXMLs = phase_step_variant_and_data.file_path_xml_schema
            psvd: ModelXMLGeneratordData = phase_step_variant_and_data
            k_input = psvd.key_input_provider
            k_xml_validator = self.new_unique_key("k_xml_validator")
            xml_validator = xvi.XMLDaoValidator(
                pi.PIData(k_xml_validator, [k_input]),
                fpXMLs,
                printer_debug=self.printer_debug
            )
            k_model_generator = self.new_unique_key(
                f"k_model_generator_{phase_step_variant_and_data.phase_step_variant.name}")
            model_generator = xsmg.XmlStringModelGenerator(
                pi.PIData(k_model_generator, [k_xml_validator]),
                printer_debug=self.printer_debug
            )
            k_validator_errors_extractor = self.new_unique_key(
                "validator_errors_extractor")
            validator_errors_extractor = vete.ValidationResultToErrorsExtractor(
                pi.PIData(k_validator_errors_extractor, [k_xml_validator]),
                key_validation_result=k_xml_validator,
                printer_debug=self.printer_debug
            )
            k_v_exc_raiser = self.new_unique_key("k_v_exc_raiser")
            v_exc_raiser = perrr.PIExceptionRaiser(
                pi.PIData(k_v_exc_raiser, [k_validator_errors_extractor]),
                key_error_input=k_validator_errors_extractor,
                printer_debug=self.printer_debug
            )
            return pb.PipelineItemsGenerated(
                [
                    xml_validator,
                    validator_errors_extractor,
                    v_exc_raiser,
                    model_generator
                ],
                k_model_generator
            )
        elif phase_step_variant_and_data.phase_step_variant == pb_shared.ModelPersistanceFormat.JSON:
            if not isinstance(phase_step_variant_and_data, ModelJSONGeneratordData):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected ModelJSONGeneratordData, got: {type(phase_step_variant_and_data)}")
            k_input = phase_step_variant_and_data.key_input_provider
            k_model_generator = self.new_unique_key("k_model_generator")
            model_generator = jsmg.JsonStringModelGenerator(
                pi.PIData(k_model_generator, [k_input]),
                printer_debug=self.printer_debug
            )
            # TODO: use "DiagramModelValidator", then gather its error, print it if necessary, etc etc, like XML does
            k_json_validator = self.new_unique_key("k_json_validator")
            json_validator = jvi.JSONValidator(
                pi.PIData(k_json_validator, [
                    # k_input -> this validator _actually_ validates an already-generated Model, not the "str/list[str]" source of it
                    k_model_generator
                ]),
                printer_debug=self.printer_debug
            )

            k_validator_errors_extractor = self.new_unique_key(
                "validator_errors_extractor")
            validator_errors_extractor = vete.ValidationResultToErrorsExtractor(
                pi.PIData(k_validator_errors_extractor, [k_json_validator]),
                key_validation_result=k_json_validator,
                printer_debug=self.printer_debug
            )
            k_v_exc_raiser = self.new_unique_key("k_v_exc_raiser")
            v_exc_raiser = perrr.PIExceptionRaiser(
                pi.PIData(k_v_exc_raiser, [k_validator_errors_extractor]),
                key_error_input=k_validator_errors_extractor,
                printer_debug=self.printer_debug
            )
            return pb.PipelineItemsGenerated(
                [
                    json_validator,
                    validator_errors_extractor,
                    v_exc_raiser,
                    model_generator
                ],
                k_model_generator
            )
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                        " : " + phase_step_variant_and_data.phase_step_variant.value)
