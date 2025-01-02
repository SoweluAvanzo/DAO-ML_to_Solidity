// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../interfaces/ICondition.sol";

contract RotationCondition is ICondition {
    function evaluate(address user) external view override returns (bool) {
        //TODO: Implement the condition smart contract logic here 
        
        return true; 
    }
}
