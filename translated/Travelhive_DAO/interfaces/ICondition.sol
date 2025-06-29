// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
interface ICondition {
    function evaluate(address user) external view returns (bool);
}
