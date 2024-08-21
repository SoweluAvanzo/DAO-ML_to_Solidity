'''

This module contains the SolidityTranslator class which is responsible for translating the logical representation of a DAO into Solidity code.

The SolidityTranslator class has the following methods:
- translate(): Translates the DAO object into Solidity code.
- generate_header(): Generates the header of the Solidity code.
- generate_contract_declaration(): Generates the contract declaration of the Solidity code.
- generate_body(): Generates the body of the Solidity code.
- generate_constructor(): Generates the constructor of the Solidity code.
- generate_functions(): Generates the functions of the Solidity code.
- generate_access_control(role_ids): Generates the access control code for the given role IDs.
- check_permissions(permission): Checks the permissions required for a given permission object.
- generate_function(permission): Generates the code for a function based on the given permission object.
- generate_closure(): Generates the closure of the Solidity code.
- save_to_file(): Saves the translated Solidity smart contract code to a .sol file.
Note: This module requires the DAOclasses module.
'''
import os
from DAOclasses import*


class SimpleSolidityTranslator:
    def __init__(self, dao, role_declaration_policy = "index", solidity_version= "^0.8.0", daoOwner = True):
        self.dao = dao
        self.role_declaration_policy = role_declaration_policy
        self.solidity_version = solidity_version
        self.control_transitivity = self.dao.hierarchical_inheritance == 1
        self.daoOwner = daoOwner

    def translate(self):
        lines = []
        lines.append(self.generate_dao_header())
        lines.append(self.generate_contract_declaration())
        lines.append(self.generate_roles())
        lines.append(self.generate_constructor())
        lines.append(self.generate_functions())
        lines.append(self.generate_closure())
        return "\n".join(lines)

    def generate_dao_header(self):
        return f"pragma solidity {self.solidity_version}; \n /**\n * @title {self.dao.dao_id} has the following mission: {self.dao.mission_statement} \n */"

    def generate_contract_declaration(self):
        return f"contract {self.dao.dao_id} {{"

    def generate_roles(self):
        lines = []
        lines.append("    address public creator;")
        lines.append("    string public name;")
        lines.append(f"// role declarations")
        #lines.append(f"    uint constant OwnerRole = 0;")
        #chekcs the role declaration policy and adopts the appropriate translation policy
        lines.append(f"    uint constant NonMember = 0;")
        if self.role_declaration_policy == "index":
            i=1
            for role in self.dao.roles.values():
                print(f"\ngeneerating the code for role: {role.role_id}")
                lines.append(f"    uint constant {role.role_id} = {i};")
                i+=1
            lines.append(f"// committee declarations")
            
            for committtee in self.dao.committees.values():
                lines.append(f"    uint constant {committtee.committee_id} = {i};")
                i+=1
            if self.daoOwner == True:
                    lines.append(f"    uint constant OwnerRole = {i};")
            #in case a topological ordering of node is impossible, the control relations are declared as a nested mapping
            lines.append("// Mapping of roles to the set of roles they can control")
            lines.append("mapping(uint256 => mapping(uint256 => bool)) public canControl;")
            #insert check that these functions are needed
            lines.append("event RoleRevoked(address indexed from, address member);")
            lines.append("event UserRoleAssigned(address indexed member, uint role);")
            lines.append("// Modifier to check if the caller has the permission to execute the function")
            lines.append("   modifier onlyController(address controller_address, address controlled_address) {")
            lines.append("    require(")
            lines.append("        canControl[roles[controller_address]][roles[controlled_address]],")
            lines.append("        \"cannot execute the requested action, due to lack of authorization.\"")
            lines.append("    );")
            lines.append("    _;")
            lines.append("}")
        
        #in case of topological ordering, the roles are declared based on their topological order
        elif self.role_declaration_policy == "topological_ordering":
            G = self.dao.dao_control_graph
            try:
                if G.graph_type == GraphType.LIST:
                    G = G.control_graph
                    print(f"\n The control graph is a list")
                    topological_order = list(nx.topological_sort(G))
                    index = {node: i for i, node in enumerate(topological_order)}
                    lines.append(f"// role declarations")
                    for role in self.dao.roles.values():
                        lines.append(f"    uint constant {role.role_id} = {index[role.role_id]};")
                    lines.append(f"// committee declarations")
                    for committee in self.dao.committees.values():
                        lines.append(f"    uint constant {committee.committee_id} = {index[committee.committee_id]};")
                    if self.daoOwner == True:
                        lines.append(f"    uint constant AdminRole = {len(topological_order)+1};")
                else: 
                    print(f"\n The control graph is not a list")
                    #self.role_declaration_policy = "index"
                    raise ValueError("Topological ordering of roles is only applicable to control graphs with list structure. Switching to index-based role declaration policy for general graph.")
                    
            except Exception as e:
                print(f"\n The control graph is not a list")
                print(f"An error occurred: {e}")
                print(f"Switching to index-based role declaration policy for general graph.")
                self.translate()

                
        lines.append("    mapping(address => uint) roles;")
        return "\n".join(lines)

    def generate_constructor(self):
        lines = []
        lines.append("    constructor(string memory _name, address _creator) {")
        lines.append("        name = _name;")
        lines.append("        creator = _creator;")
        lines.append(f"        roles[creator] = OwnerRole;")  
        if self.role_declaration_policy == "index":
            for edge in self.dao.dao_control_graph.control_graph.edges:
                lines.append(f"        canControl[{edge[0]}][{edge[1]}] = true;")          
        lines.append("    }")
          
        return "\n".join(lines)

    def generate_functions(self):
    
        lines = []
        lines.append(self.generate_core_dao_functions())
        lines.append(self.generate_user_defined_functions())
        #generate DAO core functions
        return "\n".join(lines)


    def generate_core_dao_functions(self):
        lines = []
        lines.append(self.generate_role_revoke_function())
        return "\n".join(lines)
    
    def generate_user_defined_functions(self):
        lines = []
        # Generate functions for each permission assigned to roles
        for role in self.dao.roles.values():
            for permission in role.permissions:
                if isinstance(permission, Permission):  # Check if permission is an instance of Permission class
                    lines.append(self.generate_function(permission))
        # Generate functions for each permission assigned to committees
        for committee in self.dao.committees.values():
            for permission in committee.permissions:
                if isinstance(permission, Permission):  # Check if permission is an instance of Permission class
                    lines.append(self.generate_function(permission))
                else: 
                    print(f"\n permission type: {type(permission)}")
        return "\n".join(lines)
    
        
    def generate_role_revoke_function(self):
        lines = []
        if self.role_declaration_policy == "topological_ordering":
            lines.append("function revokeRole(address member) public {" )
            lines.append('require(roles[msg.sender] > roles[member], "cannot revoke superior roles");')
        elif self.role_declaration_policy == "index":
            lines.append("function revokeRole(address member) public onlyController(msg.sender, member) {")
            lines.append("    // Revoke the role")
        lines.append(" roles[member] = NonMember;")
        lines.append("emit RoleRevoked(msg.sender, member); ")
        lines.append("}")
        return "\n".join(lines)
    
    # TODO: Implement the remaining core dao functions
    def generate_role_assignment_function(self):
        role_ids = []
        for role in self.dao.roles.values():
            role_ids.append(role.role_id)
        for committee in self.dao.committees.values():
            role_ids.append(committee.committee_id)

        lines = []
        if self.role_declaration_policy == "topological_ordering":
            lines.append("function assignRole(address member, uint role) public {")
            lines.append("    require(roles[msg.sender] > role, \"cannot assign superior roles\");")
            message = "role doesn't exist, or it is the non-member role" 
            if self.daoOwner == True:
                message = "role doesn't exist, it is the non-member role or the Owner role"
            lines.append(self.generate_access_control(role_ids, message))

        elif self.role_declaration_policy == "index":
            lines.append("function assignRole(address member, uint role) public onlyController(msg.sender, member) {")
            lines.append("require(canControl[roles[msg.sender]][role]== True, \"cannot assign superior roles\");")
        lines.append("    roles[member] = role;")
        lines.append("emit UserRoleAssigned(member, role);" )
        lines.append("}")
        return "\n".join(lines)
    #TODO: SONO ARRIVATO QUI
    #def generate_permission_delegation_function():

    def generate_function(self, permission):
        # Check the roles that have the permission and stores them in a list
        role_ids = self.check_permissions(permission)
        lines = []
        allowed_action = permission.allowed_action.replace("/", "_").replace(" ", "_").replace("\\", "")
        lines.append(f"    function {allowed_action}() public {{")
        lines.append(self.generate_access_control(role_ids))
        lines.append(f"// TODO: define the behavior of the function")
        lines.append("    }")
        return "\n".join(lines)
    
    def generate_access_control(self, role_ids, require_message = "Only authorized roles can execute this function."):
        require = "        require(" 
        for i, role_id in enumerate(role_ids):
            require +=f"roles[msg.sender] == {role_id}"
            if i < len(role_ids) - 1:
                require +=" ||"

        require +=f" , "
        require +=f'\"{require_message}\");'
        return require

    def check_permissions(self, permission):
        # Check the roles and committees that have the permission and stores them in a list
        role_ids = []
        for role in self.dao.roles.values():
            for perm in role.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(role.role_id)
                    print(f"FOR FUNCTION {permission.permission_id}, ROLE {role.role_id} is REQUIRED")
        for committee in self.dao.committees.values():
            for perm in committee.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(committee.committee_id)
                    print(f"FOR FUNCTION {permission.permission_id}, COMMITTEE {committee.committee_id} is REQUIRED")
        return role_ids

    def generate_closure(self):
        return "}"

