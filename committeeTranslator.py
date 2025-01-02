# from DAOclasses import Committee
# from translator import *
# class CommitteeTranslator:
#     def __init__(self, context: TranslationContext):
#         self.context = context
#         self.committee: Committee = None

#     def generate_smart_contract_header(self, title_comment = "") -> list[str]:
#         lines:list[str] = []
#         lines.append("// SPDX-License-Identifier: MIT")
#         lines.append(f"pragma solidity {self.context.solidity_version};")
#         lines.append(title_comment)
#         return lines
        
        
        
        
#     def generate_contract_declaration(self, contract_name):
#         return f"contract {contract_name} " + "{"
    

#     def generate_import_statements(self) -> list[str]:
#         imports = [
#             'import "@openzeppelin/contracts/governance/Governor.sol";',
#             'import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";',
#             'import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";',
#             'import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";',
#             'import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";'
#         ]
#         return imports

#     def generate_contract_declaration(self, contract_name):
#         return f"contract {contract_name}Voting is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction " + "{"

#     def generate_constructor(self, contract_name):
#         return [
#             f"    constructor(IVotes _token)",
#             f"        Governor(\"{contract_name}Voting\")",
#             "        GovernorSettings(7200 /* 1 day */, 50400 /* 1 week */, 0)",
#             "        GovernorVotes(_token)",
#             "        GovernorVotesQuorumFraction(0)",
#             "    {}"
#         ]

#     def generate_overrides(self) -> list[str]:
#         overrides = [
#             "    function votingDelay()",
#             "        public",
#             "        view",
#             "        override(Governor, GovernorSettings)",
#             "        returns (uint256)",
#             "    {",
#             "        return super.votingDelay();",
#             "    }",
#             "",
#             "    function votingPeriod()",
#             "        public",
#             "        view",
#             "        override(Governor, GovernorSettings)",
#             "        returns (uint256)",
#             "    {",
#             "        return super.votingPeriod();",
#             "    }",
#             "",
#             "    function quorum(uint256 blockNumber)",
#             "        public",
#             "        view",
#             "        override(Governor, GovernorVotesQuorumFraction)",
#             "        returns (uint256)",
#             "    {",
#             "        return super.quorum(blockNumber);",
#             "    }",
#             "",
#             "    function proposalThreshold()",
#             "        public",
#             "        view",
#             "        override(Governor, GovernorSettings)",
#             "        returns (uint256)",
#             "    {",
#             "        return super.proposalThreshold();",
#             "    }"
#         ]
#         return overrides

#     def generate_closure(self):
#         return "}"


    

#     def translateCommittee(self,committee: Committee) -> TranslatedSmartContract:
#         self.committee = committee
#         contract_name = committee.committee_id + "Voting"
#         lines:list[str] = []
#         committee_delcaration_comment = f"// @title {contract_name} in DAO {self.context.dao.dao_id}, using the voting protocol: {committee.decision_making_method}"
#         lines.extend(self.generate_smart_contract_header(committee_delcaration_comment))
#         lines.extend(self.generate_import_statements())
#         lines.append(self.generate_contract_declaration(contract_name))
#         lines.extend(self.generate_constructor(contract_name))
#         lines.extend(self.generate_overrides())
#         lines.extend(self.generate_closure())
#         # Join the lines to form the final contract
       
#         name = committee.committee_id
#         return TranslatedSmartContract(lines, name)