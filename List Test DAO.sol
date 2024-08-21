pragma solidity ^0.8.0; 
 /**
 * @title LIST has the following mission: Managing the governance of Group Currencies in the Circles UBI system. 
 */
contract LIST {
    address public creator;
    string public name;
// role declarations
    uint constant NonMember = 0;
    uint constant GroupMember = 1;
    uint constant ActiveMember = 2;
// committee declarations
    uint constant CC = 3;
    uint constant BB = 4;
    uint constant AA = 5;
    uint constant OwnerRole = 6;
// Mapping of roles to the set of roles they can control
mapping(uint256 => mapping(uint256 => bool)) public canControl;
event RoleRevoked(address indexed from, address member);
event UserRoleAssigned(address indexed member, uint role);
// Modifier to check if the caller has the permission to execute the function
   modifier onlyController(address controller_address, address controlled_address) {
    require(
        canControl[roles[controller_address]][roles[controlled_address]],
        "cannot execute the requested action, due to lack of authorization."
    );
    _;
}
    mapping(address => uint) roles;
    constructor(string memory _name, address _creator) {
        name = _name;
        creator = _creator;
        roles[creator] = OwnerRole;
        canControl[CC][BB] = true;
        canControl[BB][AA] = true;
    }
function revokeRole(address member) public onlyController(msg.sender, member) {
    // Revoke the role
 roles[member] = NonMember;
emit RoleRevoked(msg.sender, member); 
}

}