
import src.pipeline.pipeline_item as pi

import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.shared as pb_shared

import src.input.xml_file_input as xml_f_i
import src.input.txt_file_input as txt_f_i

import src.utilities.utils as u


def output_format_type(i_s: pb_shared.PersistanceType, pp_type: pb_pp.PostProcessingTransformation) -> any:
    if i_s == pb_shared.PersistanceType.FILE:
        raise Exception("Not implemented yet")
        """
        if i_t == InputType.XML:
            return InputSourceType.FILE_XML
        elif i_t == InputType.JSON:
            return InputSourceType.FILE_JSON
        """
    raise Exception(
        f"Unknown/unmanaged input source-type pair: < {i_s} ; {i_t} >")
