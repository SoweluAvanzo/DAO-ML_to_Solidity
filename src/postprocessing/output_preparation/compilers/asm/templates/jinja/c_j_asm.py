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
No differences at the moment from the super (Jinja Base) class.
"""


class CompilerASMTemplateJinja(ctjb.CompilerTemplateJinjaBase, tb_m.CompilerTemplateBaseMultipart):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_template_instance_data: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 key_is_result_as_list: str = None
                 ):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_template_instance_data=key_template_instance_data,
                         key_template_skeleton=None
                         )
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name
        self.key_is_result_as_list = key_is_result_as_list
        self.is_compilation_result_a_list = True  # default

    def compile_diagram(self,
                        diagram_instance_data: t_j_asm.TranslatedDiagram_ASM_Jinja,
                        tpbn: template_provider.TemplateProviderByName
                        ) -> cad.CompiledASM_Diagram:
        """
        Override-designed
        """
        name = diagram_instance_data.get_name()
        diagram_compiled = ""  # we don't compile the Diagram: only the DAOs
        compilated = cad.CompiledASM_Diagram(
            diagram_instance_data.get_id(),
            name,
            compiled=diagram_compiled,
            can_diagram_be_compiled=False
        )
        return compilated

    def compile_DAO(self, diagram_instance_data: t_j_asm.TranslatedDiagram_ASM_Jinja,
                    tpbn: template_provider.TemplateProviderByName,
                    dao_translated: t_j_asm.TranslatedDAO_ASM_Jinja,
                    dao_templates_loaded_by_filename_cache: dict
                    ) -> cad.CompiledASM_DAO:
        """
        Override-designed
        """
        dao_id = dao_translated.get_id()
        template_filename_dao_in = dao_translated.template_filename_input
        template_filename_dao_out = utils.sanitize_name(
            dao_translated.template_filename_output)
        template_folder_path_base = dao_translated.template_full_folders_path_from_base

        template_filename_dao_out_no_ext = template_filename_dao_out
        index_extension = template_filename_dao_out.rfind(
            f".{consts_t.ASM_FILE_EXTENSION}")
        if index_extension >= 0:
            template_filename_dao_out_no_ext = template_filename_dao_out[:index_extension]
        template_skeleton_dao = ""
        if template_filename_dao_in in dao_templates_loaded_by_filename_cache:
            template_skeleton_dao = dao_templates_loaded_by_filename_cache[
                template_filename_dao_in]
        else:
            template_filename_dao_extension = f"{template_filename_dao_in}.{self.jinja_extension}"
            print(f"\n  on {type(self)} : BEFORE getting the ASM template skeletons for DAO .... template_folder_path_base: {template_folder_path_base} ; template_filename_dao_extension: {template_filename_dao_extension}")
            template_skeleton_dao = tpbn.provide_template_skeleton_by_name(
                template_name=[template_folder_path_base, template_filename_dao_extension])
            print(
                f"\n  on {type(self)} : AFTER getting the ASM template skeletons for DAO")
            # join the template into a single string
            if template_skeleton_dao is None:
                raise Exception(
                    f"CAN'T FIND asm TEMPLATE {fu.concat_folder_filename(template_folder_path_base, template_filename_dao_extension)}")
            if isinstance(template_skeleton_dao, list):
                template_skeleton_dao = "\n".join(
                    template_skeleton_dao)
            dao_templates_loaded_by_filename_cache[template_filename_dao_in] = template_skeleton_dao

        # now compile
        print(
            f"compiling DAO in ASM with ID: ({dao_id}) and output Name: ({template_filename_dao_out})")
        # each DAO do create a sub-folder holding everything in there, even the DAO itself
        compiled_dao = super().compile_single_template(
            template_skeleton_dao, dao_translated.entity_specific_data)
        compiled_dao_filename = fu.concat_folder_filename(
            template_folder_path_base, template_filename_dao_out_no_ext, template_filename_dao_out)
        print(
            f"on ASM, compiled_dao_filename: {compiled_dao_filename}")
        compiled_dao_struct = cad.CompiledASM_DAO(
            dao_id,
            compiled_dao_filename,
            compiled_dao
        )
        return compiled_dao_struct

    def get_all_parts_to_compile_as_generator(self, instance_data: dict, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        tpbn = self.get_ith_input(
            additional_data, 1) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not isinstance(tpbn, template_provider.TemplateProviderByName):
            raise Exception("template provider by name needed")
        if not isinstance(instance_data, t_j_asm.TranslatedDiagram_ASM_Jinja):
            raise Exception(
                f"Compile template ({self.__class__.__name__}) needs diagram_instance_data of class TranslatedDiagram_ASM_Jinja (TODO: 'or subclass'), but '{type(instance_data)}' was provided")
        diagram_instance_data: t_j_asm.TranslatedDiagram_ASM_Jinja = instance_data  # alias
        compilated: cad.CompiledASM_Diagram = self.compile_diagram(
            diagram_instance_data, tpbn)
        # now, the CORE
        dao_templates_loaded_by_filename_cache = {}  # cache
        for dao_id, dao_translated in diagram_instance_data.dao_converted_by_id.items():
            if dao_translated.can_be_converted():
                # get the template
                if not isinstance(dao_translated, t_j_asm.TranslatedDAO_ASM_Jinja):
                    print(
                        f"Can't convert DAO: {dao_id} - to ASM because the dao_translated is NOT a TranslatedDAO_ASM_Jinja instance: {type(dao_translated)}")
                    break
                compiled_dao_struct: cad.CompiledASM_DAO = self.compile_DAO(
                    diagram_instance_data,
                    tpbn,
                    dao_translated,
                    dao_templates_loaded_by_filename_cache
                )
                if compiled_dao_struct is not None:
                    # TO-DO: no ASM compilation of Committees or GovernanceArea ?
                    yield compiled_dao_struct
            else:
                print(
                    f"Can't convert DAO: {dao_id} - {dao_translated.get_name()} to ASM")
        if compilated.can_diagram_be_compiled:
            yield compilated

    def compile_template(self, instance_data: dict, additional_data=None):
        print(f"compiling ASM : {type(self)}")
        self.is_compilation_result_a_list = (self.key_is_result_as_list is None) or (additional_data is None) or (
            self.key_is_result_as_list in additional_data and additional_data[self.key_is_result_as_list])
        return tb_m.CompilerTemplateBaseMultipart.compile_template(self, instance_data, additional_data=additional_data)
