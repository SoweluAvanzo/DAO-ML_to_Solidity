from translator import Translator, TranslatedSmartContract
from simple_translator import SimpleSolidityTranslator
from optimized_translator import OptimizedSolidityTranslator
from optimized_diamond_translator import OptimizedDiamondTranslator


class VotingProtocolTranslator(Translator):
    '''
    IL TEMPLATE

    // SPDX-License-Identifier: MIT
    // Compatible with OpenZeppelin Contracts ^5.0.0
    pragma solidity ^0.8.20;

    import "@openzeppelin/contracts@5.0.2/governance/Governor.sol";
    import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorSettings.sol";
    import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorCountingSimple.sol";
    import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorVotes.sol";
    import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorVotesQuorumFraction.sol";
    import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorTimelockControl.sol";

    contract MyGovernor is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction, GovernorTimelockControl {
        constructor(IVotes _token, TimelockController _timelock)
            Governor("MyGovernor")
            GovernorSettings(7200 /* 1 day */, 50400 /* 1 week */, 0)
            GovernorVotes(_token)
            GovernorVotesQuorumFraction(4)
            GovernorTimelockControl(_timelock)
        {}

        // The following functions are overrides required by Solidity.

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

        function state(uint256 proposalId)
            public
            view
            override(Governor, GovernorTimelockControl)
            returns (ProposalState)
        {
            return super.state(proposalId);
        }

        function proposalNeedsQueuing(uint256 proposalId)
            public
            view
            override(Governor, GovernorTimelockControl)
            returns (bool)
        {
            return super.proposalNeedsQueuing(proposalId);
        }

        function proposalThreshold()
            public
            view
            override(Governor, GovernorSettings)
            returns (uint256)
        {
            return super.proposalThreshold();
        }

        function _queueOperations(uint256 proposalId, address[] memory targets, uint256[] memory values, bytes[] memory calldatas, bytes32 descriptionHash)
            internal
            override(Governor, GovernorTimelockControl)
            returns (uint48)
        {
            return super._queueOperations(proposalId, targets, values, calldatas, descriptionHash);
        }

        function _executeOperations(uint256 proposalId, address[] memory targets, uint256[] memory values, bytes[] memory calldatas, bytes32 descriptionHash)
            internal
            override(Governor, GovernorTimelockControl)
        {
            super._executeOperations(proposalId, targets, values, calldatas, descriptionHash);
        }

        function _cancel(address[] memory targets, uint256[] memory values, bytes[] memory calldatas, bytes32 descriptionHash)
            internal
            override(Governor, GovernorTimelockControl)
            returns (uint256)
        {
            return super._cancel(targets, values, calldatas, descriptionHash);
        }

        function _executor()
            internal
            view
            override(Governor, GovernorTimelockControl)
            returns (address)
        {
            return super._executor();
        }
    }

    
    '''

    def generateHeader(self) -> list[str]:
        return [
            '// SPDX-License-Identifier: MIT',
            '// Compatible with OpenZeppelin Contracts ^5.0.0'
            'pragma solidity ^0.8.20;'
        ]


    def generateImport(self) -> list[str]:
        return [
            'import "@openzeppelin/contracts@5.0.2/governance/Governor.sol";',
            'import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorSettings.sol";',
            'import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorCountingSimple.sol";',
            'import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorVotes.sol";',
            'import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorVotesQuorumFraction.sol";',
            'import "@openzeppelin/contracts@5.0.2/governance/extensions/GovernorTimelockControl.sol";',
        ]

   
    
    def translate(self) -> list[TranslatedSmartContract]:
        lines:list[str] = []

        lines.extend(self.generateHeader())
        lines.extend(self.generateImport())

        # TODO : generare le altre parti mancanti

        name = "MyGovernor_VOTING_PROTOCOL" # TODO : scegliere un nome migliore ....
        return [TranslatedSmartContract(lines, name)]



class SolidityTranslator(Translator):
    def __init__(self, dao, translation_type, additional_metadata = None, diamond=False):
        self.dao = dao
        self.translation_type = translation_type
        self.additional_metadata = additional_metadata
        self.diamond = diamond
        
    def translate(self) -> list[TranslatedSmartContract]:

        # voting_protocol_translator = VotingProtocolTranslator() #TODO: instanziare il traduttore del protocollo di voto
        group_size = self.dao.metadata.user_functionalities_group_size
        if self.translation_type == "simple" or group_size == None:
            translator = SimpleSolidityTranslator(self.dao) # , voting_protocol_translator)
        elif self.translation_type == "optimized":
            if self.diamond == True:
                translator = OptimizedDiamondTranslator(self.dao)
            else:
                translator = OptimizedSolidityTranslator(self.dao) # , voting_protocol_translator)
        else:
            raise ValueError("Invalid translation type")
        return translator.translate()
    # def save_to_file(self):
    #     with open(f"{self.dao.dao_id}.sol", "w") as f:
    #         f.write(self.translate())
    #     print(f"Generated Solidity code saved to {self.dao.dao_id}.sol")


