from typing import Generator

import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_base as ctjb
import src.postprocessing.output_preparation.compilers.shared.templates.compiler_template_base_multipart as tb_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.asm.templates.compiled_asm_data as cad
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd

import src.model.dao as dao_m
import src.model.aggregable_entity as aggregable_e

import src.files.file_utils as fu
import src.utilities.utils as u

"""
No differences at the moment from the super (Jinja Base) class.
"""


class CompilerASMTemplateJinja(ctjb.CompilerTemplateJinjaBase, tb_m.CompilerTemplateBaseMultipart):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_template_name: str = None,
                 key_template_skeleton: str = None,
                 key_template_instance_data: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 ):
        super().__init__(pipeline_item_data, optional_external_data,
                         key_template_name, key_template_skeleton, key_template_instance_data)
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name

    def get_all_parts_to_compile_as_generator(self, instance_data: dict, additional_data=None) -> Generator[crt.ConvertedSubpartTemplated, None, None]:
        tpbn = self.get_ith_input(
            additional_data, 3) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not isinstance(tpbn, template_provider.TemplateProviderByName):
            raise Exception("template provider by name needed")
        template_skeleton_dao = tpbn.provide_template_skeleton_by_name(
            template_name=[template_folder_path_base, "asm ___METTERE NELLE COSTANTI___"])

        """

        #
        # TAKEN FROM "optimized dao translator"
        #

        template_path = fu.concat_folder_filename('.', "Templates", "asm", "")
        name = dao.get_name()
        output_folder = "ASM"

        #

        return super().generate_file_from_template(
            template_path,
            "DAOML",
            output_folder,
            extension=".asm",
            name_output=name,
            additional_parametrs=asm_data,
            reuse_additional_params_dit=True
        )
        """
        asd: cad.CompiledASM_DAO = None  # TODO
        yield asd
