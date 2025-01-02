// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
// @title Communitycouncil in GCDAO, using the quadratic_voting protocol


import "@openzeppelin/contracts/governance/Governor.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";

import "./interfaces/IPermissionManager.sol";


contract Communitycouncil is Governor, GovernorVotes, GovernorSettings, IPermissionManager {
     IPermissionManager public permissionManager;

    constructor(IVotes _token)
        Governor("Communitycouncil")
        GovernorVotes(_token)
        GovernorSettings(1 /* voting delay */, 45818 /* voting period */, 0) 
    {
         permissionManager = IPermissionManager(_permissionManager); 
    }

    function getVotes(address account, uint256 blockNumber) public view override returns ( uint256) {
        uint256 basicVotingPower = super.getVotes(account, blockNumber);
        return sqrt(basicVotingPower);
    }
    
    function sqrt(uint256 y) internal pure returns ( uint256 z) {
    if (y > 3) {
        z = y;
        uint256 x = y / 2 + 1;
        while (x < z) {
            z = x;
            x = (y / x + x) / 2;
        }
    } else if (y != 0) {
        z = 1;
    }
}

    function propose(address[] memory targets, uint256[] memory values, bytes[] memory calldatas, string memory description)
        public
        override
        returns (uint256)
    {
        require(permissionManager.canPropose(msg.sender, None), "User cannot propose");

        return super.propose(targets, values, calldatas, description);
    }
    
function castVote(uint256 proposalId, uint8 support)
        public
        override
        returns (uint256)
    {
        require(permissionManager.canVote(msg.sender, None), "PermissionManager: User cannot vote");
        return super.castVote(proposalId, support);
    }
 // Override proposal threshold to integrate quadratic cost (if needed)
    function proposalThreshold() public view override(Governor, GovernorSettings) returns (uint256) {
        return super.proposalThreshold();
    }

    // Override votingDelay to specify the delay between proposal and voting
    function votingDelay() public view override(Governor, GovernorSettings) returns (uint256) {
        return super.votingDelay();
    }

    // Override votingPeriod to specify the duration of the voting period
    function votingPeriod() public view override(Governor, GovernorSettings) returns (uint256) {
        return super.votingPeriod();
    }

    // Override quorum function to specify the quorum required for a vote to pass
    function quorum(uint256 blockNumber) public view override(Governor, GovernorVotes) returns (uint256) {
        return super.quorum(blockNumber);
    }
}
