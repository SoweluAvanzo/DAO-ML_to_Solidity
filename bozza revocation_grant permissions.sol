// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
/**
 * @title GCDAO
 * @notice Managing the governance of Group Currencies in the Circles UBI system.
 */
contract GCDAO {
    mapping(address => uint32) public roles;
    uint16[7] public role_permissions;
    uint32 public constant GroupMember = 0; // ID : 0 , control bitmask: 0
    uint32 public constant TreasuryManager = 3585; // ID : 1 , control bitmask: 1110000
    uint32 public constant ActiveMember = 2; // ID : 2 , control bitmask: 0
    uint32 public constant GeneralAssembly = 3075; // ID : 3 , control bitmask: 0000000....1100000'00011
    uint32 public constant EconomicCouncil = 3076; // ID : 4 , control bitmask: 1100000
    uint32 public constant CommunityCouncil = 2053; // ID : 5 , control bitmask: 1000000
    uint32 public constant TechnicalCouncil = 2054; // ID : 6 , control bitmask: 1000000


    modifier controlledBy(uint32 target_role_id, address controller_role_address) {
       uint32 controller_role_id = roles[controller_role_address];
        //we obtain the control relations of the controller role by shifting the its id by the number of bits contained in ids
        require( (controller_role_id >> 5 ) &
                (1 << ( target_role_id & 31 )
            ) != 0, "the given controller can't perform the given operation on the given controlled one" );
        _;
    }


 
    modifier hasPermission(address _executor, uint16 _permissionIndex) {
        require(role_permissions[uint16(roles[_executor] & 31)] & (uint16(1) << _permissionIndex) != 0, "User does not have this permission");
        _;
    }
            
    constructor(address _owner, address _GeneralAssembly, address _EconomicCouncil, address _CommunityCouncil, address _TechnicalCouncil) {
         _owner = msg.sender;
        role_permissions[GroupMember & 31] = 28;

        role_permissions[TreasuryManager & 31] = 160;

        role_permissions[ActiveMember & 31] = 0;

        role_permissions[GeneralAssembly & 31] = 3;

        role_permissions[EconomicCouncil & 31] = 64;

        role_permissions[CommunityCouncil & 31] = 12544;

        role_permissions[TechnicalCouncil & 31] = 19968;

         roles[_GeneralAssembly] = GeneralAssembly; 

         roles[_EconomicCouncil] = EconomicCouncil; 

         roles[_CommunityCouncil] = CommunityCouncil; 

         roles[_TechnicalCouncil] = TechnicalCouncil; 

    }

        function assignRole(address _user, uint32 _role) external controlledBy(_role,msg.sender) {
            roles[_user] = _role;
        }

        function revokeRole(address _user, uint32 _role) external controlledBy(_role,msg.sender) {
            delete roles[_user];
        }
             
        function grantPermission(uint32 _role, uint16 _permissionIndex) external controlledBy(_role, msg.sender) hasPermission(msg.sender, _permissionIndex) {

            uint16 new_role_value;
            new_role_value = role_permissions[_role & 31] | (uint16(1) << _permissionIndex);
            role_permissions[_role & 31] = new_role_value;

            

         }

         function revokePermission(uint32 _role, uint16  _permissionIndex) external controlledBy(_role, msg.sender) hasPermission(msg.sender, _permissionIndex) {
            //_role & ~(uint32(1) << _permissionIndex);

            
            uint16 new_role_value;
            new_role_value = role_permissions[_role & 31] & ~(uint16(1) << _permissionIndex);
            role_permissions[_role & 31] = new_role_value;
         }
         

        function activate_suspend_service_provision() external hasPermission(msg.sender, 0) {
            // TODO: Implement the function logic here
        }
                

        function evaluate_service_provision() external hasPermission(msg.sender, 1) {
            // TODO: Implement the function logic here
        }
                

        function propose_service_provision() external hasPermission(msg.sender, 2) {
            // TODO: Implement the function logic here
        }
                

        function update_user_profile() external hasPermission(msg.sender, 3) {
            // TODO: Implement the function logic here
        }
                

        function funding_request_submission() external hasPermission(msg.sender, 4) {
            // TODO: Implement the function logic here
        }
                

        function set_limits_to_group_currency_minting() external hasPermission(msg.sender, 5) {
            // TODO: Implement the function logic here
        }
                

        function add_remove_allowed_collateral_type() external hasPermission(msg.sender, 6) {
            // TODO: Implement the function logic here
        }
                

        function funding_request_assessment() external hasPermission(msg.sender, 7) {
            // TODO: Implement the function logic here
        }
                

        function set_membership_requirements() external hasPermission(msg.sender, 8) {
            // TODO: Implement the function logic here
        }
                

        function suspension_of_the_group_currency() external hasPermission(msg.sender, 9) {
            // TODO: Implement the function logic here
        }
                

        function upgrade_Group_Currency_smart_contracts() external hasPermission(msg.sender, 10) {
            // TODO: Implement the function logic here
        }
                

        function upgrade_DAO_smart_contracts() external hasPermission(msg.sender, 11) {
            // TODO: Implement the function logic here
        }
                

        function include_exclude_group_members() external hasPermission(msg.sender, 12) {
            // TODO: Implement the function logic here
        }
                

        function set_contribution_attestation() external hasPermission(msg.sender, 13) {
            // TODO: Implement the function logic here
        }
                

        function member_data_management() external hasPermission(msg.sender, 14) {
            // TODO: Implement the function logic here
        }
                
}
