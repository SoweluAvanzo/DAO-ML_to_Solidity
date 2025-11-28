
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb
import src.phases_builders.shared as pb_shared

import src.input.xml_file_input as xml_f_i
import src.input.txt_file_input as txt_f_i

import src.utilities.utils as u
import src.utilities.errors as e_c


class InputType(psv.PhaseSubstepVariants):
    XML = "xml"
    JSON = "json"
    # YAML="yaml"
    # BSON = "bson"
    # BINARY = "bytes"


class InputSourceType(psv.PhaseSubstepVariants):
    FILE_XML = (pb_shared.PersistanceType.FILE.value, InputType.XML.value)
    FILE_JSON = (pb_shared.PersistanceType.FILE.value, InputType.JSON.value)
    # FILE_YAML
    # FILE_BSON
    # FILE_BINARY
    # API_XML
    # API_JSON
    # API_YAML
    # API_BSON
    # API_BINARY
    # DB_XML
    # DB_JSON
    # DB_YAML
    # DB_BSON
    # DB_BINARY

#


class AdditionalDataInput(pb.AdditionalDataSubPhase):
    def __init__(self, phase_step_variant: InputSourceType, filepath: str,
                 should_strip_line: bool = False
                 ):
        if not (isinstance(phase_step_variant, InputSourceType) or (phase_step_variant[0] == pb_shared.PersistanceType.FILE)):
            raise Exception(
                f"Incompatible phase_step_variant: {phase_step_variant}")
        super().__init__(phase_step_variant)
        self.filepath = filepath
        self.should_strip_line = should_strip_line


class FileXMLAdditionalDataSubPhase(AdditionalDataInput):
    def __init__(self, filepath: str,
                 xml_version: str,
                 should_strip_line: bool = False
                 ):
        super().__init__(InputSourceType.FILE_XML,
                         filepath, should_strip_line=should_strip_line)
        self.xml_version = xml_version


class FileJSONAdditionalDataSubPhase(AdditionalDataInput):
    def __init__(self, filepath: str,
                 should_strip_line: bool = False
                 ):
        super().__init__(InputSourceType.FILE_JSON,
                         filepath, should_strip_line=should_strip_line)

#


def input_source_type(i_s: pb_shared.PersistanceType, i_t: InputType) -> InputSourceType:
    if i_s == pb_shared.PersistanceType.FILE:
        if i_t == InputType.XML:
            return InputSourceType.FILE_XML
        elif i_t == InputType.JSON:
            return InputSourceType.FILE_JSON
    raise Exception(
        f"Unknown/unmanaged input & source-type pair: < {i_s} ; {i_t} >")


class InputFactory(pb.PipelineItemFactory):

    def __init__(self, key_unique_producer: pb_shared.KeyUniqueProducer,
                 printer_debug: u.PrinterDebug = None):
        super().__init__(key_unique_producer, printer_debug=printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return InputSourceType

    def new_pipeline_item_from_variant(self, pi_data: pi.PIData,
                                       additional_data: pb.AdditionalDataSubPhase
                                       ) -> list[pi.PipelineItem]:
        # the real factory
        if additional_data.phase_step_variant == InputSourceType.FILE_XML:
            if not isinstance(additional_data, FileXMLAdditionalDataSubPhase):
                raise Exception(
                    f"Additional Data is expected to be a (sub)class of FileXMLAdditionalDataSubPhase, but is: {type(additional_data)}")
            return [
                xml_f_i.TextFileInputXML(pi_data,
                                         filepath=additional_data.filepath,
                                         xml_version=additional_data.xml_version,
                                         should_strip_line=additional_data.should_strip_line
                                         )
            ]
        elif additional_data.phase_step_variant == InputSourceType.FILE_JSON:
            if not isinstance(additional_data, FileJSONAdditionalDataSubPhase):
                raise Exception(
                    f"Additional Data is expected to be a (sub)class of FileXMLAdditionalDataSubPhase, but is: {type(additional_data)}")
            return [
                txt_f_i.TextFileInput(pi_data,
                                      filepath=additional_data.filepath,
                                      should_strip_line=additional_data.should_strip_line
                                      )
            ]
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                        " : " + phase_step_variant_and_data.phase_step_variant.value)
