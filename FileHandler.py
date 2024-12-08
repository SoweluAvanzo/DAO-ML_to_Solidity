import sys
import json
import os
import traceback
from XMLValidator import ConstraintValidator

from antlr4 import *
from XMLLexer import XMLLexer
from XMLParser import XMLParser

#from parse_xml import DAO_ML_Visitor
from DAOVisitor2 import DAOVisitor2
#from translator import ContractSourcetype
from DiagramManager import DiagramManager
from solidity_translator import SolidityTranslator
import utils as u
from TestGenerator import *
from DAO_simulator import *
from translator import TranslatedSmartContract, Translator

if __name__ is not None and "." in __name__:
    from .XMLLexer import XMLLexer
    from .XMLParser import XMLParser
else:
    from XMLLexer import XMLLexer
    from XMLParser import XMLParser

def check_and_make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_base_folder(folder_base):
    return folder_base if folder_base != None else os.getcwd()

def concat_folder_filename(*parts):
    return os.path.join(parts)


def save_json(daos, folder_path=None):
    folder = "./out/json/daos" if folder_path is None else folder_path
    check_and_make_folder(folder)
    for dao in daos.values():
        filename = f"{folder}/dao_{u.camel_case(dao.dao_name)}.json"
        with open(filename, "w") as f:
            json.dump(dao.toJSON(), f)
    #print("Success", "DAO properties have been saved to JSON files")


class TranslationData:
    def __init__(self, folder_name:str, contract_name:str, contract_translator:Translator, tests_translator:TestGeneratorOptimized) -> None:
        self.folder_name:str = folder_name
        self.contract_name:str = contract_name
        self.contract_translator:Translator = contract_translator
        self.tests_translator:TestGeneratorOptimized = tests_translator
        
def translate_SCs(xml_file, translation_logic):
    
    try:
        # PARTE 1) LETTURA XML

        condition_validator = ConstraintValidator(xml_file, "data/XSD_DAO_ML.xsd")
        condition_validator.validate_dao_ml_diagram()
        input_stream = FileStream(xml_file)
        lexer = XMLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = XMLParser(stream)
        tree = parser.document()

        visitor = DAOVisitor2()

        # PARTE 2) Dato l'input, CREARE ISTANZA DI "DiagramManager"
        diagram_manager = DiagramManager()
        visitor.parseDiagramTree(tree, diagram_manager)

        print(f"\n\n________ DIAGRAM MANAGER CREATED _____\n\n")

        # PARTE 3, ... ) GENERAZIONE ".sol", dei test, e dell'output .. INSOMMA, TUTTO IL RESTO

        #visitor.visit(tree)
        #save_json(diagram_manager.daoByID)
        contracts_to_write: list[TranslationData] = []
        # at first, gather all translators
        
        superfolder_name = "./translated/"

        for dao_id in diagram_manager.daoByID.keys():
            dao = diagram_manager.get_dao_by(dao_id)
            dao_name = dao.dao_name
            # the translator uses the selected translation logic
            #if diamond_enabled.get()==True:
            #    translator = SolidityTranslator(dao, translation_logic.get(), diamond=True)  
            #elif diamond_enabled.get()==False:
            translator = SolidityTranslator(dao, translation_logic , diamond=False)
            #else:
            #    print("error with diamond configuration: ", diamond_enabled)
            tests_translator = TestGeneratorOptimized(dao, translation_logic == 'optimized', translator)
            contracts_to_write.append(TranslationData(dao_name, dao_name, translator, tests_translator))
             
            #contracts_to_write.extend(all_translated_smart_contract__tests)
            
            # each committee is a Smart Contract by its own
        # then, translate each Smart Contract into its translated version
        write_SCs(contracts_to_write,superfolder_name)
    
    except Exception as e:
        traceback.print_exception(e)
        print("Error", f"An error occurred: {e}")
        

def write_SCs(contracts_to_write:list[TranslationData],superfolder_name):
        for translation_data in contracts_to_write:
            folder_name = translation_data.folder_name
            name = translation_data.contract_name
            translator = translation_data.contract_translator

            folder_path = f'{superfolder_name}/{folder_name}'
            check_and_make_folder(folder_path)

            translated_smart_contracts = translator.translate()
            
            for tsc in translated_smart_contracts:
                if tsc is not None and tsc.testable:
                    if tsc.folder is not None:
                        folder_path_with_subfolder = f'{folder_path}/{tsc.folder}'
                        check_and_make_folder(folder_path_with_subfolder)
                    else:
                        folder_path_with_subfolder = folder_path
                    solidity_code = tsc.get_code_as_lines()
                    if solidity_code is not None:
                        try:
                            filename = tsc.name + ".sol"
                            full_path = f'{folder_path_with_subfolder}/{filename}'

                            with open(full_path, 'w') as f:
                                for line in solidity_code:
                                    f.write(line)
                                    f.write('\n')
                                    f.flush()
                        except Exception as ex:
                            print(f"Exception while writing the source code of {name}")
                            print(ex)
                            print("the solidity code:")
                            for line in solidity_code:
                                if isinstance(line, str):
                                    print(line)
                                else:
                                    print("Error".join(line))
                                    
                        #test_folder = f"{folder_path_with_subfolder}/tests"
                        test_folder = "./Templates/test_scripts/"
                        check_and_make_folder(test_folder)
                        try:
                            all_translated_smart_contract__tests = translation_data.tests_translator.generate_test_script(test_folder) #test_template_path)
                            for t in all_translated_smart_contract__tests:
                                try:
                                    check_and_make_folder(t.folder)
                                    with open( f"{t.folder}/{t.name}{t.extension}", "w") as f:
                                        for line in t.lines_of_code:
                                            f.write(line)
                                            f.write('\n')
                                            f.flush()
                                except Exception as ex:
                                    print(f"Exception while writing the source code of test {t.name}")
                                    print(ex)
                                    traceback.print_exception(ex)
                        except Exception as ee:
                            print(f"Exception while writing TESTS for '{tsc.name}'")
                            print(f"{tsc.name} is {tsc}")
                            print(ee)
                            traceback.print_exception(ee)
                
        dao_ids = ", ".join(td.contract_name for td in contracts_to_write) + ".sol"
        print("Success", f"Solidity code has been generated for {dao_ids}")

def generate_simulations(n_daos=3, n_roles=20, n_permissions=35, sparsity_coefficient=0.4, permissions_per_role=3):
    #steps for generating dao scs: 
# initialize the DAOGenerator: _init__(self,n_daos:int, n_roles: int, n_permissions: int, sparsity_coefficient: float, permissions_per_role, Translator: Translator)
# initialize DAOSimulator:  __init__(self, translator: SolidityTranslator, test_generator: TestGeneratorOptimized)
# DAOGenerator obj.generate_daos
# DAOSimulator obj.translate_daos
    dao_gen = DAOGenerator(n_daos, n_roles, n_permissions, sparsity_coefficient, permissions_per_role)
    dao_gen.generate_daos()
    daos = dao_gen.get_daos()
    contracts_to_write = []
    for dao in daos:
            dao_name = dao.dao_name
            # the translator uses the selected translation logic
            #if diamond_enabled.get()==True:
            #    translator = SolidityTranslator(dao, translation_logic.get(), diamond=True)  
            #elif diamond_enabled.get()==False:
            translator = SolidityTranslator(dao, "optimized", diamond=False)
            #else:
            #    print("error with diamond configuration: ", diamond_enabled)
            tests_translator = TestGeneratorOptimized(dao, True, translator)
            translation_data = TranslationData(dao_name, dao_name, translator, tests_translator)
            contracts_to_write.append(translation_data)
            print(contracts_to_write)
    return contracts_to_write

def print_json(xml_file):
    folder = "./out/json"
    check_and_make_folder(folder)

    if not xml_file:
        print("Error", "Please enter the XML file name.")
        return None

    try:
        condition_validator = ConstraintValidator(xml_file, "data/XSD_DAO_ML.xsd")
        condition_validator.validate_dao_ml_diagram()
        input_stream = FileStream(xml_file)
        lexer = XMLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = XMLParser(stream)
        tree = parser.document()
        visitor = DAOVisitor2()
        diagram_manager = DiagramManager()        
        visitor.parseDiagramTree(tree, diagram_manager)
        save_json(diagram_manager.daoByID)
        print("Success", "DAO properties have been saved to JSON files")
    except Exception as e:
        traceback.print_exception(e)
        print("Error", f"An error occurred: {e}")