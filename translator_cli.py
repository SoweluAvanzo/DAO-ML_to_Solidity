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

if __name__ is not None and "." in __name__:
    from .XMLLexer import XMLLexer
    from .XMLParser import XMLParser
else:
    from XMLLexer import XMLLexer
    from XMLParser import XMLParser

def check_and_make_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    


def save_json(daos, folder_path=None):
    folder = "./out/json/daos" if folder_path is None else folder_path
    check_and_make_folder(folder)
    for dao in daos.values():
        filename = f"{folder}/dao_{dao.dao_name}.json"
        with open(filename, "w") as f:
            json.dump(dao.toJSON(), f)
    #print("Success", "DAO properties have been saved to JSON files")


class TranslationData:
    def __init__(self, folder_name, contract_name, contract_translator) -> None:
        self.folder_name = folder_name
        self.contract_name = contract_name
        self.contract_translator = contract_translator
        
def translate(xml_file, translation_logic):
    
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
        #visitor.visit(tree)
        #save_json(diagram_manager.daoByID)
        contracts_to_write: list[TranslationData] = []
        # at first, gather all translators

        for dao_id in diagram_manager.daoByID.keys():
            dao = diagram_manager.get_dao_by(dao_id)
            # the translator uses the selected translation logic
            #if diamond_enabled.get()==True:
            #    translator = SolidityTranslator(dao, translation_logic.get(), diamond=True)  
            #elif diamond_enabled.get()==False:
            translator = SolidityTranslator(dao, translation_logic, diamond=False)
            #else:
            #    print("error with diamond configuration: ", diamond_enabled)
            contracts_to_write.append(TranslationData(dao_id, dao_id, translator))
            # each committee is a Smart Contract by its own
            '''
            for committee in dao.committees.values():
                translator = SolidityTranslator(committee, translation_logic.get())
                contracts_to_write.append(TranslationData(dao_id, committee.committee_id, translator) )
            '''

        # then, translate each Smart Contract into its translated version
        for translation_data in contracts_to_write:
            superfolder_name = "./translated/"
            folder_name = translation_data.folder_name
            name = translation_data.contract_name
            translator = translation_data.contract_translator

            folder_path = f'{superfolder_name}/{folder_name}'
            check_and_make_folder(folder_path)

            translated_smart_contracts = translator.translate()
            for tsc in translated_smart_contracts:
                if tsc is not None:
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
                
        dao_ids = ", ".join(td.contract_name for td in contracts_to_write) + ".sol"
        print("Success", f"Solidity code has been generated for {dao_ids}")

    except Exception as e:
        traceback.print_exception(e)
        print("Error", f"An error occurred: {e}")

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
              
def main(argv):
    
    if len(argv) < 3:
        print("Error", "Please enter the function you wish to call (translate, to_json) followed by XML file name. You can also select the translation logic (simple or optimized)")
        return
    xml_file = argv[2]
    if argv[1]=="translate":
        translation_logic= argv[3] if len(argv) > 3 else "simple"
        translate(xml_file, translation_logic)
    elif argv[1]=="to_json":
        print_json(xml_file)
    else:
        print("Error", "Invalid function name. Please, enter translate followed by the xml file path, or to_json followed by the XML file path. to execute the desired action")
        
if __name__ == '__main__':
    main(sys.argv)