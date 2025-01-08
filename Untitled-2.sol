// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "./interfaces/IPermissionManager.sol";
// @title Decentralized_Destination_Management_Organization has the following mission: Manage the governance of an individual destination on the platform
contract Decentralized_Destination_Management_Organization is IPermissionManager {
// role declarations
    uint NonMember = 0;
    uint DDMO_Member = 1;
    uint Magister = 2;
    uint Host = 3;
    uint Analyst = 4;
    uint Worker = 5;
    uint Student = 6;
    uint DDMO_Board_Member = 7;
    uint Freelancer = 8;
    uint Institutional_Representative = 9;
    uint Mentor = 10;
    uint Decentralized_Destination_Management_OrganizationOwner = 11;
// committee declarations
    uint DDMO_Council = 12;
    // Mapping of roles to the set of roles they can control
    mapping(uint => mapping(uint => bool)) public controlRelations;
    // Modifier to check if the caller has the permission to execute the function
     modifier controlledBy(uint controller_role, uint controlled_role) {
    require(
        controlRelations[controller_role][controlled_role],
        "Controller does not have the required permissions over the controlled role"
    );
    _;
}
    mapping(uint => mapping(uint => uint8)) public committeeMemberships;
    mapping(address => uint) roles;
    event RoleRevoked(address indexed from, address member);
    event RoleAssigned(address indexed member, uint role);
    constructor( address _owner, address _DDMO_Council) {
        roles[_owner] = Decentralized_Destination_Management_OrganizationOwner;
//assign roles to committees
roles[_DDMO_Council] = DDMO_Council; 

        controlRelations[Decentralized_Destination_Management_OrganizationOwner][DDMO_Member] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Decentralized_Destination_Management_OrganizationOwner] = true;
        controlRelations[DDMO_Council][Magister] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Magister] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][DDMO_Council] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Host] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Analyst] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Worker] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Student] = true;
        controlRelations[DDMO_Council][DDMO_Board_Member] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][DDMO_Board_Member] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Freelancer] = true;
        controlRelations[DDMO_Council][Institutional_Representative] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Institutional_Representative] = true;
        controlRelations[DDMO_Council][Mentor] = true;
        controlRelations[Decentralized_Destination_Management_OrganizationOwner][Mentor] = true;

//Assigning voting and proposal rights to roles and committees. 1 stands for voting rights, 2 for proposal.
        committeeMemberships[DDMO_Board_Member][DDMO_Council] = 1;
        committeeMemberships[DDMO_Board_Member][DDMO_Council] = 2;
    }
function revokeRole(address member) public controlledBy(roles[msg.sender], roles[member]) {
    require(member != address(0), "Invalid member address");
    uint current_role_id = roles[member];
    // Ensure the member has an assigned role (not already a NonMember)
    require(current_role_id != NonMember, "Role must be assigned to revoke");

    // Revoke the role by setting it to NonMember
    roles[member] = NonMember;

    emit RoleRevoked(msg.sender, member);
}

function assignRole(address member, uint new_role_id) public controlledBy(roles[msg.sender], new_role_id) {
    require(member != address(0), "Invalid member address");
    require(new_role_id != NonMember, "Invalid new role");
    
    uint current_role_id = roles[member];

    // Ensure the member is either a NonMember or the caller controls the current role
    require(
        current_role_id == NonMember || controlRelations[roles[msg.sender]][current_role_id],
        "Cannot assign role: caller lacks control over the member's current role"
    );

    // Assign the new role
    roles[member] = new_role_id;
    emit RoleAssigned(member, new_role_id);
}

function isCommitteeMember(address _user, uint _committee) external view returns (uint) {
    return committeeMemberships[roles[_user]][_committee];
}
function hasRole(address _user) external view returns (uint) {
    return roles[_user];
}
function can_control(address _controller, address _controlled) external view returns (bool) {
    return controlRelations[roles[_controller]][roles[_controlled]];
}
    function Supply_Service() public{
        require(roles[msg.sender] == DDMO_Member || roles[msg.sender] == Magister || roles[msg.sender] == Host || roles[msg.sender] == Analyst || roles[msg.sender] == Worker || roles[msg.sender] == Student || roles[msg.sender] == DDMO_Board_Member || roles[msg.sender] == Freelancer || roles[msg.sender] == Institutional_Representative || roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Propose_Task_Delegation() public{
        require(roles[msg.sender] == DDMO_Member || roles[msg.sender] == Magister || roles[msg.sender] == Host || roles[msg.sender] == Analyst || roles[msg.sender] == Worker || roles[msg.sender] == Student || roles[msg.sender] == DDMO_Board_Member || roles[msg.sender] == Freelancer || roles[msg.sender] == Institutional_Representative || roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Execute_Task() public{
        require(roles[msg.sender] == DDMO_Member || roles[msg.sender] == Magister || roles[msg.sender] == Host || roles[msg.sender] == Analyst || roles[msg.sender] == Worker || roles[msg.sender] == Student || roles[msg.sender] == DDMO_Board_Member || roles[msg.sender] == Freelancer || roles[msg.sender] == Institutional_Representative || roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Share_Task() public{
        require(roles[msg.sender] == DDMO_Member || roles[msg.sender] == Magister || roles[msg.sender] == Host || roles[msg.sender] == Analyst || roles[msg.sender] == Worker || roles[msg.sender] == Student || roles[msg.sender] == DDMO_Board_Member || roles[msg.sender] == Freelancer || roles[msg.sender] == Institutional_Representative || roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Request_DDMO_Change() public{
        require(roles[msg.sender] == DDMO_Member || roles[msg.sender] == Magister || roles[msg.sender] == Host || roles[msg.sender] == Analyst || roles[msg.sender] == Worker || roles[msg.sender] == Student || roles[msg.sender] == DDMO_Board_Member || roles[msg.sender] == Freelancer || roles[msg.sender] == Institutional_Representative || roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function report_task_unaccomplishment() public{
        require(roles[msg.sender] == DDMO_Member || roles[msg.sender] == Magister || roles[msg.sender] == Host || roles[msg.sender] == Analyst || roles[msg.sender] == Worker || roles[msg.sender] == Student || roles[msg.sender] == DDMO_Board_Member || roles[msg.sender] == Freelancer || roles[msg.sender] == Institutional_Representative || roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function block_user() public{
        require(roles[msg.sender] == Magister || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Oversee_Dispute() public{
        require(roles[msg.sender] == Magister || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Trigger_dispute_resolution() public{
        require(roles[msg.sender] == Magister || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function resolve_dispute() public{
        require(roles[msg.sender] == Magister || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function access_data() public{
        require(roles[msg.sender] == Analyst || roles[msg.sender] == Student || roles[msg.sender] == Institutional_Representative || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function approve_AI_Recommendations() public{
        require(roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function approve_KYB() public{
        require(roles[msg.sender] == Mentor || roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function suspend_DDMO() public{
        require(roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner || roles[msg.sender] == DDMO_Council , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function liquidate_DDMO() public{
        require(roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner || roles[msg.sender] == DDMO_Council , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function merge_DDMO() public{
        require(roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner || roles[msg.sender] == DDMO_Council , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function update_destination_portal() public{
        require(roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner || roles[msg.sender] == DDMO_Council , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function update_duration_of_user_block() public{
        require(roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner || roles[msg.sender] == DDMO_Council , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function update_number_of_Council_participants() public{
        require(roles[msg.sender] == Decentralized_Destination_Management_OrganizationOwner || roles[msg.sender] == DDMO_Council , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
}
