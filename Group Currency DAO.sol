pragma solidity ^0.8.0; 
 /**
 * @title GCDAO has the following mission: Managing the governance of Group Currencies in the Circles UBI system. 
 */
contract GCDAO {
    address public creator;
    string public name;
// role declarations
    uint constant OwnerRole = 0;
    uint constant GroupMemberRole = 1;
    uint constant TreasuryManagerRole = 2;
    uint constant ActiveMemberRole = 3;
// committee declarations
    uint constant GeneralAssemblyRole = 4;
    uint constant EconomicCouncilRole = 5;
    uint constant CommunityCouncilRole = 6;
    uint constant TechnicalCouncilRole = 7;
    mapping(address => uint) roles;
    constructor(string memory _name, address _creator) public {
        name = _name;
        creator = _creator;
        roles[creator] = OwnerRole;
    }
    function propose_service_provision() public {
        require(roles[msg.sender] == GroupMemberRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function update_user_profile() public {
        require(roles[msg.sender] == GroupMemberRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function funding_request_submission() public {
        require(roles[msg.sender] == GroupMemberRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function funding_request_assessment() public {
        require(roles[msg.sender] == TreasuryManagerRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function set_limits_to_group_currency_minting() public {
        require(roles[msg.sender] == TreasuryManagerRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function suspend_service_provision() public {
        require(roles[msg.sender] == GeneralAssemblyRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function evaluate_service_provision() public {
        require(roles[msg.sender] == GeneralAssemblyRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function add_remove_allowed_collateral_type() public {
        require(roles[msg.sender] == EconomicCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function set_contribution_attestation() public {
        require(roles[msg.sender] == CommunityCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function set_membership_requirements() public {
        require(roles[msg.sender] == CommunityCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function include_exclude_members() public {
        require(roles[msg.sender] == CommunityCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function upgrade_Group_Currency_smart_contracts() public {
        require(roles[msg.sender] == TechnicalCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function member_data_management() public {
        require(roles[msg.sender] == TechnicalCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function suspension_of_the_Group_Currency() public {
        require(roles[msg.sender] == TechnicalCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
    function upgrade_DAO_smart_contracts() public {
        require(roles[msg.sender] == TechnicalCouncilRole , "Only authorized roles can execute this function.");
//TODO: define the behavior of the function
    }
}