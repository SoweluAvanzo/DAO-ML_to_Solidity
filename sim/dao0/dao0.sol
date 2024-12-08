// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
/**
 * @title dao0
 * @notice  
 */
import "./interfaces/IPermissionManager.sol";
contract dao0 is IPermissionManager {
    bool internal committee_initialization_blocked;
    mapping(address => uint64) internal roles;
    uint64[21] internal role_permissions;
    uint64 internal  role0 = 0; // ID : 0 , control bitmask: 0
    uint64 internal  role1 = 1; // ID : 1 , control bitmask: 0
    uint64 internal  role2 = 2; // ID : 2 , control bitmask: 0
    uint64 internal  role3 = 3; // ID : 3 , control bitmask: 0
    uint64 internal  role4 = 4; // ID : 4 , control bitmask: 0
    uint64 internal  role5 = 5; // ID : 5 , control bitmask: 0
    uint64 internal  role6 = 6; // ID : 6 , control bitmask: 0
    uint64 internal  role7 = 7; // ID : 7 , control bitmask: 0
    uint64 internal  role8 = 8; // ID : 8 , control bitmask: 0
    uint64 internal  role9 = 9; // ID : 9 , control bitmask: 0
    uint64 internal  role10 = 10; // ID : 10 , control bitmask: 0
    uint64 internal  role11 = 11; // ID : 11 , control bitmask: 0
    uint64 internal  role12 = 12; // ID : 12 , control bitmask: 0
    uint64 internal  role13 = 13; // ID : 13 , control bitmask: 0
    uint64 internal  role14 = 14; // ID : 14 , control bitmask: 0
    uint64 internal  role15 = 15; // ID : 15 , control bitmask: 0
    uint64 internal  role16 = 16; // ID : 16 , control bitmask: 0
    uint64 internal  role17 = 17; // ID : 17 , control bitmask: 0
    uint64 internal  role18 = 18; // ID : 18 , control bitmask: 0
    uint64 internal  role19 = 19; // ID : 19 , control bitmask: 0
    uint64 internal  dao0Owner = 20; // ID : 20 , control bitmask: 0
 //Events
    event RoleRevoked(address indexed user, uint64 indexed role);
    event RoleAssigned(address indexed user, uint64 indexed role);
    event PermissionGranted(uint64 indexed role, uint64 indexed permission);
    event PermissionRevoked(uint64 indexed role, uint64 indexed permission);


    modifier controlledBy(address sender, uint64 user_target_role_id, bool allowNullRole) {
         //we obtain the control relations of the controller role by shifting the its id by the number of bits contained in ids
         //the sender must control BOTH the target role AND the user's role
        require(
            ( // "CAN the sender control the target user (through its role)?"
                (allowNullRole && (user_target_role_id == 0)) || // allow to add role if the user has not already one assigned to it
                ((
                    (user_target_role_id >> 6) // get the role's bitmask 
                    &  // (... and then perform the bitwise-and with ...)
                    ( uint64(1) << ( roles[sender] & 63 ) ) // sender_role_index
                ) != 0) // THE FINAL CHECK
            )
            , "the given controller can't perform the given operation on the given controlled one" );
            
            
        _;
    }


 
    modifier hasPermission(address _executor, uint64 _permissionIndex) {
        require(role_permissions[uint64(roles[_executor] & 63)] & (uint64(1) << _permissionIndex) != 0, "User does not have this permission");
        _;
    }
            
    constructor(
) {
        role_permissions[role0 & 63] = 7;

        role_permissions[role1 & 63] = 7;

        role_permissions[role2 & 63] = 7;

        role_permissions[role3 & 63] = 7;

        role_permissions[role4 & 63] = 7;

        role_permissions[role5 & 63] = 7;

        role_permissions[role6 & 63] = 7;

        role_permissions[role7 & 63] = 7;

        role_permissions[role8 & 63] = 7;

        role_permissions[role9 & 63] = 7;

        role_permissions[role10 & 63] = 7;

        role_permissions[role11 & 63] = 7;

        role_permissions[role12 & 63] = 7;

        role_permissions[role13 & 63] = 7;

        role_permissions[role14 & 63] = 7;

        role_permissions[role15 & 63] = 7;

        role_permissions[role16 & 63] = 7;

        role_permissions[role17 & 63] = 7;

        role_permissions[role18 & 63] = 7;

        role_permissions[role19 & 63] = 7;

        role_permissions[dao0Owner & 63] = 0;

roles[msg.sender] = dao0Owner;
}
    function initializeCommittees() external {
        require(roles[msg.sender] == dao0Owner && committee_initialization_blocked == false && , "Invalid committee initialization");
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
        
        function assignRole(address _user, uint64 _role) external controlledBy(msg.sender, roles[_user], true) controlledBy(msg.sender, _role, false) {
            require(_user != address(0) , "Invalid user address" );
            
            roles[_user] = _role;
            emit RoleAssigned(_user, _role);
        }

        function revokeRole(address _user, uint64 _role) external controlledBy(msg.sender, roles[_user], false) controlledBy(msg.sender, _role, false) {
            require(roles[_user] == _role, "User's role and the role to be removed don't coincide" );

            delete roles[_user];
            emit RoleRevoked(_user, _role);

        }

        function grantPermission(uint64 _role, uint64 _permissionIndex) external hasPermission(msg.sender, _permissionIndex) {
            require(canControl(roles[msg.sender], _role), "cannot grant permission, as the control relation is lacking");
            uint64 new_role_perm_value;
            new_role_perm_value  = role_permissions[_role & 63 ] | (uint64(1) << _permissionIndex);
            role_permissions[_role & 63 ] = new_role_perm_value;
            
            emit PermissionGranted(_role, _permissionIndex);

        }

        function revokePermission(uint64 _role, uint64  _permissionIndex) external hasPermission(msg.sender, _permissionIndex) {
            require(canControl(roles[msg.sender], _role), "cannot revoke permission, as the control relation is lacking");
            uint64 new_role_perm_value;
            new_role_perm_value = role_permissions[_role & 63] & ~(uint64(1) << _permissionIndex);
            role_permissions[_role & 63] = new_role_perm_value;

            emit PermissionRevoked(_role, _permissionIndex);

        }

        function hasRole(address user) external view returns(uint64) {
            return roles[user];

        }

        function has_permission(address user, uint64 _permissionIndex) external view returns (bool) {
            if (role_permissions[uint64(roles[user] & 63)] & (uint64(1) << _permissionIndex) != 0){ 
                return true;

            }else{

                return false;
            }
        }
             
         

        function permission0() external hasPermission(msg.sender, 0) {
            // TODO: Implement the function logic here
        }
                

        function permission1() external hasPermission(msg.sender, 1) {
            // TODO: Implement the function logic here
        }
                

        function permission2() external hasPermission(msg.sender, 2) {
            // TODO: Implement the function logic here
        }
                

        function permission3() external hasPermission(msg.sender, 3) {
            // TODO: Implement the function logic here
        }
                

        function permission4() external hasPermission(msg.sender, 4) {
            // TODO: Implement the function logic here
        }
                

        function permission5() external hasPermission(msg.sender, 5) {
            // TODO: Implement the function logic here
        }
                

        function permission6() external hasPermission(msg.sender, 6) {
            // TODO: Implement the function logic here
        }
                

        function permission7() external hasPermission(msg.sender, 7) {
            // TODO: Implement the function logic here
        }
                

        function permission8() external hasPermission(msg.sender, 8) {
            // TODO: Implement the function logic here
        }
                

        function permission9() external hasPermission(msg.sender, 9) {
            // TODO: Implement the function logic here
        }
                

        function permission10() external hasPermission(msg.sender, 10) {
            // TODO: Implement the function logic here
        }
                

        function permission11() external hasPermission(msg.sender, 11) {
            // TODO: Implement the function logic here
        }
                

        function permission12() external hasPermission(msg.sender, 12) {
            // TODO: Implement the function logic here
        }
                

        function permission13() external hasPermission(msg.sender, 13) {
            // TODO: Implement the function logic here
        }
                

        function permission14() external hasPermission(msg.sender, 14) {
            // TODO: Implement the function logic here
        }
                

        function permission15() external hasPermission(msg.sender, 15) {
            // TODO: Implement the function logic here
        }
                

        function permission16() external hasPermission(msg.sender, 16) {
            // TODO: Implement the function logic here
        }
                

        function permission17() external hasPermission(msg.sender, 17) {
            // TODO: Implement the function logic here
        }
                

        function permission18() external hasPermission(msg.sender, 18) {
            // TODO: Implement the function logic here
        }
                

        function permission19() external hasPermission(msg.sender, 19) {
            // TODO: Implement the function logic here
        }
                

        function permission20() external hasPermission(msg.sender, 20) {
            // TODO: Implement the function logic here
        }
                

        function permission21() external hasPermission(msg.sender, 21) {
            // TODO: Implement the function logic here
        }
                

        function permission22() external hasPermission(msg.sender, 22) {
            // TODO: Implement the function logic here
        }
                

        function permission23() external hasPermission(msg.sender, 23) {
            // TODO: Implement the function logic here
        }
                

        function permission24() external hasPermission(msg.sender, 24) {
            // TODO: Implement the function logic here
        }
                

        function permission25() external hasPermission(msg.sender, 25) {
            // TODO: Implement the function logic here
        }
                

        function permission26() external hasPermission(msg.sender, 26) {
            // TODO: Implement the function logic here
        }
                

        function permission27() external hasPermission(msg.sender, 27) {
            // TODO: Implement the function logic here
        }
                

        function permission28() external hasPermission(msg.sender, 28) {
            // TODO: Implement the function logic here
        }
                

        function permission29() external hasPermission(msg.sender, 29) {
            // TODO: Implement the function logic here
        }
                

        function permission30() external hasPermission(msg.sender, 30) {
            // TODO: Implement the function logic here
        }
                

        function permission31() external hasPermission(msg.sender, 31) {
            // TODO: Implement the function logic here
        }
                

        function permission32() external hasPermission(msg.sender, 32) {
            // TODO: Implement the function logic here
        }
                

        function permission33() external hasPermission(msg.sender, 33) {
            // TODO: Implement the function logic here
        }
                

        function permission34() external hasPermission(msg.sender, 34) {
            // TODO: Implement the function logic here
        }
                
}
