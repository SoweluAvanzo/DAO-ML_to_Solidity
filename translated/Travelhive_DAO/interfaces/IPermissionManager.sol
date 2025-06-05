// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
interface IPermissionManager {
    function has_permission(address user, uint32 permissionIndex) external view returns (bool);
    function canVote(address user, uint32 permissionIndex) external view returns (bool);
    function canPropose(address user, uint32 permissionIndex) external view returns (bool);
}
