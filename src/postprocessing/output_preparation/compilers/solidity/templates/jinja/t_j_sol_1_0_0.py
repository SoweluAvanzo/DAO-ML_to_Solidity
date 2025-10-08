from typing import Generator

import src.pipeline.pipeline_item as pi
#import src.model.diagram_manager as dm
#import src.postprocessing.output_preparation.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd
import src.postprocessing.output_preparation.compilers.shared.templates.template_base_multipart as tb_m
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.t_j_solidity as tjs
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.compilers.solidity.compiled_solidity_data as csd
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg
import src.postprocessing.model_conversion.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as conv_sol_jinja_1_0_0
import src.postprocessing.model_conversion.shared.templates.conversion_result_template as crt

import src.postprocessing.model_conversion.shared.templates.consts_template as consts_t
import src.files.file_utils as file_utils

SOLIDITY_EXTENSION_OUTPUT = "sol"

class TemplateJinjaSolidity_1_0_0(tjs.TemplateJinjaSolidity, tb_m.TemplateBaseMultipart):
    """
    @param key_template_skeleton_factory_by_name: key of a function that, provided a template name, returns its skeleton.
    Must be an instance of "TemplateProviderByName"
    """
    def __init__(self, pipeline_item_data: pi.PIData, \
                optional_external_data=None, \
                key_diagram_instance_data:str=None, \
                key_diagram_model:str=None, \
                key_template_skeleton_provider_by_name:str=None, \
                key_is_result_as_list:str=None \
            ):
        tjs.TemplateJinjaSolidity.__init__(self, \
        #super().__init__( \
        # tjs.TemplateJinjaSolidity.__init__(\
            pipeline_item_data, \
            optional_external_data=optional_external_data, \
            key_template_instance_data=key_diagram_instance_data, \
            key_template_skeleton=None, \
            key_diagram_model=key_diagram_model \
        )
        #tb_m.TemplateBaseMultipart.__init__(pipeline_item_data, optional_external_data=optional_external_data)
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name
        self.key_is_result_as_list = key_is_result_as_list
        # self.base_folder_templates = base_folder_templates if base_folder_templates is not None else consts_t.DEFAULT_BASE_FOLDER_TEMPLATES

    #

    def get_all_parts_to_compile_as_generator(self, instance_data:dict, additional_data=None) -> Generator[crt.ConvertedSubpartTemplated, None, None]:
        diagram_instance_data = instance_data #alias
        if additional_data is None:
            raise Exception(f"Compile template ({self.__class__.__name__}) needs non-None additional_data (from inputs) to get stuff")
        if not isinstance(diagram_instance_data, conv_sol_jinja_1_0_0.ConvertedDiagram_Jinja_1_0_0):
            raise Exception(f"Compile template ({self.__class__.__name__}) needs diagram_instance_data of class ConvertedDiagram_Jinja_1_0_0 (TODO: 'or subclass'), but '{type(diagram_instance_data)}' was provided")

        # diagram_model:dm.DiagramManager = self.get_ith_input(additional_data, 1) if self.key_diagram_model is None else additional_data[self.key_diagram_model], \

        tpbn = self.get_ith_input(additional_data, 2) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not isinstance(tpbn, template_provider.TemplateProviderByName):
            raise Exception("template provider by name needed")
        id = 1
        name = diagram_instance_data.get_name()
        diagram_compied = "" # we don't compile the Diagram: onlu
        # so, currently (2025-08-13) there's no use of : diagram_instance_data.entity_specific_data
        # neither of: tpbn
        compilated = csd.CompiledSolidityDiagram(
            id,
            name,
            compiled=diagram_compied
        )
        # ... and ? let's start the DAO part
        dao_templates_loaded_by_filename = {}
        committee_templates_loaded_by_filename = {}
        # now, the CORE
        for dao_id, dao_translated in diagram_instance_data.daos_by_id.items():
            compiled_dao_struct:csd.CompiledSolidityDAO = None
            if dao_translated.can_be_converted():
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
                    template_folder_path_base = ""
                template_skeleton_dao = None
                if template_filename_dao_in in dao_templates_loaded_by_filename:
                    template_skeleton_dao = dao_templates_loaded_by_filename[template_filename_dao_in]
                else:
                    template_filename_dao_extension = f"{template_filename_dao_in}.{self.jinja_extension}"
                    print(f"\n  on {type(self)} : BEFORE getting the template skeletons for DAO .... template_folder_path_base: {template_folder_path_base} ; template_filename_dao_extension: {template_filename_dao_extension}")
                    template_skeleton_dao = tpbn.provide_template_skeleton_by_name(template_name=[template_folder_path_base, template_filename_dao_extension])
                    print(f"\n  on {type(self)} : AFTER getting the template skeletons for DAO")
                    # join the template into a single string
                    if template_skeleton_dao is None:
                        raise Exception(f"CAN'T FIND TEMPLATE {file_utils.concat_folder_filename(template_folder_path_base, template_filename_dao_extension)}")
                    if isinstance(template_skeleton_dao, list):
                        template_skeleton_dao = "\n".join(template_skeleton_dao)
                    dao_templates_loaded_by_filename[template_filename_dao_in] = template_skeleton_dao
                #now compile
                print(f"compiling DAO with ID: ({dao_id}) and output Name: ({template_filename_dao_out})")
                compiled_dao = super().compile_single_template(template_skeleton_dao, dao_translated.entity_specific_data)
                # each DAO do create a sub-folder holding everything in there, even the DAO itself
                compiled_dao_filename = file_utils.concat_folder_filename(template_folder_path_base, template_filename_dao_out, f"{template_filename_dao_out}.{SOLIDITY_EXTENSION_OUTPUT}")
                compiled_dao_struct = csd.CompiledSolidityDAO(dao_id, compiled_dao_filename, compiled_dao)
                # TODO: (2025-08-23) ADD ALL INTERFACES AND OTHER CONTRACTS IN DAO INTO "dao_translated.interfaces_and_dao_related_compiled_contracts"
                if isinstance(dao_translated, conv_sol_jinja_1_0_0.ConvertedDAO_Jinja_1_0_0):
                    # COMPILE ALL OF THE FOLLOWING ANYTHING RELATED WITH A DAO (but not the DAO itself)
                    for map_compiled_adjacent_contracts in [\
                            dao_translated.interfaces_and_fullpath_by_filenames, \
                            dao_translated.conditions_converted_by_name \
                        ]:
                        for filename, converted_thing in map_compiled_adjacent_contracts.items():
                            if converted_thing.can_be_converted():
                                template_input_filename_extension = f"{converted_thing.template_filename_input}.{self.jinja_extension}"
                                template_skeleton = tpbn.provide_template_skeleton_by_name(template_name=[\
                                    converted_thing.template_full_folders_path_from_base, \
                                    template_input_filename_extension
                                    ])
                                if isinstance(template_skeleton, list):
                                    template_skeleton = "\n".join(template_skeleton)
                                compiled_thing = super().compile_single_template(template_skeleton, converted_thing.entity_specific_data)
                                compiled_filename = file_utils.concat_folder_filename(converted_thing.template_full_folders_path_from_base, f"{converted_thing.template_filename_output}.{SOLIDITY_EXTENSION_OUTPUT}")
                                print(f"compiled_filename of interfaces/conditions: {compiled_filename}")
                                compiled_thing_wrapper = cgd.CompiledUnitWithID(None, compiled_filename, compiled_thing)
                                compiled_dao_struct.interfaces_and_dao_related_compiled_contracts[filename] = compiled_thing_wrapper
                                yield compiled_thing_wrapper
                            else:
                                print(f"Can't convert THING: {filename} - {converted_thing.get_name()}")
                compilated.add_dao(compiled_dao_struct)
                yield compiled_dao_struct
            else:
                print(f"Can't convert DAO: {dao_id} - {dao_translated.get_name()}")
            # TODO: (2025-08-13) compile each Committee ... (2025-09-04) is there something missing?
            for committee_id, committee_translated in dao_translated.committees_by_id.items():
                if committee_translated.can_be_converted():
                    # lists are allowed to load sub-templates in sub-folders
                    # i.e., lists are valid argument to :
                    # template_filename_simple_majority = ["voting_protocols", "simple_majority.{SOLIDITY_EXTENSION_OUTPUT}.jinja"]
                    # template_skeleton__voting__simple_majority = tpbn.provide_template_skeleton_by_name( \
                    #     template_name=template_filename_simple_majority )
                    template_skeleton_committee_path = ""
                    template_filename_input = ""
                    if isinstance(committee_translated, conv_sol_jinja_1_0_0.ConvertedCommittee_Jinja_1_0_0):
                        template_skeleton_committee_path = committee_translated.voting_protocol_template_file_fullpath
                        template_filename_input = committee_translated.template_filename_input
                    else:
                        template_filename_input = f"{committee_translated}.{SOLIDITY_EXTENSION_OUTPUT}.jinja"
                        template_skeleton_committee_path = file_utils.concat_folder_filename(template_folder_path_base, consts_t.NAME_FOLDER_TEMPLATES_VOTING_PROTOCOL, template_filename_input)
                    # recycle if possible
                    template_skeleton_committee = None
                    if template_filename_input in committee_templates_loaded_by_filename:
                        template_skeleton_committee = committee_templates_loaded_by_filename[template_filename_input]
                    else:
                        template_skeleton_committee = tpbn.provide_template_skeleton_by_name(template_name=template_skeleton_committee_path)
                        if isinstance(template_skeleton_committee, list):
                            template_skeleton_committee = "\n".join(template_skeleton_committee)
                        committee_templates_loaded_by_filename[template_filename_input] = template_skeleton_committee
                    compiled_committee_filename = file_utils.concat_folder_filename(template_folder_path_base, f"{committee_translated.template_filename_output}.{SOLIDITY_EXTENSION_OUTPUT}")
                    compiled_committee = super().compile_single_template(template_skeleton_committee, committee_translated.entity_specific_data)
                    compiled_committee_struct = csd.CompiledSolidityCommittee(committee_id, compiled_committee_filename, compiled_committee)
                    compiled_dao_struct.add_committee_data_to_dao(compiled_committee_struct)
                    yield compiled_committee_struct
                else:
                    print(f"Can't convert COMMITTEE: {committee_id} - {committee_translated.get_name()}")
                """
                TODO
                if isinstance(committee_translated, conv_sol_jinja_1_0_0.ConvertedCommittee_Jinja_1_0_0):
                    committee_translated.additional_modules_instances_by_name
                """
        yield compilated

    def compile_template(self, \
            diagram_instance_data:stg.ConvertedDiagram, \
            additional_data=None \
        ) -> csd.CompiledSolidityDiagram:
        if self.key_is_result_as_list is None or additional_data is None or (self.key_is_result_as_list in additional_data and additional_data[self.key_is_result_as_list]):
            #return super(tb_m.TemplateBaseMultipart, self)
            return tb_m.TemplateBaseMultipart.compile_template(self, instance_data=diagram_instance_data, additional_data=additional_data)
        for cp in self.get_all_parts_to_compile_as_generator(instance_data=diagram_instance_data, additional_data=additional_data):
            if isinstance(cp, csd.CompiledSolidityDiagram):
                return cp
        print(f"{type(self)} returns NOTHING on compile_template")
        return None
    
