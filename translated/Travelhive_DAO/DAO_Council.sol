// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// @title DaoCouncil in Travelhive_DAO, using the optimistic_governance protocol


import "@openzeppelin/contracts/governance/Governor.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";

import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";

import "./interfaces/IPermissionManager.sol";


contract DaoCouncil is Governor, GovernorSettings, GovernorVotes, GovernorVotesQuorumFraction  {

    // State variables
    IPermissionManager public permissionManager;
    struct Proposal {
        bool vetoed;
        uint256 creationTime;
        bool executed;
    }

    uint256 public challengePeriod; // Duration of the challenge period
    mapping(uint256 => Proposal) public proposals; // Track the status of proposals

    // Constructor
    constructor(IVotes _token, address _permissionManager, uint256 _challengePeriod)
        Governor(DaoCouncil)
        GovernorSettings(7200 /* 1 day */, 50400 /* 1 week */, 0)
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(0)
    {
        permissionManager = IPermissionManager(_permissionManager); 
        challengePeriod = _challengePeriod; // Set the challenge period duration
    }

    function propose(address[] memory targets, uint256[] memory values, bytes[] memory calldatas, string memory description)
        public
        override
        returns (uint256)
    {
        require(permissionManager.canPropose(msg.sender, 18), "User cannot propose");
        uint256 proposalId = super.propose(targets, values, calldatas, description);
        // Create a new proposal in pending state, can be vetoed within the challenge period
        proposals[proposalId] = Proposal({
            vetoed: false,
            creationTime: block.timestamp,
            executed: false
        });

        return proposalId;
    }

    // Function to veto a proposal within the challenge period
    function vetoProposal(uint256 proposalId) public {
        require(permissionManager.canVote(msg.sender, 19), "User cannot vote");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.vetoed, "Proposal already vetoed");
        require(block.timestamp < proposal.creationTime + challengePeriod, "Challenge period expired");

        proposal.vetoed = true;
    }

    // Execute proposal optimistically after the challenge period if not vetoed
    function executeProposal(uint256 proposalId) public {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(block.timestamp >= proposal.creationTime + challengePeriod, "Challenge period not over");

        // If the proposal is vetoed, prevent execution
        require(!proposal.vetoed, "Proposal has been vetoed");

        // Execute the proposal using the inherited Governor functions
        super.execute(proposalId);

        proposal.executed = true;
    }

    // Override other Governor functions as necessary
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
