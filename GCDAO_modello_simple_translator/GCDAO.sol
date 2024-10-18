// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
// @title GCDAO has the following mission: Managing the governance of Group Currencies in the Circles UBI system.
import "./interfaces/IPermissionManager.sol";
contract GCDAO is IPermissionManager {
    address public creator;
    string public name;
// role declarations
    uint constant NonMember = 0;
    uint constant GroupMember = 1;
    uint constant TreasuryManager = 2;
    uint constant ActiveMember = 3;
    uint constant GCDAOOwner = 4;
// committee declarations
    uint constant GeneralAssembly = 5;
    uint constant EconomicCouncil = 6;
    uint constant CommunityCouncil = 7;
    uint constant TechnicalCouncil = 8;
    uint constant OwnerRole = 9;
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
    mapping(uint => mapping(uint => uint)) public committeeMemberships;

    mapping(address => uint) roles;
    constructor(string memory _name, address _creator, address _GeneralAssembly, address _EconomicCouncil, address _CommunityCouncil, address _TechnicalCouncil) {
        name = _name;
        creator = _creator;
        roles[creator] = OwnerRole;
//assign roles to committees
roles[_GeneralAssembly] = GeneralAssembly; 

roles[_EconomicCouncil] = EconomicCouncil; 

roles[_CommunityCouncil] = CommunityCouncil; 

roles[_TechnicalCouncil] = TechnicalCouncil; 

        canControl[TreasuryManager][EconomicCouncil] = true;
        canControl[EconomicCouncil][CommunityCouncil] = true;
        canControl[GeneralAssembly][TechnicalCouncil] = true;
        canControl[GeneralAssembly][CommunityCouncil] = true;
        canControl[TechnicalCouncil][TechnicalCouncil] = true;
        canControl[CommunityCouncil][TechnicalCouncil] = true;
    } 
    function revokeRole(address member) public onlyController(msg.sender, member) {
        // Revoke the role
        roles[member] = NonMember;
        emit RoleRevoked(msg.sender, member); 
    }
function assignRole(address member, uint role) public onlyController(msg.sender, member) {
require(canControl[roles[msg.sender]][role]== true, "cannot assign superior roles");
    roles[member] = role;
emit UserRoleAssigned(member, role);
}

function isCommitteeMember(address member, uint committee) external view returns (uint) {
    require(roles[member] != NonMember, "User is not a member of the DAO");
        return committeeMemberships[roles[member]][committee];
    }
    function propose_service_provision() public{
        require(roles[msg.sender] == GroupMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function update_user_profile() public{
        require(roles[msg.sender] == GroupMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function funding_request_submission() public{
        require(roles[msg.sender] == GroupMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function General_Assembly_Voting_Right() public{
        require(roles[msg.sender] == GroupMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function General_Assembly_Proposal_Right() public{
        require(roles[msg.sender] == GroupMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function funding_request_assessment() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function set_limits_to_group_currency_minting() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Economic_Council_Voting_Right() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Economic_Council_Proposal_Right() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Community_Council_Voting_Right() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == ActiveMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Community_Council_Proposal_Right() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == ActiveMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Technical_Council_Voting_Right() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == ActiveMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function Technical_Council_Proposal_Right() public{
        require(roles[msg.sender] == TreasuryManager || roles[msg.sender] == ActiveMember || roles[msg.sender] == GCDAOOwner , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function suspend_service_provision() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == GeneralAssembly , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function evaluate_service_provision() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == GeneralAssembly , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function add_remove_allowed_collateral_type() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == EconomicCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function set_membership_requirements() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == CommunityCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function suspension_of_the_Group_Currency() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == TechnicalCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function upgrade_Group_Currency_smart_contracts() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == TechnicalCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function upgrade_DAO_smart_contracts() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == TechnicalCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function include_exclude_members() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == CommunityCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function set_contribution_attestation() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == CommunityCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
    function member_data_management() public{
        require(roles[msg.sender] == GCDAOOwner || roles[msg.sender] == TechnicalCouncil , "Only authorized roles can execute this function.");
// TODO: define the behavior of the function
    }
}
