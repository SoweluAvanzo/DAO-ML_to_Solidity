

import networkx as nx
from DAOclasses import DAO, Committee, GraphType, Permission
from translator import TranslatedSmartContract, Translator, CommitteeTranslator, TranslationContext

#class BaseTranslator:
    #TODO
    

class SimpleSolidityTranslator(Translator):
    def __init__(self, dao: DAO, role_declaration_policy = "index", solidity_version= "^0.8.0", daoOwner = True):
        self.context = TranslationContext(dao, role_declaration_policy, solidity_version, daoOwner)
        self.committee_permission_indices:dict[str, int]= {}
        self.context.role_declaration_policy = "index" if self.context.dao.dao_control_graph.graph_type != GraphType.LIST else "topological_ordering"

    def translateDao(self) -> TranslatedSmartContract:
        lines:list[str] = []

        DAO_mission_statement_comment = f"// @title {self.context.dao.dao_id} has the following mission: {self.context.dao.mission_statement}"
        lines.extend(self.generate_smart_contract_header(DAO_mission_statement_comment))

        lines.extend(self.generate_contract_declaration(self.context.dao.dao_id))
        lines.extend(self.generate_roles())
        #lines.extend(self.generate_roles_V2())
        
        lines.extend(self.generate_constructor())
        lines.extend(self.generate_functions())
        lines.append(self.generate_closure())

        name = self.context.dao.dao_id
        return TranslatedSmartContract(lines, name)


    def translate(self) -> list[TranslatedSmartContract]:
        all_smart_contracts: list[TranslatedSmartContract] = []
        all_smart_contracts.append(self.translateDao())
        # at first, translate all Committees
        ct = CommitteeTranslator(self.context)
        for c in self.context.dao.committees.values():
            translated_committee = ct.translateCommittee(c, voting_permission_index=self.committee_permission_indices[c.committee_id], proposal_permission_index=self.committee_permission_indices[c.committee_id], optimized=False) 
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
        return TranslatedSmartContract(lines, "IPermissionManager", folder="interfaces")


    def generate_smart_contract_header(self, title_comment = "") -> list[str]:
        lines:list[str] = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version};")
        lines.append(f"import \"./interfaces/IPermissionManager.sol\";")
        lines.append(title_comment)
        return lines
        
    def generate_contract_declaration(self, contract_name) -> list[str]:
        return [f"contract {contract_name} is IPermissionManager " + "{"]


    # def generate_roles_indexes(self, role_declaration_policy, dao: DAO)-> list[list[str, int]]: # NOTE: rigatta solo per poter isolare questa generazione E riciclarla all'interno del BaseTranslator
    #     names_and_indexes:list[list[str, int]] = [
    #         ["NonMember", 0]
    #     ]
        
    #     if role_declaration_policy == "index":
    #         i=1
    #         names_and_indexes.append(["// role declarations", -1]) # NOTE: a negative value indicates a comment, so that line must be append as-is
    #         for role in dao.roles.values():
    #             print(f"\ngeneerating the code for role: {role.role_id}")
    #             names_and_indexes.append([role.role_id, i])
    #             i+=1
    #         names_and_indexes.append(["// committee declarations", -1]) # NOTE: a negative value indicates a comment, so that line must be append as-is
    #         for committtee in dao.committees.values():
    #             names_and_indexes.append([committtee.committee_id, i])
    #             #new committee permission indices insertion, which is used in the generation of the committee for handling the membership logic.
    #             self.committee_permission_indices[committtee.committee_id] = i
    #             print(f"\n committee assigned permission index: {i} for committee: {committtee.committee_id}")
    #             i+=1
    #         if self.context.daoOwner == True:
    #             names_and_indexes.append(["// owner role", -1])
    #             names_and_indexes.append(["OwnerRole", i])
        
    #     #in case of topological ordering, the roles are declared based on their topological order
    #     elif role_declaration_policy == "topological_ordering":
    #         G = dao.dao_control_graph
    #         try:
    #             if G.graph_type == GraphType.LIST:
    #                 G = G.control_graph
    #                 print(f"\n The control graph is a list")
    #                 topological_order = list(nx.topological_sort(G))
    #                 indexes = {node: i+1 for i, node in enumerate(topological_order)}
    #                 names_and_indexes.append(["// role declarations", -1]) # NOTE: a negative value indicates a comment, so that line must be append as-is
    #                 for role in dao.roles.values():
    #                     names_and_indexes.append([role.role_id, indexes[role.role_id]])
    #                 names_and_indexes.append(["// committee declarations", -1]) # NOTE: a negative value indicates a comment, so that line must be append as-is
    #                 for committee in dao.committees.values():
    #                     names_and_indexes.append([committee.committee_id, indexes[committee.committee_id]])
    #                     #new committee permission indices insertion
    #                     self.committee_permission_indices[committee.committee_id] = indexes[committee.committee_id]
    #                 if self.context.daoOwner == True:
    #                     names_and_indexes.append(["// admin role", -1])
    #                     names_and_indexes.append(["AdminRole", len(topological_order)+1])
    #             else: 
    #                 print(f"\n The control graph is not a list")
    #                 raise ValueError("Topological ordering of roles is only applicable to control graphs with list structure. Switching to index-based role declaration policy for general graph.")      
    #         except Exception as e:
    #             print(f"\n The control graph is not a list")
    #             print(f"An error occurred: {e}")
    #             print(f"Switching to index-based role declaration policy for general graph.")
    #             #self.translate()
    #     return names_and_indexes

    # def generate_roles_V2(self) -> list[str]: # NOTE: rigatta solo per poter isolare questa generazione E riciclarla all'interno del BaseTranslator
    #     lines:list[str] = []
    #     lines.append("    address public creator;")
    #     lines.append("    string public name;")
    #     roles_indexes = self.generate_roles_indexes(self.context.role_declaration_policy, self.context.dao)
    #     for r_i in roles_indexes:
    #         role_name_or_comment = r_i[0]
    #         index = r_i[1]
    #         if index >= 0:
    #             lines.append(f"    uint {role_name_or_comment} = {index};")
    #         else: # it's a comment
    #             lines.append(role_name_or_comment)
    #     lines.append("    // Mapping of roles to the set of roles they can control")
    #     lines.append("    mapping(uint256 => mapping(uint256 => bool)) public canControl;")
    #     #insert check that these functions are needed
    #     lines.append("    event RoleRevoked(address indexed from, address member);")
    #     lines.append("    event UserRoleAssigned(address indexed member, uint role);")
    #     lines.append("    // Modifier to check if the caller has the permission to execute the function")
    #     lines.append("        modifier onlyController(address controller_address, address controlled_address) {")
    #     lines.append("            require(")
    #     lines.append("                canControl[roles[controller_address]][roles[controlled_address]],")
    #     lines.append("                \"cannot execute the requested action, due to lack of authorization.\"")
    #     lines.append("            );")
    #     lines.append("            _;")
    #     lines.append("        }")
    #     lines.append("    mapping(address => uint) roles;")
    #     return lines

    def generate_roles(self) -> list[str]:
        lines:list[str] = []
        lines.append("    address public creator;")
        lines.append("    string public name;")
        lines.append(f"// role declarations")
        #lines.append(f"    uint OwnerRole = 0;")
        #chekcs the role declaration policy and adopts the appropriate translation policy
        lines.append(f"    uint NonMember = 0;")
        if self.context.role_declaration_policy == "index":
            i=1
            for role in self.context.dao.roles.values():
                print(f"\ngeneerating the code for role: {role.role_id}")
                lines.append(f"    uint {role.role_id} = {i};")
                i+=1
            lines.append(f"// committee declarations")
            
            for committtee in self.context.dao.committees.values():
                lines.append(f"    uint {committtee.committee_id} = {i};")
                #new committee permission indices insertion, which is used in the generation of the committee for handling the membership logic.
                self.committee_permission_indices[committtee.committee_id] = i
                print(f"\n committee assigned permission index: {i} for committee: {committtee.committee_id}")
                i+=1
            # if self.context.daoOwner == True:
            #         lines.append(f"    uint public {self.context.dao.dao_id}Owner = {i};")
            #in case a topological ordering of node is impossible, the control relations are declared as a nested mapping
            lines.append("    // Mapping of roles to the set of roles they can control")
            lines.append("    mapping(uint => mapping(uint => bool)) public canControl;")
            lines.append("    // Modifier to check if the caller has the permission to execute the function")
            lines.append("        modifier onlyController(address controller_address, address controlled_address) {")
            lines.append("            require(")
            lines.append("                canControl[roles[controller_address]][roles[controlled_address]],")
            lines.append("                \"cannot execute the requested action, due to lack of authorization.\"")
            lines.append("            );")
            lines.append("            _;")
            lines.append("        }")
        
        #in case of topological ordering, the roles are declared based on their topological order
        elif self.context.role_declaration_policy == "topological_ordering":
            G = self.context.dao.dao_control_graph
            try:
                print(f"G.control_graph type is {G.graph_type}")
                if G.graph_type == GraphType.LIST:
                    
                    print(f"\n The control graph is a list")
                    topological_order = list(nx.topological_sort(G.control_graph))
                    print(f"\n The topological order is {topological_order}")
                    print(f"\nits enumerate is {enumerate(topological_order)}")
                    indexes = {}
                    indexes["NonMember"] = 0
                    x = 1
                    for role in self.context.dao.roles.values():
                        if role.role_id not in topological_order:
                            indexes[role.role_id] = x
                            print(f"\n role: {role.role_id} is not in the graph, so it is assigned the index {x}")
                            x+=1
                    for committee in self.context.dao.committees.values():
                        if committee.committee_id not in topological_order:
                            indexes[committee.committee_id] = x
                            x+=1
                            print(f"\n committee: {committee.committee_id} is not in the graph, so it is assigned the index {x}")
                    
                    top_indexes = {node: i+x for i, node in enumerate(topological_order)}
                    indexes.update(top_indexes)
                    print(f"\n The indexes are {indexes}")
                    lines.append(f"// role declarations")
                    for role in self.context.dao.roles.values():
                        lines.append(f"    uint public {role.role_id} = {indexes[role.role_id]};")
                        print(f"\n role assigned permission index: {role.role_id} for role: {role.role_id}")
                    lines.append(f"// committee declarations")
                    for committee in self.context.dao.committees.values():
                        lines.append(f"    uint public {committee.committee_id} = {indexes[committee.committee_id]};")
                        self.committee_permission_indices[committee.committee_id] = indexes[committee.committee_id]
                        print(f"\n committee assigned permission index: {committee.committee_id} for committee: {committee.committee_id}")
                    # if self.context.daoOwner == True:
                    #     lines.append(f"    uint public {self.context.dao.dao_id}Owner = {len(indexes)};")
                else: 
                    print(f"\n The control graph is not a list")
                    self.context.role_declaration_policy = "index"
                    raise ValueError("Topological ordering of roles is only applicable to control graphs with list structure. Switching to index-based role declaration policy for general graph.")
                    
            except Exception as e:
                print(f"\n The control graph is {G.control_graph}, it has the following structure: {G.control_graph.nodes}, edges: {G.control_graph.edges}")
                print(f"An error occurred: {e}")
                print(f"Switching to index-based role declaration policy for general graph.")
                #self.translate()

        lines.append("    mapping(uint => mapping(uint => uint8)) public committeeMemberships;")
        lines.append("    mapping(address => uint) roles;")
        #insert check that these functions are needed
        lines.append("    event RoleRevoked(address indexed from, address member);")
        lines.append("    event UserRoleAssigned(address indexed member, uint role);")       
        return lines

    def generate_constructor(self) -> list[str]:
        lines:list[str] = []
        committee_list_param = [f"address _{x}" for x in [committee.committee_id for committee in self.context.dao.committees.values()] ]
        committee_address_list = ', '.join(committee_list_param)
        lines.append(f"    constructor(string memory _name, address _owner, {committee_address_list}) " + "{")
        lines.append("        name = _name;")
        if self.context.daoOwner == True:
            lines.append(f"        roles[_owner] = {self.context.dao.dao_id}Owner;")
        lines.append(f"//assign roles to committees")
        lines.extend(f"roles[_{committee.committee_id}] = {committee.committee_id}; \n"  for committee in self.context.dao.committees.values())
        if self.context.role_declaration_policy == "index":
            for edge in self.context.dao.dao_control_graph.control_graph.edges:
                lines.append(f"        canControl[{edge[1]}][{edge[0]}] = true;")
                #voting and proposal right assignment
            lines.append("\n//Assigning voting and proposal rights to roles and committees. 1 stands for voting rights, 2 for proposal.")
            for entity,target_committee in self.context.dao.role_and_committee_voting_right_dict.items():
                lines.append(f"        committeeMemberships[{entity}][{target_committee}] = 1;")
            for entity,target_committee in self.context.dao.role_and_committee_proposal_right_dict.items():
                lines.append(f"        committeeMemberships[{entity}][{target_committee}] = 2;")        
        lines.append("    }")

          
        return lines

    def generate_functions(self) -> list[str]:
    
        lines:list[str] = []
        lines.extend(self.generate_core_dao_functions())
        #lines.extend(self.generate_user_defined_functions())
        lines.extend(self.generate_user_defined_functions_V2()) # rifatto per questioni di efficienza
        #generate DAO core functions
        return lines


    def generate_core_dao_functions(self) -> list[str]:
        lines:list[str] = []
        lines.extend(self.generate_role_revoke_function())
        lines.extend(self.generate_role_assignment_function())
        lines.extend(self.generate_isCommitteeMember_function())
        return lines
    
    # def generate_membership_assignment_function(self) -> list[str]:
    #     lines:list[str] = []
    #     lines.append("function assignMembership(address _user, uint _committee, uint _membership) public onlyController(msg.sender, _user) {")
    #     lines.append("    require(_membership == 1 || _membership == 2, \"Invalid membership type\");")
    #     lines.append("    committeeMemberships[roles[_user]][_committee] = uint8(_membership);")
    #     lines.append("}")
    #     return lines

    def generate_isCommitteeMember_function(self) -> list[str]:
        lines = []
        lines.append("function isCommitteeMember(address _user, uint _committee) external view returns (uint) {")
        lines.append("    return committeeMemberships[roles[_user]][_committee];")
        lines.append("}")
        return lines
    # def generate_user_defined_functions(self):
    #     lines:list[str] = []
    #     # Generate functions for each permission assigned to roles
    #     for role in self.context.dao.roles.values():
    #         for permission in role.permissions:
    #             if isinstance(permission, Permission):  # Check if permission is an instance of Permission class
    #                 lines.extend(self.generate_function(permission))
    #     # Generate functions for each permission assigned to committees
    #     for committee in self.context.dao.committees.values():
    #         for permission in committee.permissions:
    #             if isinstance(permission, Permission):  # Check if permission is an instance of Permission class
    #                 lines.extend(self.generate_function(permission))
    #             else: 
    #                 print(f"\n permission type: {type(permission)}")
    #     return lines
    
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
                holder_id = permissions_holder.committee_id if type(permissions_holder) == Committee else permissions_holder.role_id # NOTE: dopo il refactoring, questa riga sara' soltanto "permissions_holder.id"
                print(f"collecting permissions for {type(permissions_holder)} with ID {holder_id}")
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
                            print(f"\n invalid permission type: {type(permission)} for {type(permissions_holder)} with ID {holder_id}")

        for perm_invokers_data in permission_invokers_by_p_ID.values():
            permission = perm_invokers_data[0]
            invokers_id = perm_invokers_data[1]
            print(f"permission with ID: << {permission.permission_id} >> has this invokers: [ { ', '.join(invokers_id) } ]\n")
            lines.extend(self.generate_function(permission, invokers_id))
        
        return lines
    
        
    def generate_role_revoke_function(self) -> list[str]:
        lines:list[str] = []
        if self.context.role_declaration_policy == "topological_ordering":
            lines.append("    function revokeRole(address member) public {" )
            lines.append('        require(roles[msg.sender] > roles[member], "cannot revoke superior roles");')
        elif self.context.role_declaration_policy == "index":
            lines.append("    function revokeRole(address member) public onlyController(msg.sender, member) {")
            lines.append("        // Revoke the role")
        lines.append("        roles[member] = NonMember;")
        lines.append("        emit RoleRevoked(msg.sender, member); ")
        lines.append("    }")
        return lines
    
    # TODO: Implement the remaining core dao functions
    def generate_role_assignment_function(self) -> list[str]:
        # TODO: do the "topological_ordering" role declaration policy let ALL roles and committees
        # to be a valid policy to perform an assignment of a role (it is intended: "after considering
        # the roles's hierarchy") ?
        role_ids = []
        for role in self.context.dao.roles.values():
            role_ids.append(role.role_id)
        for committee in self.context.dao.committees.values():
            role_ids.append(committee.committee_id)

        lines:list[str] = []
        if self.context.role_declaration_policy == "topological_ordering":
            lines.append("    function assignRole(address member, uint role) public {")
            lines.append("        require(roles[msg.sender] > role, \"cannot assign superior roles\");")
            message = "role doesn't exist, or it is the non-member role" 
            if self.context.daoOwner == True:
                message = "role doesn't exist, it is the non-member role or the Owner role"
            lines.append(self.generate_access_control(role_ids, message))

        elif self.context.role_declaration_policy == "index":
            lines.append("function assignRole(address member, uint role) public onlyController(msg.sender, member) {")
            lines.append("require(canControl[roles[msg.sender]][role]== true, \"cannot assign superior roles\");")
        lines.append("    roles[member] = role;")
        lines.append("emit UserRoleAssigned(member, role);" )
        lines.append("}")
        return lines
   
    #TODO generate_permission_delegation_function():

    def generate_function(self, permission: Permission, role_ids:list[str] = None) -> list[str]:
        # Check the roles that have the permission and stores them in a list
        if role_ids is None and permission.voting_right == False and permission.proposal_right == False:
            role_ids = self.check_permissions(permission)
        lines:list[str] = []
        allowed_action = permission.allowed_action.replace("/", "_").replace(" ", "_").replace("\\", "")
        lines.append(f"    function {allowed_action}() public" + "{")
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
        return "".join(req_parts)

    def check_permissions(self, permission: Permission) -> list[str]:
        # Check the roles and committees that have the permission and stores them in a list
        role_ids:list[str] = []
        for role in self.context.dao.roles.values():
            for perm in role.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(role.role_id)
                    print(f"FOR FUNCTION {permission.permission_id}, ROLE {role.role_id} is REQUIRED")
        for committee in self.context.dao.committees.values():
            for perm in committee.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(committee.committee_id)
                    print(f"FOR FUNCTION {permission.permission_id}, COMMITTEE {committee.committee_id} is REQUIRED")
        return role_ids

    def generate_closure(self):
        return "}"

