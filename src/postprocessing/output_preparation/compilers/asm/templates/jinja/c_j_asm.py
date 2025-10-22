import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_standard_model_multipart as c_t_j_sm_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.asm.templates.compiled_asm_data as cad
# import src.postprocessing.model_translation.shared.templates.conversion_result_template as crt
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd
import src.postprocessing.output_preparation.compilers.shared.compiled_model_data as cmd

import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt
import src.postprocessing.model_translation.asm.t_j_asm as t_j_asm

import src.postprocessing.consts_template as consts_t

"""
No differences at the moment from the super (Jinja Base) class.
"""


# (ctj_m.CompilerTemplateJinjaMultipart):
class CompilerASMTemplateJinja(c_t_j_sm_m.CompilerStandardModelMultipart_TemplateJinja):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_diagram_instance_data: str = None,
                 key_diagram_model: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 key_is_result_as_list: str = None
                 ):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_diagram_instance_data=key_diagram_instance_data,
                         key_diagram_model=key_diagram_model,
                         key_template_skeleton_provider_by_name=key_template_skeleton_provider_by_name,
                         key_is_result_as_list=key_is_result_as_list
                         )

    #

    def get_compiled_file_extension(self) -> str:
        return consts_t.ASM_FILE_EXTENSION

    def is_root_of_compilation(self, compiled_part: cgd.CompiledUnitWithID):
        return isinstance(compiled_part, cad.CompiledASM_Diagram)

    #

    def compile_committee(self, diagram_instance_data: trmt.TranslatedDiagramTemplated,
                          tpbn: template_provider.TemplateProviderByName,
                          dao_translated: trmt.TranslatedDAOTemplated,
                          templates_loaded_by_filename_cache: dict,
                          committee_translated: trmt.TranslatedCommitteeTemplated,
                          ) -> cmd.CompiledCommitteeData:
        return None  # nothing to compile here

    #

    def check_translated_dao(self, dao_translated) -> bool:
        return isinstance(dao_translated, t_j_asm.TranslatedDAO_ASM_Jinja)

    def new_compiled_DAO(self, diagram_instance_data: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated, name_dao: str, compiled_dao) -> cmd.CompiledDAOData:
        dao_id = dao_translated.get_id()
        compiled_dao_struct = cad.CompiledASM_DAO(
            dao_id,
            name_dao,
            compiled_dao
        )
        return compiled_dao_struct

#

    def new_compiled_diagram(self, diagram_instance_data: trmt.TranslatedDiagramTemplated,  name_diagram: str, compiled_diagram) -> cmd.CompiledDiagramData:
        compilated = cad.CompiledASM_Diagram(
            diagram_instance_data.get_id(),
            name_diagram,
            compiled=compiled_diagram,
            can_diagram_be_compiled=False
        )
        return compilated

    def check_instance_data(self, instance_data: dict, additional_data=None):
        if not isinstance(instance_data, t_j_asm.TranslatedDiagram_ASM_Jinja):
            raise Exception(
                f"instance_data is of type {type(instance_data)} rether than TranslatedDiagram_ASM_Jinja")
        return True

    def compile_diagram(self,
                        diagram_instance_data: t_j_asm.TranslatedDiagram_ASM_Jinja,
                        tpbn: template_provider.TemplateProviderByName
                        ) -> cad.CompiledASM_Diagram:
        """
        Override-designed
        """
        name = diagram_instance_data.get_name()
        diagram_compiled = ""  # we don't compile the Diagram: only the DAOs
        compilated = self.new_compiled_diagram(
            diagram_instance_data, name, diagram_compiled)
        return compilated
