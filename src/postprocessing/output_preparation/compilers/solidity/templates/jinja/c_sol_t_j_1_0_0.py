from typing import Generator

import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_multipart as ctj_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.shared.templates.compiled_model_data_templated as cmdt
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_solidity_t_j as tjs
import src.postprocessing.output_preparation.compilers.solidity.templates.compiled_model_solidity_t as cmst
import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt

import src.postprocessing.model_translation.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as conv_sol_jinja_1_0_0

import src.postprocessing.consts_template as consts_t
import src.files.file_utils as file_utils
import src.utilities.constants as consts
import src.utilities.utils as u
import src.utilities.errors as e_c

KEY__TEMPLATE_FOLDER_PATH_BASE = "template_folder_path_base"
KEY__DAO_FOLDER_OUTPUT_PATH = "dao_folder_output_path"


class CompilerSolidityTemplateJinja_1_0_0(tjs.CompilerSolidityTemplateJinja, ctj_m.CompilerTemplateJinjaMultipart):
    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_diagram_instance_data: str = None,
                 key_diagram_model: str = None,
                 key_template_skeleton_provider_by_name: str = None,
                 key_is_result_as_list: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        """
        @param key_template_skeleton_provider_by_name: key of a function that, provided a template name, returns its skeleton.
        Must be an instance of "TemplateProviderByName"
        """
        tjs.CompilerSolidityTemplateJinja.__init__(
            self, pipeline_item_data,
            optional_external_data=optional_external_data,
            key_template_instance_data=key_diagram_instance_data,
            key_template_skeleton=None,
            key_diagram_model=key_diagram_model,
            printer_debug=printer_debug
        )
        ctj_m.CompilerTemplateJinjaMultipart.__init__(
            self, pipeline_item_data,
            optional_external_data=optional_external_data,
            key_diagram_instance_data=key_diagram_instance_data,
            key_diagram_model=key_diagram_model,
            key_template_skeleton_provider_by_name=key_template_skeleton_provider_by_name,
            key_is_result_as_list=key_is_result_as_list,
            printer_debug=printer_debug
        )

    #

    def is_root_of_compilation(self, compiled_part: cmdt.CompiledWithOutputPath) -> bool:
        return isinstance(compiled_part, cmst.CompiledSolidityDiagramTemplated)

    def check_instance_data(self, instance_data: dict, additional_data=None):
        if not isinstance(instance_data, conv_sol_jinja_1_0_0.TranslatedDiagram_Jinja_1_0_0):
            raise Exception(
                f"Compile template ({type(self)}) needs instance_data of class TranslatedDiagram_Jinja_1_0_0 (TODO: 'or subclass'), but '{type(instance_data)}' was provided")
        return True

    #

    def add_template_extensions(self, fn: str):
        return f"{fn}.{consts.SOLIDITY_EXTENSION_OUTPUT}.jinja"

    #
    #

    # TODO: (2025-01-24) START REFACTORING THE "compile_all_parts_as_generator" BY SPLITTING IT INTO THESE SUB-PARTS (for easier extension in subclasses)

    def compile_governance_area(self, diagram_translated: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated, governance_area_translated: trmt.TranslatedGovernanceAreaTemplated, additional_data=None) -> cmst.CompiledSolidityGovernanceAreaTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        """
        Overriding the parameter type to a Template-specific subclass
        """
        self.print_error(
            f"Can't compile a Governance Area: {e_c.ERROR_TEXT__NOT_IMPLEMENTED}")
        yield None

    def compile_committee(self, diagram_translated: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated, committee_translated: trmt.TranslatedCommitteeTemplated, additional_data=None) -> cmst.CompiledSolidityCommitteeTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        dao_templates_loaded_by_filename: dict[str, str] = \
            additional_data["dao_templates_loaded_by_filename"]
        templates_loaded_by_filename_cache: dict[str, str] = \
            additional_data["templates_loaded_by_filename_cache"]
        template_folder_path_base: str = additional_data[KEY__TEMPLATE_FOLDER_PATH_BASE]
        dao_folder_output_path: str = additional_data[KEY__DAO_FOLDER_OUTPUT_PATH]
        tpbn: template_provider.TemplateProviderByName = self.get_template_skeleton_provider_by_name(

            additional_data)
        #
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
                template_filename_input = file_utils.sanitize_filename(
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
            committee_id: str = committee_translated.get_id()
            compiled_committee_struct = cmst.CompiledSolidityCommitteeTemplated(
                committee_id, compiled_committee,
                output_full_path=compiled_committee_fullpath
            )
            yield compiled_committee_struct
        else:
            print(
                f"Can't convert COMMITTEE: {committee_id} - {committee_translated.get_name()}")
            yield None

    def compile_dao(self, diagram_translated: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated, additional_data=None) -> cmst.CompiledSolidityDAOTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        dao_templates_loaded_by_filename: dict[str, str] = \
            additional_data["dao_templates_loaded_by_filename"]
        templates_loaded_by_filename_cache: dict[str, str] = \
            additional_data["templates_loaded_by_filename_cache"]
        tpbn: template_provider.TemplateProviderByName = self.get_template_skeleton_provider_by_name(
            additional_data)
        #
        template_folder_path_base = ""
        dao_id: str = dao_translated.get_id()
        compiled_dao_struct: cmst.CompiledSolidityDAOTemplated = None
        if dao_translated.can_be_converted():
            # get the template
            template_filename_dao_in = ""
            template_filename_dao_out = ""
            if isinstance(dao_translated, conv_sol_jinja_1_0_0.TranslatedDAO_Jinja_1_0_0):
                template_filename_dao_in = dao_translated.template_filename_input
                template_filename_dao_out = dao_translated.translated_name_output
                template_folder_path_base = dao_translated.suggested_input_template_folders_path_from_base
            else:
                template_filename_dao_in = file_utils.sanitize_filename(
                    dao_translated.get_name())
                template_filename_dao_out = template_filename_dao_in
                template_folder_path_base = ""
            template_skeleton_dao = None
            if template_filename_dao_in in dao_templates_loaded_by_filename:
                template_skeleton_dao = dao_templates_loaded_by_filename[template_filename_dao_in]
            else:
                template_filename_dao_extension = f"{template_filename_dao_in}.{self.jinja_extension}"
                self.print_msg(
                    f"in {type(self)}, compiling all parts as generator, .... -> template_folder_path_base: ::{template_folder_path_base}## , template_filename_dao_extension: ::{template_filename_dao_extension}##")
                template_skeleton_dao = tpbn.provide_template_skeleton_by_name(
                    template_name=[template_folder_path_base, template_filename_dao_extension])
                # join the template into a single string
                if template_skeleton_dao is None:
                    raise Exception(
                        f"CAN'T FIND TEMPLATE {file_utils.concat_folder_filename(template_folder_path_base, template_filename_dao_extension)}")
                elif isinstance(template_skeleton_dao, list):
                    self.print_msg(
                        f"template_skeleton_dao (in type: {type(self)})")
                    self.print_msg(template_skeleton_dao)
                    filtered_tsd = [
                        line for line in template_skeleton_dao if line is not None]
                    if len(template_skeleton_dao) != len(filtered_tsd):
                        raise Exception(
                            f"In class ({type(self)}), the template at '{file_utils.concat_folder_filename(template_folder_path_base, template_filename_dao_extension)}' is reading some None lines ({len(template_skeleton_dao) - len(filtered_tsd)} out of {len(template_skeleton_dao)} are None)")
                    template_skeleton_dao = "\n".join(
                        template_skeleton_dao)
                dao_templates_loaded_by_filename[template_filename_dao_in] = template_skeleton_dao
            # now compile
            template_filename_dao_out = file_utils.sanitize_filename(
                template_filename_dao_out)
            compiled_dao = super().compile_single_template(
                template_skeleton_dao, dao_translated.entity_specific_data)
            # each DAO do create a sub-folder holding everything in there, even the DAO itself

            template_filename_dao_out_ext = f"{template_filename_dao_out}.{consts.SOLIDITY_EXTENSION_OUTPUT}"
            dao_folder_output_path = file_utils.concat_folder_filename(
                template_folder_path_base, consts_t.FOLDERS_PATH_OUTPUT_SOLIDITY, template_filename_dao_out)
            compiled_dao_filename = file_utils.concat_folder_filename(
                dao_folder_output_path, template_filename_dao_out_ext)
            compiled_dao_struct = cmst.CompiledSolidityDAOTemplated(
                dao_id, compiled_dao,
                output_full_path=compiled_dao_filename
            )
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
                            compiled_thing_wrapper = cmdt.CompiledWithOutputPath(
                                None, compiled_thing,
                                output_full_path=compiled_filename
                            )
                            compiled_dao_struct.interfaces_and_dao_related_compiled_contracts[
                                filename] = compiled_thing_wrapper
                            yield compiled_thing_wrapper
                        # else:
        # else:
        additional_data[KEY__TEMPLATE_FOLDER_PATH_BASE] = template_folder_path_base
        additional_data[KEY__DAO_FOLDER_OUTPUT_PATH] = dao_folder_output_path
        for committee_id, committee_translated in dao_translated.committees_by_id.items():
            compiled_things = self.compile_committee(diagram_translated,
                                                     dao_translated,
                                                     committee_translated,
                                                     additional_data=additional_data
                                                     )
            if compiled_things is not None:
                if not u.is_generator(compiled_things):
                    compiled_things = [compiled_things]  # make it iterable
                for compiled_part in compiled_things:
                    if isinstance(compiled_part, cmst.CompiledSolidityCommitteeTemplated):
                        compiled_dao_struct.add_committee_data_to_dao(
                            compiled_part)
                    yield compiled_part
            """
            TODO (20/10/2025)
            if isinstance(committee_translated, conv_sol_jinja_1_0_0.TranslatedCommittee_Jinja_1_0_0):
                committee_translated.additional_modules_instances_by_name
            """
        """
        TODO (04/02/2026) - compile also the GovernanceAreas related to the DAO (if any) ... shoulw we?
        """
        for governance_area_id, governance_area_translated in dao_translated.governance_areas_by_id.items():
            compiled_things = self.compile_governance_area(diagram_translated,
                                                           dao_translated,
                                                           governance_area_translated,
                                                           additional_data=additional_data
                                                           )
            if compiled_things is not None:
                if not u.is_generator(compiled_things):
                    compiled_things = [compiled_things]  # make it iterable
                for compiled_part in compiled_things:
                    if isinstance(compiled_part, cmst.CompiledSolidityGovernanceAreaTemplated):
                        compiled_dao_struct.add_governance_area_to_dao(
                            compiled_part)
                    yield compiled_part
        # DAO done
        del additional_data[KEY__TEMPLATE_FOLDER_PATH_BASE]
        del additional_data[KEY__DAO_FOLDER_OUTPUT_PATH]
        yield compiled_dao_struct

    def compile_diagram(self, diagram_translated: trmt.TranslatedDiagramTemplated, additional_data=None) -> cmst.CompiledSolidityDiagramTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        if additional_data is None:
            additional_data = {}
        diagram_instance_data: conv_sol_jinja_1_0_0.TranslatedDiagram_Jinja_1_0_0 = diagram_translated  # alias
        name = diagram_instance_data.get_name()
        # we don't compile the Diagram: only the DAOs (and Committes ... and GovernanceAreas?)
        diagram_compiled = f"N/A: in current implementation (2025-12-18) of the Solidity Converter ({type(self)}), there's no implementation of the Diagram"
        # so, currently (2025-08-13) there's no use of : diagram_instance_data.entity_specific_data
        # neither of: tpbn
        template_filename_diagram_out = file_utils.sanitize_filename(name)
        template_filename_diagram_out_ext = f"{template_filename_diagram_out}.{consts.SOLIDITY_EXTENSION_OUTPUT}"
        diagram_folder_output_path = file_utils.concat_folder_filename(
            diagram_instance_data.suggested_input_template_folders_path_from_base, consts_t.FOLDERS_PATH_OUTPUT_SOLIDITY, template_filename_diagram_out
        )
        compiled_diagram_filename = file_utils.concat_folder_filename(
            diagram_folder_output_path, template_filename_diagram_out_ext)
        # the compiled diagram
        compiled_diagram = cmst.CompiledSolidityDiagramTemplated(diagram_instance_data.get_id(),
                                                                 compiled=diagram_compiled,
                                                                 output_full_path=compiled_diagram_filename,
                                                                 can_diagram_be_compiled=False  # might change in the future
                                                                 )
        # ... and ? let's start the DAO part
        dao_templates_loaded_by_filename: dict[str, str] = {}
        templates_loaded_by_filename_cache: dict[str, str] = {}
        # ... prepare the additional data to pass to data required by sub-compilations
        additional_data["dao_templates_loaded_by_filename"] = dao_templates_loaded_by_filename
        additional_data["templates_loaded_by_filename_cache"] = templates_loaded_by_filename_cache
        # now, the CORE
        for dao_id, dao_translated in diagram_instance_data.daos_by_id.items():
            compiled_things = self.compile_dao(
                diagram_translated, dao_translated, additional_data=additional_data)
            if compiled_things is not None:
                if not u.is_generator(compiled_things):
                    compiled_things = [compiled_things]  # make it iterable
                for compiled_part in compiled_things:
                    if isinstance(compiled_part, cmst.CompiledSolidityDAOTemplated):
                        compiled_diagram.add_dao(compiled_part)
                    yield compiled_part
        del additional_data["dao_templates_loaded_by_filename"]
        del additional_data["templates_loaded_by_filename_cache"]
        yield compiled_diagram

    #
    #
    #

    def compile_all_parts_as_generator(self, instance_data: dict, tpbn: template_provider.TemplateProviderByName, additional_data=None) -> Generator[cmdt.CompiledWithOutputPath, None, None]:
        diagram_instance_data: conv_sol_jinja_1_0_0.TranslatedDiagram_Jinja_1_0_0 = instance_data  # alias
        if additional_data is None:
            additional_data = {}
        compiled: cmst.CompiledSolidityDiagramTemplated | Generator[cmdt.CompiledWithOutputPath, None, None] = self.compile_diagram(
            instance_data,
            additional_data=additional_data
        )
        if u.is_generator(compiled):
            yield from compiled
        else:
            yield compiled
