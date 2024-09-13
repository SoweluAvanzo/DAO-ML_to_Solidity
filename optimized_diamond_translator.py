import networkx as nx
from DAOclasses import*
from translator import CommitteeTranslatorDiamond
from optimized_translator import *

class OptimizedDiamondTranslator(OptimizedSolidityTranslator):
    def __init__(self, dao: DAO):
        super().__init__(dao)

    def generate_header(self):
        lines = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version};")
        lines.append(f"/**")
        lines.append(f" * @title {self.context.dao.dao_id} permission manager library")
        lines.append(f" * @notice {self.context.dao.mission_statement}")
        lines.append(f" */")
        return "\n".join(lines)
       
    def generate_library_declaration(self, lib_type):     
        lines = []
        lines.append(f"library Lib{self.context.dao.dao_id}{lib_type} {'{'}")
        lines.append(f"bytes32 constant {self.context.dao.dao_id.upper()}_POSITION = keccak256(\"{self.context.dao.dao_id}.{lib_type}.storage\");")
        return "\n".join(lines)
    
    def generate_storage_access_function(self):
        lines = []
        dao_id = self.context.dao.dao_id
        lines.append(f"function get{dao_id}Storage() internal pure returns ({dao_id}Storage storage ds) {'{'}")
        lines.append(f"    bytes32 position = {dao_id.upper()}_POSITION;")
        lines.append(f"    assembly {'{'}")
        lines.append(f"        ds.slot := position")
        lines.append(f"    {'}'}")
        lines.append(f"{'}'}")
        #lines.append(f"    return storage;")
        return "\n".join(lines)
    
    def translateDao(self) -> TranslatedSmartContract: 
        lines = []
        lines.append(self.generate_header())
        lines.append(self.generate_library_declaration("PermissionManager"))
        lines.append(self.generate_storage_struct())
        lines.append(self.generate_modifier_control_relation())
        lines.append(self.generate_has_permission_modifier())
        lines.append(self.generate_storage_access_function())
        lines.append(self.generate_functions())
        lines.append(self.generate_permission_functions())  
        lines.append(self.generate_closure())
        name = self.context.dao.dao_id
        folder = "libraries"
        return TranslatedSmartContract(lines, name, folder=folder)


    def generate_modifier_control_relation(self):
        id_var_type = self.get_variable_type()
        id_bit_size = self.group_size.value[1]
        mask = self.id_mask # calcolato nel costruttore

        lines = []
        lines.append("\n")
        lines.append(f"    modifier controlledBy({id_var_type} target_role_id, address controller_role_address) {'{'}")
        lines.append(f"       GCDAOStorage storage ds = getGCDAOStorage();")
        lines.append(f"       {id_var_type} controller_role_id = ds.roles[controller_role_address];")
        lines.append("        //we obtain the control relations of the controller role by shifting the its id by the number of bits contained in ids")
        lines.append(f"        require( (controller_role_id >> {id_bit_size} ) &")
        lines.append(f"                (1 << ( target_role_id & {mask} )") #we obtain the id of the target role by using the bit mask which removes its control relations
        lines.append(f"            ) != 0, \"the given controller can\'t perform the given operation on the given controlled one\" );") #we check if the controller can control the target role
        lines.append("        _;")
        lines.append("    }")
        lines.append("\n")
        return "\n".join(lines)

    def generate_facet():
        lines = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version};")
        lines.append(f"/**")
        lines.append(f" * @title {self.context.dao.dao_id}")
        lines.append(f" * @notice {self.context.dao.mission_statement}")
        lines.append(f" */")
        lines.append("import {IDaoRegistry} from \"../interfaces/IDaoRegistry.sol\";")
        lines.append(f"library Lib{self.context.dao.dao_id}Facet {'{'}")
        
        folder = "facets"
        
    

    def generate_has_permission_modifier(self):
        #id_var_type = self.get_variable_type()
        is_role_access_optimized = self.group_size is not None
        eventual_addressing_manipulation = f" & {self.id_mask}" if is_role_access_optimized else ""

        return f""" 
    modifier hasPermission(address _executor, {self.perm_var_type} _permissionIndex) {{
        // we access the storage of the DAO through the getter function
        {self.context.dao.dao_id}Storage storage ds = get{self.context.dao.dao_id}Storage();

        require(ds.role_permissions[{self.perm_var_type}(ds.roles[_executor]{eventual_addressing_manipulation})] & ({self.perm_var_type}(1) << _permissionIndex) != 0, "User does not have this permission");
        _;
    }}
            """
    

    def generate_functions(self):
        id_var_type = self.get_variable_type()

        return f"""
        
        function assignRole(address _user, {id_var_type} _role) external controlledBy(_role,msg.sender) {{
        GCDAOStorage storage ds = getGCDAOStorage();
            ds.roles[_user] = _role;
        }}

        function revokeRole(address _user, {id_var_type} _role) external controlledBy(_role,msg.sender) {{
        GCDAOStorage storage ds = getGCDAOStorage();
            delete ds.roles[_user];
        }}
            """
 # function grantPermission({id_var_type} _role, uint8 _permissionIndex) external controlledBy(roles[msg.sender],_role) {{
        #     roles[_role] |= (uint256(1) << _permissionIndex);
        # }}

        # function revokePermission({id_var_type} _role, uint8 _permissionIndex) external controlledBy(roles[msg.sender],_role) {{
        #     roles[_role] &= ~(uint256(1) << _permissionIndex);
        # }}

    def generate_storage_struct(self):
        id_var_type = self.get_variable_type()
        lines = []
        lines.append(f"struct {self.context.dao.dao_id}Storage {'{'}")

        lines.append(f"    mapping(address => {id_var_type}) roles;")
        is_role_access_optimized = self.group_size is not None
        if is_role_access_optimized:
            # since both the Roles and Committees are pre-defined and, therefore, fixed, they works ad Enum,
            # therefore their total amount is fixed -> the "role_permissions" array can be optimized as a 
            # "fixed array" by specifying its size
            total_roles_amount = len(self.context.dao.roles) + len(self.context.dao.committees)
            lines.append(f"    {self.perm_var_type}[{total_roles_amount}] role_permissions;")
        else:
            lines.append(f"    mapping({id_var_type} => {self.perm_var_type}) role_permissions;")
        i = 0
        functionalities_ids = {}
        
        for role in self.context.dao.roles.values():
            functionalities_ids[role.role_id] = i
            i += 1
        for committee in self.context.dao.committees.values():
            functionalities_ids[committee.committee_id] = i
            i += 1

        for role in self.context.dao.roles.values():
            lines.append(f"    {id_var_type} {role.role_id};")
        for committee in self.context.dao.committees.values():
            lines.append(f"    {id_var_type} {committee.committee_id};")
        lines.append("}")
        return "\n".join(lines)
    


    
    def translate(self) -> list[TranslatedSmartContract]:
            all_smart_contracts: list[TranslatedSmartContract] = []

            # at first, translate all Committees
            ct = CommitteeTranslatorDiamond(self.context)
            for c in self.context.dao.committees.values():
                translated_committee = ct.translateCommittee(c) 
                all_smart_contracts.append(translated_committee)
            all_smart_contracts.append(self.translateDao())
            
            return all_smart_contracts

        

        