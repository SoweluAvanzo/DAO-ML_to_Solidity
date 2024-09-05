import os
from DAOclasses import*
from translator import TranslatedSmartContract, CommitteeTranslator, TranslationContext, Translator

class OptimizedSolidityTranslator(Translator):
    def __init__(self, dao):

        self.context = TranslationContext(dao, role_declaration_policy = None, solidity_version = "^0.8.0", daoOwner = True)
        #self.dao = dao
        self.group_size = self.context.dao.metadata.user_functionalities_group_size
        self.id_mask = self.recalculate_id_mask()
        self.perm_var_type = self.get_permission_array_size()
    def recalculate_id_mask(self):
        id_mask = 0
        for i in range(self.group_size.value[1]):
            id_mask |= 1 << i
        return id_mask
    
    def generate_modifier_control_relation(self):
        id_var_type = self.get_variable_type()
        id_bit_size = self.group_size.value[1]
        mask = self.id_mask # calcolato nel costruttore

        lines = []
        lines.append("\n")
        lines.append(f"modifier canControl({id_var_type} controller_role_id, {id_var_type} target_role_id) {{")
        lines.append("//we obtain the control relations of the controller role by shifting the its id by the number of bits contained in ids")
        lines.append(f"        require( (controller_role_id >> {id_bit_size} ) &")
        lines.append(f"                (1 << ( target_role_id & {mask} )") #we obtain the id of the target role by using the bit mask which removes its control relations
        lines.append(f"            ) != 0, \"the given controller can\'t perform the given operation on the given controlled one\" );") #we check if the controller can control the target role
        lines.append("        _;")
        lines.append("    }")
        lines.append("\n")
        return "\n".join(lines)

    def translateDao(self) -> TranslatedSmartContract: 
        lines = []
        lines.append(self.generate_header())
        lines.append(self.generate_contract_declaration())
        lines.append(self.generate_state_variables())
        lines.append(self.generate_modifier_control_relation())
        lines.append(self.generate_has_permission_modifier())
        lines.append(self.generate_constructor())
        lines.append(self.generate_functions())
        lines.append(self.generate_permission_functions())  
        lines.append(self.generate_closure())
        name = self.context.dao.dao_id
        return TranslatedSmartContract(lines, name)
        #return "\n".join(lines)

    def translate(self) -> list[TranslatedSmartContract]:
            all_smart_contracts: list[TranslatedSmartContract] = []

            # at first, translate all Committees
            ct = CommitteeTranslator(self.context)
            for c in self.context.dao.committees.values():
                translated_committee = ct.translateCommittee(c) 
                all_smart_contracts.append(translated_committee)

            # TODO: governance area

            # in the end, the DAO itself
            all_smart_contracts.append(self.translateDao())
            
            return all_smart_contracts

    def generate_header(self):
        lines = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version}")
        lines.append(f"/**")
        lines.append(f" * @title {self.context.dao.dao_id}")
        lines.append(f" * @notice {self.context.dao.mission_statement}")
        lines.append(f" */")
        return "\n".join(lines)
        return f"pragma solidity {self.context.solidity_version}\n/**\n * @title {self.context.dao.dao_id}\n * @notice {self.context.dao.mission_statement}\n */"

    def generate_contract_declaration(self):
        return f"contract {self.context.dao.dao_id} {{"
    
    def get_control_bitflags(self, role_or_committee,group_size, functionalities_ids):
            bits_for_id = group_size.value[1]
            mask = 0
            for controller in role_or_committee.controllers:
                index = functionalities_ids[controller]
                mask |= (1 << (index + bits_for_id))
            return mask

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
        if len(self.context.dao.permissions) <= 8:
            perm_var_type = "uint8" 
        elif len(self.context.dao.permissions) <= 16:
            perm_var_type ="uint16"
        elif len(self.context.dao.permissions)  <= 32:
            perm_var_type = "uint32"
        elif len(self.context.dao.permissions)  <= 64:
            perm_var_type = "uint64"
        elif len(self.context.dao.permissions) <= 128:
            perm_var_type = "uint128"
        elif len(self.context.dao.permissions) <= 256:
            perm_var_type = "uint256"
        return perm_var_type

    def generate_state_variables(self):
        id_var_type = self.get_variable_type()
        
        lines = []
        lines.append(f"    mapping(address => {id_var_type}) private roles;")
        lines.append(f"    mapping({id_var_type}=> {self.perm_var_type}) private role_permissions;")
        i = 0
        functionalities_ids = {}
        
        for role in self.context.dao.roles.values():
            functionalities_ids[role.role_id] = i
            i += 1
        for committee in self.context.dao.committees.values():
            functionalities_ids[committee.committee_id] = i
            i += 1
        
        
        for role in self.context.dao.roles.values():
            control_mask = self.get_control_bitflags(role,self.group_size, functionalities_ids)
            final_id = functionalities_ids[role.role_id] | control_mask
            lines.append(f"    {id_var_type} public constant {role.role_id} = {final_id};")
        for committee in self.context.dao.committees.values():
            control_mask = self.get_control_bitflags(committee,self.group_size, functionalities_ids)
            final_id = functionalities_ids[committee.committee_id] | control_mask
            lines.append(f"    {id_var_type} public constant {committee.committee_id} = {final_id};")
        return "\n".join(lines)



    def generate_constructor(self):
        committee_list_param = [f"address _{x}" for x in [committee.committee_id for committee in self.context.dao.committees.values()] ]
        committee_address_list = ', '.join(committee_list_param)
        lines = []
        lines.append(f"    constructor(address _owner, {committee_address_list}) {{")
        lines.append("_owner = msg.sender;")
        # for role in self.context.dao.roles.values():
        #     control_mask = self.get_control_mask(role)
        #     lines.append(f"        controlRelations[{role.role_id}] = {control_mask};")
        # for committee in self.context.dao.committees.values():
        #     control_mask = self.get_control_mask(committee)
        #     lines.append(f"        controlRelations[{committee.committee_id}] = {control_mask};")
        lines.append(self.generate_role_permission_mapping())
        for committee in self.context.dao.committees.values():
            lines.append(f"roles[_{committee.committee_id}] = {committee.committee_id}; \n" )
        lines.append("    }")
        return "\n".join(lines)

    
    def generate_has_permission_modifier(self):
        id_var_type = self.get_variable_type()

        return f"""
        modifier hasPermission(address _executor, uint8 _permissionIndex) {{
            require(role_permissions[roles[_executor]] & (uint256(1) << _permissionIndex) != 0, "User does not have this permission");
            _;
        }}
            """
#TODO: Sono arrivato qui: implementare le funzioni per assegnare e revocare i permessi correttamente
    def generate_functions(self):
        id_var_type = self.get_variable_type()

        return f"""
        function assignRole(address _user, {id_var_type} _role) external canControl(roles[msg.sender],_role) {{
            roles[_user] = _role;
        }}

        function revokeRole(address _user, {id_var_type} _role) external canControl(roles[msg.sender],_role) {{
            delete roles[_user];
        }}
            """
 # function grantPermission({id_var_type} _role, uint8 _permissionIndex) external canControl(roles[msg.sender],_role) {{
        #     roles[_role] |= (uint256(1) << _permissionIndex);
        # }}

        # function revokePermission({id_var_type} _role, uint8 _permissionIndex) external canControl(roles[msg.sender],_role) {{
        #     roles[_role] &= ~(uint256(1) << _permissionIndex);
        # }}
        
    #TO BE TESTED
    def generate_role_permission_mapping(self):
        # Create a mapping from role IDs to the indices of the permissions they have
        role_permissions_mapping = {}
        for role in self.context.dao.roles.values():
            role_permissions_mapping[role.role_id] = [self.get_permission_index(permission.permission_id) for permission in role.permissions]
        for committee in self.context.dao.committees.values():
            role_permissions_mapping[committee.committee_id] = [self.get_permission_index(permission.permission_id) for permission in committee.permissions]
        
        # Generate the Solidity code to set the role_permissions mapping
        lines = []
        for role, permission_indices in role_permissions_mapping.items():
                # Initialize the bitflag for the given role
                bitflag = 0
                # Set the bit for each permission index
                for index in permission_indices:
                    bitflag |= (1 << index)
                lines.append(f"role_permissions[{role}] = {bitflag};\n")
        return "\n".join(lines)
    
    
    def generate_permission_functions(self):
        lines = []
        for perm in self.context.dao.permissions:
            function_name = self.preprocess_function_name(perm)
            permission_index = self.get_permission_index(perm)
            lines.append(f"""
        function {function_name}() external hasPermission(msg.sender, {permission_index}) {{
            // TODO: Implement the function logic here
        }}
                """)
        return "\n".join(lines)

    # def get_control_mask(self, role_or_committee):
    #     mask = 0
    #     for controller in role_or_committee.controllers:
    #         index = self.context.dao.roles.index(controller) if controller in self.context.dao.roles else self.context.dao.committees.index(controller)
    #         mask |= (1 << index)
    #     return mask

    def preprocess_function_name(self, function_name):
        return function_name.replace("/", "_").replace(" ", "_").replace("\\", "")


    def get_permission_index(self, permission):
        #Map permission_id to an integer index
        permission_index_map = {permission: idx for idx, permission in enumerate(self.context.dao.permissions)}
        return permission_index_map[permission]

    def generate_closure(self):
        return "}"

