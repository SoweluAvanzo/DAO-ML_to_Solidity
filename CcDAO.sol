/**
 * @title CcDAO has the following mission: Mission statement here 
 */
contract CcDAO {
    address public creator;
    string public name;
    uint constant ROLE_OWNER = 0;
// committee declarations
    mapping(address => uint) roles;
    constructor(string memory _name, address _creator) public {
        name = _name;
        creator = _creator;
        roles[creator] = ROLE_OWNER;
    }
    function transferToken() public {
        require(
            roles[msg.sender] == ROLE_OWNER
            , "Only authorized roles can execute the transferToken function.");
//TODO: define the behavior of the function
    }
}