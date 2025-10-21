from typing import Generator

import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_multipart as ctj_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.solidity.tests.compiled_sol_test_data as c_st_data
# import src.postprocessing.model_translation.shared.templates.conversion_result_template as crt
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd

import src.postprocessing.model_translation.solidity.tests.solidity_tests_translator as st_t
import src.postprocessing.model_translation.solidity.tests.jinja.solidity_tests_translator_jinja_hardhat as st_t_j

# import src.model.dao as dao_m
# import src.model.aggregable_entity as aggregable_e


import src.postprocessing.consts_template as consts_t
import src.files.file_utils as fu
import src.utilities.utils as utils
# import src.utilities.constants as consts

"""
_1_0_0
"""


class CompilerSolidityTestsTemplateJinja(ctj_m.CompilerTemplateJinjaMultipart):
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

    # TODO: PRENDERE ISPIRAZIONE DA C_J_ASM, che implementa c_t_j_multipart_

    def is_root_of_compilation(self, compiled_part: cgd.CompiledUnitWithID):
        return isinstance(compiled_part, c_st_data.CompiledSolidityTest_Diagram)

    def check_instance_data(self, instance_data: dict, additional_data=None):
        if not isinstance(instance_data, st_t.TranslatedDiagram_SolidityTest):
            raise Exception(
                f"instance_data is of type {type(instance_data)} rether than TranslatedDiagram_ASM_Jinja")
        return True

    #

    def compile_diagram(self,
                        diagram_instance_data: st_t.TranslatedDiagram_SolidityTest,
                        tpbn: template_provider.TemplateProviderByName
                        ) -> c_st_data.CompiledSolidityTest_Diagram:
        """
        Override-designed
        """
        name = diagram_instance_data.get_name()
        diagram_compiled = ""  # we don't compile the Diagram: only the DAOs
        compilated = c_st_data.CompiledSolidityTest_Diagram(
            diagram_instance_data.get_id(),
            name,
            compiled=diagram_compiled,
            can_diagram_be_compiled=False
        )
        return compilated

    def compile_DAO(self, diagram_instance_data: st_t.TranslatedDiagram_SolidityTest,
                    tpbn: template_provider.TemplateProviderByName,
                    dao_translated: st_t.TranslatedDAO_SolidityTest,
                    dao_templates_loaded_by_filename_cache: dict
                    ) -> st_t.TranslatedDAO_SolidityTest:

        # TODO
        return None

    def compile_all_parts_as_generator(self, instance_data: dict, tpbn: template_provider.TemplateProviderByName, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        diagram_instance_data: st_t.TranslatedDiagram_SolidityTest = instance_data  # alias
        compilated: c_st_data.CompiledSolidityTest_Diagram = self.compile_diagram(
            diagram_instance_data, tpbn)

        # TODO: this WHOLE BODY is taken from "c_j_asm.py" AND CAN BE ABSTRACTED AWAY
        # now, the CORE
        dao_templates_loaded_by_filename_cache = {}  # cache
        for dao_id, dao_translated in diagram_instance_data.daos_by_id.items():
            if dao_translated.can_be_converted():
                # get the template
                if not isinstance(dao_translated, st_t.TranslatedDAO_SolidityTest):
                    print(
                        f"Can't convert DAO: {dao_id} - to ASM because the dao_translated is NOT a TranslatedDAO_ASM_Jinja instance: {type(dao_translated)}")
                    break
                compiled_dao_struct: st_t.TranslatedDAO_SolidityTest = self.compile_DAO(
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
