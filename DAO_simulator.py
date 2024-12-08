from optimized_translator import *
import networkx as nx
from DAOclasses import *
from translator import *
import random
from typing import List
from TestGenerator import *
from solidity_translator import *
#implements the simulation design
class DAOGenerator:
    def __init__(self,n_daos:int, n_roles: int, n_permissions: int, sparsity_coefficient: float, permissions_per_role):
        self.n_daos = n_daos
        self.n_roles_max = n_roles
        self.n_permissions_max = n_permissions
        self.sparsity_coefficient = sparsity_coefficient
        self.permissions_per_role = permissions_per_role
        self.Translator = Translator
        self.daos_by_id = {}
        
    def generate_daos(self):
        self.daos_by_id = {}
        for value in range(self.n_daos): 
            self.daos_by_id[f"dao{value}"] = self.generate_dao(value)
            #TODO:translate DAOs
            
    def get_daos(self):
        print(self.daos_by_id.values())
        return self.daos_by_id.values()
            
    
    def generate_dao(self, dao_index: int): 
        roles = self.generate_roles()
        permissions = self.generate_permissions()            
        #assign permissions to roles
        #assign controllers to roles
        #assign permissions to current DAO
        roles= self.assign_role_permissions(roles, permissions)
        roles = self.generate_control_relations(roles, dao_index)
        generated_dao = DAO(f"dao{dao_index}",f"dao{dao_index}", mission_statement=" ", hierarchical_inheritance=False)
        for permission in permissions:
            generated_dao.add_permission(permission)
        for role in roles:
            generated_dao.add_role(role)
        generated_dao.metadata.save_user_functionalities_group_size(roles,[])
            #print(f'Control Graph {cg_wrapper.control_graph} created for DAO: {dao_id} \n')
        generated_dao.dao_control_graph = ControlGraph(generated_dao)
        owner_role_name = f"{generated_dao.dao_name}Owner".replace(" ", "_")
        owner_role = Role(role_id = owner_role_name, role_name= owner_role_name, role_assignment_method = "Non Assignable", n_agent_min =None, n_agent_max=None, agent_type=None)
        generated_dao.add_role(owner_role)
        generated_dao.owner_role = owner_role

        return generated_dao
    
    def generate_roles(self):
        roles = []
        for value in range(self.n_roles_max):
            roles.append(Role(f"role{value}", f"role{value}", None, None, None, None))
        return roles
    
    def generate_permissions(self):
        permissions = []
        for value in range(self.n_permissions_max):
            permissions.append(Permission(f"permission{value}", f"permission{value}", "operational", None, False, False))
        return permissions
    
    def assign_role_permissions(self, roles: List[Role], permissions: List[Permission]):
        role_permissions = []
        for role in roles:
            i=1
            for permission in permissions:
                if i <= self.permissions_per_role:
                    role.add_permission(permission)
                    role_permissions.append(role)
                    i+=1
        return role_permissions
    
    
    
    def generate_control_relations(self, roles: List[Role], dao_index: int):
        num_roles = len(roles)
        sparsity = (self.sparsity_coefficient / self.n_daos) * dao_index
        max_possible_edges = num_roles * (num_roles - 1)
        target_edges = int(sparsity * max_possible_edges)

        # Step 1: Initialize empty control relations
        all_possible_edges = [(role.role_id, target.role_id) for role in roles for target in roles if role != target]

        # Step 2: Randomly select edges to match the target sparsity
        selected_edges = random.sample(all_possible_edges, target_edges)

        # Step 3: Assign controllers to roles based on selected edges
        for source, target in selected_edges:
            for role in roles:
                if role.role_id == source:
                    role.add_controller(target)
        
        return roles


class DAOSimulator:
    def __init__(self):
        self.dao_smart_contracts_by_DAO_ID  = {} 
        self.dao_tests_by_DAO_ID = {}
        self.translated_smart_contract_list = []
        
    def translate_daos(self, daos, translation_type):
        contracts_to_write = []
        
        for dao in daos:
            translation_data = tuple
            dao_name = dao.dao_name
            # the translator uses the selected translation logic
            #if diamond_enabled.get()==True:
            #    translator = SolidityTranslator(dao, translation_logic.get(), diamond=True)  
            #elif diamond_enabled.get()==False:
            translator = SolidityTranslator(dao, translation_type, diamond=False)
            #else:
            #    print("error with diamond configuration: ", diamond_enabled)
            tests_translator = TestGeneratorOptimized(dao)
            translation_data[0]= dao_name
            translation_data[1] = dao_name
            translation_data[2]= translator
            translation_data[3]= tests_translator
            contracts_to_write.append(translation_data)
            return contracts_to_write
        
            
    def generate_tests(self, daos):
        for dao in daos:
           test_generator = TestGeneratorOptimized(dao, True)     
           test_generator.generate_test_script("test")

    
              
           
#steps for generating dao scs: 
# initialize the DAOGenerator: _init__(self,n_daos:int, n_roles: int, n_permissions: int, sparsity_coefficient: float, permissions_per_role, Translator: Translator)
# initialize DAOSimulator:  __init__(self, translator: SolidityTranslator, test_generator: TestGeneratorOptimized)
# DAOGenerator obj.generate_daos
# DAOSimulator obj.translate_daos

        
         
        
        