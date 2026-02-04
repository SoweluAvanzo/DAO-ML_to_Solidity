from typing import Generator

import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.compiled_unit_with_id as cuwid
import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_multipart as ctj_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_sol_t_j_1_0_0 as tjs_1_0_0
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_solidity_t_j as tjs
import src.postprocessing.output_preparation.compilers.solidity.compiled_model_solidity as csd
import src.postprocessing.model_translation.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as conv_sol_jinja_1_0_0

import src.postprocessing.consts_template as consts_t
import src.files.file_utils as file_utils
import src.utilities.constants as consts
import src.utilities.utils as u


class CompilerSolidityTemplateJinja_1_1_0(tjs_1_0_0.CompilerSolidityTemplateJinja_1_0_0):
    def __init__(self, pipeline_item_data: pi.PIData,
                 optional_external_data=None,
                 key_diagram_instance_data: str = None,
                 key_diagram_model: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 key_is_result_as_list: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        if not isinstance(pipeline_item_data, pi.PIData):
            raise Exception(
                f"pipeline_item_data is not a PIData: {type(pipeline_item_data)}")
        tjs_1_0_0.CompilerSolidityTemplateJinja_1_0_0.__init__(
            self,
            pipeline_item_data,
            optional_external_data=optional_external_data,
            key_diagram_instance_data=key_diagram_instance_data,
            key_diagram_model=key_diagram_model,
            key_template_skeleton_provider_by_name=key_template_skeleton_provider_by_name,
            key_is_result_as_list=key_is_result_as_list,
            printer_debug=printer_debug
        )
