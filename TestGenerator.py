from DAOclasses import *
from jinja2 import Template
import os
import utils as u
from translator import *
from optimized_translator import *

class TestGeneratorOptimized:
    def __init__(self, dao: DAO):
        translator = OptimizedSolidityTranslator(dao)
        translator.translate()
        self.dao = dao
        self.context = translator.context         
        self.roles_to_final_index = translator.role_to_final_index
        self.address_dict = {}
        print(self.roles_to_final_index)
        
    def generate_test_script(self, folder_template_path: str) -> list[TranslatedSmartContract]:
        return [\
            self.generate_test_from_template(folder_template_path, "test_3") \
                ] # TODO: add the other tests, if any
    
    def generate_test_from_template(self, template_path: str, name: str, output_folder="test", extension=".js") -> TranslatedSmartContract:
        # Define the full path to the template file
        file_name_and_path = template_path + name + extension + ".jinja"
        # Initialize an empty list to store each rendered line
        rendered_lines = []
        addresses_list = self.generate_address_list()
        addressesByEntityValue = self.generate_addresses_by_entity_value()
        owner_id_bitmask = self.roles_to_final_index[ self.dao.owner_role.role_id]
        owner_role_value = owner_id_bitmask

        with open(file_name_and_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
            template = Template(template_content)
            rendered_lines = template.render(
                solidity_version=self.context.solidity_version,
                addresses_list=addresses_list,
                addressesByEntityValue=addressesByEntityValue,
                owner=owner_id_bitmask,
                DAO_name=self.dao.dao_name.replace(" ", "_"),
                owner_role_value=owner_role_value,
                control_relation_results=self.generate_control_tests_expected_results()
            ).splitlines()

        # Return a TranslatedSmartContract object with the list of rendered lines
        return TranslatedSmartContract(rendered_lines, self.context.dao.dao_name + "_test", folder=output_folder, extension=extension)
    
    def generate_address_dict(self) -> None:
        self.address_dict = {f"{role.role_id}": f"{role.role_name.replace(" ","_")}Address" for role in self.dao.roles.values()}
        
    
    def generate_address_list(self) -> list[str]:
        return [ f"addr{i +1}" for i in range(len(self.dao.roles) + len(self.dao.committees) -1) ]

    def generate_addresses_by_entity_value(self) -> dict[int, str]:
        abEV = {}
        owner_role = self.dao.owner_role
        address_role = "owner"
        owner_id = owner_role.role_id
        abEV[ self.roles_to_final_index[ owner_id] ] = address_role

        i = 1
        for id in self.dao.roles.keys():
            if owner_id != id:
                abEV[ self.roles_to_final_index[ id ] ] = f"addr{i}"
                i += 1
        for id in self.dao.committees.keys():
            abEV[ self.roles_to_final_index[ id ] ] = f"addr{i}"
            i += 1
        return abEV
    
    def generate_control_tests_expected_results(self) -> list[tuple[int, int, bool]]:
        entities = [*self.dao.roles.values(), *self.dao.committees.values()]
        controlledBy = {entity.get_id(): set(entity.controllers) for entity in entities}
        return [(self.roles_to_final_index[entity.get_id()], self.roles_to_final_index[controlled_entity.get_id()], entity.get_id() in controlledBy[controlled_entity.get_id()]) for entity in entities for controlled_entity in entities]
        
