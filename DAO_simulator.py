from optimized_translator import *
import networkx as nx
from DAOclasses import *
from translator import TranslatedSmartContract, CommitteeTranslator, TranslationContext, Translator
import random
from typing import List
#implements the simulation design
class DAOGenerator:
    def __init__(self,n_daos:int, n_roles: int, n_permissions: int, sparsity_coefficient: float, permissions_per_role, Translator: Translator):
        self.n_daos = n_daos
        self.n_roles_max = n_roles
        self.n_permissions_max = n_permissions
        self.sparsity_coefficient = sparsity_coefficient
        self.permissions_per_role = permissions_per_role
        self.Translator = Translator
        self.dao_smart_contracts_by_DAO_ID = {}
        self.dao_tests_by_DAO_ID = {}
        
    def generate_daos(self):
        self.dao_smart_contracts_by_DAO_ID = {}
        for value in range(self.n_daos): 
            self.dao_smart_contracts_by_DAO_ID[f"dao{value}"] = self.generate_dao(value)
            #TODO:translate DAOs
            
    
    def generate_dao(self, dao_index: int): 
        roles = self.generate_roles()
        permissions = self.generate_permissions()            
        #assign permissions to roles
        #assign controllers to roles
        #assign permissions to current DAO
        roles= self.assign_role_permissions(roles, permissions)
        roles = self.generate_control_relations(roles, dao_index)
        return DAO(f"dao{dao_index}", roles, permissions, mission_statement=" ", hierarchical_inheritance=False)
    
    def generate_roles(self):
        roles = []
        for value in range(self.n_roles_max):
            roles.append(Role(f"role{value}", f"role{value}"))
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
    def __init__(self, dao_generator : DAOGenerator):
        self.translator = Translator()
        self.committee_translator = CommitteeTranslator()
        self.translated_smart_contract_list = []
        
         
        
        