

import networkx as nx
from DAOclasses import DAO, Committee, GraphType, Permission
from translator import *

#class BaseTranslator:
    #TODO
    

class SimpleSolidityTranslator(Translator):
    def __init__(self, dao: DAO, role_declaration_policy = "index", solidity_version= "^0.8.0", daoOwner = True):
        self.context = TranslationContext(dao, role_declaration_policy, solidity_version, daoOwner)
        self.context.entity_to_data= {} # type_return_of(newEntityData)
        self.committee_permission_indices:dict[str, int]= {}
        self.context.role_declaration_policy = "index" if self.context.dao.dao_control_graph.graph_type != GraphType.LIST else "topological_ordering"
        self.role_to_final_index = {}
        
        for role in self.context.dao.roles.values():
            role.role_name = self.preprocess_entity_name(role.role_name)
        for committee in self.context.dao.committees.values():
            committee.committee_description = self.preprocess_entity_name(committee.committee_description)
        


    def translateDao(self) -> TranslatedSmartContract:
        lines:list[str] = []

        DAO_mission_statement_comment = f"// @title {self.preprocess_entity_name(self.context.dao.dao_name)} has the following mission: {self.context.dao.mission_statement}"
        lines.extend(self.generate_smart_contract_header(DAO_mission_statement_comment))

        lines.extend(self.generate_contract_declaration(self.context.dao.dao_name.replace(" ", "_")))
        lines.extend(self.generate_roles())
        
        lines.extend(self.generate_constructor())
        lines.extend(self.generate_functions())
        lines.append(self.generate_closure())

        name = self.preprocess_entity_name(self.context.dao.dao_name)
        return TranslatedSmartContract(lines, name, testable=True)
    

    def translate(self) -> list[TranslatedSmartContract]:
        all_smart_contracts: list[TranslatedSmartContract] = []
        all_smart_contracts.append(self.translateDao())
        # at first, translate all Committees
        ct = CommitteeTranslator(self.context)
        for c in self.context.dao.committees.values():
            translated_committee = ct.translateCommittee(c, voting_permission_index=self.committee_permission_indices[c.committee_description], proposal_permission_index=self.committee_permission_indices[c.committee_description], optimized=False) 
            all_smart_contracts.append(translated_committee)
            all_smart_contracts.append(self.generate_IPermissionManager_interface())        
        return all_smart_contracts


    def generate_IPermissionManager_interface(self):
        lines = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version};")
        lines.append("interface IPermissionManager {")
        lines.append(f"    function isCommitteeMember(address user, uint committee) external view returns (uint);")
        lines.append("}")
        return TranslatedSmartContract(lines, "IPermissionManager", folder="interfaces", testable=True)


    def generate_smart_contract_header(self, title_comment = "") -> list[str]:
        lines:list[str] = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version};")
        lines.append(f"import \"./interfaces/IPermissionManager.sol\";")
        lines.append(title_comment)
        return lines
        

    def generate_contract_declaration(self, contract_name) -> list[str]:
        return [f"contract {contract_name} is IPermissionManager " + "{"]

    def preprocess_entity_name(self, entity_name:str) -> str:
        return entity_name.replace(" ", "_").replace("/", "_").replace("\\", "_").replace("(", "").replace(")", "").replace(":", "").replace(";", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace("\"", "").replace("’", "").replace("‘", "").replace("“", "").replace("”", "").replace("–", "").replace("-", "").replace("—", "").replace("–", "").replace("—", "")


    def generate_roles(self) -> list[str]:
        lines:list[str] = []
        lines.append(f"// role declarations")
        #chekcs the role declaration policy and adopts the appropriate translation policy
        lines.append(f"    uint NonMember = 0;")
        self.role_to_final_index["NonMember"] = 0
        if self.context.role_declaration_policy == "index":
            i=1
            for role in self.context.dao.roles.values():   
                lines.append(f"    uint {role.role_name} = {i};")
                self.role_to_final_index[role.role_id] = i
                self.context.entity_to_data[role.role_id] = newEntityData(final_id=role.role_id, name=role.role_name, index=i, original_id=role.role_id, entity_type=EntityTypeControllable.ROLE)
                i+=1
            lines.append(f"// committee declarations")
            
            for committee in self.context.dao.committees.values():
                lines.append(f"    uint {committee.committee_description} = {i};")
                self.context.entity_to_data[committee.committee_id] = newEntityData(final_id=committee.committee_id, name=committee.committee_description, index=i, original_id=committee.committee_id, entity_type=EntityTypeControllable.COMMITTEE)
                #new committee permission indices insertion, which is used in the generation of the committee for handling the membership logic.
                self.committee_permission_indices[committee.committee_description] = i
                self.role_to_final_index[committee.committee_id] = i
                i+=1
       
            #in case a topological ordering of node is impossible, the control relations are declared as a nested mapping
            lines.append("    mapping(uint => mapping(uint => bool)) public controlRelations;")
            lines.append("        modifier controlledBy(uint controller_value, uint controlled_value) {")
            lines.append("            require(")
            lines.append(f"              controlRelations[controller_value][controlled_value],")
            lines.append("              \"cannot execute the requested action, due to lack of authorization.\"")
            lines.append("            );")
            lines.append("            _;")
            lines.append("        }")
        
        #in case of topological ordering, the roles are declared based on their topological order
        elif self.context.role_declaration_policy == "topological_ordering":
            G = self.context.dao.dao_control_graph
            try:
                if G.graph_type == GraphType.LIST:
                    
                    print(f"\n The control graph is a list")
                    topological_order = list(nx.topological_sort(G.control_graph))
                    indexes = {}
                    indexes["NonMember"] = 0
                    self.role_to_final_index["NonMember"] = 0
                    x = 1
                    for role in self.context.dao.roles.values():
                        if role.role_name not in topological_order:
                            indexes[role.role_name] = x
                            self.role_to_final_index[role.role_id] = x
                            self.context.entity_to_data[role.role_id] = newEntityData(final_id=role.role_id, name=role.role_name, index=indexes[role.role_id], original_id=role.role_id, entity_type=EntityTypeControllable.ROLE)
                            x+=1
                    for committee in self.context.dao.committees.values():
                        if committee.committee_description not in topological_order:
                            indexes[committee.committee_description] = x
                            self.role_to_final_index[committee.committee_id] = x
                            self.context.entity_to_data[committee.committee_id] = newEntityData(final_id=committee.committee_id, name=committee.committee_description, index=indexes[committee.committee_id], original_id=committee.committee_id, entity_type=EntityTypeControllable.COMMITTEE)
                            x+=1
                    
                    top_indexes = {node: i+x for i, node in enumerate(topological_order)}
                    indexes.update(top_indexes)
                    lines.append(f"// role declarations")
                    for role in self.context.dao.roles.values():
                        lines.append(f"    uint public {role.role_name} = {indexes[role.role_name]};")
                    lines.append(f"// committee declarations")
                    for committee in self.context.dao.committees.values():
                        lines.append(f"    uint public {committee.committee_description} = {indexes[committee.committee_description]};")
                        self.committee_permission_indices[committee.committee_description] = indexes[committee.committee_description]
                       
                    # if self.context.daoOwner == True:
                    #     lines.append(f"    uint public {self.context.dao.dao_name.replace(" ", "_")}Owner = {len(indexes)};")
                else: 
                    print(f"\n The control graph is not a list")
                    self.context.role_declaration_policy = "index"
                    raise ValueError("Topological ordering of roles is only applicable to control graphs with list structure. Switching to index-based role declaration policy for general graph.")
                    
            except Exception as e:
                print(f"An error occurred: {e}")

        lines.append("    mapping(uint => mapping(uint => uint8)) public committeeMemberships;")
        lines.append("    mapping(address => uint) roles;")
        #insert check that these functions are needed
        lines.append("    event RoleRevoked(address indexed from, address member);")
        lines.append("    event RoleAssigned(address indexed member, uint role);")       
        return lines

    def generate_constructor(self) -> list[str]:
        lines:list[str] = []
        committee_list_param = [f"address _{x}" for x in [committee.committee_description for committee in self.context.dao.committees.values()] ]
        committee_address_list = ', '.join(committee_list_param)
        is_last = "" if committee_address_list == [] else ","
        lines.append(f"    constructor( address _owner{is_last} {committee_address_list}) " + "{")
        if self.context.daoOwner == True:
            lines.append(f"        roles[_owner] = {self.context.dao.dao_name.replace(" ", "_")}Owner;")
        lines.append(f"//assign roles to committees")
        lines.extend(f"roles[_{committee.committee_description}] = {committee.committee_description}; \n"  for committee in self.context.dao.committees.values())
        if self.context.role_declaration_policy == "index":
            for edge in self.context.dao.dao_control_graph.control_graph.edges:
                controller = self.context.dao.committees[edge[1]].committee_description if edge[1] in self.context.dao.committees else self.context.dao.roles[edge[1]].role_name
                controlled = self.context.dao.committees[edge[0]].committee_description if edge[0] in self.context.dao.committees else self.context.dao.roles[edge[0]].role_name
                
                lines.append(f"        controlRelations[{controller}][{controlled}] = true;")
                #voting and proposal right assignment
            lines.append("\n//Assigning voting and proposal rights to roles and committees. 1 stands for voting rights, 2 for proposal.")
            for entity,target_committee in self.context.dao.role_and_committee_voting_right_dict.items():
                entity = self.context.dao.committees[entity].committee_description if entity in self.context.dao.committees else self.context.dao.roles[entity].role_name
                target_committee = self.context.dao.committees[target_committee].committee_description
                lines.append(f"        committeeMemberships[{entity}][{target_committee}] = 1;")
            for entity,target_committee in self.context.dao.role_and_committee_proposal_right_dict.items():
                entity = self.context.dao.committees[entity].committee_description if entity in self.context.dao.committees else self.context.dao.roles[entity].role_name
                target_committee = self.context.dao.committees[target_committee].committee_description
                lines.append(f"        committeeMemberships[{entity}][{target_committee}] = 2;")        
        lines.append("    }")          
        return lines

    def generate_functions(self) -> list[str]:    
        lines:list[str] = []
        lines.extend(self.generate_core_dao_functions())
        lines.extend(self.generate_user_defined_functions_V2()) # rifatto per questioni di efficienza
        #generate DAO core functions
        return lines

    def generate_has_role_function(self) -> list[str]:
        lines = []
        lines.append("function hasRole(address _user) external view returns (uint) {")
        lines.append("    return roles[_user];")
        lines.append("}")
        return lines
    
    def generate_can_control_function(self) -> list[str]:
        lines = []
        lines.append("function can_control(address _controller, address _controlled) external view returns (bool) {")
        lines.append("    return controlRelations[roles[_controller]][roles[_controlled]];")
        lines.append("}")
        return lines

    def generate_core_dao_functions(self) -> list[str]:
        lines:list[str] = []
        lines.extend(self.generate_role_revoke_function())
        lines.extend(self.generate_role_assignment_function())
        lines.extend(self.generate_isCommitteeMember_function())
        lines. extend(self.generate_has_role_function())
        lines.extend(self.generate_can_control_function())
        return lines
    
  

    def generate_isCommitteeMember_function(self) -> list[str]:
        lines = []
        lines.append("function isCommitteeMember(address _user, uint _committee) external view returns (uint) {")
        lines.append("    return committeeMemberships[roles[_user]][_committee];")
        lines.append("}")
        return lines

    
    def generate_user_defined_functions_V2(self):
        lines:list[str] = []

        # for each Permission (whose ID is the key of this map), collect all
        # Role and/or Committee (to be precise: their IDs) since those are
        # the only ones invoking that said Permission
        permission_invokers_by_p_ID:dict[str, list[Permission, list[str]]] = {}
        # Generate functions for each permission assigned to ...
        for permissions_holders_collection in [
                self.context.dao.roles.values(),
                self.context.dao.committees.values()
            ]:
            for permissions_holder in permissions_holders_collection: # Role/Committee
                holder_id = permissions_holder.committee_description if type(permissions_holder) == Committee else permissions_holder.role_name # NOTE: dopo il refactoring, questa riga sara' soltanto "permissions_holder.id"
                for permission in permissions_holder.permissions:
                    if permission.voting_right == False and permission.proposal_right == False:
                        if isinstance(permission, Permission):  # Check if permission is an instance of Permission class
                            perm_invokers_data:list[Permission, list[str]] = None
                            p_id = permission.permission_id
                            if p_id in permission_invokers_by_p_ID:
                                perm_invokers_data = permission_invokers_by_p_ID[p_id]
                            else:
                                perm_invokers_data = [permission, []]
                                permission_invokers_by_p_ID[p_id] = perm_invokers_data
                            perm_invokers_data[1].append(holder_id)
                        else: 
                            print(f"\n ERROR: invalid permission type: {type(permission)} for {type(permissions_holder)} with ID {holder_id}")

        for perm_invokers_data in permission_invokers_by_p_ID.values():
            
            permission = perm_invokers_data[0]
            invokers_id = perm_invokers_data[1]
            lines.extend(self.generate_function(permission, invokers_id))
        for permission in self.context.dao.permissions.values():
            if permission.voting_right == False and permission.proposal_right == False:
                if permission.permission_id not in permission_invokers_by_p_ID:
                    lines.extend(self.generate_function(permission))
        
        return lines
    
        
    def generate_role_revoke_function(self) -> list[str]:
        lines:list[str] = []
        if self.context.role_declaration_policy == "topological_ordering":
            lines.append("function revokeRole(address member) public {" )
            lines.append('        require(roles[msg.sender] > roles[member], "cannot revoke superior roles");')
        elif self.context.role_declaration_policy == "index":
            lines.append("function revokeRole(address member) public controlledBy(roles[msg.sender], roles[member]) {")
            lines.append("    require(member != address(0),\" invalid member address \");" )
            lines.append("    uint current_role_id = roles[member];")
            lines.append("    //Ensure the member has an assigned role (not already a NonMember)")
            lines.append("    require(current_role_id != NonMember, \"Role must be assigned to revoke\");")
            lines.append("    // Revoke the role")
        lines.append("    roles[member] = NonMember;")
        lines.append("    emit RoleRevoked(msg.sender, member); ")
        lines.append("    }")
        return lines
    
    
    # TODO: Implement the remaining core dao functions
    def generate_role_assignment_function(self) -> list[str]:
        # TODO: do the "topological_ordering" role declaration policy let ALL roles and committees
        # to be a valid policy to perform an assignment of a role (it is intended: "after considering
        # the roles's hierarchy") ?
        role_ids = []
        for role in self.context.dao.roles.values():
            role_ids.append(role.role_name)
        for committee in self.context.dao.committees.values():
            role_ids.append(committee.committee_description)

        lines:list[str] = []
        if self.context.role_declaration_policy == "topological_ordering":
            lines.append("    function assignRole(address member, uint new_role_id) public controlledBy(roles[msg.sender], new_role_id) {")
            lines.append("    require(member != address(0),\" invalid member address \");" )
            lines.append("        require(roles[msg.sender] > role, \"cannot assign superior roles\");")
            message = "role doesn't exist, or it is the non-member role" 
            if self.context.daoOwner == True:
                message = "role doesn't exist, it is the non-member role or the Owner role"
            lines.append(self.generate_access_control(role_ids, message))

        elif self.context.role_declaration_policy == "index":
            lines.append("function assignRole(address member, uint new_role_id) public controlledBy(roles[msg.sender], new_role_id) {")
            lines.append("    require(member != address(0),\" invalid member address \");" )
            lines.append("    uint current_role_id = roles[member];")
            lines.append("    // Ensure the member is either a NonMember or the caller controls the current role")
            lines.append("    require(")
            lines.append("       current_role_id == NonMember || controlRelations[roles[msg.sender]][current_role_id],")
            lines.append("       \"Cannot assign role: caller lacks control over the member's current role\"")
            lines.append("      );")
            lines.append("    // Assign the new role")
            lines.append("    roles[member] = new_role_id;")
            lines.append("    emit RoleAssigned(member, new_role_id);")
        lines.append("}")
        return lines
   

    def generate_function(self, permission: Permission, role_ids:list[str] = None) -> list[str]:
        # Check the roles that have the permission and stores them in a list
        if role_ids is None and permission.voting_right == False and permission.proposal_right == False:
            role_ids = self.check_permissions(permission)
        lines:list[str] = []
        allowed_action = permission.allowed_action.replace("/", "_").replace(" ", "_").replace("\\", "")
        lines.append(f"    function {allowed_action}() public" + "{")
        if role_ids is not None:
            lines.append(self.generate_access_control(role_ids))
        lines.append(f"// TODO: define the behavior of the function")
        lines.append("    }")
        return lines
    

    def generate_access_control(self, role_ids, require_message = "Only authorized roles can execute this function.") -> str:
        req_parts:list[str] = [
            "        require(",
            " || ".join(
                f"roles[msg.sender] == {role_id}"
                    for role_id in role_ids
                ),
            f' , \"{require_message}\");'
        ]
        final_req_parts = "".join(req_parts) if len(role_ids) > 0 else "        // No roles are authorized to execute this function."
        return final_req_parts


    def check_permissions(self, permission: Permission) -> list[str]:
        # Check the roles and committees that have the permission and stores them in a list
        role_ids:list[str] = []
        for role in self.context.dao.roles.values():
            for perm in role.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(role.role_name)
        for committee in self.context.dao.committees.values():
            for perm in committee.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(committee.committee_description)
        return role_ids

    def generate_closure(self):
        return "}"
