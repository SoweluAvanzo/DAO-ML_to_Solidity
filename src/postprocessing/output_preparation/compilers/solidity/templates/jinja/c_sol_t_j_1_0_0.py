from typing import Generator

import src.pipeline.pipeline_item as pi
# import src.model.diagram_manager as dm
# import src.postprocessing.output_preparation.templates.jinja.c_t_j_base as tjb
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd
import src.postprocessing.output_preparation.compilers.shared.templates.compiler_template_base_multipart as tb_m
import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_multipart as ctj_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_solidity_t_j as tjs
import src.postprocessing.output_preparation.compilers.solidity.compiled_solidity_data as csd
import src.postprocessing.model_translation.shared.translation_result_model as trm
import src.postprocessing.model_translation.shared.templates.translation_result_template as crt
import src.postprocessing.model_translation.solidity.solidity_translator_general as stg
import src.postprocessing.model_translation.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as conv_sol_jinja_1_0_0

import src.postprocessing.consts_template as consts_t
import src.files.file_utils as file_utils
import src.utilities.constants as consts
import src.files.file_utils as fu


class CompilerSolidityTemplateJinja_1_0_0(tjs.CompilerSolidityTemplateJinja, ctj_m.CompilerTemplateJinjaMultipart):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_diagram_instance_data: str = None,
                 key_diagram_model: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 key_is_result_as_list: str = None
                 ):
        """
        @param key_template_skeleton_provider_by_name: key of a function that, provided a template name, returns its skeleton.
        Must be an instance of "TemplateProviderByName"
        """
        tjs.CompilerSolidityTemplateJinja.__init__(self, pipeline_item_data,
                                                   optional_external_data=optional_external_data,
                                                   key_template_instance_data=key_diagram_instance_data,
                                                   key_template_skeleton=None,
                                                   key_diagram_model=key_diagram_model
                                                   )
        ctj_m.CompilerTemplateJinjaMultipart.__init__(self, pipeline_item_data,
                                                      optional_external_data=optional_external_data,
                                                      key_diagram_instance_data=key_diagram_instance_data,
                                                      key_diagram_model=key_diagram_model,
                                                      key_template_skeleton_provider_by_name=key_template_skeleton_provider_by_name,
                                                      key_is_result_as_list=key_is_result_as_list
                                                      )

    #

    def is_root_of_compilation(self, compiled_part: cgd.CompiledUnitWithID):
        return isinstance(compiled_part, csd.CompiledSolidityDiagram)

    def check_instance_data(self, instance_data: dict, additional_data=None):
        if not isinstance(instance_data, conv_sol_jinja_1_0_0.TranslatedDiagram_Jinja_1_0_0):
            raise Exception(
                f"Compile template ({type(self)}) needs instance_data of class TranslatedDiagram_Jinja_1_0_0 (TODO: 'or subclass'), but '{type(instance_data)}' was provided")
        return True

    #

    def add_template_extensions(self, fn: str):
        return f"{fn}.{consts.SOLIDITY_EXTENSION_OUTPUT}.jinja"

    def compile_all_parts_as_generator(self, instance_data: dict, tpbn: template_provider.TemplateProviderByName, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        diagram_instance_data: conv_sol_jinja_1_0_0.TranslatedDiagram_Jinja_1_0_0 = instance_data  # alias
        name = diagram_instance_data.get_name()
        # we don't compile the Diagram: only the DAOs (and Committes ... and GovernanceAreas?)
        diagram_compiled = ""
        # so, currently (2025-08-13) there's no use of : diagram_instance_data.entity_specific_data
        # neither of: tpbn
        compilated = csd.CompiledSolidityDiagram(
            diagram_instance_data.get_id(),
            name,
            compiled=diagram_compiled,
            can_diagram_be_compiled=False
        )
        # ... and ? let's start the DAO part
        dao_templates_loaded_by_filename = {}
        templates_loaded_by_filename_cache = {}
        # now, the CORE
        for dao_id, dao_translated in diagram_instance_data.daos_by_id.items():
            compiled_dao_struct: csd.CompiledSolidityDAO = None
            if dao_translated.can_be_converted():
                # get the template
                template_filename_dao_in = ""
                template_filename_dao_out = ""
                template_folder_path_base = ""
                if isinstance(dao_translated, conv_sol_jinja_1_0_0.TranslatedDAO_Jinja_1_0_0):
                    template_filename_dao_in = dao_translated.template_filename_input
                    template_filename_dao_out = dao_translated.translated_name_output
                    template_folder_path_base = dao_translated.suggested_input_template_folders_path_from_base
                else:
                    template_filename_dao_in = fu.sanitize_filename(
                        dao_translated.get_name())
                    template_filename_dao_out = template_filename_dao_in
                    template_folder_path_base = ""
                template_skeleton_dao = None
                if template_filename_dao_in in dao_templates_loaded_by_filename:
                    template_skeleton_dao = dao_templates_loaded_by_filename[template_filename_dao_in]
                else:
                    template_filename_dao_extension = f"{template_filename_dao_in}.{self.jinja_extension}"
                    template_skeleton_dao = tpbn.provide_template_skeleton_by_name(
                        template_name=[template_folder_path_base, template_filename_dao_extension])
                    # join the template into a single string
                    if template_skeleton_dao is None:
                        raise Exception(
                            f"CAN'T FIND TEMPLATE {file_utils.concat_folder_filename(template_folder_path_base, template_filename_dao_extension)}")
                    if isinstance(template_skeleton_dao, list):
                        template_skeleton_dao = "\n".join(
                            template_skeleton_dao)
                    dao_templates_loaded_by_filename[template_filename_dao_in] = template_skeleton_dao
                # now compile
                template_filename_dao_out = fu.sanitize_filename(
                    template_filename_dao_out)
                compiled_dao = super().compile_single_template(
                    template_skeleton_dao, dao_translated.entity_specific_data)
                # each DAO do create a sub-folder holding everything in there, even the DAO itself

                template_filename_dao_out_ext = f"{template_filename_dao_out}.{consts.SOLIDITY_EXTENSION_OUTPUT}"
                dao_folder_output_path = file_utils.concat_folder_filename(
                    template_folder_path_base, consts_t.FOLDERS_PATH_OUTPUT_SOLIDITY, template_filename_dao_out)
                compiled_dao_filename = file_utils.concat_folder_filename(
                    dao_folder_output_path, template_filename_dao_out_ext)
                compiled_dao_struct = csd.CompiledSolidityDAO(
                    dao_id, compiled_dao_filename, compiled_dao)
                if isinstance(dao_translated, conv_sol_jinja_1_0_0.TranslatedDAO_Jinja_1_0_0):
                    # COMPILE ALL OF THE FOLLOWING ANYTHING RELATED WITH A DAO (but not the DAO itself)
                    for map_compiled_adjacent_contracts in [
                        dao_translated.interfaces_and_fullpath_by_filenames,
                        dao_translated.conditions_converted_by_name
                    ]:
                        for filename, translated_thing in map_compiled_adjacent_contracts.items():
                            if translated_thing.can_be_converted():
                                template_input_filename_extension = f"{translated_thing.template_filename_input}.{self.jinja_extension}" \
                                    if not translated_thing.template_filename_input.endswith(self.jinja_extension) \
                                    else translated_thing.template_filename_input
                                template_skeleton = tpbn.provide_template_skeleton_by_name(template_name=[
                                    translated_thing.suggested_input_template_folders_path_from_base,
                                    template_input_filename_extension
                                ])
                                if isinstance(template_skeleton, list):
                                    template_skeleton = "\n".join(
                                        template_skeleton)
                                compiled_thing = super().compile_single_template(
                                    template_skeleton, translated_thing.entity_specific_data)
                                compiled_filename = file_utils.concat_folder_filename(
                                    dao_folder_output_path,
                                    translated_thing.suggested_input_template_folders_path_from_base, f"{translated_thing.translated_name_output}.{consts.SOLIDITY_EXTENSION_OUTPUT}")
                                compiled_thing_wrapper = cgd.CompiledUnitWithID(
                                    None, compiled_filename, compiled_thing)
                                compiled_dao_struct.interfaces_and_dao_related_compiled_contracts[
                                    filename] = compiled_thing_wrapper
                                yield compiled_thing_wrapper
                            # else:
                compilated.add_dao(compiled_dao_struct)
                yield compiled_dao_struct
            # else:
            for committee_id, committee_translated in dao_translated.committees_by_id.items():
                if committee_translated.can_be_converted():
                    # lists are allowed to load sub-templates in sub-folders
                    # i.e., lists are valid argument to :
                    # template_filename_simple_majority = ["voting_protocols", "simple_majority.{consts.SOLIDITY_EXTENSION_OUTPUT}.jinja"]
                    # template_skeleton__voting__simple_majority = tpbn.provide_template_skeleton_by_name( \
                    #     template_name=template_filename_simple_majority )
                    template_filename_input = ""
                    if isinstance(committee_translated, conv_sol_jinja_1_0_0.TranslatedCommittee_Jinja_1_0_0):
                        template_filename_input = committee_translated.template_filename_input
                    else:
                        template_filename_input = fu.sanitize_filename(
                            committee_translated.get_name())
                    template_skeleton_committee_path = file_utils.concat_folder_filename(
                        template_folder_path_base, consts_t.NAME_FOLDER_TEMPLATES_VOTING_PROTOCOL,
                        self.add_template_extensions(template_filename_input)
                    )
                    # recycle if possible
                    template_skeleton_committee = None
                    if template_filename_input in templates_loaded_by_filename_cache:
                        template_skeleton_committee = templates_loaded_by_filename_cache[
                            template_filename_input]
                    else:
                        template_skeleton_committee = tpbn.provide_template_skeleton_by_name(
                            template_name=template_skeleton_committee_path)
                        if isinstance(template_skeleton_committee, list):
                            template_skeleton_committee = "\n".join(
                                template_skeleton_committee)
                        templates_loaded_by_filename_cache[template_filename_input] = template_skeleton_committee
                    # committee_folder_output_path = file_utils.check_and_make_folder([ ...])
                    committee_folder_output_path = dao_folder_output_path
                    compiled_committee_fullpath = file_utils.concat_folder_filename(
                        committee_folder_output_path, f"{committee_translated.translated_name_output}.{consts.SOLIDITY_EXTENSION_OUTPUT}")
                    compiled_committee = super().compile_single_template(
                        template_skeleton_committee, committee_translated.entity_specific_data)
                    compiled_committee_struct = csd.CompiledSolidityCommittee(
                        committee_id, compiled_committee_fullpath, compiled_committee)
                    compiled_dao_struct.add_committee_data_to_dao(
                        compiled_committee_struct)
                    yield compiled_committee_struct
                else:
                    print(
                        f"Can't convert COMMITTEE: {committee_id} - {committee_translated.get_name()}")
                """
                TODO (20/10/2025)
                if isinstance(committee_translated, conv_sol_jinja_1_0_0.TranslatedCommittee_Jinja_1_0_0):
                    committee_translated.additional_modules_instances_by_name
                """
        yield compilated
