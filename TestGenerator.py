from DAOclasses import *
from jinja2 import Template
import os
import utils as u
from translator import *
from optimized_translator import *
from simple_translator import *

class TestGeneratorOptimized:
    # NOTA 3: questa classe deve trovarsi in coda alla pipelone (lettura/parsing -> DiagramManager -> traduzione ".sol" -> test)
    def __init__(self, dao: DAO, optimized = False, translator:Translator=None):
        self.optimized = optimized
        #if optimized:
        #    translator = OptimizedSolidityTranslator(dao)
        #else:
        #    translator = SimpleSolidityTranslator(dao)
            
       
        #translator.translate() # NOTA 1: la sua UNICA utilita e' quella di riempire "translator.context.entity_to_data"
        self.dao = dao
        self.context = translator.context

        # NOTA 2: a questa classe serve una DAO gia' tradotta, in quanto ha i dati gia' preparati

        self.entity_to_data = translator.context.entity_to_data  # dict entity_id -> {"final_id": int, "name": str, "index": int, "original_id": str}
        self.address_dict = {}
        
    def generate_test_script(self, folder_template_path: str) -> list[TranslatedSmartContract]:
        if self.optimized:
            script_name = "optimized_test_script_template"  
        else:
            script_name = "standard_test_script_template"
        return [\
            self.generate_test_from_template(folder_template_path, script_name) \
                ] # TODO: add the other tests, if any
    
    def generate_test_from_template(self, template_path: str, name: str, output_folder="test", extension=".js") -> TranslatedSmartContract:
        # Define the full path to the template file
        file_name_and_path = f"{template_path}/{name}{extension}.jinja"
        # Initialize an empty list to store each rendered line
        rendered_lines = []
        addresses_list = self.generate_address_list()
        addressesByEntityValue = self.generate_addresses_by_entity_value()
        owner_id_bitmask = self.entity_to_data[ self.dao.owner_role.role_id]['final_id']
        print(f"in generate_test_from_template (test generator)- owner_id_bitmask is {owner_id_bitmask}")
        owner_role_value = owner_id_bitmask # redundant, but kept for clarity
        permission_tests_expected_results = self.generate_permission_tests_expected_results()

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
                control_relation_results=self.generate_control_tests_expected_results(),
                permissions=permission_tests_expected_results,
                committee_addresses=[ \
                    #entity_data['final_id'] : entity_data['address'] \
                    entity_data['address'] \
                    for entity_data in self.entity_to_data.values() \
                        if entity_data['entity_type'] == EntityTypeControllable.COMMITTEE \
                ]
            ).splitlines()

        # Return a TranslatedSmartContract object with the list of rendered lines
        return TranslatedSmartContract(rendered_lines, self.context.dao.dao_name + "_test", folder=output_folder, extension=extension)
    
    # def generate_address_dict(self) -> None:
    #     self.address_dict = {f"{role.role_id}": f"{role.role_name.replace(" ","_")}Address" for role in self.dao.roles.values()}
        
    
    def generate_address_list(self) -> list[str]:
        entities = [*self.dao.roles.values(), *self.dao.committees.values()]
        addresses_list = [f"addr{index}" for index, entity in enumerate(entities) if entity.get_id() != self.dao.owner_role.role_id ]

        return addresses_list 

    def generate_addresses_by_entity_value(self) -> dict[int, dict[str, any]]: # see "optimized_translator.newEntityData(...)"
        abEV = {}
        owner_role = self.dao.owner_role
        print(f"in generate_address_list (test generator) - owner_role is {owner_role}")
        address_role = "owner"

        entity_data_by_original_id = { e['original_id'] : e for e in self.entity_to_data.values()}
        print(f"in generate_address_list - entity_data_by_original_id is {entity_data_by_original_id}")

        #reminder: the "final_id" is the justapposition of "bitmasn" + "id"
        i = 0
        owner_id = owner_role.role_id
        for entity_id in self.dao.roles.keys(): # note: type "entity_id" == str
            if owner_id != entity_id:
                entity_data = entity_data_by_original_id[ entity_id ]
                entity_data['address'] = f"addr{i}"
                abEV[ entity_data['final_id'] ] = entity_data['address']
                i += 1
            else:
                print(f"IN THE LOOP OF generate_address_list - owner_id is {owner_id}, WITH ID {entity_id} AND INDEX {i}")
        entity_data = entity_data_by_original_id[ owner_id ]
        abEV[ entity_data['final_id'] ] = address_role
        i+=1
        for entity_id in self.dao.committees.keys():
            entity_data = entity_data_by_original_id[ entity_id ]
            entity_data['address'] = f"addr{i}"
            abEV[ entity_data['final_id'] ] = entity_data['address']
            i += 1
        return abEV
        
    # def generate_committee_addresses(self) -> list[str]:
    #     committee_list = [f"addr{i}" for i in range(1, len(self.dao.committees) + 1)]
    #     return committee_list
    
    def generate_control_tests_expected_results(self) -> list[tuple[int, int, bool]]:
        entities = [*self.dao.roles.values(), *self.dao.committees.values()]
        controlledBy = {entity.get_id(): set(entity.controllers) for entity in entities}
        return [ \
            (
                # the controller
                self.entity_to_data[entity.get_id()]['final_id'], \
                # the one who gets controlled by
                self.entity_to_data[controlled_entity.get_id()]['final_id'], \
                # the test
                entity.get_id() in controlledBy[controlled_entity.get_id()] \
            ) \
            # cartesian product
            for entity in entities \
                for controlled_entity in entities \
        ]
        
 
    def generate_permission_tests_expected_results(self)-> list[tuple[int,str,bool]]:
        entities = [*self.dao.roles.values(), *self.dao.committees.values()]
        #Filter permissions that correspond to actual function invocations in the DAO. Hence, we need to remove voting and prpoposal permissions.
        postprocessed_permissions = []
        for permission in self.dao.permissions.values():
            if permission.voting_right == False and permission.proposal_right == False:
                postprocessed_permissions.append(permission)
        
        permission_tests_expected_results = [(self.entity_to_data[entity.get_id()]['final_id'], permission.allowed_action.replace("/", "_").replace(" ", "_").replace("\\", ""), permission in entity.permissions and permission.voting_right == False and permission.proposal_right == False) for entity in entities for permission in postprocessed_permissions]
        print(permission_tests_expected_results)
        return permission_tests_expected_results
