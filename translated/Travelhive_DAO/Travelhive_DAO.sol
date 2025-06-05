// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
/**
 * @title Travelhive_DAO
 * @notice Manage the Travelhive ecosystem governance
 */
import "./interfaces/IPermissionManager.sol";
import "./interfaces/ICondition.sol";
contract Travelhive_DAO is IPermissionManager {
    bool internal committee_initialization_blocked;
    mapping(address => uint32) internal roles;
    mapping(uint32 => ICondition) internal voting_conditions;
    mapping(uint32 => ICondition) internal proposal_conditions;
    uint32[14] internal role_permissions;
    uint32[14] internal all_roles = [
        24576, // #0) Advisor -> ID : 0 , control bitmask: 1100000000
        24577, // #1) Founder -> ID : 1 , control bitmask: 1100000000
        24578, // #2) Master_Node -> ID : 2 , control bitmask: 1100000000
        24579, // #3) Marketing_Delegate -> ID : 3 , control bitmask: 1100000000
        24580, // #4) Investor -> ID : 4 , control bitmask: 1100000000
        24581, // #5) Developer -> ID : 5 , control bitmask: 1100000000
        24582, // #6) Ambassador -> ID : 6 , control bitmask: 1100000000
        24583, // #7) DAO_Member -> ID : 7 , control bitmask: 1100000000
        8200, // #8) Travelhive_DAOOwner -> ID : 8 , control bitmask: 100000000
        24585, // #9)  DAO_Council -> ID : 9 , control bitmask: 1100000000
        24586, // #10)  Marketing_Board -> ID : 10 , control bitmask: 1100000000
        24587, // #11)  Financial_Board -> ID : 11 , control bitmask: 1100000000
        24588, // #12)  Travelware_Board -> ID : 12 , control bitmask: 1100000000
        24589 // #13)  Development_Board -> ID : 13 , control bitmask: 1100000000
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
                    index_new_role < 14 // checking for "index out of bounds"
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
uint32[] memory roleIds, 
address[] memory votingConditionAddresses, 
address[] memory proposalConditionAddresses, 
) {
        role_permissions[0] = 51298496; // #0) Advisor 

        role_permissions[1] = 51298496; // #1) Founder 

        role_permissions[2] = 202277056; // #2) Master_Node 

        role_permissions[3] = 4096704; // #3) Marketing_Delegate 

        role_permissions[4] = 13533376; // #4) Investor 

        role_permissions[5] = 202277056; // #5) Developer 

        role_permissions[6] = 4099264; // #6) Ambassador 

        role_permissions[7] = 950464; // #7) DAO_Member 

        role_permissions[8] = 268435455; // #8) Travelhive_DAOOwner 

        role_permissions[9] = 69667; // #9) DAO_Council 

        role_permissions[10] = 77859; // #10) Marketing_Board 

        role_permissions[11] = 69695; // #11) Financial_Board 

        role_permissions[12] = 69923; // #12) Travelware_Board 

        role_permissions[13] = 69667; // #13) Development_Board 

roles[msg.sender] = all_roles[8]; // Travelhive_DAOOwner
for (uint256 i = 0; i < roleIds.length; i++) { 
     voting_conditions[roleIds[i]] = ICondition(votingConditionAddresses[i]);
     proposal_conditions[roleIds[i]] = ICondition(proposalConditionAddresses[i]);
}
    function initializeCommittees(address _DAO_Council, address _Marketing_Board, address _Financial_Board, address _Travelware_Board, address _Development_Board) external {
        require(roles[msg.sender] == all_roles[8], "Only the owner can initialize the Dao");  // Travelhive_DAOOwner
    require(committee_initialization_blocked == false && _DAO_Council != address(0) && _Marketing_Board != address(0) && _Financial_Board != address(0) && _Travelware_Board != address(0) && _Development_Board != address(0), "Invalid committee initialization");
        roles[_DAO_Council] = all_roles[0]; // DAO_Council
        roles[_Marketing_Board] = all_roles[1]; // Marketing_Board
        roles[_Financial_Board] = all_roles[2]; // Financial_Board
        roles[_Travelware_Board] = all_roles[3]; // Travelware_Board
        roles[_Development_Board] = all_roles[4]; // Development_Board
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
             
         

        function modify_salary_distribution_policy() external hasPermission(msg.sender, 0) {
            // TODO: Implement the function logic here
        }
                

        function upgrade_platform_feature() external hasPermission(msg.sender, 1) {
            // TODO: Implement the function logic here
        }
                

        function transfer_tokens() external hasPermission(msg.sender, 2) {
            // TODO: Implement the function logic here
        }
                

        function approve_project_budget() external hasPermission(msg.sender, 3) {
            // TODO: Implement the function logic here
        }
                

        function cut_project_funding() external hasPermission(msg.sender, 4) {
            // TODO: Implement the function logic here
        }
                

        function Modify_salary_distribution_policy() external hasPermission(msg.sender, 5) {
            // TODO: Implement the function logic here
        }
                

        function supply_service() external hasPermission(msg.sender, 6) {
            // TODO: Implement the function logic here
        }
                

        function execute_task() external hasPermission(msg.sender, 7) {
            // TODO: Implement the function logic here
        }
                

        function assign_task() external hasPermission(msg.sender, 8) {
            // TODO: Implement the function logic here
        }
                

        function post_event() external hasPermission(msg.sender, 9) {
            // TODO: Implement the function logic here
        }
                

        function verify_institutional_profile() external hasPermission(msg.sender, 10) {
            // TODO: Implement the function logic here
        }
                

        function appoint_destination_committee() external hasPermission(msg.sender, 11) {
            // TODO: Implement the function logic here
        }
                

        function create_new_DDMO() external hasPermission(msg.sender, 12) {
            // TODO: Implement the function logic here
        }
                

        function propose_campaign_budget() external hasPermission(msg.sender, 13) {
            // TODO: Implement the function logic here
        }
                

        function Veto_Proposal() external hasPermission(msg.sender, 14) {
            // TODO: Implement the function logic here
        }
                

        function apply_for_governance_role() external hasPermission(msg.sender, 15) {
            // TODO: Implement the function logic here
        }
                

        function activate_role_delegation() external hasPermission(msg.sender, 16) {
            // TODO: Implement the function logic here
        }
                

        function request_task_delegation() external hasPermission(msg.sender, 17) {
            // TODO: Implement the function logic here
        }
                

            function canVote(address user, uint32 permissionIndex) external view returns (bool) {
                require(role_permissions[uint32(roles[user] & 31)] & (uint32(1) << permissionIndex) != 0, "User does not have this permission");
                
                ICondition _condition = voting_conditions[roles[msg.sender]] ;
                return (_condition == ICondition(address(0))) || _condition.evaluate(user);
            
            }

            function canPropose(address user, uint32 permissionIndex) external view returns (bool) {
                require(role_permissions[uint32(roles[user] & 31)] & (uint32(1) << permissionIndex) != 0, "User does not have this permission");
                
                ICondition _condition = proposal_conditions[roles[msg.sender]] ;
                return (_condition == ICondition(address(0))) || _condition.evaluate(user);
            
            }
}
