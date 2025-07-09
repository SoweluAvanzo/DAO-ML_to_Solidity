// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// @title DdmoCouncil in Decentralized_Destination_Management_Organization, using the simple_majority protocol


import "@openzeppelin/contracts/governance/Governor.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";

import "./interfaces/IPermissionManager.sol";


contract DdmoCouncil is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction {
    
    // State variables
    IPermissionManager public permissionManager;

    // Constructor
    constructor(IVotes _token, address _permissionManager)
        Governor("DdmoCouncil")
        GovernorSettings(7200 /* 1 day */, 50400 /* 1 week */, 0)
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(0)
    {
        permissionManager = IPermissionManager(_permissionManager); 
    }

    function castVote(uint256 proposalId, uint8 support)
        public
        override
        returns (uint256)
    {
        require(permissionManager.canVote(msg.sender, 20), "User cannot vote");
        return super.castVote(proposalId, support);
    }

    // Override proposal logic to include permission check before proposing
    function propose(address[] memory targets, uint256[] memory values, bytes[] memory calldatas, string memory description)
        public
        override
        returns (uint256)
    {
        require(permissionManager.canPropose(msg.sender, 19), "User cannot propose");
        return super.propose(targets, values, calldatas, description);
    }

    function votingDelay()
        public
        view
        override(Governor, GovernorSettings)
        returns (uint256)
    {
        return super.votingDelay();
    }

    function votingPeriod()
        public
        view
        override(Governor, GovernorSettings)
        returns (uint256)
    {
        return super.votingPeriod();
    }

    function quorum(uint256 blockNumber)
        public
        view
        override(Governor, GovernorVotesQuorumFraction)
        returns (uint256)
    {
        return super.quorum(blockNumber);
    }

    function proposalThreshold()
        public
        view
        override(Governor, GovernorSettings)
        returns (uint256)
    {
        return super.proposalThreshold();
    }
    
}
