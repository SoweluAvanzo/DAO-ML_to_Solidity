'''
from simple_translator import SimpleSolidityTranslator
from optimized_translator import OptimizedSolidityTranslator
'''

from DAOclasses import DAO, Committee, GraphType, Permission
from jinja2 import Template
import os
import utils as u

class TranslatedSmartContract:
    def __init__(self, lines_of_code, name, folder = None):
        self.lines_of_code = lines_of_code
        self.name = name
        self.folder = folder
    def get_code_as_text(self) -> str:
        return "\n".join(self.lines_of_code)
    def get_code_as_lines(self) -> list[str]:
        return self.lines_of_code
    

class Translator:
    def translate(self) -> list[TranslatedSmartContract]:
        pass

    def generate_file_from_template(self, template_path: str, name: str, output_folder: str, extension=".sol") -> TranslatedSmartContract:
        # Define the full path to the template file
        
        file_name_and_path = template_path + name + extension + ".jinja"
        
        # Initialize an empty list to store each rendered line
        rendered_lines = []

        # Open the template file and read it line by line
        with open(file_name_and_path, 'r', encoding='utf-8') as f:
            # For each line in the template, render it individually
            for line in f:
                # Create a Jinja2 template object for each line
                template = Template(line)
                # Render the line with any dynamic content (e.g., Solidity version)
                rendered_line = template.render(solidity_version=self.context.solidity_version)
                # Append the rendered line to the list of rendered lines
                rendered_lines.append(rendered_line)
        if extension == ".sol":
        # Return a TranslatedSmartContract object with the list of rendered lines
            return TranslatedSmartContract(rendered_lines, name, folder=output_folder)

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
    def __init__(self, dao: DAO, role_declaration_policy = "topological_order", solidity_version= "^0.8.0", daoOwner = True):
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
        
        
    def get_voting_protocol_list(self):
        directory_path = './Templates/voting_protocols'

        # Get a list of all files and directories
        items = os.listdir(directory_path)
        for item in items:
            # Check if the item is a file
            if os.path.isfile(item):

                # Print the item name
                print(item)
        return items
        #generate_voting_protocol_from_template(decision_making_method, state_var_declarations, dao_name, imports, constructor_parameters, inherited_contracts,  constructor_actions, vote_requirement, proposal_requirement, template_path, name= contract_name, output_folder="", extension=".sol"))
    
    def generate_voting_protocol_from_template(self, committee_name, decision_making_method_name, 
                                           state_var_declarations = " ", dao_name =" ", imports = " ", 
                                           constructor_parameters=" ", inherited_contracts= " ", 
                                           constructor_actions =" ", vote_requirement= " ", 
                                           proposal_requirement =" ", template_path : str="Templates/voting_protocols/", 
                                           name: str= "", output_folder: str ="", extension=".sol", custom=False) -> list[str]:
            # Define the full path to the template file
            if custom == False:
                file_name_and_path = template_path + decision_making_method_name + extension + ".jinja"
            else:
                file_name_and_path = template_path + "custom_decision_making_template" + extension + ".jinja"
            
            # Initialize an empty list to store the rendered result
            rendered_lines = []
            
            # Open the template file and read it all at once
            with open(file_name_and_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            # Create a Jinja2 template object for the whole content
            template = Template(template_content)
            
            # Render the template with all dynamic variables
            rendered_content = template.render(
                contract_name=u.camel_case(committee_name), 
                solidity_version=self.context.solidity_version,decision_making_method_name = decision_making_method_name,
                state_var_declarations=state_var_declarations,
                dao_name=dao_name,
                imports=imports,
                constructor_parameters=constructor_parameters,
                inherited_contracts=inherited_contracts,
                constructor_actions=constructor_actions,
                vote_requirement=vote_requirement,
                proposal_requirement=proposal_requirement
            )
            rendered_lines = rendered_content.splitlines() 
            return rendered_lines


    def generate_contract_declaration(self, contract_name):
        return f"contract {contract_name} " + "{"
    
    

    def generate_import_statements(self) -> list[str]:
        imports = [
            'import "@openzeppelin/contracts/governance/Governor.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";',
            'import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";',
            'import "./interfaces/IPermissionManager.sol";'
        ]
        return imports

    # def generate_contract_declaration(self, contract_name):
    #     return f"contract {contract_name}Voting is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction, IPermissionManager " + "{"
    
    # def generate_IPermissionManager_reference(self):
    #     return f"IPermissionManager public permissionManager;"
    
    # def generate_constructor(self, contract_name):
    #     return f"""
    #     constructor(IVotes _token, address _permissionManager)
    #     Governor(\"{contract_name}Voting\")
    #     GovernorSettings(7200 /* 1 day */, 50400 /* 1 week */, 0)
    #     GovernorVotes(_token)
    #     GovernorVotesQuorumFraction(0)
    #     {{
    #         permissionManager = IPermissionManager(_permissionManager); 
    #     }}
    #         """
    

    # def generate_overrides(self, voting_permission_index=None, proposal_permission_index=None):
    #        return f""" 
    #        // Override voting logic to include permission check before voting
    #         function castVote(uint256 proposalId, uint8 support)
    #             public
    #             override
    #             returns (uint256)
    #         {{
    #         // Check if the msg.sender has permission to vote before allowing them to cast a vote
    #         require(permissionManager.canVote(msg.sender, {voting_permission_index}), "PermissionManager: User cannot vote");
            
    #         return super.castVote(proposalId, support);
    #         }}

    #         // Override proposal logic to include permission check before proposing
    #         function propose(address[] memory targets, uint256[] memory values, bytes[] memory calldatas, string memory description)
    #             public
    #             override
    #             returns (uint256)
    #         {{
    #         require(permissionManager.canPropose(msg.sender, {proposal_permission_index}), "User cannot propose");
            
    #         return super.propose(targets, values, calldatas, description);
    #         }}

    #         // Override Governor functions with the inherited implementations
    #         function votingDelay()
    #             public
    #             view
    #             override(Governor, GovernorSettings)
    #             returns (uint256)
    #         {{
    #         return super.votingDelay();
    #         }}

    #         function votingPeriod()
    #             public
    #             view
    #             override(Governor, GovernorSettings)
    #             returns (uint256)
    #         {{
    #             return super.votingPeriod();
    #         }}

    #         function quorum(uint256 blockNumber)
    #             public
    #             view
    #             override(Governor, GovernorVotesQuorumFraction)
    #             returns (uint256)
    #         {{
    #             return super.quorum(blockNumber);
    #         }}

    #         function proposalThreshold()
    #             public
    #             view
    #             override(Governor, GovernorSettings)
    #             returns (uint256)
    #         {{
    #             return super.proposalThreshold();
    #         }}
    
    #     """
        

    # def generate_closure(self):
    #     return "}"


    def translateCommittee(self,committee: Committee, voting_permission_index=None, proposal_permission_index=None, decision_making_method=None,optimized=False ) -> TranslatedSmartContract:
        self.committee = committee
        contract_name = committee.committee_id 
        decision_making_method = committee.decision_making_method
        lines:list[str] = []
        #committee_delcaration_comment = f"// @title {contract_name} in DAO {self.context.dao.dao_id}, using the voting protocol: {committee.decision_making_method}"
        #generate the voting protocol contract from a template
        template_path = "Templates/voting_protocols/"
        vote_requirement = f'require(permissionManager.canVote(msg.sender, {voting_permission_index}), "User cannot vote");' if optimized else f'require(permissionManager.isCommitteeMember(msg.sender, {voting_permission_index})==1, "User cannot vote");'
        proposal_requirement = f'require(permissionManager.canPropose(msg.sender, {proposal_permission_index}), "User cannot propose");' if optimized else f'require(permissionManager.isCommitteeMember(msg.sender, {proposal_permission_index})==2, "User cannot propose");'
        state_var_declarations = "IPermissionManager public permissionManager;"
        constructor_actions= "permissionManager = IPermissionManager(_permissionManager); "
        inherited_contracts=", IPermissionManager"
        name = committee.committee_id
        constructor_parameters = ", address _permissionManager"
        imports=self.generate_import_statements()
        dao_name= self.context.dao.dao_id
        if decision_making_method == None:
            decision_making_method = "custom_decision_making_method"
        template_name = decision_making_method + ".sol.jinja"
        if template_name in self.get_voting_protocol_list():
            lines.extend(self.generate_voting_protocol_from_template(committee_name=committee.committee_id, decision_making_method_name=decision_making_method, state_var_declarations= state_var_declarations,dao_name= dao_name,imports= imports, constructor_parameters= constructor_parameters, inherited_contracts=inherited_contracts, constructor_actions= constructor_actions,vote_requirement= vote_requirement, proposal_requirement=proposal_requirement, template_path=template_path, name= contract_name, output_folder="", extension=".sol"))
        else:
            #print(f"Voting protocol {committee.decision_making_method} not found in folder {template_path}")
            lines.extend(self.generate_voting_protocol_from_template(committee_name=committee.committee_id, decision_making_method_name=committee.decision_making_method,dao_name= dao_name, template_path=template_path, name= contract_name, custom=True))
        # lines.extend(self.generate_smart_contract_header(committee_delcaration_comment))
        # lines.extend(self.generate_import_statements())
        # lines.append(self.generate_contract_declaration(contract_name))
        # lines.append(self.generate_IPermissionManager_reference())
        # lines.append(self.generate_constructor(contract_name))
        # lines.append(self.generate_overrides(voting_permission_index, proposal_permission_index))
        # lines.append(self.generate_closure())
        # Join the lines to form the final contract
        #voting protocol translation: 
        return TranslatedSmartContract(lines, name)
    

class CommitteeTranslatorDiamond(CommitteeTranslator):
    def __init__(self, context: TranslationContext):
        super().__init__(context)

        
    def translateCommittee(self,committee: Committee) -> TranslatedSmartContract:
        self.committee = committee
        contract_name = committee.committee_id + "Voting" + "Facet"
        lines:list[str] = []
        committee_delcaration_comment = f"// @title {contract_name} in DAO {self.context.dao.dao_id}"
        lines.extend(self.generate_smart_contract_header(committee_delcaration_comment))
        lines.extend(self.generate_import_statements())
        lines.append(self.generate_contract_declaration(contract_name))
        #lines.extend(self.generate_constructor(contract_name))
        lines.extend(self.generate_overrides())
        lines.extend(self.generate_closure())
        folder = "facets"
        return TranslatedSmartContract(lines, contract_name, folder=folder)
    



    # def generate_library_declaration(self, lib_type, comment = ""):
    #     lines:list[str] = []
    #     lines.append(comment)
    #     lines.append(f"library Lib{lib_type} {'{'}")
    #     return lines
    
    # def generate_library_header(self):
    #     lines = []
    #     lines.append("// SPDX-License-Identifier: MIT")
    #     lines.append(f"pragma solidity {self.context.solidity_version};")
    #     return lines
    

    # def translateCommittee(self,committee: Committee) -> TranslatedSmartContract:
    #     self.committee = committee
    #     contract_name = committee.committee_id + "Voting"
    #     lines:list[str] = []
    #     committee_delcaration_comment = f"// @title Committee {self.committee.committee_id} in DAO {self.context.dao.dao_id}"
    #     lines.extend(self.generate_library_header())
    #     lines.extend(self.generate_import_statements())
    #     lines.extend(self.generate_library_declaration(contract_name, committee_delcaration_comment))
    #     lines.extend(self.generate_overrides())
    #     lines.extend(self.generate_closure())
        # name = committee.committee_id
        # folder = "libraries"
        # return TranslatedSmartContract(lines, name, folder=folder)

