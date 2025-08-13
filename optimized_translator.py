import os
import networkx as nx
from DAOclasses import*
from translator import *
from jinja2 import Template
import utils as u
from enum import Enum

class RoleInConditionCheckType(Enum):
    RETURN = 1
    REQUIRE = 2
    EXPRESSION = 3


class SolidityOptimizedTranslationContext(TranslationContext):
    def __init__(self, dao:DAO, solidity_version= "^0.8.0", daoOwner = True):
        '''
        TODO: translation context with all the data created to actually produce a Solidity file.
        All Entities (Role & Committee) 's IDs, all bitmasks, the bitmasks's mak, etc.
        This class is meant to be provided to all possible translators (Solidity file, Python stub 
        proxying the deployed DAOs, a Colored Petri Nets embedding of the whole DAO, etc ...).
        '''
        super().__init__(dao, solidity_version=solidity_version, daoOwner=daoOwner)
        self.group_size = None
        self.id_mask = None
        self.perm_var_type = None
        self.permission_to_index:dict[str, int] = {permission: idx for idx, permission in enumerate(dao.permissions)}
        self.entity_to_data:dict[str, dict[str, any]] = {} # type_return_of(newEntityData)
        

class OptimizedSolidityTranslator(Translator):
    def __init__(self, dao: DAO):
        self.context = SolidityOptimizedTranslationContext(dao, solidity_version = "^0.8.0", daoOwner = True)
        self.group_size = self.context.dao.metadata.user_functionalities_group_size
        self.id_mask = self.recalculate_id_mask()
        self.perm_var_type = self.get_permission_array_size()
        

    def recalculate_id_mask(self):
        id_mask = 0
        for i in range(self.group_size.value[1]):
            id_mask |= 1 << i
        return id_mask
    
    def generate_modifier_control_relation_OLD(self):
        id_var_type = self.get_variable_type()
        id_bit_size = self.group_size.value[1]
        mask = self.id_mask # calcolato nel costruttore
        
        lines = []
        lines.append("\n")
        lines.append(f"    modifier controlledBy(address sender, {id_var_type} user_target_role_id, bool allowNullRole) {'{'}")
        lines.append("         //we obtain the control relations of the controller role by shifting the its id by the number of bits contained in ids")
        lines.append("         //the sender must control BOTH the target role AND the user's role")
        lines.append(f"        require(")
        lines.append(f"            ( // \"CAN the sender control the target user (through its role)?\"")
        lines.append(f"                (allowNullRole && (user_target_role_id == 0)) || // allow to add role if the user has not already one assigned to it")
        lines.append(f"                ((")
        lines.append(f"                    (user_target_role_id >> {id_bit_size}) // get the role's bitmask ")
        lines.append(f"                    &  // (... and then perform the bitwise-and with ...)")
        lines.append(f"                    ( {id_var_type}(1) << ( roles[sender] & {mask} ) ) // sender_role_index")
        lines.append(f"                ) != 0) // THE FINAL CHECK")
        lines.append(f"            )")
        lines.append(f"            , \"the given controller can\'t perform the given operation on the given controlled one\" );")
        lines.append(f"            ")
        lines.append(f"            ")
        lines.append("        _;")
        lines.append("    }")
        lines.append("\n")
        return "\n".join(lines)

    def generate_modifier_sanity_check_user_exists(self):
        '''
        Deprecated
        '''
        return '''
        modifier sanityCheck_user_exists(address user){
            require(roles[user] != 0, \"The user must exists\");
            _;
        }
        '''

    def generate_modifier_role_exists(self):
        '''
        Deprecated
        '''
        id_var_type = self.get_variable_type()
        id_bit_size = self.group_size.value[1]
 
        formatting_args={
            "_id_var_type": id_var_type,
            "_id_bit_size": id_bit_size,
        }
        return '''
        modifier sanityCheck_role_exists({_id_var_type} role){
            {_id_var_type} index_role = role & {_mask};
            require(roles[user] != 0, \"The user must exists\");
            _;
        }
        '''

    def generate_modifier_control_relation(self):
        id_var_type = self.get_variable_type()
        id_bit_size = self.group_size.value[1]
        mask = self.id_mask # calcolato nel costruttore
        entities_amount = len(self.context.dao.roles) + len(self.context.dao.committees)

        formatting_args={
            "_id_var_type": id_var_type,
            "_id_bit_size": id_bit_size,
            "_mask": mask,
            "_entities_amount": entities_amount
        }
        
        lines = []
        lines.append("\n")
        #lines.append(f"    modifier controlledBy(address sender, {id_var_type} user_target_role_id, bool allowNullRole) {'{'}")
        lines.append(\
        '''
        modifier controlledBy(address sender, {_id_var_type} user_role_id, bool allowNullRole_user, {_id_var_type} new_role_id) {{
            //we obtain the control relations of the controller role by shifting the its id by the number of bits contained in ids
            //the sender must control BOTH the target role AND the user's role

            {_id_var_type} index_new_role = new_role_id & {_mask};
            {_id_var_type} sender_role_index = ( {_id_var_type}(1) << ( roles[sender] & {_mask} ) );

            require(
                ( // the new role must be a valid one
                    index_new_role < {_entities_amount} // checking for \"index out of bounds\"
                )
                && ( // \"check the sender and target user control relation\"
                    (allowNullRole_user && (user_role_id == 0)) || // allow to add role if the user doesn't have one
                    ((
                        (user_role_id >> {_id_bit_size}) // get the user role's bitmask 
                        &  // (... and then perform the bitwise-and with ...)
                        sender_role_index
                    ) != 0) // final check
                ) &&
                ( // \"control relation check between sender and the target role\"
                    (
                        ( all_roles[index_new_role] >> {_id_bit_size}) // get the new role's bitmask from those internally stored
                        &  // (... and then perform the bitwise-and with ...)
                        sender_role_index
                    ) != 0 // final check
                )
                , \"the given controller can\'t perform the given operation on the given controlled one\" );
            _;
        }}
        '''.format(**formatting_args))
        
        lines.append("\n")
        return "\n".join(lines)


    def translateDao(self) -> TranslatedSmartContract: 
        lines = []
        lines.append(self.generate_header())
        lines.append(self.generate_contract_declaration())
        lines.append(self.generate_state_variables())
        lines.append(self.generate_modifier_control_relation())
        lines.append(self.generate_has_permission_modifier())
        #lines.append(self.generate_constructor())
        lines.append(self.generate_constructor_v2())
        lines.append(self.generate_committee_initialization_function())
        lines.append(self.generate_functions())
        lines.append(self.generate_permission_functions())  
        lines.append(self.generate_closure())
        name = self.context.dao.dao_name
        return TranslatedSmartContract(lines, name, testable=True)
        #return "\n".join(lines)


    def generate_IPermissionManager_interface(self):
        lines = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append("pragma solidity ^0.8.0;")
        lines.append("interface IPermissionManager {")
        lines.append(f"    function has_permission(address user, {self.perm_var_type} permissionIndex) external view returns (bool);")
        if self.context.dao.committees != {}:
            lines.append(f"    function canVote(address user, {self.perm_var_type} permissionIndex) external view returns (bool);")
            lines.append(f"    function canPropose(address user, {self.perm_var_type} permissionIndex) external view returns (bool);")
        lines.append("}")
        return TranslatedSmartContract(lines, "IPermissionManager", folder="interfaces", testable=True)
    
    def generate_ICondition_interface(self):
        lines = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append("pragma solidity ^0.8.0;")
        lines.append("interface ICondition {")
        lines.append("    function evaluate(address user) external view returns (bool);")
        lines.append("}")
        return TranslatedSmartContract(lines, "ICondition", folder="interfaces", testable=True)

    def translate(self) -> list[TranslatedSmartContract]:
            #print("TRANSLATE() -- invocato")
            all_smart_contracts: list[TranslatedSmartContract] = [
                self.translate_DAO_to_ASM(self.context.dao)
            ]
            # at first, translate all Committees
            ct = CommitteeTranslator(self.context)
            for c in self.context.dao.committees.values():
                print(f"\t translating committee: {c.committee_description}")
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
            # in the end, the DAO itself
            all_smart_contracts.append(self.translateDao())
            
            return all_smart_contracts
    


    def generate_header(self):
        lines = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version};")
        lines.append(f"/**")
        lines.append(f" * @title {self.context.dao.dao_name}")
        lines.append(f" * @notice {self.context.dao.mission_statement}")
        lines.append(f" */")
        return "\n".join(lines)

    def generate_contract_declaration(self):
        lines = []
        lines.append("import \"./interfaces/IPermissionManager.sol\";")
        if self.context.dao.conditions != []:
            lines.append(f"import \"./interfaces/ICondition.sol\";")
        lines.append( f"contract {self.context.dao.dao_name} is IPermissionManager {'{'}")
        return "\n".join(lines)
    
    def get_control_bitflags(self, role_or_committee, r_o_c_ID, group_size, functionalities_ids):
            bits_for_id = group_size.value[1]
            mask = 0
            is_transitive = self.context.control_transitivity

            if not self.context.dao.dao_control_graph.control_graph.has_node(r_o_c_ID):
                return 0, 0

            all_controllers = list( nx.descendants(self.context.dao.dao_control_graph.control_graph, r_o_c_ID) ) \
                if is_transitive else \
                role_or_committee.controllers
            if is_transitive and self.context.dao.dao_control_graph.control_graph.has_edge(r_o_c_ID, r_o_c_ID):
                all_controllers.append(r_o_c_ID)
            for controller in all_controllers:
                index = functionalities_ids[controller]
                mask |= (1 << index) 
            return  mask << bits_for_id, mask

    def get_variable_type(self):
        id_var_type = "bytes32"
        if self.group_size == UserFunctionalitiesGroupSize.SMALL:
            id_var_type = "uint32"
        elif self.group_size == UserFunctionalitiesGroupSize.MEDIUM:
            id_var_type = "uint64"
        elif self.group_size == UserFunctionalitiesGroupSize.LARGE:
            id_var_type = "uint128"
        elif self.group_size == UserFunctionalitiesGroupSize.EXTRA_LARGE:
            id_var_type = "uint256"
        return id_var_type
    
    def get_permission_array_size(self):
        perm_var_type = None
        permissions_amount = len(self.context.dao.permissions)
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

    def generate_state_variables(self, visibility = "internal", constant = ""):
        id_var_type = self.get_variable_type()
        
        lines = []
        lines.append(f"    bool {visibility} committee_initialization_blocked;")
        lines.append(f"    mapping(address => {id_var_type}) {visibility} roles;")
        if self.context.dao.voting_conditions != {}:
            lines.append(f"    mapping({id_var_type} => ICondition) {visibility} voting_conditions;")
        if self.context.dao.proposal_conditions != {}:
            lines.append(f"    mapping({id_var_type} => ICondition) {visibility} proposal_conditions;")
        if self.context.dao.assignment_conditions != {}:        
            lines.append(f"    mapping({id_var_type} => ICondition) {visibility} assignment_conditions;")
        # Now, define the way a "role_permission" must work; in particular how
        # its data is accessed: if we are still "optimizing" (i.e., the
        # "self.group_size" is NOT "None", i.e. its value is a UserFunctionalitiesGroupSize
        # ones) then we could extract an index from a role and define the 
        # "role_permissions" as an array;
        # otherwise, "role_permission" is a straightforward "mapping", i.e. the
        # "role" as a whole is used as the mapping's key
        is_role_access_optimized = self.group_size is not None
        if is_role_access_optimized:
            # since both the Roles and Committees are pre-defined and, therefore, fixed, they work ad Enum,
            # therefore their total amount is fixed -> the "role_permissions" array can be optimized as a 
            # "fixed array" by specifying its size
            total_roles_amount = len(self.context.dao.roles) + len(self.context.dao.committees)
            lines.append(f"    {self.perm_var_type}[{total_roles_amount}] {visibility} role_permissions;")
        else:
            lines.append(f"    mapping({id_var_type} => {self.perm_var_type}) {visibility} role_permissions;")
        i = 0
        functionalities_ids = {}
        
        for role in self.context.dao.roles.values():
            functionalities_ids[role.role_id] = i
            i += 1
        for committee in self.context.dao.committees.values():
            functionalities_ids[committee.committee_id] = i
            i += 1
        
        entities_amount = len(self.context.dao.roles) + len(self.context.dao.committees)
        lines.append(f"    {id_var_type}[{entities_amount}] {visibility} all_roles = [")

        index_entity = 0
        for role in self.context.dao.roles.values():
            mask_shifted_for_id_bits, original_mask = self.get_control_bitflags(role, role.role_id, self.group_size, functionalities_ids)
            final_id = functionalities_ids[role.role_id] | mask_shifted_for_id_bits
            name_sanitized = role.role_name.replace(" ","_")
            lines.append(f"        {final_id}{',' if index_entity != (entities_amount -1) else ''} // #{index_entity}) {name_sanitized} -> ID : {functionalities_ids[role.role_id]} , control bitmask: { '{0:b}'.format( original_mask ) }")
            index_entity += 1

            self.context.entity_to_data[role.role_id] = newEntityData(final_id=final_id, name=name_sanitized, index=index_entity, original_id=role.role_id, entity_type=EntityTypeControllable.ROLE.value)
            
        for committee in self.context.dao.committees.values():
            mask_shifted_for_id_bits, original_mask = self.get_control_bitflags(committee, committee.committee_id, self.group_size, functionalities_ids)
            final_id = functionalities_ids[committee.committee_id] | mask_shifted_for_id_bits
            name_sanitized = committee.committee_description.replace(" ","_")
            lines.append(f"        {final_id}{',' if index_entity != (entities_amount -1) else ''} // #{index_entity})  {name_sanitized} -> ID : {functionalities_ids[committee.committee_id]} , control bitmask: { '{0:b}'.format( original_mask ) }")
            index_entity += 1
            self.context.entity_to_data[committee.committee_id] = newEntityData(final_id=final_id, name=name_sanitized, index=index_entity, original_id=committee.committee_id, entity_type=EntityTypeControllable.COMMITTEE.value)

        #print(self.context.entity_to_data)

        lines.append("    ];")
        #generate events
        lines.append(self.generate_events())
        return "\n".join(lines)
    
    def generate_events(self):
        id_var_type = self.get_variable_type()
        lines = []
        lines.append(f" //Events")
        lines.append(f"    event RoleRevoked(address indexed user, {id_var_type} indexed role);")
        lines.append(f"    event RoleAssigned(address indexed user, {id_var_type} indexed role);")
        lines.append(f"    event PermissionGranted({id_var_type} indexed role, {self.perm_var_type} indexed permission);")
        lines.append(f"    event PermissionRevoked({id_var_type} indexed role, {self.perm_var_type} indexed permission);")
        return "\n".join(lines)


    def generate_constructor_v2(self):
        id_var_type = self.get_variable_type()
        lines = []
        lines.append("    constructor(")
        if self.context.dao.conditions != []:
            lines.append(f"{id_var_type}[] memory roleIds, ")
        if self.context.dao.voting_conditions != {}:        
            lines.append("address[] memory votingConditionAddresses, ")
        if self.context.dao.proposal_conditions != {}:
            lines.append("address[] memory proposalConditionAddresses, ")
        if self.context.dao.assignment_conditions != {}:
            lines.append("address[] memory assignmentConditionAddresses")
        lines.append(") {")
            
        lines.append(self.generate_role_permission_mapping())
        if self.context.daoOwner:
            lines.append(f"roles[msg.sender] = all_roles[{len(self.context.dao.roles)-1}]; // {self.context.dao.dao_name}Owner")
        if self.context.dao.conditions != []:
            lines.append("for (uint256 i = 0; i < roleIds.length; i++) { ")
        if self.context.dao.voting_conditions != {}:
            lines.append("     voting_conditions[roleIds[i]] = ICondition(votingConditionAddresses[i]);")
        if self.context.dao.proposal_conditions != {}:
            lines.append("     proposal_conditions[roleIds[i]] = ICondition(proposalConditionAddresses[i]);")
        if self.context.dao.assignment_conditions != {}:
            lines.append("     assignment_conditions[roleIds[i]] = ICondition(assignmentConditionAddresses[i]);")
            lines.append("      }")
        lines.append("}")
        return "\n".join(lines)
        


    def generate_constructor(self):
        committee_list_param = [f"address _{x}" for x in [committee.committee_description.replace(" ", "_")for committee in self.context.dao.committees.values()] ]
        committee_address_list = ', '.join(committee_list_param)
        lines = []
        lines.append(f"    constructor( {committee_address_list}) {'{'}")
        lines.append(" require(roleIds.length == votingConditionAddresses.length, \"Role ID and voting condition count mismatch\");")
        lines.append(" require(roleIds.length == proposalConditionAddresses.length, \"Role ID and proposal condition count mismatch\");")
        lines.append(" require(roleIds.length == assignmentConditionAddresses.length, \"Role ID and assignment condition count mismatch\"); \n")
        lines.append(self.generate_role_permission_mapping())
        for committee in self.context.dao.committees.values():
            lines.append(f"         roles[_{committee.committee_description.replace(' ','_')}] = {committee.committee_description.replace(' ','_')}; \n" )
        if self.context.daoOwner:
            #lines.append(f"        roles[msg.sender] = {self.context.dao.dao_name}Owner;")
            lines.append(f"        roles[msg.sender] = all_roles[{len(self.context.dao.roles)}]; // {self.context.dao.dao_name}Owner")
 
        lines.append("    }")
        return "\n".join(lines)

    
    def generate_has_permission_modifier(self):
        #id_var_type = self.get_variable_type()
        is_role_access_optimized = self.group_size is not None
        eventual_addressing_manipulation = f" & {self.id_mask}" if is_role_access_optimized else ""

        return f""" 
    modifier hasPermission(address _executor, {self.perm_var_type} _permissionIndex) {{
        require(role_permissions[{self.perm_var_type}(roles[_executor]{eventual_addressing_manipulation})] & ({self.perm_var_type}(1) << _permissionIndex) != 0, "User does not have this permission");
        _;
    }}
            """
    

    def generate_committee_initialization_function(self, visibility = "external"):
        committee_list_param = [f"address _{x}" for x in [committee.committee_description.replace(" ","_") for committee in self.context.dao.committees.values()] ]
        committee_address_list = ', '.join(committee_list_param)
        lines = []
        lines.append(f"    function initializeCommittees({committee_address_list}) {visibility} {'{'}")
        index_role_owner = len(self.context.dao.roles) -1
        lines.append(f"        require(roles[msg.sender] == all_roles[{index_role_owner}], \"Only the owner can initialize the Dao\");  // {self.context.dao.dao_name}Owner")
        if len(self.context.dao.committees) > 0:
            committee_requires = ' && '.join([f"_{x} != address(0)" for x in [committee.committee_description.replace(" ","_") for committee in self.context.dao.committees.values()] ])
            lines.append(f"    require(committee_initialization_blocked == false && {committee_requires}, \"Invalid committee initialization\");")
 
            committees_as_list = list(self.context.dao.committees.values())
            for index_committee, committee in enumerate(committees_as_list):
                sanitized_committee_name = committee.committee_description.replace(" ","_")
                lines.append(f"        roles[_{sanitized_committee_name}] = all_roles[{index_committee}]; // {sanitized_committee_name}")
            lines.append("        committee_initialization_blocked = true;")
        lines.append("    }")
        return "\n".join(lines)
    
    def generate_functions(self):
        id_var_type = self.get_variable_type()
        perm_var_type = self.perm_var_type
        is_role_access_optimized = self.group_size is not None
        eventual_addressing_manipulation = f" & {self.id_mask}" if is_role_access_optimized else ""

        return f"""
        
        function canControl({id_var_type} controller, {id_var_type} controlled) public pure returns(bool controls){{
             // ( "CAN the sender control the target user (through its role)?"
                //(allowNullRole && (target_role_id == 0)) || // allow to add role if the user has not already one assigned to it
                if((
                    (controlled >> {self.group_size.value[1]} ) // get the role's bitmask 
                    &  // (and then perform the bitwise-and with ...)
                    ({id_var_type}(1) << ( controller & {self.id_mask} )) // (...) get the sender role's index AND shift it accordingly 
                ) != 0 ){{
                    controls = true;
                     return controls;}} else {{return controls;}}
        }}
        
        function assignRole(address _user, {id_var_type} _role) external controlledBy(msg.sender, roles[_user], true, _role) {{
            require(_user != address(0) , "Invalid user address" );
            {self.generate_user_role_condition_evaluation("assignment_conditions", "_user", RoleInConditionCheckType.REQUIRE) if self.context.dao.assignment_conditions != {} else ""}
            roles[_user] = _role;
            emit RoleAssigned(_user, _role);
        }}

        function revokeRole(address _user, {id_var_type} _role) external controlledBy(msg.sender, roles[_user], false, _role) {{
            require(roles[_user] == _role, "User's role and the role to be removed don't coincide" );

            delete roles[_user];
            emit RoleRevoked(_user, _role);
        }}

        function grantPermission({id_var_type} _role, {perm_var_type} _permissionIndex) external hasPermission(msg.sender, _permissionIndex) {{
            require(canControl(roles[msg.sender], _role), "cannot grant permission, as the control relation is lacking");
            {perm_var_type} new_role_perm_value;
            new_role_perm_value  = role_permissions[_role & {self.id_mask} ] | ({perm_var_type}(1) << _permissionIndex);
            role_permissions[_role & {self.id_mask} ] = new_role_perm_value;
            
            emit PermissionGranted(_role, _permissionIndex);
        }}

        function revokePermission({id_var_type} _role, {perm_var_type}  _permissionIndex) external hasPermission(msg.sender, _permissionIndex) {{
            require(canControl(roles[msg.sender], _role), "cannot revoke permission, as the control relation is lacking");
            {perm_var_type} new_role_perm_value;
            new_role_perm_value = role_permissions[_role & {self.id_mask}] & ~({perm_var_type}(1) << _permissionIndex);
            role_permissions[_role & {self.id_mask}] = new_role_perm_value;

            emit PermissionRevoked(_role, _permissionIndex);
        }}

        function hasRole(address user) external view returns({id_var_type}) {{
            return roles[user];
        }}

        function has_permission(address user, {self.perm_var_type} _permissionIndex) external view returns (bool) {{
            if (role_permissions[{self.perm_var_type}(roles[user]{eventual_addressing_manipulation})] & ({self.perm_var_type}(1) << _permissionIndex) != 0){{ 
                return true;
            }}else{{
                return false;
            }}
        }}
             
         """
      
    def generate_role_permission_mapping(self):
        # Create a mapping from role IDs to the indices of the permissions they have
        entities_permissions = []
        for role in self.context.dao.roles.values():
            entities_permissions.append((role.role_name.replace(" ","_"), [self.get_permission_index(permission.permission_id) for permission in role.permissions]))
        for committee in self.context.dao.committees.values():
            entities_permissions.append((committee.committee_description.replace(" ","_"), [self.get_permission_index(permission.permission_id) for permission in committee.permissions]))
            
        # define the way a "role_permission" must work; in particular how
        # its data is accessed: if we are still "optimizing" (i.e., the
        # "self.group_size" is NOT "None", i.e. its value is a UserFunctionalitiesGroupSize ones)
        # then we could extract an index from a role and define the "role_permissions" as an array;
        # otherwise, "role_permission" is a straightforward "mapping", i.e. the "role" as a whole is used
        # as the mapping's key
        is_role_access_optimized = self.group_size is not None
        role_to_index_fn = lambda irao, r, index_role: f"{index_role}" if irao else r
        # Generate the Solidity code to set the role_permissions mapping
        lines = []
        for index_entity, entity_data in enumerate(entities_permissions, start=0):
                role = entity_data[0]
                permission_indices = entity_data[1]
                # Initialize the bitflag for the given role
                bitflag = 0
                # Set the bit for each permission index
                for index in permission_indices:
                    bitflag |= (1 << index)
                lines.append(f"        role_permissions[{role_to_index_fn(is_role_access_optimized,role, index_entity)}] = {bitflag}; // #{index_entity}) {role} \n")
        return "\n".join(lines)
    
    def generate_user_role_condition_evaluation(self, condition_mapping_name, user_variable_name, roleInConditionCheckType: RoleInConditionCheckType = RoleInConditionCheckType.RETURN):
        condition_fetching = lambda is_generating_variable: f"{'ICondition _condition =' if is_generating_variable else ''} {condition_mapping_name}[roles[msg.sender]] {';' if is_generating_variable else ''}"
        expression_check = lambda is_previously_fetched: f"({'_condition' if is_previously_fetched else condition_fetching(False)} == ICondition(address(0))) || {'_condition' if is_previously_fetched else condition_fetching(False)}.evaluate({user_variable_name})"
        if roleInConditionCheckType == RoleInConditionCheckType.RETURN:
            return f"""
                {condition_fetching(True)}
                return {expression_check(True)};
            """
        elif roleInConditionCheckType == RoleInConditionCheckType.REQUIRE:
            return f"""
                {condition_fetching(True)}
                require({expression_check(True)}, "User does not meet the required conditions");
            """
        elif roleInConditionCheckType == RoleInConditionCheckType.EXPRESSION:
            return f"{expression_check(False)}"
        raise Exception(f"Invalid RoleInConditionCheckType: {roleInConditionCheckType}")

    def generate_permission_functions(self):
        lines = []
        voting_function = False
        proposal_function = False
        for perm in self.context.dao.permissions.values():
            if perm.voting_right:
                voting_function = True
            if perm.proposal_right:
                proposal_function = True
            if perm.voting_right or perm.proposal_right:
                continue
            function_name = self.preprocess_function_name(perm.allowed_action)
            permission_index = self.get_permission_index(perm.permission_id)
            lines.append(f"""
        function {function_name}() external hasPermission(msg.sender, {permission_index}) {{
            // TODO: Implement the function logic here
        }}
                """)
            
        if voting_function:
            lines.append(f"""
            function canVote(address user, {self.perm_var_type} permissionIndex) external view returns (bool) {'{'}
                require(role_permissions[{self.perm_var_type}(roles[user] & 31)] & ({self.perm_var_type}(1) << permissionIndex) != 0, "User does not have this permission");
                {self.generate_user_role_condition_evaluation("voting_conditions", "user") if self.context.dao.voting_conditions != {} else "return true;"}
            {'}'}""")

        if proposal_function:
            lines.append(f"""
            function canPropose(address user, {self.perm_var_type} permissionIndex) external view returns (bool) {'{'}
                require(role_permissions[{self.perm_var_type}(roles[user] & 31)] & ({self.perm_var_type}(1) << permissionIndex) != 0, "User does not have this permission");
                {self.generate_user_role_condition_evaluation("proposal_conditions", "user") if self.context.dao.proposal_conditions != {} else "return true;"}
            {'}'}""")
            
        return "\n".join(lines)


    def preprocess_function_name(self, function_name):
        return function_name.replace("/", "_").replace(" ", "_").replace("\\", "")


    def get_permission_index(self, permission):
        #Map permission_id to an integer index
        return self.context.permission_to_index[permission]

    def generate_closure(self):
        return "}"


    def translate_DAO_to_ASM(self, dao:DAO) -> TranslatedSmartContract:
        asm_data = {}
        template_path = os.path.join('.', "Templates", "asm", "")
        name = "DAOML"
        output_folder = "ASM"
        #
        controls_relation:dict[str, set[str]] = {} # reverse directio of "is_controlled_by"
        entities_controllable:list[list[BaseEntity]] = [dao.roles.values(),  dao.committees.values()]
        for entities in entities_controllable:
            for e_slave in entities:
                masters:list[str] = e_slave.controllers
                for master_controller in masters:
                    slaves_set:set[str] = None
                    if master_controller in controls_relation:
                        slaves_set = controls_relation[master_controller]
                    else:
                        slaves_set = set()
                        controls_relation[master_controller] = slaves_set
                    slaves_set.add(e_slave.get_id())
        asm_data["roles"] = [
            {
                "name": r.role_name,
                "permissions": [p.permission_id for p in r.permissions],
                "controls": list(controls_relation[r.get_id()]) if r.get_id() in controls_relation else [],
                "aggregation": "" if len(r.aggregated) <= 0 else r.aggregated[0].get_name()
            }
            for r in dao.roles.values()
        ]
        asm_data["committees"] = [
            {
                "name": c.committee_description,
                "permissions": [p.permission_id for p in c.permissions],
                "controls":  list(controls_relation[c.get_id()]) if c.get_id() in controls_relation else [],
                "aggregation": "" if len(c.aggregated) <= 0 else c.aggregated[0].get_name()
            }
            for c in dao.committees.values()
        ] 
        asm_data["permissions"] = [
            {
                "name": p.permission_id,
                "governanceArea": p.ref_gov_area
            }
            for p in dao.permissions.values()
        ]
        asm_data["governanceAreas"] = [] # no governance area management defined at this stage of development
        asm_data["users"] = [] # no user pre-defined (apart from the Owner) at this stage of development
        asm_data["custom_operations"] = [] # no custom operation defined at this stage of development
        #
        return super().generate_file_from_template(
            template_path,
            name,
            output_folder,
            extension = ".asm",
            additional_parametrs=asm_data,
            reuse_additional_params_dit=True
        )

class ConditionTranslator:
    def __init__(self, context: TranslationContext):
        self.context = context
        
    def generate_condition_from_template(self, template_path: str, condition_name: str, condition_logic, return_value, extension=".sol") -> TranslatedSmartContract:
    # Define the full path to the template file
        output_folder = "conditions"
        file_name_and_path = template_path + "ConditionImplementation" + extension + ".jinja"
        # Initialize an empty list to store each rendered line
        rendered_lines = []
        # Open the template file and read it line by line
        with open(file_name_and_path, 'r', encoding='utf-8') as f:
            # For each line in the template, render it individually
            for line in f:
                # Create a Jinja2 template object for each line
                template = Template(line)
                # Render the line with any dynamic content (e.g., Solidity version)
                rendered_line = template.render(solidity_version=self.context.solidity_version,condition_name=u.camel_case(condition_name), condition_logic=condition_logic,return_value=return_value )
                rendered_lines.append(rendered_line)
        # Return a TranslatedSmartContract object with the list of rendered lines
        return TranslatedSmartContract(rendered_lines, u.camel_case(condition_name), folder=output_folder, testable=True)
