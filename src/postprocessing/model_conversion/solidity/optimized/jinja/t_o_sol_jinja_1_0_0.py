

import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.model_converter_base as mcb
import src.postprocessing.model_conversion.model_converter_configurable as mcc
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg
#import src.postprocessing.model_conversion.solidity.optimized.solidity_converter_optimized as sol_transl_opt
import src.postprocessing.model_conversion.solidity.optimized.jinja.solidity_converter_optimized_jinja as sol_transl_opt_jinja
import src.model.enums.user_functionalities_group_size as user_functionalities_group_size_module
import src.model.enums.entity_type_controllable as etc
import src.model.aggregable_entity as aggregable_e
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
#import src.model.enums.user_functionalities_group_size as user_functionalities_group_size_module
import src.model.enums.relation_type as rt

VERSION = "1.0.0"


#
# TRANSLATION OUTPUT
#


class TranslatedCommittee_Jinja_1_0_0(stg.TranslatedCommittee):
    def __init__(self, committee:c.Committee, committee_specific_data:dict, \
            voting_protocol_specific_data:dict=None         
        ):
        super().__init__(committee, committee_specific_data)
        self.additional_modules_instances_by_name:dict[str, list[dict]] = [] # as of "translator.py # CommitteeTranslator", there are A LOT of additional templates to be created for each Committee
        self.voting_protocol_specific_data = voting_protocol_specific_data

class TranslatedDAO_Jinja_1_0_0(stg.TranslatedDAO):
    def __init__(self, dao:d.DAO, dao_specific_data:dict):
        super().__init__(dao, dao_specific_data)
        self.conditions_transated = [] # tuples of ( output_filename, compiled_template )
        self.i_permissions_manager_translated = [] #a single tuple ; depends on dao's committees

"""
"""
class TranslatedDiagram_Jinja_1_0_0(stg.TranslatedDiagram):
    def __init__(self, diagram:dm.DiagramManager, diagram_specific_data:dict):
        super().__init__(diagram, diagram_specific_data)

#
# THE ACTUAL TRANSLATOR
#


class SolidityConverterOptimizedJinja_1_0_0(sol_transl_opt_jinja.SolidityConverterOptimizedJinja):
    """
    All of this subclasses bear the responsibility of declaring and defining which kind of templates they are using
    """

    def __init__(self, pipeline_item_data: pi.PIData, \
                all_voting_protocols:dict=None, \
                key_model:str=None, \
                key_converter_type:str=None, \
                key_converter_version:str=None, \
                key_converter_target:str=None, \
            ):
        super().__init__(\
            pipeline_item_data, \
            key_model, \
            key_converter_type, \
            key_converter_version, \
            key_converter_target \
        )
        self.all_voting_protocols = all_voting_protocols
    
    def select_delegator(self, diagram:dm.DiagramManager, translator_type:str, version:str,  additional_data:dict=None) -> mcb.ModelConverterBase:
        return self
    
    def convert(self, diagram, additional_data:dict=None) -> mcb.ModelConversionResultBase:
        #raise Exception("SolidityConverterOptimizedJinja_1_0_0 translation NOT IMPLEMENTED YET")
        print("YAYYYYYYy SolidityConverterOptimizedJinja_1_0_0 conversioooooooooooooon")
        # TODO THE REAL TRANSLATION!
        return self.translate_diagram_solidity(diagram, additional_data)
        """
        # See " optimized_translator.py # OptimizedSolidityTranslator"
        
        OptimizedSolidityTranslator
        -> def translate(self)
    
            # at first, translate all Committees
            ct = CommitteeTranslator(self.context)
            - for c in self.context.dao.committees.values():
            - - translated_committee = ct.translateCommittee(c, proposal_permission_index , voting_permission_index, optimized=True) 
        
            - for condition in self.context.dao.conditions:

                ConditionTranslator
                # translateCommittee
                -> file_name_and_path = template_path + "ConditionImplementation" + extension + ".jinja"
                - - -> extension = ".sol" ?
                - - -> template_path =
        """


    def translate_diagram_solidity(self, diagram:dm.DiagramManager, additional_data:dict=None) -> stg.TranslatedDiagram:
        diagram_specific_data_translated = {
            "solidity_version": additional_data[self.key_converter_target] if self.key_converter_target in additional_data \
                else additional_data[mcc.ModelConverterConfigurable.KEY_ADDITIONAL_DATA_TARGET_VERSION]
        }
        td = self.new_translated_diagram(diagram, diagram_specific_data_translated) 
        diagram_specific_data_translated["uniqueID"] = diagram.uniqueID
        diagram_specific_data_translated["relations_by_dao"] = { \
            dao_id: [ \
                #note: the rt.RelationType instance can be retrieved back by writing :
                #    rt.RelationType[ name_of_enum_instance ]
                ( rel_data[0].name if isinstance(rel_data[0], rt.RelationType) else f"{rel_data[0]}", rel_data[1], rel_data[2] ) \
                for rel_data in diagram.relations_by_dao[dao_id] \
                ] \
            for dao_id in diagram.relations_by_dao.keys()
        }
        # TODO: fare il controGraphGenerator, somehow, se necessario
        # c'e' altro da completare e, quindi, mettere dentro a "diagram_specific_data_translated"
        # dao
        for dao_id in diagram.daoByID.keys():
            dao = diagram.daoByID[dao_id]
            translated_dao = self.translate_DAO_solidity(diagram, dao)
            td.add_translated_dao(translated_dao)
        return td

    def translate_DAO_solidity(self, diagram: dm.DiagramManager, dao: d.DAO) -> stg.TranslatedDAO:
        dao_specific_data_translated = {}
        voting_protocol_specific_data = {}
        dao_translated = self.new_translated_dao(diagram, dao, dao_specific_data_translated)
        # vars
        entities_amount = len(dao.roles) + len(dao.committees)
        group_size:user_functionalities_group_size_module.UserFunctionalitiesGroupSize = dao.metadata.user_functionalities_group_size
        group_mask_size = group_size.get_mask_size()
        id_var_type = self.get_variable_type(dao, group_size)
        is_role_access_optimized = group_size is not None
        functionalities_ids = self.compute_states_variables__functionalities_ids(dao)
        rccd = self.compute_states_variables__roles_committee_computed_data(dao, functionalities_ids, group_size)
        entity_to_data = rccd["entity_to_data"]
        roles_computed_data = rccd["roles_computed_data"]
        committees_computed_data = rccd["committees_computed_data"]
        mask_id = group_size.get_mask_id()
        permission_to_index:dict[str, int] = {permission: idx for idx, permission in enumerate(dao.permissions)}
        space_to_underscore_fn = lambda t: t.replace(" ", "_")
        # generate_header
        dao_specific_data_translated["dao_name"] = dao.dao_name
        # generate_contract_declaration
        dao_specific_data_translated["mission_statement"] = dao.mission_statement
        dao_specific_data_translated["dao_conditions"] = dao.conditions
        # generate_state_variables
        dao_specific_data_translated["visibility"] = "internal"
        dao_specific_data_translated["id_var_type"] = id_var_type
        dao_specific_data_translated["perm_var_type"] = self.get_permission_array_size(dao)
        dao_specific_data_translated["voting_conditions"] = dao.voting_conditions
        dao_specific_data_translated["proposal_conditions"] = dao.proposal_conditions
        dao_specific_data_translated["assignment_conditions"] = dao.assignment_conditions
        # generate_has_permission_modifier
        dao_specific_data_translated["is_role_access_optimized"] = is_role_access_optimized
        dao_specific_data_translated["total_roles_amount"] = entities_amount
        dao_specific_data_translated["roles"] = dao.roles
        dao_specific_data_translated["committees"] = dao.committees
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
        dao_specific_data_translated["constructor_parameters"] = self.get_dao_constructor_parameters(dao, id_var_type)
        body_constructor_data = self.get_dao_constructor_body(dao, id_var_type)
        if body_constructor_data is not None:
            dao_specific_data_translated.update(body_constructor_data)
        # ... generate_role_permission_mapping
        dao_specific_data_translated["entities_permissions"] = self.generate_role_permission_mapping_data(dao, space_to_underscore_fn, permission_to_index, is_role_access_optimized)
        # generate_committee_initialization_function
        dao_specific_data_translated["visibility_committee_initialization_function"] = "external"
        dao_specific_data_translated["space_to_underscore_fn"] = space_to_underscore_fn
        # generate_functions
        dao_specific_data_translated["group_size_bitmask"] = group_mask_size
        dao_specific_data_translated["id_mask"] = mask_id
        # generate_permission_functions
        dao_specific_data_translated["permissions"] = list(dao.permissions.values())
        dao_specific_data_translated["permission_index_by_id"] = permission_to_index
        dao_specific_data_translated["function_permission_name_by_id"] = self.get_function_permission_name_by_id(dao)
        has_voting_proposal = self.has_default_functions_overridden(dao)
        dao_specific_data_translated["voting_function"] = has_voting_proposal["voting_function"]
        dao_specific_data_translated["proposal_function"] = has_voting_proposal["proposal_function"]
        
        # TODO: 2025-08-06
        # 1) TESTAREEEE
        # 2) translate_committee_solidity 
        for c in dao.committees.values():
            c_t = self.translate_committee_solidity(diagram, dao, c)
            dao_translated.add_translated_committee(c_t)
        return dao_translated

    def translate_committee_solidity(self, diagram: dm.DiagramManager, dao: d.DAO, committee: c.Committee) -> stg.TranslatedDAO:
        committee_specific_data_translated = {}
        voting_protocol_specific_data = {}
        committee_translated:TranslatedCommittee_Jinja_1_0_0 = self.new_translated_committee(diagram, dao, committee, committee_specific_data_translated)
        committee_translated.voting_protocol_specific_data = voting_protocol_specific_data
        # TODO: 2025-08-06 : completare il resto della traduzione dentro a "committee_specific_data_translated"

        """
        
            all_smart_contracts: list[TranslatedSmartContract] = []
            # at first, translate all Committees
            ct = CommitteeTranslator(self.context)
            for c in self.context.dao.committees.values():
                voting_permission_key = c.committee_id + "VotingRight"
                proposal_permission_key = c.committee_id + "ProposalRight"
                voting_permission_index = self.context.permission_to_index[voting_permission_key]
                proposal_permission_index = self.context.permission_to_index[proposal_permission_key]
                translated_committee = ct.translateCommittee(c, proposal_permission_index , voting_permission_index, optimized=True) 
                all_smart_contracts.append(translated_committee)
            all_smart_contracts.append(self.generate_IPermissionManager_interface())
            if self.context.dao.conditions != []:
                all_smart_contracts.append(self.generate_ICondition_interface()) 
                for condition in self.context.dao.conditions:
                    if condition is not None:
                        c= ConditionTranslator(self.context)
                        condition_sc = c.generate_condition_from_template("Templates/", \
                            condition_name= u.camel_case(condition), \
                            condition_logic="//TODO: Implement the condition smart contract logic here", \
                            return_value = "true", \
                            extension=".sol")
                        all_smart_contracts.append(condition_sc)
        """

        # TODO: (2025-08-13)
        # under "translator.py", see "generate_voting_protocol_from_template"
        # ... it's called in "translator.py/CommitteeTranslator#translateCommittee(..)"

        # START translateCommittee ...
        voting_permission_key = committee.get_id() + "VotingRight"
        proposal_permission_key = committee.get_id() + "ProposalRight"
        voting_permission_index = self.context.permission_to_index[voting_permission_key]
        proposal_permission_index = self.context.permission_to_index[proposal_permission_key]
        
        #
        contract_name = committee.committee_description.replace(" ","_")
        self.prepare_committee_voting_protocol(diagram, dao, committee, committee_translated)
        decision_making_method = committee.decision_making_method

        # ... END translateCommittee.

        return committee_translated

    # overrides 

    def new_translated_diagram(self, diagram:dm.DiagramManager, other_data=None) -> TranslatedDiagram_Jinja_1_0_0:
        return TranslatedDiagram_Jinja_1_0_0(diagram, diagram_specific_data=other_data)

    def new_translated_dao(self, diagram:dm.DiagramManager, dao:d.DAO, other_data=None) -> TranslatedDAO_Jinja_1_0_0:
        return TranslatedDAO_Jinja_1_0_0(dao, other_data)

    def new_translated_committee(self, diagram:dm.DiagramManager, dao:d.DAO, committee:c.Committee, other_data=None) -> TranslatedCommittee_Jinja_1_0_0:
        return TranslatedCommittee_Jinja_1_0_0(committee, other_data)

    #

    # helper functions

    #

    def get_variable_type(self, dao:d.DAO, group_size:user_functionalities_group_size_module.UserFunctionalitiesGroupSize):
        id_var_type = "bytes32" if group_size is None else f"uint{group_size.to_maximum_size()}"
        return id_var_type
    
    
    def get_permission_array_size(self, dao:d.DAO):
        perm_var_type = None
        permissions_amount = len(dao.permissions)
        if permissions_amount <= 8:
            perm_var_type = "uint8" 
        elif permissions_amount <= 16:
            perm_var_type ="uint16"
        elif permissions_amount  <= 32:
            perm_var_type = "uint32"
        elif permissions_amount  <= 64:
            perm_var_type = "uint64"
        elif permissions_amount <= 128:
            perm_var_type = "uint128"
        elif permissions_amount <= 256:
            perm_var_type = "uint256"
        return perm_var_type
    
    def compute_states_variables__functionalities_ids(self, dao:d.DAO):
        i = 0
        functionalities_ids = {}
        for role in dao.roles.values():
            functionalities_ids[role.get_id()] = i
            i += 1
        for committee in dao.committees.values():
            functionalities_ids[committee.get_id()] = i
            i += 1
        return functionalities_ids
    
    
    def __get_control_bitflags(self, \
        dao:d.DAO, \
        role_or_committee: aggregable_e.AggregableEntity, \
        r_o_c_ID:str, \
        group_size:user_functionalities_group_size_module.UserFunctionalitiesGroupSize, \
        functionalities_ids \
        ):
            bits_for_id = group_size.value[1]
            mask = 0
            is_transitive = dao.hierarchical_inheritance == 1 or dao.hierarchical_inheritance == "1"
            if not dao.dao_control_graph.has_node(r_o_c_ID):
                return 0, 0
            all_controllers = dao.dao_control_graph.get_all_descendants_of(r_o_c_ID) \
                if is_transitive else \
                role_or_committee.controllers
            if is_transitive and dao.dao_control_graph.has_edge(r_o_c_ID, r_o_c_ID):
                all_controllers.append(r_o_c_ID)
            for controller in all_controllers:
                index = functionalities_ids[controller]
                mask |= (1 << index) 
            return  mask << bits_for_id, mask

    def compute_states_variables__roles_committee_computed_data(self, dao:d.DAO, functionalities_ids, group_size):
        #entities_amount = len(dao.roles) + len(dao.committees)
        index_entity = 0
        entity_to_data = {}
        roles_computed_data = {}
        committees_computed_data = {}
        for role in dao.roles.values():
            mask_shifted_for_id_bits, original_mask = self.__get_control_bitflags(dao, role, role.get_id(), group_size, functionalities_ids)
            final_id = functionalities_ids[role.get_id()] | mask_shifted_for_id_bits
            name_sanitized = role.role_name.replace(" ","_")
            #lines.append(f"        {final_id}{',' if index_entity != (entities_amount -1) else ''} // #{index_entity}) {name_sanitized} -> ID : {functionalities_ids[role.get_id()]} , control bitmask: { '{0:b}'.format( original_mask ) }")
            index_entity += 1
            ed = newEntityData( \
                final_id=final_id, \
                name=name_sanitized, \
                index=index_entity, \
                original_id=role.get_id(), \
                entity_type=etc.EntityTypeControllable.ROLE.value, \
                mask=original_mask
            )
            entity_to_data[role.get_id()] = ed
            roles_computed_data[role.get_id()] = ed
            
        for committee in dao.committees.values():
            mask_shifted_for_id_bits, original_mask = self.__get_control_bitflags(dao, committee, committee.get_id(), group_size, functionalities_ids)
            final_id = functionalities_ids[committee.get_id()] | mask_shifted_for_id_bits
            name_sanitized = committee.committee_description.replace(" ","_")
            #lines.append(f"        {final_id}{',' if index_entity != (entities_amount -1) else ''} // #{index_entity})  {name_sanitized} -> ID : {functionalities_ids[committee.get_id()]} , control bitmask: { '{0:b}'.format( original_mask ) }")
            index_entity += 1
            ed = newEntityData( \
                final_id=final_id, \
                name=name_sanitized, \
                index=index_entity, \
                original_id=committee.get_id(), \
                entity_type=etc.EntityTypeControllable.COMMITTEE.value, \
                mask=original_mask
            )
            entity_to_data[committee.get_id()] = ed
            committees_computed_data[committee.get_id()] = ed
        return { \
            "entity_to_data": entity_to_data, \
            "roles_computed_data": roles_computed_data, \
            "committees_computed_data": committees_computed_data \
        }

    def get_dao_constructor_parameters(self, dao:d.DAO, id_var_type:str) -> dict:
        params:list[dict] = []
        if dao.conditions != []:
            params.append({"type": id_var_type, "name": "roleIds"})
        if dao.voting_conditions != {}:
            params.append({"type": "address", "name": "votingConditionAddresses"})
        if dao.proposal_conditions != {}:
            params.append({"type": "address", "name": "proposalConditionAddresses"})
        if dao.assignment_conditions != {}:
            params.append({"type": "address", "name": "assignmentConditionAddresses"})
        return params
    
    def generate_role_permission_mapping_data(self, dao:d.DAO, space_to_underscore_fn, permission_to_index:dict, is_role_access_optimized:bool):
        # permission_to_index:dict[str, int]
        entities_permissions = []
        entities_map_list:list[dict[str, aggregable_e.AggregableEntity]] = [ \
            dao.roles, \
            dao.committees \
        ]
        role_to_index_fn = lambda irao, r, i_e: f"{i_e}" if irao else r
        index_entity = 0
        for entity_map in entities_map_list:
            for entity in entity_map.values():
                permission_indices = [permission_to_index[permission.get_id()] for permission in entity.permissions]
                # Set the bit for each permission index
                bitflag = 0
                for index in permission_indices:
                    bitflag |= (1 << index)
                e_name = space_to_underscore_fn(entity.get_name())
                entities_permissions.append({ \
                    "entity_name": e_name,
                    "permission_indices": permission_indices,
                    "bitflag": bitflag,
                    "index_entity_in_dao": role_to_index_fn(is_role_access_optimized, e_name, index_entity),
                    "index_entity": index_entity
                })
                index_entity += 0
        return  entities_permissions

    def get_dao_constructor_body(self, dao:d.DAO, id_var_type:str) -> dict:
        return {
            "dao_owner": True
        }
    
    def get_function_permission_name_by_id(self, dao:d.DAO):
        return {
            perm.get_id(): perm.allowed_action.replace("/", "_").replace(" ", "_").replace("\\", "") # sanitize the name
            for perm in dao.permissions.values()
        }
    
    def has_default_functions_overridden(self, dao:d.DAO):
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

    #

    # Committee stuffs

    #

    def prepare_committee_voting_protocol(self, diagram:dm.DiagramManager, dao:d.DAO, committee:c.Committee, committee_conversion:TranslatedCommittee_Jinja_1_0_0, \
            committee_name: str="", \
            decision_making_method: str="", \
        ):
        template_name = f"{decision_making_method}.sol.jinja"
        is_custom = self.all_voting_protocols
        

def newEntityData(final_id=0, name="", index=-1, original_id="", address="", entity_type:etc.EntityTypeControllable=None, mask:int=-1):
    if entity_type == None:
        entity_type = etc.EntityTypeControllable.ROLE.value # default
    return {\
        "final_id": final_id, \
        "name": name, \
        "index": index, \
        "original_id": original_id, \
        "address": address, \
        "entity_type": entity_type, \
        "mask": mask
    }
