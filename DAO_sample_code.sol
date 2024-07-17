
//DAO CONTRACT
    //header
    //mission_statement
/**
 * @title CcDAO represents a DAO in Cocity ecosystem.
 */
contract
    //dao_id
 [[CcDAO]] {
//DAO BODY
    //creator_address
    address public creator;
    //dao_name_var
    string public name;
        //ROLES
            //role_id
            //role_value (assigned randomly)
    uint constant [[ROLE_OWNER]] = [[40]];
        //role_mapping
    mapping(address => uint) roles;
    //DAO CONSTRUCTOR
        //PARAMETERS
            //dao_name_parameter
            //dao_creator_parameter
            //generic_parameter
constructor(
        [[string memory _name]],
        [[address _creator]]
    ) public {
        name = _name;
        creator = _creator;
        roles[creator] = ROLE_OWNER;
    }
    //FUNCTIONS
        //generic function
                //allowed_action
    function [[transferToken]](string memory _symbol, uint256 _amount, address _to) public {
                //has_permission_check
                    //allowed_role
            require(roles[msg.sender] == [[ROLE_ADMIN]] || roles[msg.sender] == [[ROLE_OWNER]], "Only admins or owners can transfer money outside the wallet");
                    //function_body
        }

        //my_role_function
    function myRole() public view returns(uint) {
        return roles[msg.sender];
    }    
        //assign_function
        function assignRole() public {
            //check_role_not_already_assigned
        require(roles[msg.sender] == ROLE_NOTMEMBER, "already a member, cannot join");

        roles[msg.sender] = ROLE_MEMBER;
    }
        //revoke_function
        function kickMember(address _member) public {
            //check_has_role

        require(roles[_member] > ROLE_NOTMEMBER, "not a member, cannot kick");
        require(roles[msg.sender] > roles[_member], "cannot kick my superiors");

        delete(roles[_member]);
    }
    //dao_contract_closure
}
    

    
//voting function
//proposal submission