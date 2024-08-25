import os
from DAOclasses import*

class OptimizedSolidityTranslator:
    def __init__(self, dao):
        self.dao = dao

    def translate(self):
        lines = []
        lines.append(self.generate_header())
        lines.append(self.generate_contract_declaration())
        lines.append(self.generate_state_variables())
        lines.append(self.generate_constructor())
        lines.append(self.generate_modifiers())
        lines.append(self.generate_functions())
        lines.append(self.generate_permission_functions())  
        lines.append(self.generate_closure())
        return "\n".join(lines)

    def generate_header(self):
        return f"pragma solidity ^0.8.0;\n/**\n * @title {self.dao.dao_id}\n * @notice {self.dao.mission_statement}\n */"

    def generate_contract_declaration(self):
        return f"contract {self.dao.dao_id} {{"

    def generate_state_variables(self):
        lines = []
        lines.append("    mapping(bytes32 => uint256) private roles;")
        lines.append("    mapping(address => bytes32) private userRoles;")
        lines.append("    mapping(bytes32 => uint256) private controlRelations;")
        lines.append("    address public creator;")
        # Declare role and committee identifiers as bytes32 constants
        for role in self.dao.roles.values():
            lines.append(f"    bytes32 public constant {role.role_id} = keccak256(\"{role.role_id}\");")
        for committee in self.dao.committees.values():
            lines.append(f"    bytes32 public constant {committee.committee_id} = keccak256(\"{committee.committee_id}\");")
        return "\n".join(lines)


    def generate_constructor(self):
        lines = []
        lines.append("    constructor() {")
        lines.append("        creator = msg.sender;")
        for role in self.dao.roles.values():
            control_mask = self.get_control_mask(role)
            lines.append(f"        controlRelations[{role.role_id}] = {control_mask};")
        for committee in self.dao.committees.values():
            control_mask = self.get_control_mask(committee)
            lines.append(f"        controlRelations[{committee.committee_id}] = {control_mask};")
        lines.append("    }")
        return "\n".join(lines)


    def generate_modifiers(self):
        return """
    modifier onlyRoleControl(bytes32 role) {
        require(canControl(userRoles[msg.sender], role), "Not authorized to perform this action");
        _;
    }

    modifier onlyPermission(bytes32 role, uint8 permissionIndex) {
        require(hasPermission(msg.sender, permissionIndex), "Not authorized to perform this action");
        _;
    }
        """

    def generate_functions(self):
        return """
    function assignRole(address _user, bytes32 _role) external onlyRoleControl(_role) {
        userRoles[_user] = _role;
    }

    function revokeRole(address _user, bytes32 _role) external onlyRoleControl(_role) {
        require(userRoles[_user] == _role, "User does not have this role");
        delete userRoles[_user];
    }

    function grantPermission(bytes32 _role, uint8 _permissionIndex) external onlyRoleControl(_role) {
        roles[_role] |= (uint256(1) << _permissionIndex);
    }

    function revokePermission(bytes32 _role, uint8 _permissionIndex) external onlyRoleControl(_role) {
        roles[_role] &= ~(uint256(1) << _permissionIndex);
    }

    function hasPermission(address _user, uint8 _permissionIndex) public view returns (bool) {
        return (roles[userRoles[_user]] & (uint256(1) << _permissionIndex)) != 0;
    }

    function canControl(bytes32 controllerRole, bytes32 controlledRole) internal view returns (bool) {
        return (controlRelations[controllerRole] & (uint256(1) << uint256(controlledRole))) != 0;
    }
        """

    def generate_permission_functions(self):
        lines = []
        for permission in self.dao.permissions.values():
            function_name = self.preprocess_function_name(permission.allowed_action)
            permission_index = self.get_permission_index(permission)

            lines.append(f"""
    function {function_name}() external onlyPermission(userRoles[msg.sender], {permission_index}) {{
        // TODO: Implement the function logic here
    }}
            """)
        return "\n".join(lines)

    def get_control_mask(self, role_or_committee):
        mask = 0
        for controller in role_or_committee.controllers:
            index = self.dao.roles.index(controller) if controller in self.dao.roles else self.dao.committees.index(controller)
            mask |= (1 << index)
        return mask

    def preprocess_function_name(self, function_name):
        return function_name.replace("/", "_").replace(" ", "_").replace("\\", "")

    def get_permission_index(self, permission):
        # Map permission_id to an integer index
        permission_index_map = {permission.permission_id: idx for idx, permission in enumerate(self.dao.permissions)}
        return permission_index_map[permission.permission_id]

    def generate_closure(self):
        return "}"

