import src.pipeline.pipeline_item as pi
import src.files.file_utils as fu
#import src.model.diagram_manager as dm
#import src.postprocessing.output_preparation.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.templates.compiled_generic_data as cgd
import src.postprocessing.output_preparation.templates.jinja.t_j_solidity as tjs
import src.postprocessing.output_preparation.templates.jinja.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.templates.jinja.compiled_solidity as tcs
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg
import src.postprocessing.model_conversion.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as conv_sol_jinja_1_0_0

import src.postprocessing.model_conversion.consts_template as consts_t
import src.files.file_utils as file_utils

class TemplateJinjaSolidity_1_0_0(tjs.TemplateJinjaSolidity):
    """
    @param key_template_skeleton_factory_by_name: key of a function that, provided a template name, returns its skeleton.
    Must be an instance of "TemplateProviderByName"
    """
    def __init__(self, pipeline_item_data: pi.PIData, \
                optional_external_data=None, \
                key_diagram_instance_data:str=None, \
                key_diagram_model:str=None, \
                key_template_skeleton_provider_by_name:str=None, \
                base_folder_templates:str=None \
                ):
        super().__init__(pipeline_item_data, optional_external_data, \
                key_diagram_instance_data=key_diagram_instance_data, \
                key_template_skeleton=None, \
                key_diagram_model=key_diagram_model \
            )
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name
        self.base_folder_templates = base_folder_templates if base_folder_templates is not None else \
            consts_t.DEFAULT_BASE_FOLDER_TEMPLATES

    #

    def compile_template(self, \
            diagram_instance_data:stg.ConvertedDiagram, \
            additional_data=None \
            ) -> tcs.CompiledSolidityDiagram:
        if additional_data is None:
            raise Exception(f"Compile template ({self.__class__.__name__}) needs non-None additional_data (from inputs) to get stuff")
        if not isinstance(diagram_instance_data, conv_sol_jinja_1_0_0.ConvertedDiagram_Jinja_1_0_0):
            raise Exception(f"Compile template ({self.__class__.__name__}) needs diagram_instance_data of class ConvertedDiagram_Jinja_1_0_0 (TODO: 'or subclass'), but '{type(diagram_instance_data)}' was provided")

        # diagram_model:dm.DiagramManager = self.get_ith_input(additional_data, 1) if self.key_diagram_model is None else additional_data[self.key_diagram_model], \

        tpbn = self.get_ith_input(additional_data, 2) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not isinstance(tpbn, template_provider.TemplateProviderByName):
            raise Exception("template provider by name needed")
        #
        # TODO 2025-08-10 perform the actual compilation for each "thing" inside "diagram_instance_data"
        # TODO (2025-08-23) do all Committees and Conditions

        id = 1
        name = diagram_instance_data.get_name()
        diagram_compied = "" # we don't compile the Diagram: onlu
        # so, currently (2025-08-13) there's no use of : diagram_instance_data.entity_specific_data
        # neither of: tpbn
        compilated = tcs.CompiledSolidityDiagram(
            id,
            name,
            compiled=diagram_compied
        )
        # ... and ? let's start the DAO part
        dao_templates_loaded_by_filename = {}
        committee_templates_loaded_by_filename = {}
        # now, the CORE
        for dao_id, dao_translated in diagram_instance_data.daos_by_id.items():
            # get the template
            template_filename_dao_in = "" #"DAOOptimizedGeneric_1_0_0"
            template_filename_dao_out = "" #"DAOOptimizedGeneric_1_0_0"
            template_folder_path_base = ""
            if isinstance(dao_translated, conv_sol_jinja_1_0_0.ConvertedDAO_Jinja_1_0_0):
                template_filename_dao_in = dao_translated.template_filename_input
                template_filename_dao_out = dao_translated.template_filename_output
                template_folder_path_base = dao_translated.template_full_folders_path_from_base
                print(f"\t dao_translated.template_full_folders_path_from_base -> {dao_translated.template_full_folders_path_from_base}")
            else:
                template_filename_dao_in = dao_translated.get_name()
                template_filename_dao_out = template_filename_dao_in
                template_folder_path_base = self.base_folder_templates
            template_skeleton_dao = None
            if template_filename_dao_in in dao_templates_loaded_by_filename:
                template_skeleton_dao = dao_templates_loaded_by_filename[template_filename_dao_in]
            else:
                template_filename_dao_extension = f"{template_filename_dao_in}.jinja"
                print(f"\n  on {type(self)} : BEFORE getting the template skeletons for DAO .... template_folder_path_base: {template_folder_path_base} ; template_filename_dao_extension: {template_filename_dao_extension}")
                template_skeleton_dao = tpbn.provide_template_skeleton_by_name(template_name=[template_folder_path_base, template_filename_dao_extension])
                print(f"\n  on {type(self)} : AFTER getting the template skeletons for DAO")
                # join the template into a single string
                if isinstance(template_skeleton_dao, list):
                    template_skeleton_dao = "\n".join(template_skeleton_dao)
                dao_templates_loaded_by_filename[template_filename_dao_in] = template_skeleton_dao
            #now compile
            print(f"compiling DAO with ID: ({dao_id}) and output Name: ({template_filename_dao_out})")
            compiled_dao = super().compile_single_template(template_skeleton_dao, dao_translated.entity_specific_data)
            # each DAO do create a sub-folder holding everything in there, even the DAO itself
            compiled_dao_filename = fu.concat_folder_filename(template_folder_path_base, template_filename_dao_out, f"{template_filename_dao_out}.sol")
            compiled_dao_struct = tcs.CompiledSolidityDAO(dao_id, compiled_dao_filename, compiled_dao)
            # TODO: (2025-08-23) ADD ALL INTERFACES AND OTHER CONTRACTS IN DAO INTO "dao_translated.interfaces_and_dao_related_compiled_contracts"
            if isinstance(dao_translated, conv_sol_jinja_1_0_0.ConvertedDAO_Jinja_1_0_0):
                # TODO: (2025-08-23) COMPILE ALL OF THE FOLLOWING
                for filename, converted_i in dao_translated.interfaces_and_fullpath_by_filenames.items():
                    template_skeleton = tpbn.provide_template_skeleton_by_name(template_name=[\
                        converted_i.template_full_folders_path_from_base, \
                        converted_i.template_filename_input
                        ])
                    if isinstance(template_skeleton, list):
                        template_skeleton = "\n".join(template_skeleton)
                    compiled_thing = super().compile_single_template(template_skeleton_dao, dao_translated.entity_specific_data)
                    compiled_filename = fu.concat_folder_filename(converted_i.template_full_folders_path_from_base, f"{converted_i.template_filename_output}.sol")
                    compiled_thing_wrapper = cgd.CompiledUnitWithID(None, compiled_filename, compiled_thing)
                    compiled_dao_struct.interfaces_and_dao_related_compiled_contracts[filename] = compiled_thing_wrapper
                """
                for ... in dao_translated.conditions_converted_by_dao_id:
                    # TODO  (2025-08-23) THOSE ARE TOTALLY MISSING FROM CONVERSION, AT THE MOMENT
                    pass
                    compiled_dao_struct.interfaces_and_dao_related_compiled_contracts[todo] = TODO
                """
            compilated.add_dao(compiled_dao_struct)

            # TODO: (2025-08-13) compile each Committee
            for committee_id, committee_translated in dao_translated.committees_by_id.items():
                # lists are allowed to load sub-templates in sub-folders
                # i.e., lists are valid argument to :
                # template_filename_simple_majority = ["voting_protocols", "simple_majority.sol.jinja"]
                # template_skeleton__voting__simple_majority = tpbn.provide_template_skeleton_by_name( \
                #     template_name=template_filename_simple_majority )
                template_skeleton_committee_path = ""
                template_filename_input = ""
                if isinstance(committee_translated, conv_sol_jinja_1_0_0.ConvertedCommittee_Jinja_1_0_0):
                    template_skeleton_committee_path = committee_translated.voting_protocol_template_file_fullpath
                    template_filename_input = committee_translated.template_filename_input
                else:
                    template_filename_input = f"{committee_translated}.sol.jinja"
                    template_skeleton_committee_path = fu.concat_folder_filename(template_folder_path_base, consts_t.NAME_FOLDER_TEMPLATES_VOTING_PROTOCOL, template_filename_input)
                # recycle if possible
                template_skeleton_committee = None
                if template_filename_input in committee_templates_loaded_by_filename:
                    template_skeleton_committee = committee_templates_loaded_by_filename[template_filename_input]
                else:
                    template_skeleton_committee = tpbn.provide_template_skeleton_by_name(template_name=template_skeleton_committee_path)
                    if isinstance(template_skeleton_committee, list):
                        template_skeleton_committee = "\n".join(template_skeleton_committee)
                    committee_templates_loaded_by_filename[template_filename_input] = template_skeleton_committee
                compiled_committee_filename = fu.concat_folder_filename(template_folder_path_base, f"{committee_translated.template_filename_output}.sol")
                compiled_committee = super().compile_single_template(template_skeleton_committee, committee_translated.entity_specific_data)
                compiled_committee_struct = tcs.CompiledSolidityCommittee(committee_id, compiled_committee_filename, compiled_committee)
                # TODO: compiled_committee_struct
                committee_translated.additional_modules_instances_by_name # TODO: WHAT TO DO WITH IT?
                """
                """
                compiled_dao_struct.add_committee_data_to_dao(compiled_committee_struct)

        return compilated
        