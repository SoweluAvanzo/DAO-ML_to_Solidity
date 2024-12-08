// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
interface IPermissionManager {
    function has_permission(address user, uint64 permissionIndex) external view returns (bool);
    function canVote(address user, uint64 permissionIndex) external view returns (bool);
    function canPropose(address user, uint64 permissionIndex) external view returns (bool);
}
