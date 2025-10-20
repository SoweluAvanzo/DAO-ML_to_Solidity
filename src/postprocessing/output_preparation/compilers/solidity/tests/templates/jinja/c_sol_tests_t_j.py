from typing import Generator

import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_base as ctjb
import src.postprocessing.output_preparation.compilers.shared.templates.compiler_template_base_multipart as tb_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.asm.templates.compiled_asm_data as cad
# import src.postprocessing.model_translation.shared.templates.conversion_result_template as crt
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd

import src.postprocessing.consts_template as consts_t

import src.postprocessing.model_translation.asm.t_j_asm as t_j_asm

# import src.model.dao as dao_m
# import src.model.aggregable_entity as aggregable_e

import src.files.file_utils as fu
import src.utilities.utils as utils
# import src.utilities.constants as consts

"""
_1_0_0
"""


class CompilerSolidityTestsTemplateJinja(ctjb.CompilerTemplateJinjaBase, tb_m.CompilerTemplateBaseMultipart):

    # TODO: PRENDERE ISPIRAZIONE DA C_J_ASM, che implementa c_t_j_multipart_
