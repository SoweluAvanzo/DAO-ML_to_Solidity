// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
/**
 * @title Decentralized_Destination_Management_Organization
 * @notice Manage the governance of an individual destination on the platform
 */
import "./interfaces/IPermissionManager.sol";
contract Decentralized_Destination_Management_Organization is IPermissionManager {
    bool internal committee_initialization_blocked;
    mapping(address => uint32) internal roles;
    uint32[12 + 1] internal role_permissions; // "+1" to allow the 0-index "null Role"
    uint32[12] internal all_roles = [
        32768, // #0) DDMO_Member -> ID : 0 , control bitmask: 10000000000
        98305, // #1) Magister -> ID : 1 , control bitmask: 110000000000
        32770, // #2) Host -> ID : 2 , control bitmask: 10000000000
        32771, // #3) Analyst -> ID : 3 , control bitmask: 10000000000
        32772, // #4) Worker -> ID : 4 , control bitmask: 10000000000
        32773, // #5) Student -> ID : 5 , control bitmask: 10000000000
        98310, // #6) DDMO_Board_Member -> ID : 6 , control bitmask: 110000000000
        32775, // #7) Freelancer -> ID : 7 , control bitmask: 10000000000
        98312, // #8) Institutional_Representative -> ID : 8 , control bitmask: 110000000000
        98313, // #9) Mentor -> ID : 9 , control bitmask: 110000000000
        32778, // #10) Decentralized_Destination_Management_OrganizationOwner -> ID : 10 , control bitmask: 10000000000
        32779 // #11)  DDMO_Council -> ID : 11 , control bitmask: 10000000000
    ];
 //Events
    event RoleRevoked(address indexed user, uint32 indexed role);
    event RoleAssigned(address indexed user, uint32 indexed role);
    event PermissionGranted(uint32 indexed role, uint32 indexed permission);
    event PermissionRevoked(uint32 indexed role, uint32 indexed permission);



        modifier controlledBy(address sender, uint32 user_role_id, bool allowNullRole_user, uint32 new_role_id) {
            //we obtain the control relations of the controller role by shifting the its id by the number of bits contained in ids
            //the sender must control BOTH the target role AND the user's role

            uint32 index_new_role = new_role_id & 31;
            uint32 sender_role_index = ( uint32(1) << ( roles[sender] & 31 ) );

            require(
                ( // the new role must be a valid one
                    index_new_role < 12 // checking for "index out of bounds"
                )
                && ( // "check the sender and target user control relation"
                    (allowNullRole_user && (user_role_id == 0)) || // allow to add role if the user doesn't have one
                    ((
                        (user_role_id >> 5) // get the user role's bitmask 
                        &  // (... and then perform the bitwise-and with ...)
                        sender_role_index
                    ) != 0) // final check
                ) &&
                ( // "control relation check between sender and the target role"
                    (
                        ( all_roles[index_new_role] >> 5) // get the new role's bitmask from those internally stored
                        &  // (... and then perform the bitwise-and with ...)
                        sender_role_index
                    ) != 0 // final check
                )
                , "the given controller can't perform the given operation on the given controlled one" );
            _;
        }
        


 
    modifier hasPermission(address _executor, uint32 _permissionIndex) {
        require(role_permissions[uint32(roles[_executor] & 31)] & (uint32(1) << _permissionIndex) != 0, "User does not have this permission");
        _;
    }
            
    constructor(
) {
        role_permissions[0] = 0; // "null"/absent Role, to indicate a User having no roles at all
        role_permissions[0] = 262175; // #0) DDMO_Member 

        role_permissions[1] = 1835775; // #1) Magister 

        role_permissions[2] = 262175; // #2) Host 

        role_permissions[3] = 270367; // #3) Analyst 

        role_permissions[4] = 262175; // #4) Worker 

        role_permissions[5] = 270367; // #5) Student 

        role_permissions[6] = 1835039; // #6) DDMO_Board_Member 

        role_permissions[7] = 262175; // #7) Freelancer 

        role_permissions[8] = 1843231; // #8) Institutional_Representative 

        role_permissions[9] = 1868063; // #9) Mentor 

        role_permissions[10] = 2097151; // #10) Decentralized_Destination_Management_OrganizationOwner 

        role_permissions[11] = 220160; // #11) DDMO_Council 

roles[msg.sender] = all_roles[10]; // Decentralized_Destination_Management_OrganizationOwner
}
    function initializeCommittees(address _DDMO_Council) external {
        require(roles[msg.sender] == all_roles[10], "Only the owner can initialize the Dao");  // Decentralized_Destination_Management_OrganizationOwner
    require(committee_initialization_blocked == false && _DDMO_Council != address(0), "Invalid committee initialization");
        roles[_DDMO_Council] = all_roles[0]; // DDMO_Council
        committee_initialization_blocked = true;
    }

        
        function canControl(uint32 controller, uint32 controlled) public pure returns(bool controls){
             // ( "CAN the sender control the target user (through its role)?"
                //(allowNullRole && (target_role_id == 0)) || // allow to add role if the user has not already one assigned to it
                if((
                    (controlled >> 5 ) // get the role's bitmask 
                    &  // (and then perform the bitwise-and with ...)
                    (uint32(1) << ( controller & 31 )) // (...) get the sender role's index AND shift it accordingly 
                ) != 0 ){
                    controls = true;
                     return controls;} else {return controls;}
        }
        
        function assignRole(address _user, uint32 _role) external controlledBy(msg.sender, roles[_user], true, _role) {
            require(_user != address(0) , "Invalid user address" );
            
            roles[_user] = _role;
            emit RoleAssigned(_user, _role);
        }

        function revokeRole(address _user, uint32 _role) external controlledBy(msg.sender, roles[_user], false, _role) {
            require(roles[_user] == _role, "User's role and the role to be removed don't coincide" );

            delete roles[_user];
            emit RoleRevoked(_user, _role);
        }

        function grantPermission(uint32 _role, uint32 _permissionIndex) external hasPermission(msg.sender, _permissionIndex) {
            require(canControl(roles[msg.sender], _role), "cannot grant permission, as the control relation is lacking");
            uint32 new_role_perm_value;
            new_role_perm_value  = role_permissions[_role & 31 ] | (uint32(1) << _permissionIndex);
            role_permissions[_role & 31 ] = new_role_perm_value;
            
            emit PermissionGranted(_role, _permissionIndex);
        }

        function revokePermission(uint32 _role, uint32  _permissionIndex) external hasPermission(msg.sender, _permissionIndex) {
            require(canControl(roles[msg.sender], _role), "cannot revoke permission, as the control relation is lacking");
            uint32 new_role_perm_value;
            new_role_perm_value = role_permissions[_role & 31] & ~(uint32(1) << _permissionIndex);
            role_permissions[_role & 31] = new_role_perm_value;

            emit PermissionRevoked(_role, _permissionIndex);
        }

        function hasRole(address user) external view returns(uint32) {
            return roles[user];
        }

        function has_permission(address user, uint32 _permissionIndex) external view returns (bool) {
            if (role_permissions[uint32(roles[user] & 31)] & (uint32(1) << _permissionIndex) != 0){ 
                return true;
            }else{
                return false;
            }
        }
             
         

        function Supply_Service() external hasPermission(msg.sender, 0) {
            // TODO: Implement the function logic here
        }
                

        function Propose_Task_Delegation() external hasPermission(msg.sender, 1) {
            // TODO: Implement the function logic here
        }
                

        function Execute_Task() external hasPermission(msg.sender, 2) {
            // TODO: Implement the function logic here
        }
                

        function Share_Task() external hasPermission(msg.sender, 3) {
            // TODO: Implement the function logic here
        }
                

        function report_task_unaccomplishment() external hasPermission(msg.sender, 4) {
            // TODO: Implement the function logic here
        }
                

        function block_user() external hasPermission(msg.sender, 5) {
            // TODO: Implement the function logic here
        }
                

        function Trigger_dispute_resolution() external hasPermission(msg.sender, 6) {
            // TODO: Implement the function logic here
        }
                

        function Oversee_Dispute() external hasPermission(msg.sender, 7) {
            // TODO: Implement the function logic here
        }
                

        function approve_KYB() external hasPermission(msg.sender, 8) {
            // TODO: Implement the function logic here
        }
                

        function resolve_dispute() external hasPermission(msg.sender, 9) {
            // TODO: Implement the function logic here
        }
                

        function suspend_DDMO() external hasPermission(msg.sender, 10) {
            // TODO: Implement the function logic here
        }
                

        function liquidate_DDMO() external hasPermission(msg.sender, 11) {
            // TODO: Implement the function logic here
        }
                

        function merge_DDMO() external hasPermission(msg.sender, 12) {
            // TODO: Implement the function logic here
        }
                

        function access_data() external hasPermission(msg.sender, 13) {
            // TODO: Implement the function logic here
        }
                

        function update_destination_portal() external hasPermission(msg.sender, 14) {
            // TODO: Implement the function logic here
        }
                

        function approve_AI_Recommendations() external hasPermission(msg.sender, 15) {
            // TODO: Implement the function logic here
        }
                

        function update_duration_of_user_block() external hasPermission(msg.sender, 16) {
            // TODO: Implement the function logic here
        }
                

        function update_number_of_Council_participants() external hasPermission(msg.sender, 17) {
            // TODO: Implement the function logic here
        }
                

        function Request_DDMO_Change() external hasPermission(msg.sender, 18) {
            // TODO: Implement the function logic here
        }
                

            function canVote(address user, uint32 permissionIndex) external view returns (bool) {
                require(role_permissions[uint32(roles[user] & 31)] & (uint32(1) << permissionIndex) != 0, "User does not have this permission");
                return true;
            }

            function canPropose(address user, uint32 permissionIndex) external view returns (bool) {
                require(role_permissions[uint32(roles[user] & 31)] & (uint32(1) << permissionIndex) != 0, "User does not have this permission");
                return true;
            }
}
