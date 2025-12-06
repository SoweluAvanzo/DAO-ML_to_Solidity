
import src.pipeline.pipeline_item as pi
import src.pipeline.utilities.pi_str as pstr

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb
import src.phases_builders.shared as pb_shared

import src.input.xml_file_input as xml_f_i
import src.input.txt_file_input as txt_f_i

import src.utilities.utils as u
import src.utilities.errors as e_c


class InputTypeSourceFormat(psv.PhaseSubstepVariants):
    FILE_XML = (pb_shared.PersistanceType.FILE.value,
                pb_shared.ModelPersistanceFormat.XML.value)
    FILE_JSON = (pb_shared.PersistanceType.FILE.value,
                 pb_shared.ModelPersistanceFormat.JSON.value)
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


REVERSE_MAPPING_InputTypeSourceFormat = {
    v.value: v for v in InputTypeSourceFormat}

#


class AdditionalDataInput(pb.AdditionalDataSubPhase):
    def __init__(self, phase_step_variant: InputTypeSourceFormat, filepath: str,
                 should_strip_line: bool = False
                 ):
        if not (isinstance(phase_step_variant, InputTypeSourceFormat) or (phase_step_variant[0] == pb_shared.PersistanceType.FILE)):
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
        super().__init__(InputTypeSourceFormat.FILE_XML,
                         filepath, should_strip_line=should_strip_line)
        self.xml_version = xml_version


class FileJSONAdditionalDataSubPhase(AdditionalDataInput):
    def __init__(self, filepath: str,
                 should_strip_line: bool = False
                 ):
        super().__init__(InputTypeSourceFormat.FILE_JSON,
                         filepath, should_strip_line=should_strip_line)

#


def input_persistance_type_format(p_t: pb_shared.PersistanceType, m_p_f: pb_shared.ModelPersistanceFormat) -> InputTypeSourceFormat:
    # TODO: refactor with "match/case" unpon developing more Persistance Types and Input Formats
    if p_t == pb_shared.PersistanceType.FILE:
        if m_p_f == pb_shared.ModelPersistanceFormat.XML:
            return InputTypeSourceFormat.FILE_XML
        elif m_p_f == pb_shared.ModelPersistanceFormat.JSON:
            return InputTypeSourceFormat.FILE_JSON
    raise Exception(
        f"Unknown/unmanaged persistance type & input format pair: < {p_t} ; {m_p_f} >")


class InputFactory(pb.PipelineItemFactory):

    def __init__(self, key_unique_producer: pb_shared.KeyUniqueProducer,
                 printer_debug: u.PrinterDebug = None):
        super().__init__(key_unique_producer, printer_debug=printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return InputTypeSourceFormat

    def new_pipeline_item_from_variant(self,
                                       phase_step_variant_and_data: pb.AdditionalDataSubPhase
                                       ) -> list[pi.PipelineItem]:
        # the real factory
        if phase_step_variant_and_data.phase_step_variant == InputTypeSourceFormat.FILE_XML:
            if not isinstance(phase_step_variant_and_data, FileXMLAdditionalDataSubPhase):
                raise Exception(
                    f"Additional Data is expected to be a (sub)class of FileXMLAdditionalDataSubPhase, but is: {type(phase_step_variant_and_data)}")
            key_input = self.new_unique_key(
                f"key_input_{phase_step_variant_and_data.phase_step_variant.name}")
            k_filepath_provider = self.new_unique_key("k_filepath_provider")
            filepath_provider = pstr.PIStr(
                pi.PIData(k_filepath_provider, None),
                val=phase_step_variant_and_data.filepath
            )
            return pb.PipelineItemsGenerated([
                filepath_provider,
                xml_f_i.TextFileInputXML(
                    pi.PIData(key_input, [k_filepath_provider]),
                    filepath=phase_step_variant_and_data.filepath,
                    xml_version=phase_step_variant_and_data.xml_version,
                    should_strip_line=phase_step_variant_and_data.should_strip_line
                )
            ],
                key_input
            )
        elif phase_step_variant_and_data.phase_step_variant == InputTypeSourceFormat.FILE_JSON:
            if not isinstance(phase_step_variant_and_data, FileJSONAdditionalDataSubPhase):
                raise Exception(
                    f"Additional Data is expected to be a (sub)class of FileXMLAdditionalDataSubPhase, but is: {type(phase_step_variant_and_data)}")
            key_input = self.new_unique_key(
                f"key_input_{phase_step_variant_and_data.phase_step_variant.name}")
            k_filepath_provider = self.new_unique_key("k_filepath_provider")
            filepath_provider = pstr.PIStr(
                pi.PIData(k_filepath_provider, None),
                val=phase_step_variant_and_data.filepath
            )
            return pb.PipelineItemsGenerated([
                filepath_provider,
                txt_f_i.TextFileInput(
                    pi.PIData(key_input, [k_filepath_provider]),
                    filepath=phase_step_variant_and_data.filepath,
                    should_strip_line=phase_step_variant_and_data.should_strip_line
                )
            ],
                key_input
            )
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                        " : " + phase_step_variant_and_data.phase_step_variant.value)
