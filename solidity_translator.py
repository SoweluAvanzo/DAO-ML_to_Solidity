from translator import Translator, TranslatedSmartContract
from simple_translator import SimpleSolidityTranslator
from optimized_translator import OptimizedSolidityTranslator
from optimized_diamond_translator import OptimizedDiamondTranslator


class VotingProtocolTranslator(Translator):

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
        # set the translator that these parameters are enforcing
        self.translator_proxy:Translator = None
        # voting_protocol_translator = VotingProtocolTranslator() #TODO: instanziare il traduttore del protocollo di voto
        group_size = self.dao.metadata.user_functionalities_group_size
        if self.translation_type == "simple" or group_size == None:
            self.translator_proxy = SimpleSolidityTranslator(self.dao) # , voting_protocol_translator)
        elif self.translation_type == "optimized":
            if self.diamond == True:
                self.translator_proxy = OptimizedDiamondTranslator(self.dao)
            else:
                self.translator_proxy = OptimizedSolidityTranslator(self.dao) # , voting_protocol_translator)
        else:
            raise ValueError("Invalid translation type")
        # continue to mimic the proxy by overriding all this instances' values with the proxy ones
        self.context = self.translator_proxy.context

    def translate(self) -> list[TranslatedSmartContract]:
        # call the pre-calculated proxy
        return self.translator_proxy.translate()
    

