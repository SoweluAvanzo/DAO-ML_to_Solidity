// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
interface IPermissionManager {
    function isCommitteeMember(address user) external view returns (bool);
}
