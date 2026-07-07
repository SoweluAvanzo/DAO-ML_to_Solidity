from typing import Generator

import src.pipeline.pipeline_item as pi

import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_multipart as ctj_m
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd
import src.postprocessing.output_preparation.compilers.shared.compiled_model_data as cmd

import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt

import src.files.file_utils as fu
import src.utilities.errors as e_c


class CompilerStandardModelMultipart_TemplateJinja(ctj_m.CompilerTemplateJinjaMultipart):
    """
    <summary>
    <p>
    <div>
    Class that partially implement the Diagram compilation, by compiling it and their DAOs.
    Basically, it's the implementation of the "Strategy" pattern, leaving the abstract parts
    free to be overridden. In particular, the following methods must be implemented:
    <div>
    <ul>
    <li>is_root_of_compilation: check whether the given compilation result is the "root" of the whole compilation (usually, the Diagram-related instance)</li>
    <li>is_template_skeleton_provider: it's already implemented by checking "isinstance" of "template_provider_by_name.TemplateProviderByName", but could be overridden</li>
    <li>check_instance_data: check whether the "instance_data" (provided by the pipeline dependence) is an object created by a previously-run Translator;
      it usually checks for a subclass of "translation_result_model.TranslatedDiagram"</li>
    <li>compile_diagram: upon passing the check above, You need to compile a Diagram</li>
    <li>check_translated_dao: similarly to "check_instance_data", it checks if the provided translated DAO is of a correct class</li>
    <li>compile_DAO: similar to "compile_diagram"</li>
    <li>check_translated_committee: similarly to "check_translated_dao", it checks if the provided translated committee is of a correct class</li>
    <li>compile_committee: similar to "compile_DAO"</li>
    </ul>
    <p>
    </summary>
    """

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

    def get_compiled_file_extension(self) -> str:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compose_compiled_thing_output_path(self, tag_what_this_it: str, *parts: str) -> str:
        """
        Override-designed
        """
        return fu.concat_folder_filename(*parts)

    #

    def check_translated_committee(self, committee_translated) -> bool:
        """
        Override-designed
        Usual implementation:
        isinstance(committee_translated, trmt.TranslatedCommittee)
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def new_compiled_committee(self, diagram_instance_data: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated,
                               committee_translated: trmt.TranslatedCommitteeTemplated, name_committee: str, compiled_committee) -> cmd.CompiledCommitteeData:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_committee(self, diagram_instance_data: trmt.TranslatedDiagramTemplated,
                          tpbn: template_provider.TemplateProviderByName,
                          dao_translated: trmt.TranslatedDAOTemplated,
                          templates_loaded_by_filename_cache: dict,
                          committee_translated: trmt.TranslatedCommitteeTemplated,
                          ) -> cmd.CompiledCommitteeData:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

#

    #

    def check_translated_dao(self, dao_translated) -> bool:
        """
        Override-designed
        Usual implementation:
        isinstance(dao_translated, trmt.TranslatedDAOTemplated)
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def new_compiled_DAO(self, diagram_instance_data: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated,  name_dao: str, compiled_dao) -> cmd.CompiledDAOData:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_DAO(self, diagram_instance_data: trmt.TranslatedDiagramTemplated,
                    tpbn: template_provider.TemplateProviderByName,
                    dao_translated: trmt.TranslatedDAOTemplated,
                    templates_loaded_by_filename_cache: dict
                    ) -> cmd.CompiledDAOData:
        """
        Override-designed
        """
        dao_id = dao_translated.get_id()
        template_filename_dao_in = dao_translated.template_filename_input
        template_filename_dao_out = fu.sanitize_filename(
            dao_translated.translated_name_output)
        template_folder_path_base = dao_translated.suggested_input_template_folders_path_from_base
        # the filename OUT might have already built in the extention -> extract the name from
        template_filename_dao_out_ext = f"{template_filename_dao_out}.{self.get_compiled_file_extension()}"
        template_skeleton_dao = ""
        if template_filename_dao_in in templates_loaded_by_filename_cache:
            template_skeleton_dao = templates_loaded_by_filename_cache[
                template_filename_dao_in]
        else:
            template_filename_dao_extension = f"{template_filename_dao_in}.{self.jinja_extension}"
            template_skeleton_dao = tpbn.provide_template_skeleton_by_name(
                template_name=[template_folder_path_base, template_filename_dao_extension])
            # join the template into a single string
            if template_skeleton_dao is None:
                raise Exception(
                    f"CAN'T FIND A TEMPLATE {fu.concat_folder_filename(template_folder_path_base, template_filename_dao_extension)}")
            if isinstance(template_skeleton_dao, list):
                template_skeleton_dao = "\n".join(
                    template_skeleton_dao)
            templates_loaded_by_filename_cache[template_filename_dao_in] = template_skeleton_dao

        # now compile
        print(
            f"compiling DAO in in translator <{type(self)}> with ID: ({dao_id}) and output Name: ({template_filename_dao_out})")
        # each DAO do create a sub-folder holding everything in there, even the DAO itself
        compiled_dao = super().compile_single_template(
            template_skeleton_dao, dao_translated.entity_specific_data)
        compiled_dao_filename = self.compose_compiled_thing_output_path("dao",
                                                                        template_folder_path_base, template_filename_dao_out, template_filename_dao_out_ext)

        compiled_dao_struct: cmd.CompiledDAOData = self.new_compiled_DAO(
            diagram_instance_data, dao_translated, compiled_dao_filename, compiled_dao)

        # committee
        for committee_id, committee_translated in dao_translated.committees_by_id.items():
            if not self.check_translated_committee(committee_translated):
                print(
                    f"Can't convert Committee: {committee_id} - in translator <{type(self)}> because the committee_translated is NOT a suitable instance: {type(committee_translated)}")
                break
            compiled_committee_struct: cmd.CompiledCommitteeData = self.compile_committee(
                diagram_instance_data, tpbn, dao_translated, templates_loaded_by_filename_cache, committee_translated)
            if compiled_committee_struct is not None:
                compiled_dao_struct.add_committee(compiled_committee_struct)
        return compiled_dao_struct


#

    def new_compiled_diagram(self, diagram_instance_data: trmt.TranslatedDiagramTemplated, name_diagram: str, compiled_diagram) -> cmd.CompiledDiagramData:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_diagram(self,
                        diagram_instance_data: trmt.TranslatedDiagramTemplated,
                        tpbn: template_provider.TemplateProviderByName
                        ) -> cmd.CompiledDiagramData:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

#
#

    def compile_all_parts_as_generator(self, instance_data: dict, tpbn: template_provider.TemplateProviderByName, additional_data=None) -> Generator[cgd.CompiledUnitWithID, None, None]:
        """
        This default implementation
        """
        diagram_instance_data: trmt.TranslatedDiagramTemplated = instance_data  # alias
        compilated: cmd.CompiledDiagramData = self.compile_diagram(
            diagram_instance_data, tpbn)
        if compilated.can_diagram_be_compiled:
            yield compilated

        # TODO: this WHOLE BODY is taken from "c_j_asm.py" AND CAN BE ABSTRACTED AWAY
        # now, the CORE
        templates_loaded_by_filename_cache = {}  # cache
        for dao_id, dao_translated in diagram_instance_data.daos_by_id.items():
            if dao_translated.can_be_converted():
                # get the template
                if not self.check_translated_dao(dao_translated):
                    print(
                        f"Can't convert DAO: {dao_id} - in translator <{type(self)}> because the dao_translated is NOT a suitable instance: {type(dao_translated)}")
                    break
                compiled_dao_struct: cmd.CompiledDAOData = self.compile_DAO(
                    diagram_instance_data,
                    tpbn,
                    dao_translated,
                    templates_loaded_by_filename_cache
                )
                if compiled_dao_struct is not None:
                    # TO-DO: no ASM compilation of Committees or GovernanceArea ?
                    yield compiled_dao_struct
                    # and each other sub-parts
                    for subparts in compiled_dao_struct.get_all_compiled_subparts_as_generator():
                        if subparts is not None:
                            yield subparts
            else:
                print(
                    f"Can't convert DAO: {dao_id} - {dao_translated.get_name()} to ... (see {type(self)} specfications)")
