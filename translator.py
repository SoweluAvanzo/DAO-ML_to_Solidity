
"""

"""
import os
from DAOclasses import*
from simple_translator import*
from optimized_translator import*

class SolidityTranslator:
    def __init__(self, dao,translation_type):
        self.dao = dao
        self.translation_type = translation_type
        
    def translate(self):
        if self.translation_type == "simple":
            translator = SimpleSolidityTranslator(self.dao)
        elif self.translation_type == "optimized":
            translator = OptimizedSolidityTranslator(self.dao)
        else:
            raise ValueError("Invalid translation type")
        return translator.translate()
    def save_to_file(self):
        with open(f"{self.dao.dao_id}.sol", "w") as f:
            f.write(self.translate())
        print(f"Generated Solidity code saved to {self.dao.dao_id}.sol")