'''
def preprocess_function_name():

def translate_contract():


def DAOContract(self):
    def __init__(self):
        self.dao_contract = ""
        self.
        self.roles_int = ""
        self.committee = ""
        self.permission = ""

'''
import os
from DAOclasses import*
class SolidityTranslator:
    def __init__(self, dao):
        self.dao = dao

    def translate(self):
        lines = []
        lines.append(self.generate_header())
        lines.append(self.generate_contract_declaration())
        lines.append(self.generate_body())
        lines.append(self.generate_constructor())
        lines.append(self.generate_functions())
        lines.append(self.generate_closure())
        return "\n".join(lines)

    def generate_header(self):
        return f"pragma solidity ^0.8.0; \n /**\n * @title {self.dao.dao_id} has the following mission: {self.dao.mission_statement} \n */"

    def generate_contract_declaration(self):
        return f"contract {self.dao.dao_id} {{"

    def generate_body(self):
        lines = []
        lines.append("    address public creator;")
        lines.append("    string public name;")
        lines.append(f"// role declarations")
        lines.append(f"    uint constant OwnerRole = 0;")
        i=1
        for role in self.dao.roles:
            print(f"\ngeneerating the code for role: {role.role_id}")
            lines.append(f"    uint constant {role.role_id}Role = {i};")
            i+=1
        lines.append(f"// committee declarations")
        j=i
        for committtee in self.dao.committees:
            lines.append(f"    uint constant {committtee.committee_id}Role = {j};")
            j+=1
        lines.append("    mapping(address => uint) roles;")
        
        return "\n".join(lines)

    def generate_constructor(self):
        lines = []
        lines.append("    constructor(string memory _name, address _creator) public {")
        lines.append("        name = _name;")
        lines.append("        creator = _creator;")
        lines.append(f"        roles[creator] = OwnerRole;")  
        lines.append("    }")
        return "\n".join(lines)

    def generate_functions(self):
        lines = []
        for role in self.dao.roles:
            for permission in role.permissions:
                if isinstance(permission, Permission):  # Check if permission is an instance of Permission class
                    lines.append(self.generate_function(permission))
        for committee in self.dao.committees:
            for permission in committee.permissions:
                if isinstance(permission, Permission):  # Check if permission is an instance of Permission class
                    lines.append(self.generate_function(permission))
                else: 
                    print(f"\n permission type: {type(permission)}")
        return "\n".join(lines)
    
    def generate_access_control(self, role_ids):
        require = "        require(" 
        for i, role_id in enumerate(role_ids):
            require +=f"roles[msg.sender] == {role_id}Role"
            if i < len(role_ids) - 1:
                require +=" ||"

        require +=f" , \"Only authorized roles can execute this function.\");"
        return require

    def check_permissions(self, permission):
        role_ids = []
        for role in self.dao.roles:
            for perm in role.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(role.role_id)
                    print(f"FOR FUNCTION {permission.permission_id}, ROLE {role.role_id} is REQUIRED")
        for committee in self.dao.committees:
            for perm in committee.permissions:
                if perm.allowed_action == permission.allowed_action:
                    role_ids.append(committee.committee_id)
                    print(f"FOR FUNCTION {permission.permission_id}, COMMITTEE {committee.committee_id} is REQUIRED")
        return role_ids

    def generate_function(self, permission):
        role_ids = self.check_permissions(permission)
        lines = []
        allowed_action = permission.allowed_action.replace("/", "_").replace(" ", "_").replace("\\", "")
        lines.append(f"    function {allowed_action}() public {{")
        lines.append(self.generate_access_control(role_ids))
        lines.append(f"//TODO: define the behavior of the function")
        lines.append("    }")
        return "\n".join(lines)


    def generate_closure(self):
        return "}"

    def save_to_file(self):
        contract_code = self.translate()
        with open(f"{self.dao.dao_id}.sol", "w") as file:
            file.write(contract_code)
        print(f"Contract {self.dao.dao_id}.sol has been created.")

