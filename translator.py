'''
from simple_translator import SimpleSolidityTranslator
from optimized_translator import OptimizedSolidityTranslator
'''

from DAOclasses import DAO, Committee, GraphType, Permission

class TranslatedSmartContract:
    def __init__(self, lines_of_code, name):
        self.lines_of_code = lines_of_code
        self.name = name
    def get_code_as_text(self) -> str:
        return "\n".join(self.lines_of_code)
    def get_code_as_lines(self) -> list[str]:
        return self.lines_of_code

    
class Translator:
    def translate(self) -> list[TranslatedSmartContract]:
        pass

'''
class SolidityTranslator_OLD(Translator):
    def __init__(self, source, translation_type, additional_metadata = None):
        self.source = source
        self.translation_type = translation_type
        self.additional_metadata = additional_metadata
        
    def translate(self) -> list[TranslatedSmartContract]:     
        if self.translation_type == "simple":
            translator = SimpleSolidityTranslator(self.source)
        elif self.translation_type == "optimized":
            translator = OptimizedSolidityTranslator(self.source)
        else:
            raise ValueError("Invalid translation type")
        return translator.translate()
    # def save_to_file(self):
    #     with open(f"{self.dao.dao_id}.sol", "w") as f:
    #         f.write(self.translate())
    #     print(f"Generated Solidity code saved to {self.dao.dao_id}.sol")
'''

class TranslationContext:
    def __init__(self, dao: DAO, role_declaration_policy = "index", solidity_version= "^0.8.0", daoOwner = True):
        self.dao = dao
        self.role_declaration_policy = role_declaration_policy
        self.solidity_version = solidity_version
        self.control_transitivity = dao.hierarchical_inheritance == 1 or dao.hierarchical_inheritance == "1"
        self.daoOwner = daoOwner


class CommitteeTranslator:
    def __init__(self, context: TranslationContext):
        self.context = context
        self.committee: Committee = None

    def generate_smart_contract_header(self, title_comment = "") -> list[str]:
        lines:list[str] = []
        lines.append("// SPDX-License-Identifier: MIT")
        lines.append(f"pragma solidity {self.context.solidity_version};")
        lines.append(title_comment)
        return lines
        
        
        
        
    def generate_contract_declaration(self, contract_name):
        return f"contract {contract_name} " + "{"
    

    def generate_import_statements(self) -> list[str]:
        imports = [
            'import "@openzeppelin/contracts/governance/Governor.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";'
        ]
        return imports

    def generate_contract_declaration(self, contract_name):
        return f"contract {contract_name}Voting is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction " + "{"

    def generate_constructor(self, contract_name):
        return [
            f"    constructor(IVotes _token)",
            f"        Governor(\"{contract_name}Voting\")",
            "        GovernorSettings(7200 /* 1 day */, 50400 /* 1 week */, 0)",
            "        GovernorVotes(_token)",
            "        GovernorVotesQuorumFraction(0)",
            "    {}"
        ]

    def generate_overrides(self) -> list[str]:
        overrides = [
            "    function votingDelay()",
            "        public",
            "        view",
            "        override(Governor, GovernorSettings)",
            "        returns (uint256)",
            "    {",
            "        return super.votingDelay();",
            "    }",
            "",
            "    function votingPeriod()",
            "        public",
            "        view",
            "        override(Governor, GovernorSettings)",
            "        returns (uint256)",
            "    {",
            "        return super.votingPeriod();",
            "    }",
            "",
            "    function quorum(uint256 blockNumber)",
            "        public",
            "        view",
            "        override(Governor, GovernorVotesQuorumFraction)",
            "        returns (uint256)",
            "    {",
            "        return super.quorum(blockNumber);",
            "    }",
            "",
            "    function proposalThreshold()",
            "        public",
            "        view",
            "        override(Governor, GovernorSettings)",
            "        returns (uint256)",
            "    {",
            "        return super.proposalThreshold();",
            "    }"
        ]
        return overrides

    def generate_closure(self):
        return "}"


    

    def translateCommittee(self,committee: Committee) -> TranslatedSmartContract:
        self.committee = committee
        contract_name = committee.committee_id + "Voting"
        lines:list[str] = []
        committee_delcaration_comment = f"// @title {contract_name} in DAO {self.context.dao.dao_id}"
        lines.extend(self.generate_smart_contract_header(committee_delcaration_comment))
        lines.extend(self.generate_import_statements())
        lines.append(self.generate_contract_declaration(contract_name))
        lines.extend(self.generate_constructor(contract_name))
        lines.extend(self.generate_overrides())
        lines.extend(self.generate_closure())
        # Join the lines to form the final contract
       
        name = committee.committee_id
        return TranslatedSmartContract(lines, name)