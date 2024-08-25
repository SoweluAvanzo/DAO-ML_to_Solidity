'''
from simple_translator import SimpleSolidityTranslator
from optimized_translator import OptimizedSolidityTranslator
'''


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
