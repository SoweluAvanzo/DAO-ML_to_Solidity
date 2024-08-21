
"""

"""
import os
from DAOclasses import*
from simple_translator import*
from optimized_translator import*
from enum import Enum


class ContractSourcetype (Enum):
    DAO = 1
    COMMITTEE = 2
    
class SolidityTranslator:
    def __init__(self, source, source_type: ContractSourcetype, translation_type, additional_metadata = None):
        self.source_type = source_type
        self.source = source
        self.translation_type = translation_type
        self.additional_metadata = additional_metadata
        
    def translate(self):
        if self.source_type != ContractSourcetype.DAO:
            return None
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