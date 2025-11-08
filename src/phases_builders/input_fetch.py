
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb

import src.input.xml_file_input as xml_f_i
import src.input.txt_file_input as txt_f_i

import src.utilities.utils as u


class InputSource(psv.PhaseSubstepVariants):
    FILE = "file"
    # PROGRAMMATIC_PROVIDER = "prog"  # basically, a
    DATABASE = "db"
    # API="api"


class InputType(psv.PhaseSubstepVariants):
    XML = "xml"
    JSON = "json"
    # YAML="yaml"
    # BSON = "bson"
    # BINARY = "bytes"


class InputSourceType(psv.PhaseSubstepVariants):
    FILE_XML = (InputSource.FILE.value, InputType.XML.value)
    FILE_JSON = (InputSource.FILE.value, InputType.JSON.value)
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


def input_source_type(i_s: InputSource, i_t: InputType) -> InputSourceType:
    if i_s == InputSource.FILE:
        if i_t == InputType.XML:
            return InputSourceType.FILE_XML
        elif i_t == InputType.JSON:
            return InputSourceType.FILE_JSON
    raise Exception(f"Unknown input source-type pair: < {i_s} ; {i_t} >")


class InputFactory(pb.PipelineItemFactory):

    def __init__(self, printer_debug: u.PrinterDebug = None):
        super().__init__(printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return InputSourceType

    def new_pipeline_item(self, phase_step_variant: psv.PhaseSubstepVariants, pi_data: pi.PIData, additional_data: dict = None) -> pi.PipelineItem:
        if not isinstance(phase_step_variant, InputSourceType):
            raise self.not_PSV_instance_exception(phase_step_variant)
        # the real factory
        if additional_data is None:
            additional_data = {}
        if phase_step_variant == InputSourceType.FILE_XML:
            return xml_f_i.TextFileInputXML(pi_data,
                                            filepath=additional_data.get(
                                                "filepath", None),
                                            xml_version=additional_data.get(
                                                "xml_version", None),
                                            should_strip_line=additional_data.get(
                                                "should_strip_line", False)
                                            )
        elif phase_step_variant == InputSourceType.FILE_JSON:
            return txt_f_i.TextFileInput(pi_data,
                                         filepath=additional_data.get(
                                             "filepath", None),
                                         should_strip_line=additional_data.get(
                                             "should_strip_line", False)
                                         )
        raise Exception(f"Unknown phase_step_variant: {phase_step_variant}")
