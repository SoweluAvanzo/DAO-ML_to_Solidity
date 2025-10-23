
import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.translation_result_base as crb
import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt
import src.postprocessing.model_translation.shared.templates.translation_result_template as crt
import src.postprocessing.model_translation.model_translator_configurable as mcc
# import src.postprocessing.model_conversion.solidity.optimized.solidity_converter_optimized as sol_transl_opt
import src.postprocessing.model_translation.solidity.optimized.jinja.solidity_translator_optimized_jinja as sol_transl_opt_jinja
import src.postprocessing.model_translation.solidity.shared_utils as shared_utils_sol

import src.model.enums.user_functionalities_group_size as user_functionalities_group_size_module
import src.model.aggregable_entity as aggregable_entity
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
# import src.model.enums.user_functionalities_group_size as user_functionalities_group_size_module
import src.model.enums.relation_type as rt

import src.postprocessing.consts_template as consts_t
import src.utilities.utils as utils
import src.utilities.constants as consts
import src.files.file_utils as fu

VERSION = "1.0.0"

FILENAME_VOTING_PROTOCOL_CUSTOM = "custom_decision_making_template"

#
# TRANSLATION OUTPUT
#


class TranslatedCommittee_Jinja_1_0_0(trmt.TranslatedCommitteeTemplated):
    def __init__(self, committee: c.Committee, committee_specific_data: dict,
                 voting_protocol_specific_data: dict = None,
                 is_convertible: bool = True
                 ):
        trmt.TranslatedCommitteeTemplated.__init__(
            self, committee, committee_specific_data,
            voting_protocol_specific_data=voting_protocol_specific_data,
            is_convertible=is_convertible)
        # as of "translator.py # CommitteeTranslator", there are A LOT of additional templates to be created for each Committee
        self.additional_modules_instances_by_name: dict[str, list[dict]] = []


class TranslatedDAO_Jinja_1_0_0(trmt.TranslatedDAOTemplated):
    def __init__(self, dao: d.DAO, dao_specific_data: dict,
                 is_convertible: bool = True
                 ):
        trmt.TranslatedDAOTemplated.__init__(
            self, dao, dao_specific_data, is_convertible=is_convertible)
        # dict of ( output_filename, compiled_template )
        self.conditions_converted_by_name: dict[str,
                                                crt.TranslatedSubpartTemplated] = {}
        # a dict of ( output_filename, compiled_template ) ; depends on dao's committees
        self.interfaces_and_fullpath_by_filenames: dict[str, crt.TranslatedSubpartTemplated] = {
        }


class TranslatedDiagram_Jinja_1_0_0(trmt.TranslatedDiagramTemplated):
    def __init__(self, diagram: dm.DiagramManager, diagram_specific_data: dict,
                 is_convertible: bool = True
                 ):
        trmt.TranslatedDiagramTemplated.__init__(
            self, diagram, diagram_specific_data, is_convertible=is_convertible)
        self.interfaces_converted_specific_data = {}

#
# THE ACTUAL TRANSLATOR
#


class SolidityTranslatorOptimizedJinja_1_0_0(sol_transl_opt_jinja.SolidityTranslatorOptimizedJinja):
    """
    All of this subclasses bear the responsibility of declaring and defining which kind of templates they are using
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 key_model: str = None,
                 key_converter_type: str = None,
                 key_converter_version: str = None,
                 key_converter_target: str = None,
                 all_voting_protocols: set = None,
                 key_all_voting_protocols: str = None
                 ):
        super().__init__(
            pipeline_item_data,
            key_model,
            key_converter_type,
            key_converter_version,
            key_converter_target
        )
        self.key_all_voting_protocols = key_all_voting_protocols
        self.all_voting_protocols: set = all_voting_protocols

    def translate(self, diagram, additional_data: dict = None) -> crb.ModelConversionResultBase:
        if self.all_voting_protocols is None:
            k = self.key_all_voting_protocols
            if self.key_all_voting_protocols is None:
                k = additional_data["key_all_voting_protocols"]
            self.all_voting_protocols = additional_data[k]
        # THE REAL TRANSLATION!
        return self.translate_Diagram(diagram, additional_data)

    #

    def translate_Diagram(self, diagram: dm.DiagramManager, additional_data: dict = None) -> TranslatedDiagram_Jinja_1_0_0:
        version = additional_data[self.key_converter_target] if self.key_converter_target in additional_data \
            else additional_data[mcc.ModelTranslatorConfigurable.KEY_ADDITIONAL_DATA_TARGET_VERSION]
        if version is None or version.strip() == "":
            version = VERSION
        version_for_file = version.replace('.', '_')
        solidity_version = consts_t.SOLIDITY_VERSION_DEFAULT
        diagram_specific_data_translated = {
            "solidity_version": solidity_version
        }
        td = self.new_translated_diagram(
            diagram, diagram_specific_data_translated)
        td.is_convertible
        diagram_specific_data_translated["uniqueID"] = diagram.uniqueID
        diagram_specific_data_translated["relations_by_dao"] = {
            dao_id: [ \
                # note: the rt.RelationType instance can be retrieved back by writing :
                #    rt.RelationType[ name_of_enum_instance ]
                (rel_data[0].name if isinstance(rel_data[0], rt.RelationType)
                 else f"{rel_data[0]}", rel_data[1], rel_data[2])
                for rel_data in diagram.relations_by_dao[dao_id]
            ]
            for dao_id in diagram.relations_by_dao.keys()
        }
        # TODO: fare il controlGraphGenerator, somehow, se necessario
        # c'e' altro da completare e, quindi, mettere dentro a "diagram_specific_data_translated"
        # dao
        for dao_id in diagram.daoByID.keys():
            dao = diagram.daoByID[dao_id]
            translated_dao = self.translate_DAO(diagram, dao,
                                                solidity_version=solidity_version,
                                                version_target=version,
                                                version_for_file=version_for_file
                                                )
            td.add_translated_dao(translated_dao)
        return td

    def translate_DAO(self, diagram: dm.DiagramManager, dao: d.DAO,
                      solidity_version: str = consts_t.SOLIDITY_VERSION_DEFAULT,
                      version_target: str = "",
                      version_for_file: str = ""
                      ) -> TranslatedDAO_Jinja_1_0_0:
        dao_specific_data_translated = {}
        dao_translated: TranslatedDAO_Jinja_1_0_0 = self.new_translated_dao(
            diagram, dao, dao_specific_data_translated)
        # crt.TranslatedSubpartTemplated
        dao_template_filename = "DAOOptimizedGeneric"
        dao_translated.translated_name_output = fu.sanitize_filename(
            dao.get_name())
        dao_translated.template_filename_input = f"{dao_template_filename}_{version_for_file}"
        dao_translated.suggested_input_template_folders_path_from_base = ""
        # vars
        entities_amount = len(dao.roles) + len(dao.committees)
        group_size: user_functionalities_group_size_module.UserFunctionalitiesGroupSize = dao.metadata.user_functionalities_group_size
        group_mask_size = group_size.get_mask_size()
        id_var_type = self.get_variable_type(dao, group_size)
        is_role_access_optimized = group_size is not None
        functionalities_ids = self.compute_states_variables__functionalities_ids(
            dao)
        rccd = self.compute_states_variables__roles_committee_computed_data(
            dao, functionalities_ids, group_size)
        entity_to_data = rccd["entity_to_data"]
        roles_computed_data = rccd["roles_computed_data"]
        committees_computed_data = rccd["committees_computed_data"]
        mask_id = group_size.get_mask_id()
        permission_to_index: dict[str, int] = {
            permission: idx for idx, permission in enumerate(dao.permissions)}

        space_to_underscore_fn = fu.sanitize_filename
        # generate_header
        dao_specific_data_translated["solidity_version"] = solidity_version
        dao_specific_data_translated["dao_name"] = fu.sanitize_filename(
            dao.dao_name)
        # generate_contract_declaration
        dao_specific_data_translated["mission_statement"] = dao.mission_statement
        dao_specific_data_translated["dao_conditions"] = dao.conditions
        # generate_state_variables
        dao_specific_data_translated["visibility"] = "internal"
        dao_specific_data_translated["id_var_type"] = id_var_type
        dao_specific_data_translated["perm_var_type"] = self.get_permission_array_size(
            dao)
        dao_specific_data_translated["voting_conditions"] = dao.voting_conditions
        dao_specific_data_translated["proposal_conditions"] = dao.proposal_conditions
        dao_specific_data_translated["assignment_conditions"] = dao.assignment_conditions
        # ... generate_events
        # generate_has_permission_modifier
        dao_specific_data_translated["is_role_access_optimized"] = is_role_access_optimized
        dao_specific_data_translated["total_roles_amount"] = entities_amount
        dao_specific_data_translated["roles"] = dao.roles
        dao_specific_data_translated["committees"] = dao.committees
        dao_specific_data_translated["committees_names_list"] = [
            c.get_name() for c in dao.committees.values()]
        print(
            f"dao_specific_data_translated['committees_names_list'] -> {dao_specific_data_translated['committees_names_list']}")
        dao_specific_data_translated["entities_amount"] = entities_amount
        dao_specific_data_translated["states_variables__functionalities_ids"] = functionalities_ids
        # dao_specific_data_translated.update( rccd )
        dao_specific_data_translated["entity_to_data"] = entity_to_data
        dao_specific_data_translated["roles_computed_data"] = roles_computed_data
        dao_specific_data_translated["committees_computed_data"] = committees_computed_data
        # control_relation
        dao_specific_data_translated["control_relation_id_bit_size"] = group_mask_size
        dao_specific_data_translated["control_relation_mask"] = mask_id
        # generate_constructor_v2
        dao_specific_data_translated["constructor_parameters"] = self.get_dao_constructor_parameters(
            dao, id_var_type)
        body_constructor_data = self.get_dao_constructor_body(dao, id_var_type)
        if body_constructor_data is not None:
            dao_specific_data_translated.update(body_constructor_data)
        # ... generate_role_permission_mapping
        dao_specific_data_translated["entities_permissions"] = self.generate_role_permission_mapping_data(
            dao, space_to_underscore_fn, permission_to_index, is_role_access_optimized)
        # generate_committee_initialization_function
        dao_specific_data_translated["visibility_committee_initialization_function"] = "external"
        dao_specific_data_translated["space_to_underscore_fn"] = space_to_underscore_fn
        # generate_functions
        dao_specific_data_translated["group_size_bitmask"] = group_mask_size
        dao_specific_data_translated["id_mask"] = mask_id
        # generate_permission_functions
        dao_specific_data_translated["permissions"] = list(
            dao.permissions.values())
        dao_specific_data_translated["permission_index_by_id"] = permission_to_index
        dao_specific_data_translated["function_permission_name_by_id"] = self.get_function_permission_name_by_id(
            dao)
        has_voting_proposal = self.has_default_functions_overridden(dao)
        dao_specific_data_translated["voting_function"] = has_voting_proposal["voting_function"]
        dao_specific_data_translated["proposal_function"] = has_voting_proposal["proposal_function"]

        # TODO: 2025-08-22
        for c in dao.committees.values():
            c_t = self.translate_committee_solidity(
                diagram, dao, c,
                permission_to_index,
                version_target=version_target,
                solidity_version=solidity_version,
                version_for_file=version_for_file
            )
            dao_translated.add_translated_committee(c_t)
        # 1)
        self.generate_dao_level_interfaces_data(
            diagram, dao, dao_translated,
            perm_var_type=id_var_type,
            version_target=version_target,
            solidity_version=solidity_version,
            version_for_file=version_for_file
        )
        # 2)
        self.generate_condition_from_template(
            diagram, dao, dao_translated,
            perm_var_type=id_var_type,
            version_target=version_target,
            solidity_version=solidity_version,
            version_for_file=version_for_file
        )
        return dao_translated

    def translate_committee_solidity(self,
                                     diagram: dm.DiagramManager, dao: d.DAO, committee: c.Committee,
                                     permission_to_index: dict[str, int],
                                     version_target: str = "",
                                     solidity_version: str = consts_t.SOLIDITY_VERSION_DEFAULT,
                                     version_for_file: str = ""
                                     ) -> TranslatedDAO_Jinja_1_0_0:
        committee_specific_data_translated = {}
        voting_protocol_specific_data = {}
        committee_translated: TranslatedCommittee_Jinja_1_0_0 = self.new_translated_committee(
            diagram, dao, committee,
            other_data=committee_specific_data_translated,
            is_convertible=True
        )
        print(
            f"translating committee: name={committee_translated.get_name()} ; id={committee_translated.get_id()}")
        committee_translated.voting_protocol_specific_data = voting_protocol_specific_data
        template_voting_protocol_base_path = consts_t.NAME_FOLDER_TEMPLATES_VOTING_PROTOCOL
        committee_translated.suggested_input_template_folders_path_from_base = template_voting_protocol_base_path
        committee_translated.translated_name_output = None

        # START translateCommittee ... IT WORKS BY COMPILING A VOTING TEMPLATE: THERE'S NO COMMITTEE-DEDICATED TEMPLATE

        voting_permission_key = committee.get_id() + "VotingRight"
        proposal_permission_key = committee.get_id() + "ProposalRight"
        voting_permission_index = permission_to_index[voting_permission_key]
        proposal_permission_index = permission_to_index[proposal_permission_key]

        # ... preparation of generate_voting_protocol_from_template
        committee_name = committee.committee_description.replace(" ", "_")
        decision_making_method = committee.decision_making_method
        self.prepare_committee_voting_protocol(
            diagram, dao, committee, committee_translated,
            template_voting_protocol_base_path=template_voting_protocol_base_path,
            committee_name=committee_name,
            decision_making_method=decision_making_method,
            target_version=version_target,
            solidity_version=solidity_version,
            voting_permission_index=voting_permission_index,
            proposal_permission_index=proposal_permission_index,
            version_for_file=version_for_file
        )
        return committee_translated

    # overrides

    def new_translated_diagram(self, diagram: dm.DiagramManager, other_data=None) -> TranslatedDiagram_Jinja_1_0_0:
        return TranslatedDiagram_Jinja_1_0_0(diagram, diagram_specific_data=other_data)

    def new_translated_dao(self, diagram: dm.DiagramManager, dao: d.DAO, other_data=None) -> TranslatedDAO_Jinja_1_0_0:
        return TranslatedDAO_Jinja_1_0_0(dao, other_data)

    def new_translated_committee(self, diagram: dm.DiagramManager, dao: d.DAO, committee: c.Committee, other_data=None,
                                 is_convertible=True
                                 ) -> TranslatedCommittee_Jinja_1_0_0:
        return TranslatedCommittee_Jinja_1_0_0(committee, other_data, is_convertible=is_convertible)

    #

    # helper functions

    #

    def get_variable_type(self, dao: d.DAO, group_size: user_functionalities_group_size_module.UserFunctionalitiesGroupSize):
        id_var_type = "bytes32" if group_size is None else f"uint{group_size.to_maximum_size()}"
        return id_var_type

    def get_permission_array_size(self, dao: d.DAO):
        perm_var_type = None
        permissions_amount = len(dao.permissions)
        if permissions_amount <= 8:
            perm_var_type = "uint8"
        elif permissions_amount <= 16:
            perm_var_type = "uint16"
        elif permissions_amount <= 32:
            perm_var_type = "uint32"
        elif permissions_amount <= 64:
            perm_var_type = "uint64"
        elif permissions_amount <= 128:
            perm_var_type = "uint128"
        elif permissions_amount <= 256:
            perm_var_type = "uint256"
        return perm_var_type

    def compute_states_variables__functionalities_ids(self, dao: d.DAO):
        """
        Override-designed
        """
        return shared_utils_sol.get_DAO_functionalities_ids(dao)

    def get_control_bitflags(self,
                             dao: d.DAO,
                             role_or_committee: aggregable_entity.AggregableEntity,
                             group_size: user_functionalities_group_size_module.UserFunctionalitiesGroupSize,
                             functionalities_ids: dict[str, int]
                             ):
        """
        Override-designed
        """
        return shared_utils_sol.get_control_bitflags(dao, role_or_committee, group_size, functionalities_ids)

    def compute_states_variables__roles_committee_computed_data(self, dao: d.DAO, functionalities_ids: dict[str, int], group_size: int):
        """
        Override-designed
        """
        return shared_utils_sol.get_roles_committee_computed_data(dao, functionalities_ids, group_size)

    def get_dao_constructor_parameters(self, dao: d.DAO, id_var_type: str) -> dict:
        params: list[dict] = []
        if dao.conditions != []:
            params.append({"type": id_var_type, "name": "roleIds"})
        if dao.voting_conditions != {}:
            params.append(
                {"type": "address", "name": "votingConditionAddresses"})
        if dao.proposal_conditions != {}:
            params.append(
                {"type": "address", "name": "proposalConditionAddresses"})
        if dao.assignment_conditions != {}:
            params.append(
                {"type": "address", "name": "assignmentConditionAddresses"})
        return params

    def generate_role_permission_mapping_data(self, dao: d.DAO, space_to_underscore_fn, permission_to_index: dict, is_role_access_optimized: bool):
        # permission_to_index:dict[str, int]
        entities_permissions = []
        entities_map_list: list[dict[str, aggregable_entity.AggregableEntity]] = [
            dao.roles,
            dao.committees
        ]
        def role_to_index_fn(irao, r, i_e): return f"{i_e}" if irao else r
        index_entity = 0
        for entity_map in entities_map_list:
            for entity in entity_map.values():
                permission_indices = [
                    permission_to_index[permission.get_id()] for permission in entity.permissions]
                # Set the bit for each permission index
                bitflag = 0
                for index in permission_indices:
                    bitflag |= (1 << index)
                e_name = space_to_underscore_fn(entity.get_name())
                entities_permissions.append({
                    "entity_name": e_name,
                    "permission_indices": permission_indices,
                    "bitflag": bitflag,
                    "index_entity_in_dao": role_to_index_fn(is_role_access_optimized, e_name, index_entity),
                    "index_entity": index_entity
                })
                index_entity += 1
        import json
        print(
            f"on dao '{dao.get_name()}', entities_permissions:\n\t {json.dumps(entities_permissions, indent=2)}")
        return entities_permissions

    def get_dao_constructor_body(self, dao: d.DAO, id_var_type: str) -> dict:
        return {
            "dao_owner": True
        }

    def get_function_permission_name_by_id(self, dao: d.DAO):
        return {
            # sanitize the name
            perm.get_id(): perm.allowed_action.replace("/", "_").replace(" ", "_").replace("\\", "")
            for perm in dao.permissions.values()
        }

    def has_default_functions_overridden(self, dao: d.DAO):
        voting_function = False
        proposal_function = False
        for perm in dao.permissions.values():
            if perm.voting_right:
                voting_function = True
            if perm.proposal_right:
                proposal_function = True
        return {
            "voting_function": voting_function,
            "proposal_function": proposal_function
        }

    def generate_dao_level_interfaces_data(self, diagram: dm.DiagramManager, dao: d.DAO,
                                           dao_conversion: TranslatedDAO_Jinja_1_0_0,
                                           perm_var_type: str = "address",
                                           version_target: str = VERSION,
                                           solidity_version: str = consts_t.SOLIDITY_VERSION_DEFAULT,
                                           version_for_file: str = ""
                                           ):
        interface_filename = "IPermissionManager"
        interface_related_data = {}
        interface_converted = crt.TranslatedSubpartTemplated(
            None, interface_related_data)
        interface_converted.translated_name_output = interface_filename
        interface_converted.template_filename_input = f"{interface_filename}_{version_for_file}"
        interface_converted.suggested_input_template_folders_path_from_base = consts_t.NAME_FOLDER_TEMPLATES_INTERFACES
        interface_related_data["solidity_version"] = solidity_version
        interface_related_data["perm_var_type"] = perm_var_type
        interface_related_data["committees"] = dao.committees
        dao_conversion.interfaces_and_fullpath_by_filenames[interface_filename] = interface_converted

        interface_filename = "ICondition"
        interface_related_data = {}
        interface_converted = crt.TranslatedSubpartTemplated(
            None, interface_related_data)
        interface_converted.translated_name_output = interface_filename
        interface_converted.template_filename_input = f"{interface_filename}_{version_for_file}"
        interface_converted.suggested_input_template_folders_path_from_base = consts_t.NAME_FOLDER_TEMPLATES_INTERFACES
        interface_related_data["solidity_version"] = solidity_version
        # interface_related_data["perm_var_type"] = perm_var_type
        dao_conversion.interfaces_and_fullpath_by_filenames[interface_filename] = interface_converted

    # TODO (2025-08-23) for condition in dao.conditions -> ... generate_condition_from_template
    def generate_condition_from_template(self, diagram: dm.DiagramManager, dao: d.DAO,
                                         dao_conversion: TranslatedDAO_Jinja_1_0_0,
                                         perm_var_type: str = "address",
                                         version_target: str = VERSION,
                                         solidity_version: str = consts_t.SOLIDITY_VERSION_DEFAULT,
                                         version_for_file: str = ""
                                         ):
        condition_template_input_standard = f"ConditionImplementation_{version_for_file}.{consts.SOLIDITY_EXTENSION_OUTPUT}.{consts_t.JINJA_FILE_EXTENSION}"
        for condition in dao.conditions:
            condition_name = utils.to_camel_case(condition)
            condition_related_data = {}
            condition_converted = crt.TranslatedSubpartTemplated(
                None, condition_related_data)
            condition_converted.suggested_input_template_folders_path_from_base = ""
            condition_converted.translated_name_output = condition_name
            condition_converted.template_filename_input = condition_template_input_standard
            condition_related_data["solidity_version"] = solidity_version
            condition_related_data["condition_name"] = condition_name
            # no implementation currently (2025-08-30) available; further developments (and sub-contracts)
            # might provide an actual implementation
            condition_logic = "//TODO: Implement the condition smart contract logic here"
            condition_related_data["condition_logic"] = condition_logic
            condition_related_data["return_value"] = "true"
            dao_conversion.conditions_converted_by_name[condition_name] = condition_converted

    #

    # Committee stuffs

    #

    def prepare_committee_voting_protocol(self, diagram: dm.DiagramManager, dao: d.DAO, committee: c.Committee,
                                          committee_conversion: TranslatedCommittee_Jinja_1_0_0,
                                          committee_name: str = "",
                                          decision_making_method: str = "",
                                          target_version: str = "",
                                          solidity_version: str = consts_t.SOLIDITY_VERSION_DEFAULT,
                                          voting_permission_index: int = -1,
                                          proposal_permission_index: int = -1,
                                          template_voting_protocol_base_path: str = ".",
                                          version_for_file: str = ""
                                          ):
        is_custom = False
        if decision_making_method is None:
            decision_making_method = "custom_decision_making_method"
            # is_custom = True
        else:
            decision_making_method = decision_making_method.strip()
            is_custom = decision_making_method == ""
        committee_specific_data = committee_conversion.entity_specific_data
        contract_name = utils.to_camel_case(committee_name)
        committee_specific_data["contract_name"] = contract_name
        template_name = contract_name  # decision_making_method
        if not (template_name in self.all_voting_protocols):
            template_name = FILENAME_VOTING_PROTOCOL_CUSTOM
        committee_conversion.template_filename_input = template_name
        committee_conversion.translated_name_output = contract_name

        committee_specific_data["is_custom"] = is_custom
        committee_specific_data["solidity_version"] = solidity_version
        committee_specific_data["decision_making_method_name"] = decision_making_method
        committee_specific_data["dao_name"] = dao.dao_name

        committee_specific_data["constructor_parameters"] = [
            {"param_name": "_permissionManager", "param_type": "address"}
        ]
        # NONE is defined, currently (2025-08-22)
        committee_specific_data["inherited_contracts"] = ""
        committee_specific_data["optimized"] = True
        committee_specific_data["voting_permission_index"] = voting_permission_index
        committee_specific_data["proposal_permission_index"] = proposal_permission_index
